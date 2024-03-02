from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QLabel, QVBoxLayout, QComboBox
from PyQt5.QtCore import Qt
import load_entries_in_window

added_rss_links = []
added_rss_titles = []
entries_container = None  # Define entries_container outside the function

def parse_feed():
    recent_rss_links = windows.recent_rss_links
    rss_link_title = windows.rss_link_title.text()
    rss_link = windows.rss_link.text()
    
    if ((rss_link not in added_rss_links) and (rss_link_title not in added_rss_titles)):
        recent_rss_links.insertItem(0, rss_link_title)
        added_rss_links.append(rss_link)
        added_rss_titles.append(rss_link_title)
        
        recent_rss_links.setCurrentIndex(0) # Select the most recent item
        # Remove the first item if there are more than one items
        if recent_rss_links.count() > 1:
            recent_rss_links.removeItem(1)
    



app = QApplication([])
windows = loadUi("foot.ui")
windows.show()
windows.save_new_link.clicked.connect(parse_feed) #to save new links
windows.parse_link.clicked.connect(load_entries_in_window.load_entries)
app.exec_()
