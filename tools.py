from PIL import ImageTk, Image

def loadImage(path, width, height):
    return ImageTk.PhotoImage(Image.open(path).resize((width, height), Image.ANTIALIAS))