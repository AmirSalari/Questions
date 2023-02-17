from lxml import html
import requests

page = requests.get('https://www.python.org/events/')
tree = html.fromstring(page.content)


# Provide an XPath expression that can be used to locate the first occurrence (and only the first occurrence) of an event entry page.
part_1 = tree.xpath('//ul[@class="list-recent-events menu"]/li[1]/h3[@class="event-title"]/a[1]/text()')
print(part_1)

# Provide an XPath expression that can be used to locate the dates of the first event in the page.
part_2 = tree.xpath('//ul[@class="list-recent-events menu"]/li[1]/p/time/text()')
print(part_2)

# Provide an XPath expression that can be used to locate all PyCon event occurrences only.
part_3 = tree.xpath('//ul[@class="list-recent-events menu"]/li/h3[@class="event-title"]/a[starts-with(text(),"PyCon")]/text()')
print(part_3)

# Provide an Xpath expression that can be used to locate non-online events.
part_4 = tree.xpath('//ul[@class="list-recent-events menu"]/li/p/span[text() != "Online"]/text()')
print(part_4)