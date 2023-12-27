"""
Button Implementaion that changes the background image on hover
"""
from enum import Enum, auto
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
from Paths import SQUARE_DARK_DEFAULT


class buttonState(Enum):
    DEFAULT = auto()
    HOVER = auto()


# noinspection PyUnresolvedReferences
class CustomButton(ttk.Button):
    """
    Custom button that enables automatic switching of the background image on hover
    """

    def __init__(self, master, defaultImageName: str, hoverImageName: str, **kwargs) -> None:
        """

        Args:
            master: the container of the button
            defaultImageName: name of the hovering PhotoImage.
            hoverImageName: name of the hovering PhotoImage.
            **kwargs: Keyword arguments in a dict

        Returns:
            None

        """

        super().__init__(master, image=defaultImageName, **kwargs)
        self.hoverImage = defaultImageName
        self.defaultImage = hoverImageName
        self.bind("<Enter>", self.enterHover)
        self.bind("<Leave>", self.exitHover)

    def enterHover(self, event) -> None:
        self.configure(image=self.hoverImage)

    def exitHover(self, event) -> None:
        self.configure(image=self.defaultImage)


if __name__ == "__main__":
    window = ttk.Window(
        themename="darkly",
        size=(300, 300),
    )
    window.style.configure('TButton', focuscolor='')

    D = SQUARE_DARK_DEFAULT / "Square-Dark-Default.png"
    H = SQUARE_DARK_DEFAULT / "Square-Dark-Hover.png"

    defaultImage = ttk.PhotoImage(name="default", file=D)
    hoverImage = ttk.PhotoImage(name="hover", file=H)

    MyButton = CustomButton(window,
                            "default",
                            "hover",
                            compound="center",
                            text="test")


    MyButton.pack(pady=5, padx=0)
    window.mainloop()
