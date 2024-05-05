from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time , random

def create_remote_driver(remote_url):
    print('create driver')
    user_agents = [
    # Add your list of user agents here
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        ]
    user_agent = random.choice(user_agents)
    
    # Create a remote WebDriver instance
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument(f'user-agent={user_agent}')
    print(user_agent)
    driver = webdriver.Chrome(options=options)
    print('fin de creation driver')
    
    return driver

def instagram(dd):
    try:
        driver.get("https://snapinsta.app/")
        print("start get ")
        #time.sleep(10)
        
        driver.find_element(By.XPATH,'/html/body/main/div[1]/form/div/input[1]').send_keys('https://www.instagram.com/reel/C6bHQRir3Er/?igsh=MzRlODBiNWFlZA==')
        driver.find_element(By.XPATH,'/html/body/main/div[1]/form/button').click()
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "download-bottom")))
            print("Page loaded successfully!")
            new_page_html = driver.page_source

            # Use BeautifulSoup to parse the HTML content
            new_page_soup = BeautifulSoup(new_page_html, 'html.parser')
            download_btn = new_page_soup.find("div",class_='download-bottom')
            print(download_btn.find("a")["href"]) 
            rr =  download_btn.find("a")["href"]
        except TimeoutException:
            rr = "Page didn't load within 10 seconds."
        try:
            # Wait for the cookies widget to appear (replace "cookies_widget_xpath" with the actual XPath)
            close_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/button")))

            # Close or hide the cookies widget (replace "close_button_xpath" with the XPath for the close button)
            #close_button = cookies_widget.find_element(By.XPATH, "close_button_xpath")
            close_button.click()

            # Continue with other actions on the page
        except TimeoutException:
            # Cookies widget did not appear, continue with other actions on the page
            pass
        #download_video(video_url, download_directory)
    except Exception as e:
        rr=e
            
    res={
        'status_code': 200,
        'message': str(rr),
            } 
    return res
 

# Example usage
if __name__ == "__main__":
    remote_url = "https://standalone-firefox-4-20-0-20240425.onrender.com/wd/hub"  # Replace with the actual URL of your Selenium Grid hub
    driver = create_remote_driver(remote_url)
    print('get')
    ins=instagram(driver)
    print(ins)
    driver.quit()
    print('quite')
    # Use the driver...
