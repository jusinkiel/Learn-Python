
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback

def search_google(search_query):
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    
    service = webdriver.ChromeService('/Users/justinkielpascualmontano/Documents/chromedriver-mac-x64/chromedriver')
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--allow-cross-origin-auth-prompt')

    browser = webdriver.Chrome(service=service, options=options)

    # Open browser to begin search
    browser.get(search_url)

    # XPath for the 1st image that appears in Google: //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
    for index in range(1, 50):
        img_box = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(index))))
        # Click on the thumbnail
        img_box.click()

        # XPath of the image display 
        fir_img = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div/div[3]/div[1]/a/img[1]')))

        # Wait between interaction
        time.sleep(1)
     

        # Retrieve attribute of src from the element
        try:
            img_src = fir_img.get_attribute('src')
            print(img_src)
        except Exception as e:
            traceback.print_exec()


    

link = search_google('dog')