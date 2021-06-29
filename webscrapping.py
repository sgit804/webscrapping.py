import requests
import bs4 
import BeautifulSoup
import pandas
import argparse

parser = argparse.ArgumentParser()
parser.add-argument("--page_num_max",help="enter the number of pages toparse",type=int)
args=parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-vizag/?page="
page_num_max = args.page_num_max
scraped_info_list = []

for page_num in range(1, page_num_max):
    req = requests.get(oyo_url + str(page_num))
    content = req.content
    
    soup = BeautifulSoup(content, "html.parser")
    
    all_hotels = soup.find_all("div",{"class": "hostelCardListing"})
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find{"h3", {"class": "listingHotelDescription__hotelName"}).text
    