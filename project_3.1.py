import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/2021/02/23/opinion/britney-spears-mara-wilson-hollywood.html?action=click&module=Opinion&pgtype=Homepage'

response = requests.get(url)
text = response.text

# wfh = open('../article.html', 'w')
# wfh.write(text)
# wfh.close()
#scrapee = '../article.html'

soup = BeautifulSoup(text, 'html.parser')

ti = soup.title.text                    #title is easy bc it's its own tag

by = soup.find('meta', {'name': 'byl'}) #search the meta tags for one named 'byl'
by = by['content']                      #in the meta tag called 'byl' print its 'content'

dt = soup.find('meta', {'property': 'article:published_time'})
dt = dt['content']                      #in the meta tag w the 'article:published_time' property, print its content
dt = dt[0:10]                           #then print the first 10 characters in that tag's string

ps = soup.find_all('p',{'class': "css-axufdj evys1bk0"})                 #find all of the paragraphs, the 'p' tagged objects
counter = []                            #create an empty list so we can count the paragraphs
for p in ps:                            #for loop: counting each paragraph in total paragraphs
    counter.append(p)                   # add each paragraph to 'counter' list
pcount = len(counter)                   # length of the counter list = # of paragraphs or p tags

p3 = counter[6]
p3 = p3.text

print(f'Title: {ti}')
print(f'Byline: {by}')
print(f'Date: {dt}')
print(p3)
print(f'[{pcount} text paragraphs total ]')

