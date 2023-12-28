import ttkbootstrap as ttk
from ttkbootstrap import PhotoImage
from Constants import SQUARE_DARK_DEFAULT, DARKLY
from pathlib import Path
from PIL import Image, ImageTk


class CustomButton(ttk.Button):
    """
    Class that's goal is to implement 2-3 images as the indicators for its condition and sizes to allow custom images
    to be used-in GUI's
    """
    def __init__(self,
                 master: any,
                 default_photo_path: Path,
                 hover_photo_path: Path,
                 pressed_photo_path: Path = None,
                 background: str = DARKLY["colors"]["bg"],
                 **kwargs: any
                 ) -> None:
        """

        Args:
            master: container
            default_photo_path: path of the default background photo
            hover_photo_path: path of the photo displayed on hover
            pressed_photo_path: optional photo displayed on click
            background: optional background
            **kwargs: keword arguments
        """
        super().__init__(master, **kwargs)

        self.photo_paths = {
            "default": default_photo_path,
            "hover": hover_photo_path,
        }

        self.defaultPhotoImage = PhotoImage("default", file=default_photo_path)
        self.hoverPhotoImage = PhotoImage("hover", file=hover_photo_path)

        self.photo_images = [self.defaultPhotoImage,
                             self.hoverPhotoImage]

        if pressed_photo_path:
            self.pressed_photo_image = PhotoImage("pressed", file=pressed_photo_path)
            self.photo_images.append(self.pressed_photo_image)
            self.photo_paths.update({"pressed": pressed_photo_path})

        s = ttk.Style()
        s.configure("custom.TButton", focuscolor="", borderwidth=0, bootstyle="secondary", background=background)
        s.map("custom.TButton",
              background=[("active", background), ],
              image=[("active", self.photo_images[1]), ("!active", self.photo_images[0])])

        self.configure(style="custom.TButton")

        self.bind("<Configure>", self.__resize)

    def __resize(self, event: any) -> None:
        width = self.winfo_width()
        height = self.winfo_height()
        resized_container = []
        for keys, path in self.photo_paths.items():
            image = Image.open(path)
            image = image.resize((width, height))
            photo = ImageTk.PhotoImage(image)
            resized_container.append(photo)
        self.photo_images = resized_container


if __name__ == "__main__":
    window = ttk.Window(
        themename="darkly",
        size=(300, 300),
    )

    D = SQUARE_DARK_DEFAULT / "Square-Dark-Default.png"
    H = SQUARE_DARK_DEFAULT / "Square-Dark-Hover.png"

    MyButton = CustomButton(window,
                            D,
                            H,
                            compound="center",
                            text="test", )

    MyButton.pack(pady=30)

    window.mainloop()
