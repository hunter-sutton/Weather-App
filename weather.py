import requests as reqs
from googlesearch import search
from bs4 import BeautifulSoup
import html5lib
import datetime
#from flask import Flask

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
def print_weather(main, location, curr_temp, curr_cond, weekly_forecast):
    print("\nCurrent Conditions at " + location + "\n")
    print(str(curr_temp) + " and " + curr_cond + "\n")
    today_date = str(datetime.date.today())
    for i in range(0,7):
        print("----------------------------------------")
        if (i == 0):
            print("Tonight's Forecast (" + today_date + ")\n")
            print(weekly_forecast[0].get_text())
        if (i == 1):
            #tomorrow_date = str(datetime.datetime.today() + datetime.timedelta(days=1))
            print("Tomorrow's Forecast (Day " + str(i) + ")\n")
            print(weekly_forecast[1].get_text())
        if (i > 1):
            print("Forecast for Day " + str(i) + "\n")
            print(weekly_forecast[i].get_text())

#retrieves the 7 day forecast and stores it as a list of strings
def get_weather(main):
    location = main.find('h2', class_='panel-title').get_text()
    curr_cond = main.find('p', class_='myforecast-current').get_text()
    curr_temp = main.find('p', class_='myforecast-current-lrg').get_text()
    weekly_forecast = main.find_all('div', class_='col-sm-10 forecast-text')
    print_weather(main, location, curr_temp, curr_cond, weekly_forecast)

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
        print("----------------------------------------")
        choice = ""
        choice = input("\nWould you like to look up another location? (y/n): ")
        if(choice == 'y'):
            print("----------------------------------------")
            return True
        if(choice == 'n'):
            return False
        else:
            print("\nERROR: Invalid Input\n")

#def write_file():
    #open a new file on the desktop
    #fill the file with new forecast info, weekly

#loop for program run
def app_run():
    quit = False

    while (quit == False):
        #gets the weather.gov URL of desired location
        URL = get_url()

        #parses the html tree and finds main
        main = nav_html()

        #finds weather and prints it neatly-ish
        get_weather(main)

        #check if the user wants to search again
        if(run_again() == False):
            quit = True

#flask stuff
#app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Welcome"