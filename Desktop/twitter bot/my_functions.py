# Function to be called when "Share now" button is clicked
def push_post_to_twitter(entry_title, entry_summary, hashtags):
    print("Share Button is clicked!")
    print(f"title : {entry_title}")
    print(f"summary : {entry_summary}")
    print(f"hashtags : {hashtags}")
    
import webbrowser
# Function to be called when "Search" button is clicked
def search_entry(entry):
    webbrowser.open_new_tab(entry.link)
    

