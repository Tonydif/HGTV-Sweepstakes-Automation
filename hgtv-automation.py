from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from random import uniform
import re
from datetime import datetime

# Configuration and User Settings
EMAIL = 'youremail@whatever.com'
HGTV_URL = 'https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes'
DIY_URL = 'https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes'
CHROMEDRIVER_PATH = '/Path/to/Your/chromedriver'

def setup_chromedriver():
    """Sets up the ChromeDriver with options."""
    try:
        chrome_options = Options()
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("window-size=1280,800")

        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"{datetime.now()}: Error setting up ChromeDriver: {str(e)}")
        raise

def enter_hgtv_sweepstakes(driver):
    """Automates the entry for the HGTV sweepstakes."""
    try:
        print(f"{datetime.now()}: Loading HGTV page...")
        driver.get(HGTV_URL)
        time.sleep(5)
        
        get_HGTV_source = driver.page_source
        HGTV_ngxFrame = re.findall("ngxFrame\d\w+", get_HGTV_source)
        
        if not HGTV_ngxFrame:
            raise Exception("Could not find ngxFrame ID on HGTV page")
            
        HGTV_ngxFrame = HGTV_ngxFrame[0]
        print(f"{datetime.now()}: Found iframe: {HGTV_ngxFrame}")

        wait = WebDriverWait(driver, 20)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, HGTV_ngxFrame)))

        email_field = wait.until(EC.element_to_be_clickable((By.ID, "xReturningUserEmail")))
        email_field.send_keys(EMAIL)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="xCheckUser"]/span"""))).click()

        driver.switch_to.default_content()
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, HGTV_ngxFrame)))

        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="multioptin_0_Secondary"]""")))
        checkbox.click()
        time.sleep(1)
        checkbox.click()

        action = ActionChains(driver)
        action.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        print(f"{datetime.now()}: HGTV entry completed successfully")
        
    except Exception as e:
        print(f"{datetime.now()}: Error in HGTV entry: {str(e)}")
        print(f"{datetime.now()}: Current URL: {driver.current_url}")
        raise

def enter_diy_sweepstakes(driver):
    """Automates the entry for the DIY sweepstakes."""
    try:
        print(f"{datetime.now()}: Loading DIY page...")
        driver.get(DIY_URL)
        time.sleep(5)
        
        get_DIY_source = driver.page_source
        DIY_ngxFrame = re.findall("ngxFrame\d\w+", get_DIY_source)
        
        if not DIY_ngxFrame:
            raise Exception("Could not find ngxFrame ID on DIY page")
            
        DIY_ngxFrame = DIY_ngxFrame[0]
        print(f"{datetime.now()}: Found iframe: {DIY_ngxFrame}")

        wait = WebDriverWait(driver, 20)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, DIY_ngxFrame)))

        email_field = wait.until(EC.element_to_be_clickable((By.ID, "xReturningUserEmail")))
        email_field.send_keys(EMAIL)
        wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="xCheckUser"]/span"""))).click()

        driver.switch_to.default_content()
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, DIY_ngxFrame)))

        submit_button_form = wait.until(EC.element_to_be_clickable((By.ID, "xSecondaryForm")))
        submit_button_form.find_element(By.ID, "xSubmitContainer").click()

        action = ActionChains(driver)
        action.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        print(f"{datetime.now()}: DIY entry completed successfully")
        
    except Exception as e:
        print(f"{datetime.now()}: Error in DIY entry: {str(e)}")
        print(f"{datetime.now()}: Current URL: {driver.current_url}")
        raise

def main():
    """Main execution function."""
    print(f"{datetime.now()}: Starting sweepstakes entries...")
    driver = None
    try:
        driver = setup_chromedriver()
        enter_hgtv_sweepstakes(driver)
        time.sleep(10 + round(uniform(0, 5), 2))
        enter_diy_sweepstakes(driver)
        print(f"{datetime.now()}: All entries completed successfully")
    except Exception as e:
        print(f"{datetime.now()}: Fatal error during execution: {str(e)}")
    finally:
        if driver:
            try:
                driver.quit()
                print(f"{datetime.now()}: Browser closed successfully")
            except Exception as e:
                print(f"{datetime.now()}: Error closing browser: {str(e)}")

if __name__ == "__main__":
    main()
