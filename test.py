import asyncio
import pytest

from feedparser.util import FeedParserDict
from feedparser_data import Rss, RssAsync


def test_get_data_sync():
    bypass_bozo = True
    url_to_parse = 'https://foxmask.github.io/feeds/all.rss.xml'
    assert type(bypass_bozo) is bool
    assert type(url_to_parse) is str
    rss = Rss()
    data = rss.get_data(url_to_parse=url_to_parse, bypass_bozo=bypass_bozo)
    assert type(data) is FeedParserDict


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


def test_get_data_async(event_loop):
    bypass_bozo = True
    url_to_parse = 'https://foxmask.github.io/feeds/all.rss.xml'
    assert type(bypass_bozo) is bool
    assert type(url_to_parse) is str
    rss = RssAsync()
    data = event_loop.run_until_complete(rss.get_data(url_to_parse=url_to_parse, bypass_bozo=bypass_bozo))
    assert type(data) is FeedParserDict
