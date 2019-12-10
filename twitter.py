from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Twitter:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/")
        time.sleep(3)
        email = bot.find_element_by_class_name("email-input")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.email)
        time.sleep(2)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def likeTweets(self, tag, scrollausmaara):
        bot = self.bot
        bot.get("https://twitter.com/search?q=%23"+tag+"&src=typeahead_click")
        time.sleep(3)
        for i in range(1, int(scrollausmaara)):
            bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
        tweets = bot.find_elements(
            By.XPATH, '//*[@data-testid="tweet"]//a[@dir="auto"]')
        print(tweets)
        links = [elem.get_attribute("href") for elem in tweets]
        print(links)
        for link in links:
            bot.get(link)
            time.sleep(5)
            try:
                bot.find_element_by_xpath(
                    '//div[@data-testid="like"]').click()
                time.sleep(20)
            except Exception as ex:
                print("Tapahtui virhe")
                time.sleep(60)

    def likePerson(self, tag):
        bot = self.bot
        bot.get("https://twitter.com/search?q="+tag+"&src=typed_query&f=user")
        time.sleep(3)
        ids = bot.find_elements_by_xpath('//*[@data-testid]')
        links = [elem.get_attribute("data-testid") for elem in ids]
        print(links)
        remove_link = ["UserCell", "trend", "caret", 'sidebarColumn', "AppTabBar_Home_Link", 'AppTabBar_Explore_Link', 'AppTabBar_Notifications_Link',
                       'AppTabBar_DirectMessage_Link', 'AppTabBar_More_Menu', 'SideNav_NewTweet_Button', 'primaryColumn', 'SearchBox_Search_Input']
        new_links = [word for word in links if word not in remove_link]
        print(new_links)
        for link in new_links:
            try:
                bot.find_element_by_xpath(
                    '//div[@data-testid="%s"]' % link).click()
                time.sleep(10)
            except Exception as ex:
                print("Virhe")
                time.sleep(60)


email = input("Käyttäjätunnus: ")
salasana = input("Salasana: ")

otsikko = input("Anna aihe tai hashtag: ")
toiminto = input(
    "Tykätäänkö twiiteistä vai seurataanko henkilöitä? (Vastaa: 'tykkaa' tai 'seuraa'): ")

if toiminto == "tykkaa":
    sivumaara = input("Kuinka monta sivua ladataan? (vastaus numerona): ")
    botti = Twitter(email, salasana)
    botti.login()
    time.sleep(5)
    botti.likeTweets(otsikko, sivumaara)

if toiminto == "seuraa":
    botti = Twitter(email, salasana)
    botti.login()
    time.sleep(5)
    botti.likePerson(otsikko)

#python, selenium (pip), geckodriver
