'''
pip install plyer
Need to convert png images to ico format image
To get data about virus cases all over india, visit:https://www.mohfw.gov.in/
Install beautifulSoup : pip install bs4
'''
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


#Need to convert png images to ico format image
def notifyMe(title,message):
    notification.notify(
        title= title, 
        message=message,
        app_icon="D:/Python_Tutorial/Python_Projects/Images/icon.ico",
        timeout=15)

#to get data from specified url
def getData(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    while True:
        notifyMe("Sunanda", "Lets stop the spread of Corona Virus together")
        myHtmlData=getData("https://www.mohfw.gov.in/")

        #print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())#displays the data
        myDataStr=""
        table = soup.find('table', attrs={'class':'lineItemsTable'})
        table_body = soup.find('tbody') 
        rows = soup.find('tr')
        for tr in rows:
            cols = tr.find_all('td')
            myDataStr += cols.get_text()
            #print(tds[0].text)
        
            myDataStr=myDataStr[1:]
            itemlist=myDataStr.split("\n\n")

            states=['Goa','Karnataka','Maharashtra']
            for item in itemlist[0:21]:
                #print(item.split("\n"))
                dataList=item.split("\n")
                if dataList[1] in states:
                    print(dataList)
                    nTitle='Cases of Covid-19'
                    nText=f"{dataList[1]} : Indian :{dataList[2]} & Foreign:{dataList[3]}\n Cured:{dataList[4]}\nDeaths:{dataList[5]}"
                    notifyMe(nTitle,nText)
                    time.sleep(2)
            time.sleep(3600)
        

    
    
