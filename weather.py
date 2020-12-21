import requests as reqs
from googlesearch import search
from bs4 import BeautifulSoup
import html5lib

#gets desired url
def get_url():
    print()
    place = input("Enter a location in the U.S. (city + state or ZIP code): ")
    query = place + " site:weather.gov"
    URL = ""
    for j in search(query, tld="com", num=1, stop=1, pause=2):
        URL = j
    return URL

#searches for the weather in the html tree
#prints the current temp and forecast for today
def print_weather(main):
    curr_temp = main.find('p', class_='myforecast-current-lrg').get_text()
    tonight_forecast = main.find('div', class_='col-sm-10 forecast-text').get_text()
    print("\nThe current temperature is " + curr_temp)
    print("\nTonight's Forecast:")
    print(tonight_forecast)
    print()

#navigates through html tree and finds main section of html tree
def nav_html():
    r = reqs.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    html = list(soup.children)[1]
    body = list(html.children)[2]
    main = list(body.children)[1]
    return main

def run_again():
    n = False
    while(n == False):
        choice = ""
        choice = input("Would you like to look up another location? (y/n): ")
        if(choice == 'y'):
            return True
        if(choice == 'n'):
            return False
        else:
            print("\nERROR: Invalid Input\n")


#loop for program run
quit = False

while (quit == False):
    #gets the weather.gov URL of desired location
    URL = get_url()

    #parses the html tree and finds main
    main = nav_html()

    #finds weather and prints it neatly-ish
    print_weather(main)

    #check if the user wants to search again
    if(run_again() == False):
        quit = True