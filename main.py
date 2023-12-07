"""Script with simple order, convert your image to .ico"""

from PIL import Image
from tkinter import filedialog;
import os

filename = filedialog.askopenfile(title="Open file gotta be convert to .Ico").name
img = Image.open(filename)
where_to_save = filedialog.askdirectory(title="Give location where save converted file")
img.save(f"{os.path.join(where_to_save, 'favico.ico')}")
