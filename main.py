from bs4 import BeautifulSoup
from pathlib import Path
import urllib.request
import os
import csv

def getFCSIT():

    counter = 0
    thesisFile = os.path.join(Path.cwd(), 'Data', 'Faculty-of-Computer-Science-and-Information-Technology.csv')

    # Delete file if already exists
    if os.path.exists(thesisFile):
        os.remove(thesisFile)

    # Loop through 43 pages
    for x in range(1, 43):

        print('Going through FCSIT page: ' + str(x))

        # URL link
        url = "http://www.diglib.um.edu.my/umtheses/browse.asp?page=%s&level=all&faculty=W&year=all#sthash.RhHcqyBk.dpbs"%(x)
        
        # Get the site content
        content = urllib.request.urlopen(url).read()

        # Parse the HTML
        soup = BeautifulSoup(content, "html.parser")

        # Find the div
        mydivs = soup.find_all("div", {"class": "commentbox"})

        # Loop through the div
        for div in mydivs:

            # Open and write into the file
            counter = counter + 1
            with open(thesisFile, 'a') as f:
                fw = csv.writer(f, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fw.writerow([counter, div.find("a",attrs={"class":"normlink"})["title"]])      

    print('Completed FCSIT')

def getAIS():

    counter = 0
    thesisFile = os.path.join(Path.cwd(), 'Data', 'Academy-of-Islamic-Studies.csv')

    # Delete file if already exists
    if os.path.exists(thesisFile):
        os.remove(thesisFile)

    # Loop through 85 pages
    for x in range(1, 85):

        print('Going through AIS page: ' + str(x))

        # URL link
        url = "http://www.diglib.um.edu.my/umtheses/browse.asp?page=%s&level=all&faculty=I&year=all#sthash.64ZnOUYX.dpbs"%(x)
        
        # Get the site content
        content = urllib.request.urlopen(url).read()

        # Parse the HTML
        soup = BeautifulSoup(content, "html.parser")

        # Find the div
        mydivs = soup.find_all("div", {"class": "commentbox"})

        # Loop through the div
        for div in mydivs:

            # Open and write into the file
            counter = counter + 1
            with open(thesisFile, 'a') as f:
                fw = csv.writer(f, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fw.writerow([counter, div.find("a",attrs={"class":"normlink"})["title"]])      

    print('Completed AIS')

getAIS()
getFCSIT()
