from tkinter import *


class UI:
    def __init__(self) -> None:
        self.title_label = Label()
        self.time_label_info = Label()
        self.time_label = Label()
        self.text_entry = Text()

    def place_title_label(self, background_photo):
        self.title_label.config(
            text="Welcome To Disapperaing Text Writing",
            background="black",
            foreground="white",
            font=("Courier", 14, "bold"),
        )
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="n", padx=155)

    def place_time_label_info(self, background_photo):
        self.time_label_info.config(
            text="Your text will disappear in: ",
            background="black",
            foreground="white",
            font=("Courier", 13, "bold"),
        )
        self.time_label_info.grid(row=1, column=0, pady=10, sticky="e")

    def place_time_label(self, background_photo):
        self.time_label.config(
            text="5",
            background="black",
            foreground="white",
            font=("Courier", 13, "bold"),
        )
        self.time_label.grid(row=1, column=1, sticky="w")

    def place_text_entry(self):
        self.text_entry.grid(row=3, column=0, columnspan=3, rowspan=5, sticky="nswe")
