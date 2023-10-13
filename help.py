from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os
load_dotenv()
USERNAME_FB = os.getenv("USERNAME_FB")
PASSWORD_FB = os.getenv("PASSWORD_FB")


class Tinderbot():
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://tinder.com")
        main_page = self.driver.current_window_handle
        time.sleep(5)
        ############################################# Tinder log in ###############################################
        log_in = self.driver.find_element(By.XPATH, '//*[@id="u106008161"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        log_in.click()
        time.sleep(5)
        ####################################### Log in via facebook #############################################
        log_in_fb = self.driver.find_element(By.XPATH, '//*[@id="u-1622372915"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        mail_entry = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        mail_entry.send_keys(USERNAME_FB)
        time.sleep(2)
        pass_entry = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        pass_entry.send_keys(PASSWORD_FB)
        time.sleep(2)
        pass_entry.send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.switch_to.window(main_page)
        time.sleep(5)

    def like(self):
        try:
            # driver.find_element(By.XPATH, '//*[@id="q-1355571838"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
            # # '1]/div/div[3]/div/div[4]/button').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="Tinder"]/body').send_keys(Keys.ARROW_RIGHT).click()
            print("successful")
            
        except: # Close pop-up
            self.close_pop_up()

    def close_pop_up(self):
        try: # Allow location
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@id="u-1622372915"]/main/div/div/div/div[3]/button[1]').click()
        except: 
            try: # Enable Notifications
                time.sleep(5)
                self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]').click()
            except:
                try: # Close match pop-up
                        time.sleep(2)
                        self.driver.find_element(By.XPATH,'//*[@id="q-1025200637"]/main/div/div[1]/div/div[4]/button/svg').click()
                except:
                        try: # Cookies pop-up
                            time.sleep(5)
                            self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]').click()    
                        except:
                            try: # Homescreen pop-up
                                time.sleep(2)
                                self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div[2]/button[2]/div[2]/div[2]').click()    
                            except:# Buy subscription later
                                try:
                                    time.sleep(2)
                                    self.driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div[3]/button[2]/div[2]/div[2]').click()
                                except:
                                    print("Like Unsuccessful")
                                    pass