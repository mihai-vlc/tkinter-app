from tkinter import Frame
import TKinterModernThemes as TKMT


class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("My awesome application", "sun-valley", "dark")
        self.toplevel = self.root
        self.container = None
        self.screens = []
        self.active_screen = None
        self.configure_window()
        self.configure_events()

    def configure_window(self):
        self.toplevel.minsize(600, 400)
        self.toplevel.geometry("+3000+300")

    def configure_events(self):
        self.toplevel.bind("<<ChangeScreen>>", self.handle_change_screen)

    def handle_change_screen(self, event):
        screen_index = event.x
        self.activate_screen(screen_index)

    def add_screen(self, screen):
        self.screens.append(screen)

    def activate_screen(self, index):
        if self.container:
            self.container.destroy()

        self.container = Frame(self.toplevel)
        self.container.pack(side="top", fill="both", expand=True)

        Screen = self.screens[index]
        self.active_screen = Screen(self.container)

    def start(self):
        self.run()
