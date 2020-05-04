# Scrapy Projects

For parsing data on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

1. scrapy startproject quotetutorial<br />

`cd quotetutorial`
`scrapy crawl quotes`

`cd amazon_books`
`scrapy crawl amazon`

2. SAVE the data<br />
`scrapy crawl quotes -o items.json`
`scrapy crawl quotes -o items.csv`
`scrapy crawl quotes -o items.xml`
