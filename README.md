# Flipkart Scraper
A simple web scraper to scrape the product details from Flipkart using Scrapy Modue in Python

## Description

This project allows you to scrape the product details such as price,rating from Flipkart.

## Requirements
Python 3
pip3
scrapy

## Installation
pip install scrapy


## Usage
In initial, it scrape mobile phones details of 5 pages from Flipkart but you can also change it to scrape more.
      - 1.Open the `/flipkart_scraper/spiders/flipkart_scraper.py`
      - 2.Goto line 42 and change the value of `page number` to scrape more pages.

In the end of the url you will find `page=1` and this indicates that this is the url of first page,In order to change the url and scrape different website you should take care of this because a website have different pages which are of different page numbers.You can change it in line `13` and `41`

At line `41` where we declare `next_page_id` where we append the `page_number`.

In `next_page_id` we divide the url in such a way that its first part contains the url without `page_number` and second part contain the page number upto which we want to go.
    
 ## Execution
 To run this project execute the following command
            
      scrapy crawl flipkart_scraper -o flipkart.json 
It will returns a `JSON` file of name `flipkart` in the flipkart_scraper folder and the json file contains the scraped data.

## Sample Data
The sample `JSON` file is attached in the data folder


