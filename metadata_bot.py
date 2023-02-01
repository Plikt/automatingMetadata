import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

url = "https://arxiv.org/abs/2212.11181"

options = Options()
options.add_experimental_option("detach", True) #keeps window open
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)

driver.get(url)
session = requests.Session()
response = session.get(url)

#enable Bibliogrpahic Explorer
class_name = driver.find_element("xpath", "//div[@class='tab labs-display-bib']//div[@class='toggle']//div[1]//div[1]//label[1]//span[1]")
class_name.click()
time.sleep(1)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the authors -------------------------
authors = [a.text for a in soup.find_all('div', class_='authors')]

# Extract the abstract -------------------------
abstract = soup.find('blockquote', class_='abstract mathjax')

# Extract the citations -------------------------
references = []
nonMLA_references = []
bibTeX_references = []

#number of references
total_references = 1

while (True):
    #checks to see how many citations are on the page
    try:
        #checks for all citations
        references_containers = driver.find_element("xpath", "/html/body/div[2]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[%s]" % total_references)

        #outputs all citations on the page that can be shown in MLA format
        try:
            #click on reference
            references_containers = driver.find_element("xpath", "//div[@class='bib-col2']//div[%s]//div[1]//div[1]//span[1]//a[1]//img[1]" % total_references)
            references_containers.click()
            time.sleep(1)

            #click MLA button
            references_containers = driver.find_element("xpath", "//input[@id='mla']")
            if references_containers.is_enabled():
                references_containers.click()
                time.sleep(1)
            
            #If MLA button is unavailable -> send to bibTeX_references
            else:
                references_containers = driver.find_element("xpath", "/html/body/div[2]/main/div/div/div[2]/div[7]/div/div/div[3]/textarea")
                bibTeX_references.append(references_containers.text)

            #get citation
            references_containers = driver.find_element("xpath", "/html/body/div[2]/main/div/div/div[2]/div[7]/div/div/div[3]/textarea")
            references.append(references_containers.text)

            #close citation
            references_containers = driver.find_element("xpath", "/html/body/div[2]/main/div/div/div[2]/div[7]")
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, references_containers)
            
            total_references += 1

        #runs when reference is unavailable
        except:
            #outputs non MLA citation
            references_containers = driver.find_element("xpath", "/html/body/div[2]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[%s]/div[2]/div[1]/a" % total_references)
            nonMLA_references.append(references_containers.text)
            total_references += 1

    #outputs total number of ciations
    except:
        total_references = 1
        try:
            page_number = driver.find_element("xpath", "/html/body/div[2]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div/span/ul/li[6]/a")
            page_number.click()
        except:
            break


print('Authors:', authors)
print('#############################')
print('Abstract:', abstract.text)
print('#############################')
print('References:', references)
print('#############################')
print('Non MLA References:', nonMLA_references)
print('#############################')
print('BibTeX References:', bibTeX_references)