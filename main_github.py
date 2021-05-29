

from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import datetime as dt

now = str(dt.datetime.now())
top = now.split(":")
top_hour = int(top[1][0:2])
print(top_hour)

my_email = "thegoldenspruce@gmail.com"
password = "redacted"

header = {
	"User-Agent": "Chrome/90.0.4430.93",
	"Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
    #"Content-Type": "application/json",
}

#this would be for a local file
#with open(amazon.text) as file:
#    contents = file.read()
#soup = BeautifulSoup(contents,"html.parser")


url = "https://www.amazon.com/Instant-One-Touch-Multi-Use-Programmable-Pressure/dp/B07RCNHTLS/"
amazon = requests.get(url, headers=header)
soup = BeautifulSoup(amazon.text,"lxml")
#print(soup.title)
#print(soup.title.name)
#print(soup.prettify())

#print(soup.text.find("Price:"))
#split = soup.text.split("Price:")
#split2 = split[1].split(" ")
#print(split2)

product = soup.find(id="productTitle").get_text().strip()
print(product)

BUY_PRICE = 200
try:
	dollar_price = soup.find(id="priceblock_ourprice").get_text().strip()
	price = dollar_price[1:]
	price_as_float = float(price)
	message = f"Instapot: {dollar_price}"
	available = True
except:
	available = False
	message = "Not available"

if available and price_as_float < BUY_PRICE:
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(my_email,password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs="robert.lee@berkeley.edu",
			msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
			)

# my_email = "thegoldenspruce@gmail.com"
# password = "redacted"

# header = {
# 	"User-Agent": "Chrome/90.0.4430.93",
# 	"Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
#     #"Content-Type": "application/json",
# }

# #this would be for a local file
# #with open(amazon.text) as file:
# #    contents = file.read()
# #soup = BeautifulSoup(contents,"html.parser")


# url = "https://www.amazon.com/Instant-One-Touch-Multi-Use-Programmable-Pressure/dp/B07RCNHTLS/"
# amazon = requests.get(url, headers=header)
# soup = BeautifulSoup(amazon.text,"lxml")
# #print(soup.title)
# #print(soup.title.name)
# #print(soup.prettify())

# #print(soup.text.find("Price:"))
# #split = soup.text.split("Price:")
# #split2 = split[1].split(" ")
# #print(split2)

# product = soup.find(id="productTitle").get_text().strip()
# print(product)

# BUY_PRICE = 200

# loop = True
# while loop:
# 	now = str(dt.datetime.now())
# 	top = now.split(":")
# 	top_hour = int(top[1][0:2])
# 	#print(top_hour)

# 	if top_hour == 27:

# 		try:
# 			dollar_price = soup.find(id="priceblock_ourprice").get_text().strip()
# 			price = dollar_price[1:]
# 			price_as_float = float(price)
# 			message = f"Instapot: {dollar_price}"
# 			available = True
# 		except:
# 			available = False
# 			print("Not available")

# 		if available and price_as_float < BUY_PRICE:
# 			with smtplib.SMTP("smtp.gmail.com") as connection:
# 				connection.starttls()
# 				connection.login(my_email,password)
# 				connection.sendmail(
# 					from_addr=my_email,
# 					to_addrs="robert.lee@berkeley.edu",
# 					msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
# 					)
# 				loop = False
