# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO DEMONSTRATE INSTAGRAM SCRAPING USING BeautifulSoup

# Web scraping is a computer software technique of extracting information
# from websites.

# Beautiful Soup is a library that makes it easy to scrape information from
# web pages. It sits atop an HTML or XML parser, providing Pythonic idioms
# for iterating, searching, and modifying the parse tree.
# The module can be installed using - pip install beautifulsoup4

# In the following script, INSTAGRAM SCRAPING is done with the user-input
# Instagram Username to find the number of POSTS, FOLLOWERS & FOLLOWING of
# the Instagram user

# Importing the necessary packages
import requests
from bs4 import BeautifulSoup

#---

# Defining the scrapeInstagram() with the soup1 as the argument
def scrapeInstagram(soup1):
    # Creating empty list called insta_Data for saving the scrapped results
    insta_Data = []

    # Looping through the <meta> tags with attribute propety as og:description
    for meta in soup1.find_all(name="meta", attrs={"property": "og:description"}):
        # Fetching and splitting the value stored in content attribute of meta tag
        # and saving them in insta_Data List
        insta_Data = meta['content'].split()

    # When the above line is executed insta_Data[] will be as follows
    # ['No. of Followers (For e.g. 50K)', 'Followers,', 'No. of Following (For e.g. 100)', 'Following,',
    # 'No. of Posts (For e.g. 150)', 'Posts', '-', .........]

    # Fetching the required results (Followers, Following, Posts) as per the indices
    # and storing them in respective variables
    followers = insta_Data[0]
    following = insta_Data[2]
    posts = insta_Data[4]

    # Printing the results
    print("\nINSTAGRAM USERNAME :   ", insta_User)
    print("\nNo OF POSTS        :   ", posts)
    print("\nNo OF FOLLOWERS    :   ", followers)
    print("\nNo OF FOLLOWING    :   ", following)

#---

# Driver Code
if __name__ == '__main__':

    # Prompting the user to enter the INSTAGRAM USERNAME
    insta_User = input("\nENTER INSTAGRAM USERNAME : ")

    # Storing the complete URL with user-input INSTAGRAM USERNAME
    insta_URL = "https://www.instagram.com/" + insta_User

    # Sending request to the above URL and storing the response in insta_Page
    insta_Page = requests.get(insta_URL)

    # Specifying the desired format of the insta_Page using html.parser
    # html.parser allows Python to read the components of the insta_Page rather
    # than treating it as a string
    soup = BeautifulSoup(insta_Page.text, "html.parser")

    # Calling the scrapeInstagram() with soup as the argument
    scrapeInstagram(soup)

#---