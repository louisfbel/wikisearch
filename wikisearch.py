import tkinter as tk
from tkinter import ttk
import requests
from html.parser import HTMLParser

# HTML stripper class
class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_html(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return strip_erroneous(stripper.get_data())

def strip_erroneous(html):
    end = html.find("See also")
    if end:
        return html[0:end]
    return html

# return wikipedia article when submitted. Invalid requests default to random
def on_submit():
    user_input = entry.get()

    PARAMS["titles"] = user_input
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    body = DATA["query"]["pages"][0]["extract"]

    clean_text = strip_html(body)

    # Clear previous text
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, clean_text)

# create session
S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

# request parameters 
PARAMS = {
    "action": "query",
    "prop": "extracts",
    "titles": "Special:Random",
    "format": "json",
    "formatversion": 2
}

# Main window
root = tk.Tk()
root.title("Wikisearch")
root.geometry("600x400")

# Entry widget
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Search", command=on_submit)
submit_button.pack()

# Scrollable text area
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# text box
text_box = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text_box.yview)

# Thank Wikipedia
thank_box = tk.Label(root, text="Thank you, Wikipedia. I love you.")
thank_box.pack(pady=10)

# Run the application
root.mainloop()
