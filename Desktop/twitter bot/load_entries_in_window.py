import feedparser
# from entry_info import *
from tkinter_widgets import *


# Function to load and display the feed entries
def load_rss_feed():
    link = 'https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com&hl=en-US&gl=US&ceid=US:en'
    feed = feedparser.parse(link)
    show_all_entries_container(feed)

    

load_rss_feed()
