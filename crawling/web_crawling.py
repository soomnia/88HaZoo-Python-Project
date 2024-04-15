from crawling.naver_it_news import NEWS_URL_LIST
from crawling.naver_it_news import get_yesterday

# import
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pandas as pd

## ??
import asyncio

async def save_in_db():
    try:
        await create_upload_file()
        print("?")
        return {"message": "성공!!"}
    except:
        return {"error" : "save_in_db 에러"} 

async def crawling_news():
    browser = webdriver.Chrome()
    # 기사 내용 담을 리스트
    item_list = []

    for url in NEWS_URL_LIST:
        print('URL:', url['URL'])
        browser.get(url['URL'])

        # 기사 컨테이너:
        ## class="sa_text"
        link_container_list = browser.find_elements(By.CLASS_NAME, 'sa_text')
        link_list = []

        # 일단 기사 링크를 먼저 모으자
        for container in link_container_list:
            ## 링크
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
                # title = browser.find_element(By.CLASS_NAME, 'title').text
                print("양식이 달라요")
                # 다수의 것에서 벗어나는 것은 포함시키지 않기로 협의
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
        time.sleep(3)
        await create_upload_file(file_name)
        return {"message": "성공!!"}
    except:
        return {"error" : "에러 발생"} 

## TODO: asyncio 알아봐야 함..
async def save_csv_file(df: pd.DataFrame, file_name: str):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, df.to_csv, file_name)

from DB.database import SessionLocal
import csv
from DB.models import News

async def create_upload_file(file_name: str):
    db = SessionLocal()
    try:
        # CSV 파일 내용을 읽어서 데이터베이스에 저장
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            ## 첫 번째 줄을 건너 뛰기! (칼럼 명)
            next(csv_reader) 
            for row in csv_reader:
                print("data:", row)
                item = News(category=row[1],
                            title=row[2],
                            press=row[3],
                            date=row[4],
                            link=row[5],
                            content=row[6])
                db.add(item)
                db.commit()
    except Exception as e:
        db.rollback()
        return {"error": f"create_upload_file - {str(e)}"}
    finally:
        db.close()