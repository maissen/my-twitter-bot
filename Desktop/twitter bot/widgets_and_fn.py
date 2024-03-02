import tkinter as tk
from tkinter import ttk
import feedparser


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
            
            

def parse_rss(saved_links_input):
    selected_title = saved_links_input.get()
    if selected_title:
        try:
            with open("My_rss_sources.dat", "rb") as file:
                rss_sources = pickle.load(file)
        except FileNotFoundError:
            rss_sources = []

        for source in rss_sources:
            if source["title"] == selected_title:
#                 popup_message("Info", f"'{selected_title}': {source['link']}")
                link = source['link']
                feed = feedparser.parse(link)
                container_of_entries(feed)
                break
        else:
            popup_message("Info", f"No RSS selected to parse!")
    else:
        popup_message("Error", "No RSS title selected!")
        
# Function to be called when "Share now" button is clicked
def push_post_to_twitter(entry_title, entry_summary, hashtags):
    print("Share Button is clicked!")
    print(f"title : {entry_title}")
    print(f"summary : {entry_summary}")
    print(f"hashtags : {input_hashtags(hashtags)}")
    
    
import webbrowser
# Function to be called when "Search" button is clicked
def search_entry(entry):
    webbrowser.open_new_tab(entry.link)
    
    
def input_hashtags(hashtags_input):
    hashtags_list = hashtags_input.split()
    for i, item in enumerate(hashtags_list):
        if item.find("#") > -1:
            item = item.replace("#", "")
            if item.find("#") == -1:
                hashtags_list[i] = item
    
    return [tag for tag in hashtags_list if tag]  # Filter out empty strings












def save_rss(saved_links_input, rss_title, rss_link):
    title = rss_title.get()
    link = rss_link.get()
    
    if title and link:
        try:
            with open("My_rss_sources.dat", "rb") as file:
                rss_sources = pickle.load(file)
        except FileNotFoundError:
            rss_sources = []

        for source in rss_sources:
            if source["title"] == title:
                popup_message("Error", "RSS title already exists!")
                return
            if source["link"] == link:
                popup_message("Error", "RSS link already exists!")
                return

        rss_sources.append({"title": title, "link": link})
        with open("My_rss_sources.dat", "wb") as file:
            pickle.dump(rss_sources, file)

        if "-- There's no RSS saved --" in saved_links_input["values"]:
            saved_links_input.delete(saved_links_input["values"].index("-- There's no RSS saved --"))

        saved_links_input["values"] = [source["title"] for source in rss_sources]
        saved_links_input.set(title)

        rss_title.delete(0, tk.END)
        rss_link.delete(0, tk.END)

        popup_message("Success", f"{title} saved successfully")
    else:
        if not link:
            popup_message("Error", "Please enter a Link!")
        elif not title:
            popup_message("Error", "Please enter a Title!")

def delete_rss(saved_links_input):
    title_to_delete = saved_links_input.get()
    if title_to_delete:
        try:
            with open("My_rss_sources.dat", "rb") as file:
                rss_sources = pickle.load(file)
        except FileNotFoundError:
            rss_sources = []

        updated_sources = [source for source in rss_sources if source["title"] != title_to_delete]

        with open("My_rss_sources.dat", "wb") as file:
            pickle.dump(updated_sources, file)

        if updated_sources:
            saved_links_input["values"] = [source["title"] for source in updated_sources]
            saved_links_input.set(updated_sources[0]["title"])
            popup_message("Success", f"{title_to_delete} deleted successfully")
        else:
            saved_links_input["values"] = []
            saved_links_input.set("-- There's no RSS saved --")
            popup_message("Warning", "There's no saved RSS to delete")
    else:
        popup_message("Error", "No RSS title selected!")



def popup_message(title, message):
    popup = tk.Toplevel()
    popup.title(title)
    popup.geometry("300x100")
    label = ttk.Label(popup, text=message)
    label.pack(pady=20)
    # Schedule the closing of the popup after 2000 milliseconds (2 seconds)
    popup.after(2500, popup.destroy)




