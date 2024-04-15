from crawling.define import BASE_URL, CATEGORY_LIST, get_category

#
from datetime import datetime, timedelta

# 어제 날짜를 구해 URL을 완성하자!
## https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta
## https://docs.python.org/3/library/datetime.html#available-types

def get_yesterday():
    # 오늘 날짜 구하기
    today = datetime.now()
    # print(today)

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
# print(yesterday)
url_query_date = f'?date={yesterday}'
# print(url_query_date)

NEWS_URL_LIST = []

for category in CATEGORY_LIST:
    url = f"{BASE_URL}{category}{url_query_date}"
    # print(url)
    NEWS_URL_LIST.append({
        'URL': url,
        '카테고리': get_category(category)
    })

# print(NEWS_URL_LIST)