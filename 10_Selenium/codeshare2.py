from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests 
import traceback
from datetime import datetime
import os
import base64

def wait():
    time.sleep(2)

def delete_files_in_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")

def search_google(search_query):
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"

    service = webdriver.ChromeService('/Users/justinkielpascualmontano/Documents/chromedriver-mac-x64/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-web-security')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--allow-cross-origin-auth-prompt')

    driver = webdriver.Chrome(service=service, options=options)

    # Open browser to begin search
    driver.get(search_url)
    
    time.sleep(1)

    os.makedirs('./download', exist_ok=True) 
    delete_files_in_directory('/Users/justinkielpascualmontano/Downloads/Learn-Python/10_Selenium/download')

    
    for i in range(1, 50):
        url = None

        find_xpath = '//*[@id="islrg"]/div[1]/div[{index}]/a[1]/div[1]/img'.format(index = i)
        try:
            item = driver.find_element(By.XPATH, find_xpath)
            item.click()
            time.sleep(1.5)
            preview = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]')
            url = preview.get_attribute('src')
            print(i, preview.get_attribute('src'))
        except Exception as e: 
            print('error ', find_xpath)

        if url != None:
            filename = (datetime.now().strftime("%Y-%m%d %H%M%S%f")) + '.jpg'

            if url.find('base64') > 0:
                data = url.split(',')
                imgdata = base64.b64decode(data[1])
                with open('download/{}'.format(filename), 'wb') as f:
                    f.write(imgdata)
            else:
                data = requests.get(url).content 
                f = open('download/{}'.format(filename),'wb')
                f.write(data) 
                f.close() 

    return 'done'




keyword = 'cat'
link = search_google(keyword)
print("Link", link)