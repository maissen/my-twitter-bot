import tkinter as tk
from tkinter import ttk
import pickle

def load_main_window():
    # Create main window
    window = tk.Tk()
    window.title("Twitter Bot")
    
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

    # Load saved RSS sources from file
    load_saved_sources(saved_links_input)

    # Example button to call a function
    button = ttk.Button(window, text="Save RSS", command=lambda: save_rss(saved_links_input, rss_title, rss_link))
    button.grid(row=3, column=0, pady=5)  

    # Run the main event loop
    window.mainloop()

def load_saved_sources(saved_links_input):
    try:
        with open("My_rss_sources.dat", "rb") as file:
            rss_sources = pickle.load(file)
            titles = [source["title"] for source in rss_sources]
            if titles:
                saved_links_input["values"] = titles
                saved_links_input.set(titles[0])
    except FileNotFoundError:
        print("No RSS sources file found.")

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
                print("RSS title already exists!")
                return
            if source["link"] == link:
                print("RSS link already exists!")
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
    else:
        if not link:
            print("RSS link is empty!")
        elif not title:
            print("RSS title is empty!")

if __name__ == "__main__":
    load_main_window()
