# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Jobs(scrapy.Item):
    Designation = scrapy.Field()
    data_Url = scrapy.Field()
    Job_Description = scrapy.Field()
    Skill_Require = scrapy.Field()
    Requirement= scrapy.Field()
