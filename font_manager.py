import tkinter.font as tkfont

def configure_fonts(family="Helvetica", sizes=(15, 12, 12)):
    """
    Configure the default fonts for the Tkinter application.

    Args:
        family (str): The font family to use. Defaults to "Helvetica".
        sizes (tuple): The font sizes to use. Defaults to (15, 12, 12).
    """
    fonts = [tkfont.nametofont(name) for name in ["TkDefaultFont", "TkTextFont", "TkFixedFont"]]
    for font, size in zip(fonts, sizes):
        font.configure(family=family, size=size)

# Usage
configure_fonts("Segoe UI")