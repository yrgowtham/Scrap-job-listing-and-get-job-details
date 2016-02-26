import requests
from  bs4 import BeautifulSoup
def doctor():
    url = "https://www.practicematch.com/physicians/search-results.cfm"   #website to scrap
    sourcecode = requests.get(url)
    plaintext = sourcecode.text
    soup = BeautifulSoup(plaintext)
    i=0
    for link1 in soup.findAll('li', {'class': 'even'}):
            for link2 in link1.findAll("a"):
                print("Link : "+"https://www.practicematch.com"+link2.get("href"))
                for link3 in link2.findAll('p'):
                  title = link3.string
                  print(title)
            sourcecode = requests.get("https://www.practicematch.com"+link2.get("href"))
            plaintext = sourcecode.text
            soup1 = BeautifulSoup(plaintext)
            print('\033[1m'+"Job Name"+'\033[0m')
            for link1 in soup1.findAll('div',{'class':'pageHeader'}):
                print(link1.string)
            print('\033[1m'+"Job Description"+'\033[0m')
            for link1 in soup1.findAll('div',{'class':'section','id':'Section1'}):
                for link1 in link1.findAll('p'):
                    print(link1.string)
            print('\033[1m'+"Contact"+'\033[0m')
            for link1 in soup1.findAll('td',{'class':'info'}):
                for link1 in link1.findAll('a'):
                    print(link1.get("href"))

            print("**************************************************************************************************************************************************************************************************************************")
    for link7 in soup.findAll('li',{'class':''}):
      for link2 in link7.findAll("a"):
            print("Link : "+"https://www.practicematch.com"+link2.get("href"))
            for link3 in link2.findAll('p'):
                title = link3.string
                print(title)
            sourcecode = requests.get("https://www.practicematch.com"+link2.get("href"))
            plaintext = sourcecode.text
            soup = BeautifulSoup(plaintext)
            print('\033[1m'+"Job Name"+'\033[0m')
            for link1 in soup.findAll('div',{'class':'pageHeader'}):
                print(link1.string)
            print('\033[1m'+"Job Description"+'\033[0m')
            for link1 in soup.findAll('div',{'class':'section','id':'Section1'}):
                for link1 in link1.findAll('p'):
                    print(link1.string)
            print('\033[1m'+"Contact"+'\033[0m')
            for link1 in soup.findAll('td',{'class':'info'}):
                for link1 in link1.findAll('a'):
                    print(link1.get("href"))
            print("**************************************************************************************************************************************************************************************************************************")

doctor()