##
## Main window
def load_main_window():
    # Create main window
    window = tk.Tk()
    window.title("Twitter Bot")
    window.resizable(False, False)  # Make the window unresizable
    
    # Create a frame to contain label and entry for source
    source = ttk.Frame(window)
    source.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    rss_link_label = ttk.Label(source, text="Enter RSS link for source:") 
    rss_link_label.grid(row=0, column=0, sticky="w", padx=(0, 5))
    rss_link = ttk.Entry(source, width=30)
    rss_link.grid(row=0, column=1, sticky="w", padx=8, pady=10)
    rss_link.configure(background="white")
    
    # Create a frame to contain label and entry for title
    title = ttk.Frame(window)
    title.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")  
    rss_title_label = ttk.Label(title, text="Enter RSS title:") 
    rss_title_label.grid(row=0, column=0, sticky="w", padx=(0, 5))
    rss_title = ttk.Entry(title, width=30) 
    rss_title.grid(row=0, column=1, sticky="w", padx=8, pady=10)
    rss_title.configure(background="white")  
    
    # Create a frame to contain label, combobox, and buttons for saved links
    saved_links = ttk.Frame(window)
    saved_links.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    
    saved_links_label = ttk.Label(saved_links, text="Saved Links:") 
    saved_links_label.grid(row=0, column=0, sticky="w", padx=(0, 5))
    
    saved_links_input = ttk.Combobox(saved_links, width=25, state="readonly")
    saved_links_input.grid(row=0, column=1, sticky="w", padx=8, pady=10)
    saved_links_input.configure(background="white")
    saved_links_input.set("-- There's no RSS saved --")

    save_button = ttk.Button(saved_links, text="Save RSS", command=lambda: save_rss(saved_links_input, rss_title, rss_link))
    save_button.grid(row=0, column=2, padx=5)

    delete_button = ttk.Button(saved_links, text="Delete RSS", command=lambda: delete_rss(saved_links_input))
    delete_button.grid(row=0, column=3, padx=5)

    parse_button = ttk.Button(saved_links, text="Parse", command=lambda: parse_rss(saved_links_input))
    parse_button.grid(row=0, column=4, padx=5)

    # Load saved RSS sources from file
    load_saved_sources(saved_links_input)

    # Run the main event loop
    window.mainloop()
    



