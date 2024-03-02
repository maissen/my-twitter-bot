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
            popup_message("Error", "RSS link is empty!")
        elif not title:
            popup_message("Error", "RSS title is empty!")

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
                popup_message("Info", f"'{selected_title}': {source['link']}")
                break
        else:
            popup_message("Info", f"No RSS selected to parse!")
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

if __name__ == "__main__":
    load_main_window()
