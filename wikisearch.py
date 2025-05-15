"""
    wikisearch.py: wikipedia search app
    Louis Belanger 5/14/25
    contributions: https://www.mediawiki.org/wiki/API:Opensearch, ChatGPT
    uses wikipedia action api opensearch module
    to allow user to search wikipedia
"""

import tkinter as tk
import requests

# return wikipedia article when submitted. Invalid requests defaut to random
def on_submit():
    user_input = entry.get()

    PARAMS["titles"] = user_input
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    body = DATA["query"]["pages"][0]["extract"]
    print(body)

    result_label.config(text=f"Request returned: \n{type(body)}\n{body}")

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

# Create the main window
root = tk.Tk()
root.title("Wikisearch")
root.geometry("600x300")

# Create a textbox (entry widget)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", wraplength=500)
result_label.pack(pady=10)

# Run the application
root.mainloop()
