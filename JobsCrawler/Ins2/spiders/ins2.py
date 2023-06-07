import scrapy
from ..items import Jobs

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.17hats.com/careers']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data= Jobs()
        for product in response.css("div.collection-item-22"):
            data ={}         
            #page = response.url.split("/")[-2]            
            data['Designation']=product.css("div.div-block-203 div::text").extract_first()
            data['data_Url']=response.urljoin(product.css("a.job-card::attr('href')").extract_first())            
            request= scrapy.Request(response.urljoin(product.css("a.job-card::attr('href')").extract_first()), callback=self.parseJD, meta={'item': data})            
            yield request
    
    def parseJD(self,response):
        itema=response.meta['item']
        itema["Job_Description"]=response.css("p::text").extract()
        itema["Skill_Require"]=response.css("ul[role='list'] li::text").extract()
        yield itema
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
        #crawl  adax1234