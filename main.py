import requests
import html5lib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def mysb():
    driver = webdriver.Chrome('C:\Users\GRANITE\Desktop\chromedriver.exe')
    driver.get('www.facebook.com')
    elem = driver.find_element_by_id('email')
    elem.send_keys('munmridul@gmail.com')
    elem.send_keys(Keys.RETURN)
    assert "no results found " in driver.page_source
    driver.close()
    



def github():
    URL = 'https://github.com/Mridul98/AI-Reference-Papers'
    req = requests.get(URL)
    bs = BeautifulSoup(req.content,features='html5lib')
    resultset = bs.find_all('a')
    counter = 0
    for links in resultset:
        res = links['href']
    
        if( res.startswith('https') and res.endswith('.pdf')):
    #    https://github.com/Mridul98/AI-Reference-Papers/raw/master/afl(1).pdf
            res = res.replace('blob','raw')
            res = res.replace('manjunath5496','Mridul98')
            print(res)
            dl = requests.get(res)
            print(dl.headers)
            file = 'paper'+str(counter)+'.pdf'
            open(file,'wb').write(dl.content)
        
        
            counter = counter+1
            
mysb()
    

        