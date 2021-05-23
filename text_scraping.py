from urllib.request import urlopen as urlreq
from bs4 import BeautifulSoup as soup

page = 'https://bluelimelearning.github.io/my-fav-quotes/'
client =   urlreq(page)
page_html = client.read()
client.close()

page_soup = soup(page_html, "html.parser")
quotes = page_soup.findAll("div", {"class" : "quotes"})

# print(quotes[1])
print(' '*30, page_soup.h1.text.strip())

quotes_list = []
authors_list = []

for quote in quotes:
    fav_quote = quote.findAll("p" , {"class" : "aquote"})
    aquote = fav_quote[0].text.strip()
    quotes_list.append(aquote)

    fav_authors = quote.findAll("p" , {"class" : "author"})
    author = fav_authors[0].text.strip()
    authors_list.append(author)


# print(quotes_list)
# print(author_list)

Quotes = list(zip(quotes_list,authors_list))
# print(Quotes)

for i in Quotes:
    print("\n Quuote : {} \n [Author : {}]". format(i[0], i[1]))



