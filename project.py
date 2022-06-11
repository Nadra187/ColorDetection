# Import the required libraries
import tkinter as tk

# importing askopenfilename function from class filedialog
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

import colorDetection

# This function will be used to open file in read mode and only image files will be opened
# and file path will be stored
def getImage():
    filetypes = (
        ('*.jpg file', '*.jpg' ),
        ('*.jpeg file', '*.jpeg' ),
        ('*.png file', '*.png' )
    )

    filename = askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    # user did not choose the file
    if filename == '':
        showinfo(
            title='Selected image',
            message= 'No image is choosen'
        )
    else:
        colorDetection.colorDetection(filename)

# Create an instance of tkinter frame
# creating window by initializing a new Tkinter object with the help of the Tk() method.
window=tk.Tk()

# giving this window a title.
window.title(" Flying Colors ")

# Set the geometry of frame
window.geometry("800x500")

#creating button
button1 = tk.Button(window, text ="Select Image", font=('Times New Roman bold',20),
                    bg='#f00', fg= '#ff0', pady=20, padx=40,
                    command=getImage())
#lambda:
#placing button
button1.place(x=250, y=150)

#mainloop() tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, and blocks any code
# that comes after it from running until you close the window where you called the method.
window.mainloop()