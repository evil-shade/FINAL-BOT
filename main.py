from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys
import random
from random import randint
import time
from fake_useragent import UserAgent

chrm_options = webdriver.ChromeOptions()

ua = UserAgent()
chrm_options.add_argument("window-size=1400,768")
chrm_options.add_experimental_option("useAutomationExtension", False)
chrm_options.add_experimental_option("excludeSwitches", ["enable-automation"])

link = [
    "https://cylonepedia.com",
    "https://cylonepedia.com/g-c-e-ordinary-level-past-papers-english/",
    "https://cylonepedia.com/g-c-e-ordinary-level-past-papers-tamil/",
    "https://cylonepedia.com/g-c-e-ordinary-level-past-papers-sinhala/",
    "https://cylonepedia.com/2021/02/07/2019-english-medium-gce-o-l-past-papers/",
    "https://cylonepedia.com/2021/02/07/2018-english-medium-gce-o-l-past-papers/",
    "https://cylonepedia.com/2021/02/07/2017-english-medium-gce-o-l-past-papers/",
    "https://cylonepedia.com/2021/02/07/2016-english-medium-gce-o-l-past-papers/",
    "https://cylonepedia.com/2020/08/02/2015-english-gce-o-l-past-papers/"
    "https://techforhack.com",
    "https://techforhack.com/84-woocommerce-extensions-updates/",
    "https://techforhack.com/56-woocommerce-extensions-updates/",
    "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
    "https://techforhack.com/elementor_pro_3-0-4_nulled/",
    "https://techforhack.com/adobe-cc-2020-universal-crack-for-adobe-cc-2020-full-version/",
    "https://techforhack.com/wireshark-termux/",
    "https://techforhack.com/windows-10-kali-linux-subsystem-full-tutorial/",
    "https://techforhack.com/tool-x/"
]

navigation_menu = [
    '/html/body/div[1]/div/header/div[2]/div/div[1]/div/div[1]/nav/ul/li[2]/a/span',
    '/html/body/div[1]/div/header/div[2]/div/div[1]/div/div[1]/nav/ul/li[3]/a/span',
    '/html/body/div[1]/div/header/div[2]/div/div[1]/div/div[1]/nav/ul/li[4]/a/span',
    '/html/body/div[1]/div/header/div[2]/div/div[1]/div/div[1]/nav/ul/li[5]/a/span'
]


def ran_time():
    sec = randint(2, 7)
    time.sleep(sec)


def loop():
    try:
        user_agent = ua.random
        chrm_options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=chrm_options)
        # driver.maximize_window()

        action_chains = ActionChains(driver)

        ran_link = random.choice(link)
        driver.get(ran_link)
        time.sleep(5)

        i = 0
        while i < 5:
            action_chains.reset_actions()
            action_chains.send_keys(Keys.PAGE_DOWN)
            action_chains.perform()
            time.sleep(1.5)
            i += 1
        ran_time()
        # ------------------------------------------------------------------------------------------------- Rolling Down

        # i = 0
        # while i < 5:
        #     action_chains.reset_actions()
        #     action_chains.send_keys(Keys.PAGE_UP)
        #     action_chains.perform()
        #     time.sleep(1)
        #     i += 1
        # ran_time()
        # # ------------------------------------------------------------------------------------------------- Rolling Up

        try:
            ran_expath = random.choice(navigation_menu)
            element = driver.find_element_by_xpath(ran_expath)
            element.click()

        except NoSuchElementException:
            sys.stdout.write("\r ------No Such Element!")

        time.sleep(5)
        driver.delete_all_cookies()
        driver.quit()

    except Exception as e:
        e = str(e)
        sys.stdout.write(e)


if __name__ == '__main__':
    print("Evil_Shade - Traffic Bot")
    print("##################################################################################")
    print("#                                                                                #")
    print("#                                                                                #")
    print("#                             Generate free traffic                              #")
    print("#                                                                                #")
    print("#                                                                                #")
    print("##################################################################################")

    view = 0
    print(view, " ------ View Generated")

    while True:
        view += 1
        loop()
        rem_view = str(view)
        sys.stdout.write('\r' + rem_view + " ------Views Completed")
