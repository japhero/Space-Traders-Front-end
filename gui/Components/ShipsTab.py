import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from Constants import DARKLY, SQUARE_DARK_DEFAULT, RECT_DARK_DEFAULT
from CustomButton import CustomButton


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
            _path = SQUARE_DARK_DEFAULT / item
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        for key, item in (RECT_IMAGE_FILES).items():
            _path = RECT_DARK_DEFAULT / item
            self.photoimages.append(ttk.PhotoImage(name=key, file=_path))

        container = ttk.Frame(self)
        container.columnconfigure(0, weight=0)

        self.name_number = ttk.StringVar(container, "        -1")
        name_label = CustomButton(container,
                                  text=self.name_number.get(),
                                  compound="center",
                                  default_photo_path=RECT_DARK_DEFAULT / "rocketImage.png",
                                  hover_photo_path=RECT_DARK_DEFAULT / "rocketImageHover.png", )

        self.fuel_number_state = ttk.StringVar(container, "-1%")
        fuel_number_label = ttk.Label(container,
                                      text=self.fuel_number_state.get(),
                                      image="square-Default-Background",
                                      compound="center",
                                      bootstyle="light"
                                      )

        self.flight_mode_state = ttk.StringVar(container, "Idle")
        flight_mode_label = ttk.Label(container,
                                      text=self.flight_mode_state.get(),
                                      image="square-Default-Background",
                                      compound="center",
                                      bootstyle="light"
                                      )

        for i, component in enumerate([name_label, fuel_number_label, flight_mode_label]):
            component.grid(row=0, column=i, pady=5, padx=0, sticky=E)

        container.pack(fill=BOTH, expand=YES)

        @property
        def fuel_number_state(self):
            return self.flight_mode_state

        @fuel_number_state.setter
        def fuel_number_state(self, value):
            self.flight_mode_state.set(f"{value}%")

        @property
        def name_number(self):
            return self.name_number

        @name_number.setter
        def name_number(self, value):
            self.name_number.set(f"        {value}")

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
