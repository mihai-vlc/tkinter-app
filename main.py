from tkinter import Tk
from tkinter import ttk

from app import App
from screens.login_screen import LoginScreen
from screens.main_screen import MainScreen



app = App(toplevel=Tk())

style = ttk.Style()

style.theme_settings("default", {
    "App.TButton": {
        "configure": {
            "padding": (20, 10),
        },
        "map": {
            "background": [("active", "#333"), ("!disabled", "#111")], 
            "foreground": [("!disabled", "#eee")],
        }
    }
})

app.add_screen(MainScreen)
app.add_screen(LoginScreen)

app.activate_screen(0)


if __name__ == "__main__":
    app.start()


