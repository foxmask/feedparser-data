# feedparser-data
Get the data of FeedParser

## installation
```
pip install feedparser-fata
```

## usage 
```
import asyncio
from feedparser_data import Rss, RssAsync


def my_feeds():
    print("SYNC! ")
    rss = Rss()
    data = rss.get_data(url_to_parse='https://foxmask.github.io/feeds/all.rss.xml',
                        bypass_bozo=True)
    for line in data.entries:
        print(line.title)
    print("END SYNC! ")


async def my_feeds_async():
    print('ASYNC! ')
    rssasync = RssAsync()
    dataasync = await rssasync.get_data(url_to_parse='https://foxmask.github.io/feeds/all.rss.xml',
                                        bypass_bozo=True)
    for lineaysnc in dataasync.entries:
        print(lineaysnc.title)
    print('END ASYNC! ')

asyncio.run(my_feeds_async())

my_feeds()
```

