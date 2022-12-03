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
def remove_file():
    global output_path
    output_path = filedialog.asksaveasfilename(title="Save as",
     filetypes=(("png files", ".png"), ("all files", "*.*")))

    input =Image.open(input_path)

    output = remove() 

    output.save(output_path,"png")

    global my_img
    my_img = ImageTk.PhotoImage(Image.open(output_path))


    my_label.config(Image=my_img)





my_label = Label(root, text="Remove Background", font=("Arial", 20))
my_label.pack(pady=20)

open_Button = Button(root, text="Select Image", command=open_file)
open_Button.pack(pady=20)

rem_Button = Button(root, text="remove Image", command=remove_file)
rem_Button.pack(pady=20)
root.mainloop()
