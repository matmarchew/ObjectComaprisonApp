import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from CompareImages import compareImage

class MainGui(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent.wm_title("Select images")
        self.img1 = parent
        self.img2 = parent
        self.firstImage = None
        self.secondImage = None

        self.frame1 = tk.Frame(self.img1, width=500, height=400, bd=2)
        self.frame1.grid(row=1, column=0)
        self.frame2 = tk.Frame(self.img2, width=500, height=400, bd=1)
        self.frame2.grid(row=1, column=1)

        self.cv1 = tk.Canvas(self.frame1, height=390, width=490, bd=1, relief=tk.SUNKEN)
        self.cv1.grid(row=1,column=0)
        self.cv2 = tk.Canvas(self.frame2, height=390, width=490, bd=1, relief=tk.SUNKEN)
        self.cv2.grid(row=1,column=0)

        firstImageButton = tk.Button(parent, text='Select first image', height=2, width=30, command=lambda: self.loadImage(0))
        firstImageButton.grid(row=0, column=0, padx=2, pady=2)
        secondImageButton = tk.Button(parent, text='Select second image', height=2, width=30, command=lambda: self.loadImage(1))
        secondImageButton.grid(row=0, column=1, padx=2, pady=2)

        compareButton = tk.Button(parent, text='Compare images', height=2, width=30, command=lambda: compareImage(self.firstImage, self.secondImage))
        compareButton.grid(row=2, column=0, padx=2, pady=2, columnspan=2)

    def loadImage(self, k):
        path = filedialog.askopenfilename(initialdir="./Images", title="Choose your image", filetypes=(("jpeg files", "*.jpg"), ("PNG files", "*.png"), ("all files", "*.*")))
        im = Image.open(path)
        if (490 - im.size[0]) < (390 - im.size[1]):
            width = 490
            height = width * im.size[1] / im.size[0]
        else:
            height = 390
            width = height * im.size[0] / im.size[1]
        im.thumbnail((width, height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        if k == 0:
            self.firstImage = path
            self.img1 = photo
            self.cv1.create_image(0, 0, anchor='nw', image=photo)
        else:
            self.secondImage = path
            self.img2 = photo
            self.cv2.create_image(0, 0, anchor='nw', image=photo)

