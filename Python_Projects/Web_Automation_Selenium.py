from selenium import webdriver

class Music:
    def __init__(self):
        self.driver=webdriver.Chrome(r"C:\Users\DELL\Desktop\chromedriver.exe")
        
    def play(self):
        name=input("ENter youtuber name:")
        self.driver.get("https://www.youtube.com/user/"+name+"/videos")
        a=self.driver.find_element_by_xpath('//*[@id="thumbnail"]')
        a.click()
        
bot=Music()
bot.play()