import tkinter as tk


class MainGui(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        parent.wm_title("Select images")

        self.frame1 = tk.Frame(parent, width=500, height=400, bd=2)
        self.frame1.grid(row=1, column=0)
        self.frame2 = tk.Frame(parent, width=500, height=400, bd=1)
        self.frame2.grid(row=1, column=1)

        self.cv1 = tk.Canvas(self.frame1, height=390, width=490, bd=1, relief=tk.SUNKEN)
        self.cv1.grid(row=1,column=0)
        self.cv2 = tk.Canvas(self.frame2, height=390, width=490, bd=1, relief=tk.SUNKEN)
        self.cv2.grid(row=1,column=0)

        firstImageButton = tk.Button(parent, text='Select first image', height=2, width=30)
        firstImageButton.grid(row=0, column=0, padx=2, pady=2)
        secondImageButton = tk.Button(parent, text='Select second image', height=2, width=30)
        secondImageButton.grid(row=0, column=1, padx=2, pady=2)

        compareButton = tk.Button(parent, text='Compare images', height=2, width=30)
        compareButton.grid(row=2, column=0, padx=2, pady=2, columnspan=2)
