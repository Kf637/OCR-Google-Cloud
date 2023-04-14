import io
import os
import tempfile

from google.cloud import vision
from google.oauth2 import service_account
import google.api_core.exceptions
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk, ImageGrab

API_Respond_Print = False

###### SETUP FOR TEMP FOLDER ######

# Create a temporary directory with prefix "temp_OCR_"
print('Creating temp folder...')
temp_dir = tempfile.mkdtemp(prefix='temp_OCR_')

# Add an "OCR" folder to the temporary directory
folder_path = os.path.join(temp_dir, "OCR")

# Print the path of the temporary directory
print('Temporary directory created with location ',temp_dir)

# Define the file types you want to allow
filetypes = (
    ("JPEG Files", "*.jpg"),
    ("PNG Files", "*.png")
)

# Define UI
class OCRApp:
    def __init__(self, master):
        self.master = master
        master.title("Google Cloud Vision OCR")

        # Initialize Google Cloud Vision API
        credentials = service_account.Credentials.from_service_account_file('credentials.json')
        self.client = vision.ImageAnnotatorClient(credentials=credentials)

        # Create button to print API respond
        self.api_button = tk.Button(master, text="Loading....", command=self.API_Respond)
        self.api_button.pack()
        if API_Respond_Print == False:
          self.api_button.configure(text="Print API Respond Off", foreground='red')

        # Create button to load image
        self.load_button = tk.Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Create button to paste image
        self.paste_button = tk.Button(master, text="Paste Image", command=self.paste_image)
        self.paste_button.pack()

        # Initialize label to display image
        self.image_label = tk.Label(master)
        self.image_label.pack()

        # Initialize text box to display text
        self.text_box = tk.Text(master, wrap='word')
        self.text_box.pack(fill='both', expand=True)

   
     
    # Load image from file
    def load_image(self):
        
        # Get image file path from user
        #file_path = filedialog.askopenfilename()
  
        # Show file explorer and allow selection of image files only
        file_path = filedialog.askopenfilename(initialdir='/', title='Select Image File', filetypes=filetypes)


        # Check if a file was selected before attempting to open it
        if file_path:
            with open(file_path, 'rb') as f:
                image = Image.open(f)
            image = image.resize((500, 500))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

        # Process image with Google Cloud Vision OCR

            with open(file_path, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            response = self.client.document_text_detection(image=image)
            text = response.full_text_annotation.text


        # Print OCR API response payload to console
            if API_Respond_Print == True:
                    print(response)

            text = response.full_text_annotation.text
        


        # Display OCR text
            if text:
                self.text_box.delete('1.0', 'end')
                self.text_box.insert('1.0', text)
            else:
                self.text_box.delete('1.0', 'end')
                self.text_box.tag_configure('red', foreground='red')
                self.text_box.insert('1.0', 'No text could be found.', 'red')

    # Paste image from clipboard
    def paste_image(self):
        if not self.is_clipboard_image():
            self.text_box.delete('1.0', 'end')
            self.text_box.tag_configure('red', foreground='red')
            self.text_box.insert('1.0', 'Clipboard does not contain an image.', 'red')

            return

        # Get image from clipboard and preview
        image = ImageGrab.grabclipboard()
        self.paste_button.configure(text="Calling API...", foreground='red')
        if image:
            image = image.resize((500, 500))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

            # Save image to temporary file
            try:
                print('Saving file to temporary directory')
                temp_file = tempfile.NamedTemporaryFile(suffix='.png', dir=temp_dir, delete=False)
                file_path = os.path.join(temp_dir, temp_file.name.split('\\')[-1])
                image.save(file_path, 'PNG')
                temp_file.close()
                print('Image has been saved to temporary directory')
                print(file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
                self.paste_button.configure(text="An error occurred, please restart script..", foreground='red')
                self.text_box.delete('1.0', 'end')
                self.text_box.insert('1.0', f"An error occurred: {e}", 'red')


            # Process image with Google Cloud Vision OCR
            
            with io.open(file_path, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            response = self.client.document_text_detection(image=image)
            text = response.full_text_annotation.text
            self.paste_button.configure(text="Paste Image", foreground='black')

            # Print OCR API response payload to console
            if API_Respond_Print == True:
                print(response)

            text = response.full_text_annotation.text

            # Display OCR text
            if text:
                self.text_box.delete('1.0', 'end')
                self.text_box.insert('1.0', text)
            else:
                self.text_box.delete('1.0', 'end')
                self.text_box.tag_configure('red', foreground='red')
                self.text_box.insert('1.0', 'No text could be found.', 'red')



    def is_clipboard_image(self):
        clipboard = ImageGrab.grabclipboard()
        return clipboard is not None and isinstance(clipboard, Image.Image)
    
    def API_Respond(self):
        global API_Respond_Print
        if API_Respond_Print == True:
          API_Respond_Print = False
          print('API_Respond_Print is now false')
          self.api_button.configure(text="Print API Respond Off", foreground='red')
        elif API_Respond_Print == False:
          API_Respond_Print = True
          print('API_Respond_Print is now true')
          self.api_button.configure(text="Print API Respond On", foreground='green')
        
 



# Initialize UI
root = tk.Tk()
app = OCRApp(root)
root.mainloop()

