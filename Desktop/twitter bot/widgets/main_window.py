import tkinter as tk
from tkinter import ttk
import pickle
from ../widgets_and_fn import *


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