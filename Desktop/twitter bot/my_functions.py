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
    
    
def input_hashtags():
    hashtags_input = input("Enter hashtags separated by a single space (without #): ")
    hashtags_list = hashtags_input.split()
    for i, item in enumerate(hashtags_list):
        if item.find("#") > -1:
            item = item.replace("#", "")
            if item.find("#") == -1:
                hashtags_list[i] = item
    
    return [tag for tag in hashtags_list if tag]  # Filter out empty strings

