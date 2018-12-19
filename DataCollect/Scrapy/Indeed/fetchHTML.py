import scrapy
import os

class IndeedSpider(scrapy.Spider):
    name = "indeed"
    # start_urls = [
    #     'https://ca.indeed.com/Amazon-jobs-in-Canada'    
    # ]
    #company_names = ['TD', 'RBC', 'Walmart', 'CIBC', 'Scotiabank', 'Rogers Communications', 'IBM', 'TELUS', 'Tim Hortons', 'Bell Canada', 'BMO Financial Group', 'Starbucks', 'Shoppers Drug Mart', 'BlackBerry', 'University of Toronto', 'Loblaw Companies', "McDonald's", 'Deloitte', 'Canadian Tire', 'CGI', 'University of British Columbia', "McDonald's Canada", 'Shaw Communications', 'PwC', 'Manulife', "Hudson's Bay Company", 'Sobeys', 'Sears', 'Best Buy Canada', 'SAP', 'Suncor', 'Staples', 'McGill University', 'Accenture', 'Home Depot Canada', 'KPMG', 'University of Waterloo', 'Sun Life', 'Cineplex Entertainment', 'IG Wealth Management', 'Canada Post', 'ATB Financial', 'EY', 'Bombardier Aerospace', 'The Home Depot', 'Indigo Books & Music', 'HSBC Holdings', 'Costco Wholesale', 'SNC-Lavalin', 'Yellow Pages', 'McMaster University', 'Ericsson-Worldwide', 'Banque Nationale du Canada/National Bank of Canada', 'Air Canada', 'Apple', 'University of Calgary', 'Desjardins', 'GoodLife Fitness', 'Microsoft', 'York University', 'Aritzia', 'Amazon', 'AMD', 'Best Buy', "Canada's Wonderland", 'Morneau Shepell', 'Ryerson University', 'Future Shop', 'Cenovus', 'Simon Fraser University', 'Alberta Health Services', 'lululemon', 'City of Toronto', 'University of Western Ontario', 'Shell', 'Enterprise', 'YMCA', 'University Health Network', 'Sport Chek', 'Subway', 'Intact', 'Government of Canada', 'Tata Consultancy Services', 'Real Canadian Superstore', 'PepsiCo', 'Gap', 'Electronic Arts', 'Ceridian', 'Stantec', 'Concordia University', 'Citco', 'Maple Leaf Foods', 'Winners', 'Aldo', 'Husky Energy', 'Mosaic Sales Solutions', "Queen's University", 'Dollarama', 'Softchoice', 'University of Ottawa', 'Old Navy', 'Enbridge', 'Kognitive Marketing', 'GardaWorld', 'Ubisoft', 'Webcarpenter', 'Paladin Security Group', 'The Source', 'Oracle', 'Shopify']

    def start_requests(self):
        # urls = [
        #     'https://ca.indeed.com/Amazon-jobs-in-Canada'
        # ]
        with open("company_list.txt", "r") as f:
            company_names=f.read().splitlines()
        #company_names = ['TD', 'RBC', 'Walmart', 'CIBC', 'Scotiabank', 'IBM','Bell Canada', 'BMO Financial Group', 'Loblaw Companies', 'Shoppers Drug Mart', 'Canadian Tire', 'CGI', 'PwC', 'Manulife', 'Deloitte', 'Canadian Tire', 'CGI', 'Best Buy Canada', 'Shaw Communications', 'PwC', 'Manulife', "Hudson's Bay Company", 'Sobeys', 'Sears', 'Best Buy Canada', 'SAP', 'Suncor', 'Staples', 'McGill University', 'Accenture', 'Home Depot Canada', 'KPMG', 'University of Waterloo', 'Sun Life', 'Cineplex Entertainment', 'IG Wealth Management', 'Canada Post', 'ATB Financial', 'EY', 'Bombardier Aerospace', 'The Home Depot', 'Indigo Books & Music', 'HSBC Holdings', 'Costco Wholesale', 'SNC-Lavalin', 'Yellow Pages', 'McMaster University', 'Ericsson-Worldwide', 'Banque Nationale du Canada/National Bank of Canada', 'Air Canada', 'Apple', 'University of Calgary', 'Desjardins', 'GoodLife Fitness', 'Microsoft', 'York University', 'Aritzia', 'Amazon', 'AMD', 'Best Buy', "Canada's Wonderland", 'Morneau Shepell', 'Ryerson University', 'Future Shop', 'Cenovus', 'Simon Fraser University', 'Alberta Health Services', 'lululemon', 'City of Toronto', 'University of Western Ontario', 'Shell', 'Enterprise', 'YMCA', 'University Health Network', 'Sport Chek', 'Subway', 'Intact', 'Government of Canada', 'Tata Consultancy Services', 'Real Canadian Superstore', 'PepsiCo', 'Gap', 'Electronic Arts', 'Ceridian', 'Stantec', 'Concordia University', 'Citco', 'Maple Leaf Foods', 'Winners', 'Aldo', 'Husky Energy', 'Mosaic Sales Solutions', "Queen's University", 'Dollarama', 'Softchoice', 'University of Ottawa', 'Old Navy', 'Enbridge', 'Kognitive Marketing', 'GardaWorld', 'Ubisoft', 'Webcarpenter', 'Paladin Security Group', 'The Source', 'Oracle', 'Shopify']
        for name in company_names:
            url = 'https://ca.indeed.com/' + name + '-jobs-in-Canada'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #get the div desc selector
        #response.xpath('//div[@id="vjs-desc"]/div/div/div/text()')
        #get the subpage url
        subpage_urls_list = response.xpath('//h2[@class="jobtitle"]/a/@href').extract()
        if subpage_urls_list is not None:
            for subpage_url in subpage_urls_list:
                #jump to the main job page 
                detail_page = response.urljoin(subpage_url)
                #yield response.follow(next_page, callback=self.parse)
                yield scrapy.Request(detail_page, callback=self.get_job_details)

        #go to the next page (list of jobs)
        next_page_url_list = response.xpath('//div[@class="pagination"]/a/@href').extract()
        if len(next_page_url_list) > 1:
            #if it has the next page
            if response.xpath('//div[@class="pagination"]/a/span/span/text()').extract()[-1] == 'Next\xa0»':
                next_page = response.urljoin(next_page_url_list[-1])
                yield scrapy.Request(url=next_page, callback=self.parse)



    def get_job_details(self, response):
        filename = response.xpath('//h3/text()').extract()[0]
        company_name = response.xpath('//h4[@class="jobsearch-CompanyReview--heading"]/text()').extract()[0]
        if not os.path.exists(company_name):
            os.makedirs(company_name)
        
        with open('%s/%s.html' %(company_name, filename), 'wb') as f:
            f.write(response.body)
  
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)




        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        # for quote in response.css('div.vjs-desc'):
        #     yield {
        #         # 'text': quote.css('span.text::text').extract_first(),
        #         # 'author': quote.css('small.author::text').extract_first(),
        #         # 'tags': quote.css('div.tags a.tag::text').extract(),
        #     }
 
