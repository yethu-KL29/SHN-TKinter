from tkinter import *
from tkinter import filedialog
from rembg import remove
from PIL import ImageTk,Image
root = Tk()
root.title("remove background")
root.geometry("600x800")

def open_file():
    global input_path,my_img

    input_path = filedialog.askopenfilename( title="Select A File",
     filetypes=(("png files", ".png"), ("all files", "*.*")))

    
    if input_path:
        my_img = ImageTk.PhotoImage(Image.open(input_path))
        my_label.config(image=my_img,bg="black")

my_label = Label(root, text="Remove Background", font=("Arial", 20))
my_label.pack(pady=20)

open_Button = Button(root, text="Select Image", command="select_image")
open_Button.pack(pady=20)

rem_Button = Button(root, text="remove Image", command="remove_image")
rem_Button.pack(pady=20)
root.mainloop()
