"""
Scraping news website --- WASHINGTON POST , THE HINDU
"""

# Importing required libraries
import requests
from bs4 import BeautifulSoup

# Creating an Exception class name ServerNotFound
class ServerNotFound(Exception):
    """ Raises when website server did not respond """
    pass


def get_data(url,header):
    
    # Making HTTP request and downloading the response in "response" variable
    response = requests.request("GET",url, headers=header)

    if not response:
        print("\nServerNotFound")
    
    else:
        
        # Parse the html code from the downloaded response
        data = BeautifulSoup(response.text,'html.parser')
        return data
    return None


# Scraping the title of the page

def scrap_title(data):
        
    print("\n\n-------TITLE OF THE ARTICLE-------\n\n")
    scraped_title = data.head.title.string
    print(scraped_title)
    return scraped_title


# Scraping the Author name

# For WASHINGTON POST---
def scrap_auth_name(data):

    auth_name = data.find('a', attrs = {'class','gray-darkest b bb bc-gray bt-hover'})
    print("\n\nAuthor: ",auth_name.text)
    return auth_name.text

# For THE HINDU---
# def scrap_auth_name(data):

#     auth_name = data.find('a', attrs = {'class','auth-nm lnk'})
#     print("\n\nAuthor: ",auth_name.text)
#     return auth_name.text


# Scraping the date on which it last time updated

# For WASHINGTON POST---
def scrap_date(data):

    updt_date = data.find('span', attrs={'data-qa','display-date'})
    print("\n\nUpdated on: ",updt_date.text)
    return updt_date.text

# For THE HINDU
# def scrap_date(data):

#     updt_date = data.find('none')
#     print("\n\nUpdated on: ",updt_date.text)
#     return updt_date.text


# Scraping the Article Intro

def scrap_intro(data):
    
    intro = data.find('h2')
    print('\n\n--------Intro of Article-------\n\n',intro.text)
    return intro.text


# Scraping the Article content

def scrap_cont(data):
    
    content = data.find_all('p')
    print('\n\n-------------Content--------------\n\n')

    for para in content:
        
        cont_txt = para.text
        cont_txt += "\n"
        print(cont_txt)
    return cont_txt

if __name__=="__main__":
    
    #------ URL to Scrap -------
   
    #url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"
    url = # 'url'
   
    # Header of Your Browser is required
    # Example: "User-Agent": "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203 (Edition Campaign 34)"
    header = {
        #'User-Agent': "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203 (Edition Campaign 34)"
        # Your User-Agent or if same then uncomment the above line 
        }

    # First Making request and getting the data
    req_data = get_data(url, header)
    
    # Second getting title
    art_title = scrap_title(req_data)
    
    # Getting Author name
    art_auth = scrap_auth_name(req_data)
    
    # Getting Last Update date
    art_update = scrap_date(req_data)
    
    # Getting INTRO
    art_intro = scrap_intro(req_data)
    
    # Getting CONTENT
    art_cont = scrap_cont(req_data)



