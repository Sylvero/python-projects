from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import signal
import time
import datetime


class TeamsBot:
    def __init__(self, username, passwd):
        self.bot = webdriver.Chrome(executable_path=r'path_to_driver')
        self.username = username
        self.passwd = passwd
        self.lecturesDict = {
            "name_of_lecture": ["Day","hour","mins"],
        }



    def login(self):
        self.bot.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=dc935f7d-329d-420f-b1d3-2e5f354944d1&client-request-id=ec5480db-3e08-45be-b5c1-e9342e47dc04&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=be045bf3-ff7f-4132-9d5b-fa9bab5c6275&domain_hint=&sso_reload=true")
        self.bot.maximize_window()
        time.sleep(1)
        login = self.bot.find_element_by_xpath(".//*[@id='i0116']")
        login.clear()
        login.send_keys(self.username)
        time.sleep(1)
        self.bot.find_element_by_id('idSIButton9').click()
        time.sleep(4)
        passwd = self.bot.find_element_by_xpath(".//*[@id='i0118']")
        time.sleep(1)
        passwd.clear()
        passwd.send_keys(self.passwd)
        self.bot.find_element_by_id('idSIButton9').click()
        time.sleep(2)
        self.bot.find_element_by_id('idBtn_Back').click()
        time.sleep(25)
        self.bot.find_element_by_xpath("//button[@title='Odrzuć']").click()





    def getDate(self):
        now = datetime.datetime.now()
        curDay = now.strftime("%A")
        curHour = time.strftime("%H")
        curMinutes = time.strftime("%M")
        return curDay,int(curHour),int(curMinutes)



    def joinMeeting(self):
        print("I'm going to the meeting...")
        time.sleep(2)
        while True:
            try:
                elem = self.bot.find_elements_by_class_name("icons-call-jump-in")
                if len(elem) != 0:
                    self.bot.find_element_by_class_name("icons-call-jump-in").click()
                    break

            finally:
                time.sleep(2)

        time.sleep(3)
        join = self.bot.find_element_by_class_name("join-btn")
        self.bot.execute_script("arguments[0].click();", join)
        time.sleep(3)
        #self.bot.find_element_by_class_name("icons-start-conversation").click()
        time.sleep(2)
        try:
            icon = self.bot.find_element_by_class_name("icons-close")
            self.bot.execute_script("arguments[0].click();", icon)
        finally:
            time.sleep(2)


    def exitMeeting(self):
        members = self.bot.find_element_by_id("roster-button")
        self.bot.execute_script("arguments[0].click();", members)
        time.sleep(180)
        print("I'm waiting for leaving the meeting...")
        while True:
            time.sleep(2)
            try:
                number = self.bot.find_elements_by_xpath("//button[@class='roster-list-title']")[1].text
                temp = str(number)
                #print(temp)
                x = temp.split()
                if int(x[-1].strip("()")) <= 70:
                    print("Less than 70 people, I'm leaving...")
                    break
            finally:
                time.sleep(2)


        time.sleep(2)
        end = self.bot.find_element_by_id("hangup-button")
        self.bot.execute_script("arguments[0].click();", end)
        time.sleep(3)

        try:
            list2 = self.bot.find_elements_by_class_name("icons-call-end")
            if len(list2) == 0:
                print("Finish!")
                self.bot.close()
                self.bot.quit()

        finally:
            time.sleep(1)




    def searchTeam(self):
        currMeeting = ""
        day, hour, minutes = self.getDate()
        print(f'Day {day} Hour {hour}:{minutes}')
        temp = 0
        time.sleep(2)
        while True:
            day, hour, minutes = self.getDate()
            for i, [j,k] in enumerate(self.lecturesDict.items()):
                #print("index: {}, key: {}, value: {}".format(i, j, k))
                if day == k[0] and hour >= k[1] and hour < k[1]+1 :
                    currMeeting = j
            if currMeeting != "":
                break
        list = self.bot.find_elements_by_class_name("team-name-text")
        for i, name in enumerate(list):
            print(f'{i + 1}: {name.text}')
            if name.text == currMeeting:
                time.sleep(2)
                list[i].click()
                break








Bot = TeamsBot("login", "pass")
Bot.login()
Bot.searchTeam()
Bot.joinMeeting()
Bot.exitMeeting()
