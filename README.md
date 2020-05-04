# Scrapy Projects

For parsing data on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

1. Project quotetutorial<br />

`cd quotetutorial`<br />
`scrapy crawl quotes`<br />

`cd amazon_books`<br />
`scrapy crawl amazon`<br />

2. SAVE the data<br />

`scrapy crawl quotes -o items.json`<br />
`scrapy crawl quotes -o items.csv`<br />
`scrapy crawl quotes -o items.xml`<br />
