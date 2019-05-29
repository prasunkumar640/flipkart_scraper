import scrapy



class MySpider(scrapy.Spider):
    name="flipkart_scrapper"
    page_number=1
  

    
    def start_requests(self):
        urls=[
            "https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1",
            
             
             
             ]
        
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
            
    def parse(self,response):
        
        page_id= response.url.split("=")[-1]
        #creating json file
        details=response.css("div._1UoZlX")
        for detail in details:
            
            mob_name=detail.css("div._3wU53n::text").get()
            mob_price=detail.css("div._1vC4OE._2rQ-NK::text").get()
            mob_rating=detail.css("div.hGSR34::text").get()
            
            yield{
                "mob_name":mob_name,
                "mob_price":mob_price,
                "mob_rating":mob_rating,
            }
            
            
            next_page_id="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(MySpider.page_number)
            if MySpider.page_number <6:
                MySpider.page_number +=1
                next_page =response.urljoin(next_page_id)
                yield scrapy.Request(next_page,callback=self.parse)
            
        
        
        
    