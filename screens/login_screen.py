from tkinter import Button, Label


class LoginScreen:
    def __init__(self, parent):
        self.parent = parent
        self.title = Label(parent, text="Login screen")
        self.title.pack()

        self.back_button = Button(parent, text="Back", command=self.back)
        self.back_button.pack()

    def back(self):
        self.parent.event_generate("<<ChangeScreen>>", x=0)
