from tkinter import Canvas, Tk, TclVersion
from PIL import Image, ImageTk

WIN_WIDTH = 600
WIN_HEIGHT = 400

root = Tk()
root.title("My awesome application")
root.configure(background="#444")
root.minsize(WIN_WIDTH, WIN_HEIGHT)
root.geometry("+3000+300")

img_file = Image.open("./resources/background.jpg")
background_canvas = Canvas(root, background="#555")
background_canvas.pack(fill="both", expand=True)
background_item = None

resized_image = img_file.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(resized_image)
background_item = background_canvas.create_image(
    0, 0, anchor="nw", image=background_image
)


def handle_resize(event):
    resized_image = img_file.resize(size=(event.width, event.height))
    background_image = ImageTk.PhotoImage(resized_image)
    background_image.image = background_image
    background_canvas.itemconfig(background_item, image=background_image)


root.bind("<Configure>", handle_resize)

print(f"running on {TclVersion = }")


if __name__ == "__main__":
    root.mainloop()
