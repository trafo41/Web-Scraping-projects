import requests
from bs4 import BeautifulSoup as soup
import smtplib

url = "https://www.amazon.in/OnePlus-Nord-Marble-256GB-Storage/dp/B0869855B8/ref=sr_1_1?dchild=1&qid=1621789913&refinements=p_89%3AOnePlus&s=electronics&sr=1-1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66"}

price_value =  25999
email_address = "jagveeryadav041@gmail.com"
password = "test@pswd"                                # enter your account password here
receiver_mail = "jagveeryadav1299@gmail.com"


def get_price():
    page = requests.get(url, headers=headers)
    Soup = soup(page.content, 'html.parser')
    title = Soup.find(id = 'productTitle').get_text().strip()
    price = Soup.find(id = "priceblock_dealprice").get_text().split('.')[0]
    remove_currency_sign = ''.join(list(price)[2:])
    Price = ''.join(remove_currency_sign.split(','))
    print("Product : ", title)
    print("Current price :", float(Price))
    return Price


def sendmail():
    subject = "OnePlus Nord 5G price dropped"
    mailtext = 'Subject:'+subject+'\n\n'+url
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(email_address, password)
    server.sendmail(email_address, receiver_mail, mailtext)


def trackprice():
    price = float(get_price())
    if price >= price_value:
        print("Product price is still above your bid.")
    else:
        print("Price dropped, Notifying...")
        sendmail()

if __name__ == "__main__":
    trackprice()
    # get_price(  )