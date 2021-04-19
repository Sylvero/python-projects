from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import autoit
from LocalStorage import LocalStorage
import time


class Bot:
    def __init__(self):
        self.bot = webdriver.Chrome(executable_path=r'D:\projekty python\cookie\chromedriver.exe')




    def closeBrowser(self):
        self.bot.close()


    def checkUps(self):
            while True:
                list = self.bot.find_elements_by_xpath("//div[contains(@class, 'upgrade enabled')]")
                if len(list) !=0 :
                    list[0].click()
                    time.sleep(0.3)
                else:
                    break;

            while True:
                list = self.bot.find_elements_by_xpath("//div[contains(@class, 'product unlocked enabled')]")
                if len(list) != 0:
                    list[-1].click()
                    time.sleep(0.3)
                else:
                    break;



    def saveGame(self):
        file = open('save.txt', 'w')
        file.write(self.bot.execute_script('return localStorage.getItem("CookieClickerGame");'))
        file.close()
        print("Game saved")


    def loadSettings(self,choice):
        self.bot.get("https://orteil.dashnet.org/cookieclicker/")
        time.sleep(5)
        self.bot.find_element_by_partial_link_text("Got it").click()
        time.sleep(1)
        if choice == "n":
            self.bot.find_element_by_id('prefsButton').click()
            time.sleep(1)
            self.bot.find_element_by_partial_link_text("Load from file").click()
            time.sleep(1)
            autoit.win_wait_active("Otwieranie")
            autoit.send("D:\\projekty python\\cookie\\venv\\Include\\save.txt")
            autoit.send("{ENTER}")



            #print(self.bot.execute_script(" window.localStorage.getItem('CookieClickerGame')"))


    def click(self, temp):

        for i in range(10000000):
            self.bot.find_element_by_id("bigCookie").click()
            print(f'Clicked: {i}')
            if i == temp or len(self.bot.find_elements_by_xpath("//div[contains(@class, 'upgrade enabled')]")) !=0 :
                break;
            elif i % 50 == 0:
                try:
                    self.bot.find_element_by_class_name('shimmer').click()

                except:
                    pass


    def isNewGame(self):
        while True:
            choice = input("Do u wanna start new game? [y/n]\n")
            if choice in ("y,n"):
                break;
        return choice




def main():
    BotCookie =  Bot()
    choice = BotCookie.isNewGame()
    BotCookie.loadSettings(choice)
    temp = 3000
    while True:
        BotCookie.click(temp)
        BotCookie.checkUps()
        temp += 50
        BotCookie.saveGame()


if __name__ == '__main__': main()