#
# all entries container
def container_of_entries(feed):
    # Create the main window
    root = tk.Tk()
    root.title('RSS Feed Entries')

    # Create a canvas with both vertical and horizontal scrollbars
    canvas = tk.Canvas(root, width=600 + 2 * 15, height=450 + 2 * 15)
    vscrollbar = ttk.Scrollbar(root, orient='vertical', command=canvas.yview)
    hscrollbar = ttk.Scrollbar(root, orient='horizontal', command=canvas.xview)
    scrollable_frame = ttk.Frame(canvas)

    # Configure the canvas and scrollbars
    canvas.configure(yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.grid(row=0, column=0, sticky='nsew')
    vscrollbar.grid(row=0, column=1, sticky='ns')
    hscrollbar.grid(row=1, column=0, sticky='ew')

    # Add each entry to the frame
    for i, entry in enumerate(feed.entries):
        # Create a frame for the entry
        entry_frame = tk.Frame(scrollable_frame, padx=10, pady=9, cursor='hand2', background='SystemButtonFace')
        entry_frame.pack(fill='x', expand=True)

        # Create a label for the entry
        label = tk.Label(
            entry_frame, 
            text=f'{i+1}. {entry.title}', 
            wraplength=600, 
            justify='left', 
            cursor='hand2',  # Change cursor to a pointer
            background='SystemButtonFace', 
            highlightbackground='lightgray',  # Set the initial background color
            anchor='w'  # Align text to the left
        )
        label.pack(fill='x', expand=True)

        # Bind the double click event to show details of the selected entry
        label.bind('<Double-Button-1>', lambda event, entry=entry: show_clicked_entry_details(root, entry))

        # Bind the Enter event to change the background color on hover
        entry_frame.bind('<Enter>', lambda event, entry_frame=entry_frame: entry_frame.config(background='lightgray'))

        # Bind the Leave event to change the background color back when the cursor leaves
        entry_frame.bind('<Leave>', lambda event, entry_frame=entry_frame: entry_frame.config(background='SystemButtonFace'))

    # Update the canvas to ensure the scrollbar works correctly
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

    # Configure the grid to resize with the window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Run the main loop
    root.mainloop()
    
    
#
# to show the clicked entry info
def show_clicked_entry_details(root, entry):
    # Create an instance of the Tk class
    window = tk.Toplevel(root)  # Use Toplevel for additional windows
    window.title(entry.title)
    
    window.geometry("750x400") # Set the width and height of the window    
    window.configure(padx=15, pady=15) # Set the padding of the window

    # Create the first label and text input field
    title_label = tk.Label(window, text="Entry's title:")
    title_label.grid(row=0, column=0, pady=10)
    entry_title = tk.Text(window, height=5, width=30)
    entry_title.grid(row=0, column=1, sticky="ew", pady=(0, 20))  # Add a bottom margin of 20px
    
    if('title' in entry.keys()):
        entry_title.insert("1.0", entry.title)
    else:
        entry_title.insert("1.0", "This entry doesn't have a title to show!")
    
    scrollbar1 = tk.Scrollbar(window, command=entry_title.yview) # Create a scrollbar for the first text input field
    scrollbar1.grid(row=0, column=2, sticky="ns")
    entry_title.config(yscrollcommand=scrollbar1.set) # Link the scrollbar to the first text input field

    # Create the second label and text input field
    summary_label = tk.Label(window, text="Entry's summary:")
    summary_label.grid(row=1, column=0, pady=10)

    entry_summary = tk.Text(window, height=5, width=30)
    entry_summary.grid(row=1, column=1, sticky="ew", pady=(0, 20))  # Add a bottom margin of 20px
    if('summary' in entry.keys()): 
        entry_summary.insert("1.0", entry.summary)
    else:
        entry_summary.insert("1.0", "This entry doesn't have a summary to show!")
   
    scrollbar2 = tk.Scrollbar(window, command=entry_summary.yview) # Create a scrollbar for the second text input field
    scrollbar2.grid(row=1, column=2, sticky="ns")
    entry_summary.config(yscrollcommand=scrollbar2.set)

    # Create the third label and text input field
    hashtags_label = tk.Label(window, text="Recent Hashtags:")
    hashtags_label.grid(row=2, column=0, pady=10)

    recent_hashtags = tk.Text(window, height=5, width=30)
    recent_hashtags.grid(row=2, column=1, sticky="ew", pady=(0, 20))  # Add a bottom margin of 20px
    
    scrollbar3 = tk.Scrollbar(window, command=recent_hashtags.yview) # Create a scrollbar for the third text input field
    scrollbar3.grid(row=2, column=2, sticky="ns")
    recent_hashtags.config(yscrollcommand=scrollbar3.set)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)
    button_frame.grid(row=3, column=1, sticky="n", pady=(25, 0))  # Add a top margin of 25px

    # Create a button labeled "Search on web"
    button_search = tk.Button(button_frame, text="Search Entry on web", command=lambda: search_entry(entry))
    button_search.pack(side="left", padx=5)  # Add a left padding of 5px

    # Create a button labeled "Share now"
    button_share = tk.Button(button_frame, text="Share now", command=lambda: push_post_to_twitter(entry_title.get("1.0", "end-1c"), entry_summary.get("1.0", "end-1c"), recent_hashtags.get("1.0", "end-1c")))
    button_share.pack(side="right", padx=5)  # Add a right padding of 5px

    # Configure the grid to make the text input fields expand to fill the available space
    window.grid_columnconfigure(1, weight=1)

    # Start the event loop for this window
    window.mainloop()

    
    
