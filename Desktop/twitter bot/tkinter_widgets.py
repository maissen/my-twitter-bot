import tkinter as tk
from tkinter import ttk
from my_functions import *

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

    
    

