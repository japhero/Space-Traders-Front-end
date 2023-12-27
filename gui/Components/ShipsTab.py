import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
import Paths


# noinspection PyArgumentList
class ShipInfoComponent(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        self.photoimages = []

        SQUARE_IMAGE_FILES = {
            "square-Default-Background": "Square-Dark-Default.png",


        }

        RECT_IMAGE_FILES = {
            "rect-Default-Background": "Rect-Dark-Default.png",
            "rect-Default-RocketShipIcon": "rocketImage.png",
        }

        for key, item in (SQUARE_IMAGE_FILES).items():
            _path = Paths.SQUARE_DARK_DEFAULT / item
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        for key, item in (RECT_IMAGE_FILES).items():
            _path = Paths.RECT_DARK_DEFAULT / item
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        container = ttk.Frame(self)
        container.columnconfigure(0, weight=0)

        nameLabel = ttk.Label(container,
                              text="         21",
                              compound="center",
                              image="rect-Default-RocketShipIcon",
                              bootstyle="light"
                              )

        fuelNumber = ttk.Label(container,
                               text="21",
                               image="square-Default-Background",
                               compound="center",
                               bootstyle="light"
                               )

        for i, component in enumerate([nameLabel, fuelNumber]):
            component.grid(row=0, column=i, pady=5, padx=0, sticky=E)

        container.pack(fill=BOTH, expand=YES)

        # Implement Update methods for component data and also innit structure


class ShipsTab(ScrolledFrame):

    def __int__(self, master, **kwargs):
        super().__init__(master, **kwargs)


if __name__ == "__main__":
    window = ttk.Window(
        themename="darkly",
        size=(350, 450),

    )

    MainComp = ShipInfoComponent(master=window)

    window.mainloop()
