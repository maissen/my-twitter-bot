import tkinter as tk
from tkinter import scrolledtext, messagebox
import instaloader
import requests
from io import BytesIO

def display_instagram_posts(profile_url):
    # Extracting username from the profile URL
    username = profile_url.split("/")[-2]

    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        result_text.delete('1.0', tk.END)  # Clear previous results

        for post in profile.get_posts():
            result_text.insert(tk.END, f"Post URL: {post.shortcode}\n")
            result_text.insert(tk.END, f"Likes: {post.likes}\n")
            result_text.insert(tk.END, f"Caption: {post.caption}\n")
            result_text.insert(tk.END, f"Comments: {post.comments}\n")
            result_text.insert(tk.END, f"Posted at: {post.date_local}\n")
            result_text.insert(tk.END, f"Media: {post.typename}\n")
            result_text.insert(tk.END, "\n")

            # Download and display image
            image_url = post.url
            image_data = requests.get(image_url).content
            photo = tk.PhotoImage(data=image_data)

            image_label = tk.Label(window, image=photo)
            image_label.image = photo  # Keep reference to avoid garbage collection
            image_label.pack()

    except instaloader.exceptions.ProfileNotExistsException:
        messagebox.showerror("Error", f"Profile '{username}' does not exist.")

def get_profile_posts():
    profile_url = url_entry.get()
    if profile_url:
        display_instagram_posts(profile_url)
    else:
        messagebox.showwarning("Warning", "Please enter a profile URL.")

# Create main window
window = tk.Tk()
window.title("Instagram Post Viewer")

# Create URL entry
url_label = tk.Label(window, text="Enter Instagram Profile URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

# Create button to fetch posts
fetch_button = tk.Button(window, text="Fetch Posts", command=get_profile_posts)
fetch_button.pack(pady=5)

# Create text area to display posts
result_text = scrolledtext.ScrolledText(window, width=80, height=10)
result_text.pack(pady=5)

# Start the GUI event loop
window.mainloop()
