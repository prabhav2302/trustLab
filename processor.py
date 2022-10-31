from warcio.archiveiterator import ArchiveIterator
import re
import requests
import sys
from bs4 import BeautifulSoup


def checkCovid(contentString):
    covid_hitList = ['COVID-19', 'covid-19', 'COVID', 'coronavirus', 'Coronavirus']
    if any((match := substring) in contentString for substring in covid_hitList):
        return True 
    else:
        return False

def checkFinance(contentString):
    finance_hitList = ['economy', 'Economy', 'interest rate', 'Interest Rate', 'inflation', 'Inflation', 'fiscal', 'finance','Finance', 'recession', 'Recession', 'monetary policy']
    if any((match := substring) in contentString for substring in finance_hitList):
        return True 
    else:
        return False


f = open("demofile2.txt", "a")

## file_name = Specify any file name here 

if len(sys.argv) > 1:
    file_name = sys.argv[1]

stream = None
if file_name.startswith("http://") or file_name.startswith(
    "https://"
):
    stream = requests.get(file_name, stream=True).raw
else:
    stream = open(file_name, "rb")

validCounter = 0

for record in ArchiveIterator(stream):
    if record.rec_type == "warcinfo":
        continue

    if not ".com/" in record.rec_headers.get_header("WARC-Target-URI"):
        continue

    contents = (
        record.content_stream()
        .read()
        .decode("utf-8", "replace")
    )
    try:
        if contents:    
            soup = BeautifulSoup(contents, 'html.parser')
            # Use Beautiful Soup to just extract the text from the HTML file
            processed_text = soup.get_text()
            if processed_text: 
                if checkCovid(processed_text) and checkFinance(processed_text): #only add the URL to the list if the HTML text contains a word from both
                                                                                # the COVID hit list and the finance hit list
                    f.write(record.rec_headers.get_header("WARC-Target-URI")+"\n")
                    print(record.rec_headers.get_header("WARC-Target-URI"))
                    validCounter += 1
                    if validCounter >= 1000:                                    # choose how many lines of text you want to extract.     
                        f.close()    
                        exit()
    except:
        continue

      