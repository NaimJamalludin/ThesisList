from bs4 import BeautifulSoup
from pathlib import Path
import urllib.request
import os
import xlsxwriter

counter = 0
thesisFile = os.path.join(Path.cwd(), 'Data', 'CompScience.txt')

# Delete file if already exists
if os.path.exists(thesisFile):
    os.remove(thesisFile)

# Loop through 43 pages
for x in range(1, 43):

    print('Going through page: ' + str(x))

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
            anchor = div.find("a",attrs={"class":"normlink"})["title"]
            f.write(str(counter) + ". " + anchor + "\n")            

print('Completed')
