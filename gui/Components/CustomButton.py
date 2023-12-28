"""
Button Implementaion that changes the background image on hover
"""
from enum import Enum, auto
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import PhotoImage
from Constants import SQUARE_DARK_DEFAULT, DARKLY
from pathlib import Path
from PIL import Image, ImageTk


class buttonState(Enum):
    DEFAULT = auto()
    HOVER = auto()


# noinspection PyUnresolvedReferences
class CustomButton(ttk.Button):
    """
    Custom button that enables automatic switching of the background image on hover
    """

    def __init__(self,
                 master,
                 defaultPhotoPath: Path,
                 hoverPhotoPath: Path,
                 pressedPhotoPath: Path = None,
                 background=DARKLY["colors"]["bg"],
                 **kwargs
                 ) -> None:

        super().__init__(master, **kwargs)

        self.photoPaths = {
            "default": defaultPhotoPath,
            "hover": hoverPhotoPath,
        }


        self.defaultPhotoImage = PhotoImage("default", file=defaultPhotoPath)
        self.hoverPhotoImage = PhotoImage("hover", file=hoverPhotoPath)

        self.photoImages = [self.defaultPhotoImage,
                            self.hoverPhotoImage]

        if pressedPhotoPath:
            self.pressedPhotoImage = PhotoImage("pressed", file=pressedPhotoPath)
            self.photoImages.append(self.pressedPhotoImage)
            self.photoPaths.update({"pressed": pressedPhotoPath})


        s = ttk.Style()  # extract to parent class as a class variable so that it is not redefined every time
        s.configure("custom.TButton", focuscolor="", borderwidth=0, bootstyle="secondary", background=background)

        self.configure(style="custom.TButton", image=self.defaultPhotoImage)

        self.bind("<Configure>", self.resize)
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)

    def resize(self, event):
        width = self.winfo_width()
        height = self.winfo_height()

        resisedContainer = []
        for keys,path in self.photoPaths.items():
            image = Image.open(path)
            image = image.resize((width, height))
            photo = ImageTk.PhotoImage(image)
            resisedContainer.append(photo)
        self.photoImages = resisedContainer
        print(height, width)


    def onEnter(self, event):
        self["image"] = self.hoverPhotoImage

    def onLeave(self, event):
        self["image"] = self.defaultPhotoImage

    def onLeftClick(self, event):
        if self.pressedPhotoImage:
            self["image"] = self.pressedPhotoImage


if __name__ == "__main__":
    window = ttk.Window(
        themename="darkly",
        size=(300, 300),
    )

    D = SQUARE_DARK_DEFAULT / "Square-Dark-Default.png"
    H = SQUARE_DARK_DEFAULT / "Square-Dark-Hover.png"

    defaultImage = ttk.PhotoImage(name="default", file=D)
    hoverImage = ttk.PhotoImage(name="hover", file=H)

    MyButton = CustomButton(window,
                            D,
                            H,
                            compound="center",
                            text="test", )

    MyButton.grid(row=1, column=1, sticky=EW)

    window.mainloop()
