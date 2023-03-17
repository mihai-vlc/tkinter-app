from tkinter import Button, Frame, Label


class MainScreen:
    def __init__(self, parent: Frame):
        self.parent = parent
        self.title = Label(parent, text="Main screen")
        self.title.pack()

        self.next_button = Button(parent, text="Next screen", command=self.next_screen)
        self.next_button.pack()

    def next_screen(self):
        self.parent.event_generate("<<ChangeScreen>>", x=1)
