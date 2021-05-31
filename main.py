from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
import os
from PIL import Image

class converter_window:

    def openfile(self):
        '''
        Function for dialog box to select input images
        '''
        global img, import_file_path
        import_file_path = tkinter.filedialog.askopenfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", ".jpg"), ("All Files", "*.*")])
        self.input.delete(0, END)
        self.input.insert(0, import_file_path)
        img = Image.open(import_file_path)

    def convertToICO(self):
        '''
        Function for converting input image to ico
        '''
        global img, import_file_path
        print(os.path.exists(import_file_path))
        if os.path.exists(import_file_path) == True:
            if os.path.isfile(import_file_path) == True:
                export_file_path = tkinter.filedialog.asksaveasfilename(defaultextension='.ico', filetypes=[("ico files", "*.ico")])
                img.save(export_file_path)
                messagebox.showinfo("!!! SUCCESS !!!", "!!! *** FILE CONVERTED AND SAVED *** !!!")
            else:
                messagebox.showerror('!!! ERROR 502 !!!', '!!! *** IMAGE FILE"S PATH DOES NOT EXIST *** !!!')

    def __init__(self, root):
        self.root = root
        self.root.title("IMAGE TO ICON CONVERTER - BY SUHAS NIDGUNDI")
        self.root.geometry("500x240")
        self.root.wm_iconbitmap("icon.ico")
        self.root.resizable(False, False)

        self.title = Label(self.root, text="ICO CONVERTER", bg="green", fg="white", font=("helvetica", 24))
        self.title.pack(fill=X)

        Label(self.root, text="Select Input Image", font=("helvetica", 10, "bold"), fg="black", borderwidth=2).place(x=43, y=70)

        self.input = Entry(self.root, width=42, font=("console", 10), bg="lightblue", relief=GROOVE, borderwidth=2)
        self.input.place(x=45, y=100, height=33)

        btn_convert = Button(self.root, relief=FLAT, text="Choose File", font=("helvetica", 10, "bold"), activebackground="blue", activeforeground="white", bg="#0000FF", fg="white", command=self.openfile)
        btn_convert.place(x=355, y=100, width=95, height=32)

        btn_convert = Button(self.root, relief=FLAT, text="Convert to ICO", font=("helvetica", 12, 'bold'), activebackground="#FF8300", activeforeground="white", bg="#FF8300", fg="white", command=self.convertToICO)
        btn_convert.place(x=182, y=163, width=130, height=40)


if __name__ == "__main__":
    img = ''
    import_file_path = ""
    root = Tk()
    obj = converter_window(root)
    root.mainloop()