# bot.py
import random
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .config import username, password
from .utils import wait_for_element, click_element
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def create_driver(self):
        options = Options()
        options.add_argument(f"user-agent={self.get_random_user_agent()}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(options=options)
        return driver

    def get_random_user_agent(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        ]
        return random.choice(user_agents)

    # def login(self):
    #     self.driver.get('https://www.instagram.com/accounts/login/')
    #     wait_for_element(self.driver, By.NAME, 'username')
       
    #     self.driver.find_element(By.NAME, 'username').send_keys(self.username)
    #     self.driver.find_element(By.NAME, 'password').send_keys(self.password)

    #     submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    #     submit_button.click()
    #     time.sleep(10)

    # def wait_for_element(self, driver, by, value):
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))

    # def close(self):
    #     self.driver.quit()


    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        wait_for_element(self.driver, By.NAME, 'username')
       
        # Type username one character at a time
        username_field = self.driver.find_element(By.NAME, 'username')
        for char in self.username:
            username_field.send_keys(char)
            time.sleep(0.1)  # Small delay between each character

        # Type password one character at a time
        password_field = self.driver.find_element(By.NAME, 'password')
        for char in self.password:
            password_field.send_keys(char)
            time.sleep(0.1)  # Small delay between each character

        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        time.sleep(5)
        submit_button.click()
        time.sleep(10)

    def wait_for_element(self, driver, by, value):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))

    def close(self):
        self.driver.quit()



    # for disabling save login  info
    def dismiss_save_login_prompt(self):
        try:
            # Wait for the notification prompt to appear
            not_now_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][tabindex='0'].x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37"))
            )
            print("save login prompt found!")
            time.sleep(5)
            not_now_button.click()
            time.sleep(5)
            print("Clicked 'Not Now' button successfully!")
            time.sleep(10)
        except TimeoutException:
            print("save login prompt not found!")
            # If the prompt doesn't appear, do nothing
            pass

    # for disabling  notifications
    def dismiss_notification_prompt(self):
        try:
            # Wait for the notification prompt to appear
            not_now_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1'))
            )
            print("Notification prompt found!")
            time.sleep(15)
            not_now_button.click()
            time.sleep(5)
            print("Clicked 'Not Now' button successfully!")
            time.sleep(5)
        except TimeoutException:
            print("Notification prompt not found!")
            # If the prompt doesn't appear, do nothing
            pass
        



    # def follow_user(self, username):
    #     try:
    #         # Navigate to the user's profile page
    #         url = f"https://www.instagram.com/{username}/"
    #         self.driver.get(url)

    #         # Wait for the page to load
    #         WebDriverWait(self.driver, 10).until(EC.title_contains(username))

    #         # Locate the "Follow" button using the XPath
    #         follow_button = WebDriverWait(self.driver, 30).until(
    #             EC.element_to_be_clickable((By.XPATH, '//button//div[text()="Follow"]'))
    #         )

    #         if follow_button:
    #             print("Follow button found")
    #             time.sleep(1)  # Small delay before clicking

    #             # Use ActionChains to click the button
    #             actions = ActionChains(self.driver)
    #             actions.move_to_element(follow_button).click().perform()

    #             print("Attempted to follow the user!")
    #             time.sleep(5)  # Wait to ensure action is complete

    #             # Check if the follow action was successful
    #             new_button_text = follow_button.text
    #             if "Following" in new_button_text or "Requested" in new_button_text:
    #                 print("User followed successfully!")
    #             else:
    #                 print("Follow action might not have been successful.")
    #         else:
    #             print("Follow button not found or already following.")
    #     except NoSuchElementException as e:
    #         print("No such element exception:", str(e))
    #     except TimeoutException as e:
    #         print("Timeout exception:", str(e))
    #     except Exception as e:
    #         print("An error occurred:", str(e))

    
   

    # def follow_user(self, username):
    #     try:
    #         # Navigate to the user's profile page
    #         url = f"https://www.instagram.com/{username}/"
    #         self.driver.get(url)

    #         # Wait for the page to load
    #         WebDriverWait(self.driver, 10).until(EC.title_contains(username))
    #         print(f"navigated to {username}'s profile")

    #         # Wait for the follow button to be clickable
    #         follow_button = WebDriverWait(self.driver, 30).until(
    #             EC.element_to_be_clickable((By.XPATH, '//button//div[text()="Follow"]'))
    #         )

    #         if follow_button:
    #             print("Follow button found")
    #             time.sleep(1)  # Small delay before clicking

    #             # Check for any overlays or pop-ups
    #             try:
    #                 overlay = self.driver.find_element(By.XPATH, '//div[contains(@class, "mt3GC")]')
    #                 overlay.click()
    #                 print("Closed overlay")
    #             except NoSuchElementException:
    #                 pass

    #             # Ensure the follow button is visible and enabled
    #             if follow_button.is_displayed() and follow_button.is_enabled():
    #                 # Use ActionChains to simulate a more realistic click
    #                 actions = ActionChains(self.driver)
    #                 actions.move_to_element(follow_button)
    #                 actions.click(follow_button)
    #                 actions.perform()

    #                 print("Attempted to follow the user!")
    #                 time.sleep(5)  # Wait to ensure action is complete

    #                 # Wait for the button text to update
    #                 time.sleep(2)

    #                 # Check if the follow action was successful
    #                 new_button_text = follow_button.text
    #                 print(f"Button text after clicking: {new_button_text}")
    #                 if "Following" in new_button_text or "Requested" in new_button_text:
    #                     print("User followed successfully!")
    #                 else:
    #                     print("Follow action might not have been successful.")
    #             else:
    #                 print("Follow button is not visible or not enabled.")
    #         else:
    #             print("Follow button not found or already following.")
    #     except NoSuchElementException as e:
    #         print("No such element exception:", str(e))
    #     except TimeoutException as e:
    #         print("Timeout exception:", str(e))
    #     except Exception as e:
    #         print("An error occurred:", str(e))



    def follow_user(self, username):
        try:
            # Navigate to the user's profile page
            url = f"https://www.instagram.com/{username}/"
            self.driver.get(url)

            # Wait for the page to load
            WebDriverWait(self.driver, 10).until(EC.title_contains(username))
            print(f"navigated to {username}'s profile")

            # Wait for the follow button to be clickable
            follow_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button//div[text()="Follow"]'))
            )

            if follow_button:
                print("Follow button found")
                time.sleep(10)  # Wait for 5 seconds to ensure the button is fully loaded

                # Move to the follow button and click it
                actions = ActionChains(self.driver)
                actions.move_to_element(follow_button)
                actions.pause(5)  # Pause for 1 second to simulate a realistic click
                actions.click(follow_button)
                actions.perform()

                print("Attempted to follow the user!")
                time.sleep(10)  # Wait for 10 seconds to ensure the action is complete

                # Check for Instagram's feedback
                try:
                    feedback = self.driver.find_element(By.XPATH, '//div[contains(text(), "Follow request sent")]')
                    print("Follow request sent successfully!")
                    return True
                except NoSuchElementException:
                    print("Follow request not sent successfully.")
                    return False

            else:
                print("Follow button not found or already following.") # have to fix it
                return False
        except NoSuchElementException as e:
            print("No such element exception:", str(e))
            return False
        except TimeoutException as e:
            print("Timeout exception:", str(e))
            return False
        except Exception as e:
            print("An error occurred:", str(e))
            return False


    # for liking a post
    def like_post(self,like_url):
        try:
            self.driver.get(like_url)
            print("URL searched")
            time.sleep(10)  # Wait for the page to load

            # Locate the Like button using the provided CSS Selector
            like_button = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.x1i10hfl.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xcdnw81"))
            )
            
            if like_button:
                print("Like button found")
                time.sleep(3)

                # Click using JavaScript if standard click fails
                self.driver.execute_script("""
                    var element = arguments[0];
                    if (element) {
                        element.click();
                    } else {
                        console.log("Element not found.");
                    }
                """, like_button)
                
                print("Attempted to click the like button!")
                time.sleep(10)
                return True
            else:
                print("Like button not found.")
                return False
        except NoSuchElementException as e:
            print("No such element exception:", str(e))
        except TimeoutException as e:
            print("Timeout exception:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))



    # #for commenting on a post
    # def comment_on_post(self,comment_text):
    #     try:
    #         self.driver.get("https://www.instagram.com/p/C-s6Od6hPEv/")
    #         print("Navigated to post URL")
    #         time.sleep(10)  # Wait for the page to load

    #         cmnt_icon = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.x1i0vuye.xvbhtw8.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x5n08af.x78zum5.x1iyjqo2.x1qlqyl8.x1d6elog.xlk1fp6.x1a2a7pz.xexx8yu.x4uap5.x18d9i69.xkhd6sd.xtt52l0.xnalus7.xs3hnx8.x1bq4at4.xaqnwrm"))
    #         )
    #         print("comment btn found")
    #         cmnt_icon.click()
    #         # Re-locate the Comment textarea
    #         comment_textarea = WebDriverWait(self.driver, 30).until(
    #             EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Add a comment…"]'))
    #         )
    #         print("Comment textarea found")

    #         # Enter the comment text
    #         # comment_textarea.click()
    #         # comment_textarea.clear()  # Clear any existing text
    #         time.sleep(2)  # Wait for the text to be entered
    #         comment_textarea.send_keys(comment_text)
    #         time.sleep(5)
    #         # Submit the comment
    #         comment_textarea.send_keys(Keys.ENTER)
    #         print("Comment submitted successfully!")

    #         time.sleep(5)  # Wait to see the comment submission
    #     except NoSuchElementException as e:
    #         print("No such element exception:", str(e))
    #     except TimeoutException as e:
    #         print("Timeout exception:", str(e))
    #     except Exception as e:
    #         print("An error occurred:", str(e))

    # For commenting on a post
    def comment_on_post(self,post_url):
        try:
            # A list of comments to randomly choose from
            comments_list = [
                "Nice!", 
                "Really nice post!", 
                "Cool!", 
                "Wow!", 
                "Amazing content!", 
                "Great work!", 
                "Incredible!", 
                "Superb post!", 
                "Loved it!", 
                "Keep it up!"
            ]

            # Randomly select a comment from the list
            random_comment = random.choice(comments_list)

            self.driver.get(post_url)
            print("Navigated to post URL")
            time.sleep(10)  # Wait for the page to load

            # Find the comment icon and click on it
            cmnt_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.x1i0vuye.xvbhtw8.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x5n08af.x78zum5.x1iyjqo2.x1qlqyl8.x1d6elog.xlk1fp6.x1a2a7pz.xexx8yu.x4uap5.x18d9i69.xkhd6sd.xtt52l0.xnalus7.xs3hnx8.x1bq4at4.xaqnwrm"))
            )
            print("Comment button found")
            cmnt_icon.click()

            # Find the comment textarea and input the random comment
            comment_textarea = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Add a comment…"]'))
            )
            print("Comment textarea found")

            # Enter the randomly selected comment
            time.sleep(2)  # Wait for the textarea to be ready
            comment_textarea.send_keys(random_comment)
            time.sleep(5)
            
            # Submit the comment
            comment_textarea.send_keys(Keys.ENTER)
            print(f"Comment '{random_comment}' submitted successfully!")

            time.sleep(5)  # Wait to see the comment submission
            return True
        except NoSuchElementException as e:
            print("No such element exception:", str(e))
        except TimeoutException as e:
            print("Timeout exception:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))



if __name__ == '__main__':
    bot = InstagramBot(username, password)
    bot.login()
    #bot.dismiss_save_login_prompt()
    #bot.dismiss_notification_prompt()
    # bot.search_for_id("romanreigns")
    #bot.follow_user("romanreigns")
    bot.like_post()
    #bot.comment_on_post()
    bot.close()