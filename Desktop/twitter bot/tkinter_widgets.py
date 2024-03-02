import tkinter as tk
from tkinter import ttk

#
# all entries container
def show_all_entries_container(feed):
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
    root = tk.Tk()
    # Set the title of the window
    root.title("Simple Window")

    # Set the width and height of the window
    root.geometry("750x400")

    # Set the padding of the window
    root.configure(padx=15, pady=15)

    # Create the first label and text input field
    label1 = tk.Label(root, text="Entry's title:")
    label1.grid(row=0, column=0, pady=10)

    text_input1 = tk.Text(root, height=5, width=30)
    text_input1.grid(row=0, column=1, sticky="ew", pady=(0, 20))  # Add a bottom margin of 20px

    # Create a scrollbar for the first text input field
    scrollbar1 = tk.Scrollbar(root, command=text_input1.yview)
    scrollbar1.grid(row=0, column=2, sticky="ns")

    # Link the scrollbar to the first text input field
    text_input1.config(yscrollcommand=scrollbar1.set)

    # Create the second label and text input field
    label2 = tk.Label(root, text="Entry's description:")
    label2.grid(row=1, column=0, pady=10)

    text_input2 = tk.Text(root, height=5, width=30)
    text_input2.grid(row=1, column=1, sticky="ew", pady=(0, 20))  # Add a bottom margin of 20px

    # Create a scrollbar for the second text input field
    scrollbar2 = tk.Scrollbar(root, command=text_input2.yview)
    scrollbar2.grid(row=1, column=2, sticky="ns")

    # Link the scrollbar to the second text input field
    text_input2.config(yscrollcommand=scrollbar2.set)

    # Create the third label and text input field
    label3 = tk.Label(root, text="Enter Hashtags:")
    label3.grid(row=2, column=0, pady=10)

    text_input3 = tk.Text(root, height=5, width=30)
    text_input3.grid(row=2, column=1, sticky="ew", pady=(0, 20))  # Add a bottom margin of 20px

    # Create a scrollbar for the third text input field
    scrollbar3 = tk.Scrollbar(root, command=text_input3.yview)
    scrollbar3.grid(row=2, column=2, sticky="ns")

    # Link the scrollbar to the third text input field
    text_input3.config(yscrollcommand=scrollbar3.set)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.grid(row=3, column=1, sticky="n", pady=(25, 0))  # Add a top margin of 25px

    # Create a button labeled "Search on web"
    button_search = tk.Button(button_frame, text="Search on web")
    button_search.pack(side="left", padx=5)  # Add a left padding of 5px

    # Create a button labeled "Share now"
    button_share = tk.Button(button_frame, text="Share now")
    button_share.pack(side="right", padx=5)  # Add a right padding of 5px

    # Configure the grid to make the text input fields expand to fill the available space
    root.grid_columnconfigure(1, weight=1)

    # Start the event loop
    root.mainloop()
    
    

