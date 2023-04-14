from tkinter import Canvas, Frame, Label
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk

import resources


class MainScreen:
    def __init__(self, parent: Frame):
        self.parent = parent

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.configure_background()

        self.content = Frame(self.parent)
        self.content.grid(row=0, column=0, sticky="n")

        self.title = Label(
            self.content,
            text="Main screen",
            borderwidth=0,
            font=("Times New Roman", 35, BOLD),
        )
        self.title.pack()

        self.next_button = ttk.Button(
            self.content, text="Next screen", command=self.next_screen
        )
        self.next_button.pack()

        self.parent.bind("<Configure>", self.handle_resize)

    def configure_background(self):
        self.img_file = Image.open(resources.path("./resources/background.jpg"))
        self.background_canvas = Canvas(self.parent, background="#555")
        self.background_canvas.grid(row=0, column=0, sticky="news")

        resized_image = self.img_file.resize(
            (self.parent.winfo_width(), self.parent.winfo_height())
        )

        self.image = ImageTk.PhotoImage(resized_image)

        self.background_item = self.background_canvas.create_image(
            0, 0, anchor="nw", image=self.image
        )

    def handle_resize(self, event):
        resized_image = self.img_file.resize(size=(event.width, event.height))
        background_image = ImageTk.PhotoImage(resized_image)
        background_image.image = background_image
        self.background_canvas.itemconfig(self.background_item, image=background_image)

    def next_screen(self):
        self.parent.event_generate("<<ChangeScreen>>", x=1)
