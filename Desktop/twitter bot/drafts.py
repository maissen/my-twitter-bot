import tkinter as tk
from tkinter import ttk

def load_main_window():
    # Create main window
    window = tk.Tk()
    window.title("Twitter Bot")
    
    # Create a frame to contain label and entry for source
    source = ttk.Frame(window)
    source.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    rss_link_label = ttk.Label(source, text="Enter RSS link for source:") # Create the label for source
    rss_link_label.grid(row=0, column=0, sticky="w", padx=(0, 5))
    rss_link = ttk.Entry(source, width=30) # Create the text input field for source with padding
    rss_link.grid(row=0, column=1, sticky="w", padx=8, pady=10)
    rss_link.configure(background="white")  # Set background color to white
    
    # Create a frame to contain label and entry for title
    title = ttk.Frame(window)
    title.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")  
    rss_title_label = ttk.Label(title, text="Enter RSS title:") 
    rss_title_label.grid(row=0, column=0, sticky="w", padx=(0, 5))
    rss_title = ttk.Entry(title, width=30) 
    rss_title.grid(row=0, column=1, sticky="w", padx=8, pady=10)
    rss_title.configure(background="white")  
    
    # Create a frame to contain label and combobox for saved links
    saved_links = ttk.Frame(window)
    saved_links.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    saved_links_label = ttk.Label(saved_links, text="Saved Links:") 
    saved_links_label.grid(row=0, column=0, sticky="w", padx=(0, 5))
    
    # Create combobox widget
    saved_links_input = ttk.Combobox(saved_links, width=27, state="readonly")
    saved_links_input.grid(row=0, column=1, sticky="w", padx=8, pady=10)
    saved_links_input.configure(background="white")
    saved_links_input.set("-- There's no RSS saved --")

    # Example button to call a function
    button = ttk.Button(window, text="Save RSS", command=lambda: save_rss(saved_links_input, rss_title, rss_link))
    button.grid(row=3, column=0, pady=5)  

    # Run the main event loop
    window.mainloop()

def save_rss(saved_links_input, rss_title, rss_link):
    # Get RSS title and link
    title = rss_title.get()
    link = rss_link.get()
    
    # Check if the RSS title and link are not empty
    if title and link:
        # Check if the title is not already in the combobox
        if title not in saved_links_input["values"]:
            # Remove the placeholder if it exists
            if "-- There's no RSS saved --" in saved_links_input["values"]:
                saved_links_input.delete(saved_links_input["values"].index("-- There's no RSS saved --"))
            
            # Check if the link already exists in the file
            if link_exists(link):
                print("RSS link already exists!")
                return
            
            # Append RSS title and link to the file
            with open("My_rss_sources.txt", "a") as file:
                file.write(f"{title}: {link}\n")
            
            # Append RSS title to the combobox values
            saved_links_input["values"] = list(saved_links_input["values"]) + [title]
            # Select the newly added title
            saved_links_input.set(title)
            # Clear the entry fields
            rss_title.delete(0, tk.END)
            rss_link.delete(0, tk.END)
        else:
            print("RSS title already exists!")
    else:
        if not link:
            print("RSS link is empty!")
        elif not title:
            print("RSS title is empty!")

def link_exists(link):
    # Check if the link already exists in the file
    try:
        with open("My_rss_sources.txt", "r") as file:
            for line in file:
                if link in line:
                    return True
    except FileNotFoundError:
        pass  # If the file doesn't exist, the link doesn't exist
    
    return False

if __name__ == "__main__":
    load_main_window()
