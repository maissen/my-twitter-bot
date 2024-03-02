import feedparser
# from entry_info import *
from tkinter_widgets import *


# Function to load and display the feed entries
def load_rss_feed():
    link = 'https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com&hl=en-US&gl=US&ceid=US:en'
    feed = feedparser.parse(link)
    container_of_entries(feed)
#     print(feed.entries[0].keys())
#     print(feed.entries[0].title)
#     print('SUMMARY : ', feed.entries[0].summary_detail)
#     print(feed.entries[0].summary_detail)
#     print()
#     print(feed.entries[0].link)

    

load_rss_feed()
