from pathlib import Path

ASSETS_PATH = Path(__file__).parent.parent / "assets"
RECT_DARK_DEFAULT = ASSETS_PATH / "Rect-Dark-Default"
SQUARE_DARK_DEFAULT = ASSETS_PATH / "Square-Dark-Default"
DARKLY =  {
        "type": "dark",
        "colors": {
            "primary": "#375a7f",
            "secondary": "#444444",
            "success": "#00bc8c",
            "info": "#3498db",
            "warning": "#f39c12",
            "danger": "#e74c3c",
            "light": "#ADB5BD",
            "dark": "#303030",
            "bg": "#222222",
            "fg": "#ffffff",
            "selectbg": "#555555",
            "selectfg": "#ffffff",
            "border": "#222222",
            "inputfg": "#ffffff",
            "inputbg": "#2f2f2f",
        }}