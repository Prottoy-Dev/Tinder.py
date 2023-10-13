# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

# Load environment variables for Facebook login
load_dotenv()
USERNAME_FB = os.getenv("USERNAME_FB")
PASSWORD_FB = os.getenv("PASSWORD_FB")

# Define a class for the Tinder bot
class Tinderbot():
    def __init__(self):
        # Initialize the WebDriver for Microsoft Edge
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def login(self):
        # Open the Tinder website
        self.driver.get("https://tinder.com")
        main_page = self.driver.current_window_handle
        time.sleep(5)
        
        # Find and click the "Log In" button on the Tinder main page
        log_in = self.driver.find_element(By.XPATH, '//*[@id="u106008161"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        log_in.click()
        time.sleep(5)
        
        # Click the "Log in with Facebook" button on the login page
        log_in_fb = self.driver.find_element(By.XPATH, '//*[@id="u-1622372915"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()
        time.sleep(2)
        
        # Switch to the new window (Facebook login)
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        # Find the email input field and enter the Facebook username
        mail_entry = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        mail_entry.send_keys(USERNAME_FB)
        time.sleep(2)
        
        # Find the password input field and enter the Facebook password
        pass_entry = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pass_entry.send_keys(PASSWORD_FB)
        time.sleep(2)
        
        # Press Enter to log in
        pass_entry.send_keys(Keys.ENTER)
        time.sleep(10)
        
        # Switch back to the Tinder main page
        self.driver.switch_to.window(main_page)
        time.sleep(5)

    def like(self):
        try:
            # Send a right arrow key press to like the current profile
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="Tinder"]/body').send_keys(Keys.ARROW_RIGHT).click()
            print("Like Successful")
        except:
            # If the like action fails, close any pop-up that may appear
            self.close_pop_up()

    def close_pop_up(self):
        try:
            # Try to allow location access if prompted
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="u-1622372915"]/main/div/div/div/div[3]/button[1]').click()
        except:
            try:
                # Try to enable notifications if prompted
                time.sleep(5)
                self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]').click()
            except:
                try:
                    # Try to close a match pop-up if it appears
                    time.sleep(2)
                    self.driver.find_element(By.XPATH,'//*[@id="q-1025200637"]/main/div/div[1]/div/div[4]/button/svg').click()
                except:
                    try:
                        # Try to close a cookies pop-up if it appears
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]').click()
                    except:
                        try:
                            # Try to close a home screen pop-up if it appears
                            time.sleep(2)
                            self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div[2]/button[2]/div[2]/div[2]').click()
                        except:
                            try:
                                # Try to close a buy subscription later pop-up if it appears
                                time.sleep(2)
                                self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div[3]/button[2]/div[2]/div[2]').click()
                            except:
                                print("Like Unsuccessful")
                                pass
