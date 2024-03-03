import tkinter as tk
from tkinter import ttk
    
    

def is_valid_rss_feed(link):
    try:
        feed = feedparser.parse(link)
        if feed.get('bozo_exception') is None:
            return True
    except Exception as e:
        pass
    return False


    
def input_hashtags(hashtags_input):
    hashtags_list = hashtags_input.split()
    for i, item in enumerate(hashtags_list):
        if item.find("#") > -1:
            item = item.replace("#", "")
            if item.find("#") == -1:
                hashtags_list[i] = item
    
    return [tag for tag in hashtags_list if tag]  # Filter out empty strings    

    
    
# Function to be called when "Share now" button is clicked
def push_post_to_twitter(entry_title, entry_summary, hashtags):
    print("Share Button is clicked!")
    print(f"title : {entry_title}")
    print(f"summary : {entry_summary}")
    print(f"hashtags : {input_hashtags(hashtags)}")
    

import pickle
def load_saved_sources(saved_links_input):
    try:
        with open("My_rss_sources.dat", "rb") as file:
            rss_sources = pickle.load(file)
            titles = [source["title"] for source in rss_sources]
            if titles:
                saved_links_input["values"] = titles
                saved_links_input.set(titles[0])
    except FileNotFoundError:
        with open("My_rss_sources.dat", "wb") as file:
            rss_sources = []
            pickle.dump(rss_sources, file)