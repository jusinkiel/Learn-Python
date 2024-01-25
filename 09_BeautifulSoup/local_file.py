from bs4 import BeautifulSoup
from pathlib import Path
contents = Path('/Users/justinkielpascualmontano/Downloads/Learn-Python/11_HTML/learn.html').read_text()



html = BeautifulSoup(contents, 'html.parser')

# title = html.select("#firstHeading")[0].text
paragraphs = html.select("p")

print(paragraphs[1])

# for para in paragraphs:
#     print (para.text)


