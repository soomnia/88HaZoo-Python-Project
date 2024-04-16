from crawling.define import BASE_URL, CATEGORY_LIST, get_category
from crawling.utils import save_csv_file, insert_news_file

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pandas as pd

def get_yesterday():
    # 오늘 날짜 구하기
    today = datetime.now()

    # 오늘에서 하루 빼서 어제 날짜 구하기
    yesterday = today - timedelta(1)
    # print(yesterday)

    # 형변환해서 필요한 연월일만 슬라이싱
    yesterday = str(yesterday)[:10]
    # print(yesterday)

    # 쿼리에 쓰이도록 '-' 를 ''로 대체
    yesterday = yesterday.replace('-', '')
    # print(yesterday)

    return yesterday

# 최종적인 날짜 쿼리!
yesterday = get_yesterday()
url_query_date = f'?date={yesterday}'

NEWS_URL_LIST = []

for category in CATEGORY_LIST:
    url = f"{BASE_URL}{category}{url_query_date}"
    # print(url)
    NEWS_URL_LIST.append({
        'URL': url,
        '카테고리': get_category(category)
    })

async def crawling_news():
    browser = webdriver.Chrome()
    # 기사 내용 담을 리스트
    item_list = []

    for url in NEWS_URL_LIST:
        print('URL:', url['URL'])
        browser.get(url['URL'])

        #기사 목록 최하단까지 크롤링하기 위한 '기사 더보기' 클릭    
        more_button='a'
        j=1
        while len(more_button) > 0:
            more_button=browser.find_element(By.CLASS_NAME,'_CONTENT_LIST_LOAD_MORE_BUTTON').text
            if len(more_button) == 0:
                print('마지막까지 내리기 완료')
                break
            browser.find_element(By.CLASS_NAME,'_CONTENT_LIST_LOAD_MORE_BUTTON').click()
            print(f'{j}번째 클릭')
            j+=1
            time.sleep(3)
        
        # 기사 컨테이너:
        ## class="sa_text"
        link_container_list = browser.find_elements(By.CLASS_NAME, 'sa_text')
        link_list = []

        for container in link_container_list:
            link = container.find_element(By.CLASS_NAME, 'sa_text_title').get_attribute("href")

            link_list.append({
                'URL': link,
                '카테고리': url['카테고리']
            })

        # 링크로 이동해서 내용을 크롤링하자:
        ## class="sa_text"

        # 제목, 언론사, 작성일, 내용, 링크, 전체 내용
        for item in link_list:
            print("url:", item)
            
            browser.get(item['URL'])

            ## 제목
            try:
                ## id="title_area"
                title = browser.find_element(By.ID, 'title_area').text
            except:
                ## class="title"
                print("양식이 달라요")
                # 다수의 양식에서 벗어나는 것은 포함시키지 않기로 협의
                continue

            print("title:", title)
        
            ## 언론사
            ## class="media_end_head_top_logo_img"
            press = browser.find_element(By.CLASS_NAME, 'media_end_head_top_logo_img').get_attribute("title")
            print("press:", press)
            
            ## 작성일
            date = browser.find_element(By.CLASS_NAME, 'media_end_head_info_datestamp_time').text
            print("date:", date)
            
            ### 입력일
            ## class="media_end_head_info_datestamp_time _ARTICLE_DATE_TIME"
            date_input = browser.find_element(By.CLASS_NAME, '_ARTICLE_DATE_TIME').text
            print("date_input:", date_input)
            
            ## 전체 내용
            ## id="newsct_article"
            content = browser.find_element(By.ID, 'newsct_article').text
            print("content: ", content)

            item_list.append({
                '카테고리': item['카테고리'],
                '제목': title,
                '언론사': press,
                '입력 날짜': date_input,
                '링크': item['URL'],
                '전체 내용': content
            })

            time.sleep(0.5)

    browser.quit()

    df = pd.DataFrame(item_list)

    try:
        file_name = f"{get_yesterday()}_네이버_IT_과학_뉴스.csv"
        await save_csv_file(df, file_name)
        time.sleep(1)
        await insert_news_file(file_name)
        return {"message": "성공!!"}
    except:
        return {"error" : "에러 발생"} 
