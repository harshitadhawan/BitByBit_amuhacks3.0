import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
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
        image = Image.open("C:\\Users\\ayush\\Downloads\\ldc logo.PNG")
        photo = ImageTk.PhotoImage(image)
        self.panel.config(image=photo)
        self.panel.image = photo

    def open_selection_form(self):
        self.withdraw()
        selection_form = SelectionForm(self)
        selection_form.mainloop()


class SelectionForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Detect, Protect, Cultivate!")
        self.geometry("975x500")

        self.panel = tk.Label(self)
        self.panel.place(x=0, y=0, relwidth=1, relheight=1)

        self.logo_image = Image.open("C:\\Users\\ayush\\Downloads\\ldc logo hori.PNG")
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self.panel, image=self.logo_photo)
        self.logo_label.place(x=142, y=12)

        self.cotton_image = Image.open(r"C:\Users\ayush\Downloads\leaf pics\leaf pics\cotton.jpg")
        self.cotton_photo = ImageTk.PhotoImage(self.cotton_image)
        self.cotton_button = tk.Button(self.panel, image=self.cotton_photo, command=self.open_cotton)
        self.cotton_button.place(x=36, y=250)

        self.potato_image = Image.open("C:\\Users\\ayush\\Downloads\\leaf pics\\leaf pics\\potato.jpg")
        self.potato_photo = ImageTk.PhotoImage(self.potato_image)
        self.potato_button = tk.Button(self.panel, image=self.potato_photo, command=self.open_potato)
        self.potato_button.place(x=269, y=250)

        self.mango_image = Image.open("C:\\Users\\ayush\\Downloads\\leaf pics\\leaf pics\\mango.jpg")
        self.mango_photo = ImageTk.PhotoImage(self.mango_image)
        self.mango_button = tk.Button(self.panel, image=self.mango_photo, command=self.open_mango)
        self.mango_button.place(x=502, y=250)

        self.tomato_image = Image.open("C:\\Users\\ayush\\Downloads\\leaf pics\\leaf pics\\tom.jpg")
        self.tomato_photo = ImageTk.PhotoImage(self.tomato_image)
        self.tomato_button = tk.Button(self.panel, image=self.tomato_photo, command=self.open_tom)
        self.tomato_button.place(x=735, y=250)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("File Path", f"Selected file: {file_path}")

    def open_cotton(self):
        messagebox.showinfo('Box',"Select an image of cotton leaf")
        class_labels = {0: 'Bacterial Blight', 1: 'Curl Virus', 2: 'Fusarium Wilt', 3: 'Healthy'}
        self.process_image(r"D:\leaf disease\cotton\cotton_model", class_labels)

    def open_mango(self):
        messagebox.showinfo('Box',"Select an image of mango leaf")  

    def open_tom(self):
        messagebox.showinfo('Box',"Select an image of tomato leaf") 
        class_labels = {'Tomato__Bacterial_spot': 0, 'Tomato_Early_blight': 1, 'Tomato_Late_blight': 2, 'Tomato_Leaf_Mold': 3, 'Tomato_Septoria_leaf_spot': 4, 'Tomato_Spider_mites Two-spotted_spider_mite': 5, 'Tomato_Target_Spot': 6, 'Tomato_Tomato_Yellow_Leaf_Curl_Virus': 7, 'Tomato_Tomato_mosaic_virus': 8, 'Tomato__healthy': 9}
        self.process_image(r"D:\leaf disease\tomato\tomato_model", class_labels)

    def open_potato(self):
        messagebox.showinfo('Box',"Select an image of potato leaf")
        class_labels = {0: 'Early_Blight', 1: 'Healthy', 2: 'Late_Blight'}
        self.process_image(r"D:\leaf disease\potato\potato_model", class_labels)

    def load_model_and_predict(self, model_path, image):
        model = load_model(model_path)
        image = image.resize((256, 256))
        image_array = np.expand_dims(np.array(image) / 255.0, axis=0)
        result = model.predict(image_array)
        return result

    def process_image(self, model_path, labels):
        global test_image
        test_image = self.open_image()
        if test_image:
            if model_path == r"D:\leaf disease\tomato\tomato_model":
                test_image = test_image.resize((128, 128))
                test_image = test_image.reshape((1, 128, 128, 3))
            result = self.load_model_and_predict(model_path, test_image)
            predicted_labels = np.argmax(result, axis=1)
            ans = [labels[label] for label in predicted_labels]
            messagebox.showinfo("Result", ", ".join(ans))

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;*.png")])
        if file_path:
            img = Image.open(file_path)
            img.thumbnail((300, 300)) 
            return img  

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
