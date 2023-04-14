from tkinter import Tk
from tkinter import ttk

from app import App
from screens.login_screen import LoginScreen
from screens.main_screen import MainScreen


app = App()

app.add_screen(MainScreen)
app.add_screen(LoginScreen)

app.activate_screen(0)


if __name__ == "__main__":
    app.start()
