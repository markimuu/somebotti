from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Instagram:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(3)
        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.email)
        time.sleep(2)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def closeBrowser(self):
        self.bot.close()

    def FollowAndLikeTag(self, tag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/"+tag)
        time.sleep(3)
        followButton = bot.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            time.sleep(2)
        else:
            print("Seuraat jo tätä käyttäjää")
        for i in range(1, 2):
            bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
        pictures = bot.find_elements_by_tag_name("a")
        links = [elem.get_attribute("href") for elem in pictures]
        print(links)
        for link in links:
            bot.get(link)
            try:
                bot.find_element_by_xpath(
                    '//button[@class="dCJp8 afkep"]//span[@aria-label="Like"]').click()
                time.sleep(20)
            except Exception as ex:
                print("Ei löytynyt tykkäys painiketta tai sitä on jo painettu")
                time.sleep(5)


email = input("Käyttäjätunnus: ")
salasana = input("Salasana: ")
otsikko = input("Anna aihe tai hashtag: ")

botti = Instagram(email, salasana)
botti.login()
time.sleep(5)
botti.FollowAndLikeTag(otsikko)
botti.closeBrowser()
