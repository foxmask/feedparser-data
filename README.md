# feedparser-data
Get the data of FeedParser

## installation
```
pip install feedparser-fata
```

## usage 
```
>>> from feedparser_data import rss
>>> data = Rss(url_to_parse='http://foobar.tld/feed.rss')
>>> for line in data:
>>>    print(line)

```

