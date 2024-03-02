# Function to be called when "Share now" button is clicked
def push_post_to_twitter():
    print("Share Button is clicked!")
    
import webbrowser
# Function to be called when "Search" button is clicked
def search_entry(entry):
    webbrowser.open_new_tab(entry.link)
    

