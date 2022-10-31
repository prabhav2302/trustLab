# trustLab

Reflection:

## Step 1 - Accessing Data
So, initially I began the task extremely overwhelmed as I had never interacted with the .WARC data format before and I was not able to access the data using the template python script provided. However, after reading the warcio Python library documentation (https://github.com/webrecorder/warcio) and doing some additional debugging, I was able to access the data and understand the basics of the .WARC file format. 

## Step 2 - Processing Data
In order to extract the URL's that only discuss the economic impact of COVID I came up with the idea of creating two lists. The first list is called covid_hitList. Here is the covid_hitList 

covid_hitList = ['COVID-19', 'covid-19', 'COVID', 'coronavirus', 'Coronavirus']). 

The second list I created was called  finance_hitList. Here is the finance_hitList 

finance_hitList= ['economy', 'Economy', 'interest rate', 'Interest Rate', 'inflation', 'Inflation', 'fiscal', 'finance','Finance', 'recession', 'Recession', 'monetary policy']

My approach to the problem is that I would iterate through each url in the commoncrawl dataset, get the HTML content of the URL, and see if it contained a word from the covid_hitList AND the finance_hitList. I reasoned that if it contained a word from both lists this must mean that the url contains content related to the economic impact of COVID.

## Step 3 - Enhancing Model

After I ran the program, I noticed I was getting the URLs to a lot of irrelevant sites. One of the URLs for example just contained content about sports but had a link to COVID news and a link to Finance news and therefore it was getting included in my output URL list. I then realized that instead of searching the content of the whole HTML Page, which includes irrelevant <a> (hyperlink), <form> (form). I just want the text content of the HTML page. Not the hrefs, and etc. In order to just extract the text part of the page I used the BeautifulSoup python library (a HTML processing library) which goes in and extracts just the text part of the HTML. After I added this modification, the program became much much slower but was giving much better results.
