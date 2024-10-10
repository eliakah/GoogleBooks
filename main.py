import os
from dotenv import load_dotenv
from typing import Final
import requests
import json


class Google_BookSearch : 
    def fetch(q, tof , field ):
        print("This function prints a google url based on param!")
        load_dotenv()
        url = ""
        base = ["https://www.googleapis.com/books/v1/volumes?q=% s&key=% s", "https://www.googleapis.com/books/v1/volumes?q=% s+% s:% s&key=% s"]
        fields = ["any", "intitle", "inauthor", "inpublisher", "subject", "isbn"] 
        len = tof
        GOOGLE_KEY: final(str) = os.getenv("GOOGLE_KEY")
        if(len == 0):
            url = (base[0]  % (q, KEY))
        else:
            url = (base[1]  % (q, fields[tof], field, GOOGLE_KEY))
            

        
        print("q = " + q)
        print("field = " + fields[tof])
        #print("url = " + url)
        r = requests.get(url)
        print("output :" )
        result = r.json()
        print(result['totalItems'])    
        items_l = result['items']

        return items_l
        



    def print_item(item): 
        print ("title: " + item['volumeInfo']['title']) 
        print ("authors: " + item['volumeInfo']['authors'][0])   
        print ("description: " + item['volumeInfo']['description']) 
        print ("Thumbnail: " + item['volumeInfo']['imageLinks']['smallThumbnail'])
        print ("ISBN TYPE: " + item['volumeInfo']['industryIdentifiers'][0]['type'])      
        print ("ISBN VAL: " + item['volumeInfo']['industryIdentifiers'][0]['identifier'])      
        print ("Country: " + item['saleInfo']['country'])   
        print ("Sale Ability: " + item['saleInfo']['saleability'])   
        print ("list Price: " + str(item['saleInfo']['listPrice']['amount'])+ item['saleInfo']['listPrice']['currencyCode'])   
        print ("retailPrice: " + str(item['saleInfo']['retailPrice']['amount']) + item['saleInfo']['retailPrice']['currencyCode'])   
        print ("buyLink: " + item['saleInfo']['buyLink']) 

def main():
      bs = Google_BookSearch
      items = bs.fetch("etranger", 2, "albert camus")
      bs.print_item(items[0])


if __name__ == "__main__": 
     main()
    
