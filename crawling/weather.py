from crawling.utils import save_csv_file

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pandas as pd

async def get_weather_datas() -> list:
    weather_data_list = []
    browser = webdriver.Chrome()
    for cityId in range(1, 3520):
        url = f"https://worldweather.wmo.int/kr/city.html?cityId={cityId}"
        browser.get(url)
        time.sleep(0.1)

        path_elements = browser.find_element(By.CLASS_NAME, "breadcrumb").find_elements(By.TAG_NAME, "a")
        print("path_elements 전체:", path_elements)

        try:
            region = path_elements[1].text
            country = path_elements[2].text
            city = path_elements[3].text
            # country = browser.find_element(By.CLASS_NAME,'city_place_name_member').text
            # city = browser.find_element(By.CLASS_NAME,'m_city_name').text
            weather = browser.find_element(By.CLASS_NAME, "weather_icon1").get_attribute("title")
            temperature = browser.find_element(By.CLASS_NAME,'present_temp_value').text
            humidity = browser.find_element(By.CLASS_NAME,'present_rh_value').text
            wind_speed = browser.find_element(By.CLASS_NAME,'present_wind_value').text
            local_time = browser.find_element(By.CLASS_NAME,'city_currwx_issuetime').text.split("(")[0].strip()
            
            print(region, country, city, weather, temperature, humidity, wind_speed, local_time)
            
            weather_data_list.append({
            "region":region,
            "country":country,
            "city":city,
            "weather":weather,
            "temperature":temperature,
            "humidity":humidity,
            "wind_speed":wind_speed,
            "local_time":local_time
            })
        except:
            print("*"*30)
            print("해당 도시는 path_element에 문제가 있습니다.")
            print("*"*30)
            continue

    time.sleep(0.5)
    
    browser.close()
    # return weather_data_list
    df = pd.DataFrame(weather_data_list)

    file_creation_time = time.strftime("%Y%m%d %H:%M:%S", time.localtime())

    try:
        file_name = f"글로벌_날씨_{file_creation_time}.csv"
        await save_csv_file(df, file_name)
        return {"message": "날씨 데이터 저장 완료"}
    except Exception as e:
        return {"error": f"날씨 데이터 크롤링 중 에러 발생\n{e}"}