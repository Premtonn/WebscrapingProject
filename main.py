from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import lxml


zillow = "https://www.zillow.com/seattle-wa/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Seattle%2C%20WA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.88449936914064%2C%22east%22%3A-121.80509263085939%2C%22south%22%3A47.34093222917976%2C%22north%22%3A47.88399539689037%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A16037%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A806370%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    # "Host": "myhttpheader.com",
    # "Upgrade-Insecure-Requests": "1",
}
response = requests.get(zillow, headers=headers)
zillow_website = response.text

soup = BeautifulSoup(zillow_website, "html.parser")


prices = soup.find_all("div", class_="list-card-price")
only_prices = []
for price in prices:
    only_prices.append(price.text.split("+")[0].split("/")[0])

links = soup.find_all("a", class_="list-card-link")
only_links = []
for link in links:
    only_links.append(link['href'])

addresses = soup.find_all("address", class_="list-card-addr")
only_addresses = []
for address in addresses:
    only_addresses.append(address.text)
print(only_addresses)


chrome_driver_path = "C:/Development/chromedriver_win32/chromedriver.exe"

driver =webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(0, len(prices)-1):
    driver.get("https://forms.gle/J51DG9Sjmaboa8rt9")
    time.sleep(3)
    address_gap = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_gap.click()
    address_gap.send_keys(only_addresses[n])
    time.sleep(1)
    price_gap = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_gap.click()
    price_gap.send_keys(only_prices[n])
    time.sleep(1)
    link_gap = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_gap.click()
    link_gap.send_keys(only_links[n])
    time.sleep(1)
    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()


