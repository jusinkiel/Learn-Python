import requests
from bs4 import BeautifulSoup

wiki = input('Enter the wiki:')

url = "https://en.wikipedia.org/wiki/{urllib.parse.quote(wiki)}"
response = requests.get(url)

# response = None

if response is not None:
    html = BeautifulSoup(response.text, 'html.parser')

    title = html.select("#firstHeading")[0].text
    paragraphs = html.select("p")
    for para in paragraphs:
        print (para.text)

    # just grab the text up to contents as stated in question
    intro = '\n'.join([ para.text for para in paragraphs[0:5]])
    print (intro)