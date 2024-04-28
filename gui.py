import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser
from tkinter import messagebox

from keras.models import load_model
import numpy as np

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Leaf Disease Classifier")
        self.geometry("800x528")

        self.panel = tk.Label(self)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)

        self.button = tk.Button(self.panel, text="Let's Begin 🍁", command=self.open_selection_form)
        self.button.config(bg="#B3EFD0", font=("Segoe Script", 15, "bold"))
        self.button.place(x=280, y=450, width=215, height=58)
        self.button.config(cursor="hand2", relief="flat")

        self.load_background_image()

    def load_background_image(self):
        image = Image.open("C:\\Users\\Welcome\\Downloads\\ldc logo.PNG")  # Adjust the image path
        photo = ImageTk.PhotoImage(image)
        self.panel.config(image=photo)
        self.panel.image = photo

    def open_selection_form(self):
        self.withdraw()  # Hide the main form
        selection_form = SelectionForm(self)
        selection_form.mainloop()


class SelectionForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Detect, Protect, Cultivate!")
        self.geometry("1000x700")

        self.panel = tk.Label(self)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)

        self.logo_image = Image.open("C:\\Users\\Welcome\\Downloads\\ldc logo hori.PNG")  # Adjust the image path
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self.panel, image=self.logo_photo)
        self.logo_label.place(x=142, y=12)

        self.upload_button = tk.Button(self.panel, text="Upload Image", command=self.upload_image)
        self.upload_button.config(bg="#B3EFD0", font=("Segoe Script", 10))
        self.upload_button.place(x=400, y=200)

        self.cotton_image = Image.open("C:\\Users\\Welcome\\Downloads\\leaf pics\\cotton.jpg")  # Adjust the image path
        self.cotton_photo = ImageTk.PhotoImage(self.cotton_image)
        self.cotton_button = tk.Button(self.panel, image=self.cotton_photo, command=self.open_cotton)
        self.cotton_button.place(x=36, y=250)

        self.potato_image = Image.open("C:\\Users\\Welcome\\Downloads\\leaf pics\\potato.jpg")  # Adjust the image path
        self.potato_photo = ImageTk.PhotoImage(self.potato_image)
        self.potato_button = tk.Button(self.panel, image=self.potato_photo, command=self.open_potato)
        self.potato_button.place(x=269, y=250)

        self.mango_image = Image.open("C:\\Users\\Welcome\\Downloads\\leaf pics\\mango.jpg")  # Adjust the image path
        self.mango_photo = ImageTk.PhotoImage(self.mango_image)
        self.mango_button = tk.Button(self.panel, image=self.mango_photo, command=self.open_mango)
        self.mango_button.place(x=502, y=250)

        self.tomato_image = Image.open("C:\\Users\\Welcome\\Downloads\\leaf pics\\tom.jpg")  # Adjust the image path
        self.tomato_photo = ImageTk.PhotoImage(self.tomato_image)
        self.tomato_button = tk.Button(self.panel, image=self.tomato_photo, command=self.open_tom)
        self.tomato_button.place(x=735, y=250)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        # Do something with the file_path, like displaying the image
        if file_path:
            messagebox.showinfo("File Path", f"Selected file: {file_path}")


    def open_cotton(self):
        messagebox.showinfo("Potato Image Clicked", "Potato image clicked!")  # Example: showing a message box
        #webbrowser.open("cotton_disease.ipynb")  # Adjust the link or action accordingly
        
    def open_mango(self):
        messagebox.showinfo("Potato Image Clicked", "Potato image clicked!")  # Example: showing a message box
        #webbrowser.open("cotton_disease.ipynb")     
    
    def open_tom(self):
        messagebox.showinfo("Potato Image Clicked", "Potato image clicked!")  # Example: showing a message box
        #webbrowser.open("cotton_disease.ipynb") 
    
    def open_potato(self):
        # You can open a link or perform any action here
        messagebox.showinfo("Potato Image Clicked", "Potato image clicked!")  # Example: showing a message box

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
