import os
import time
import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk
import random

IMAGES_DIR = 'images'
QUOTES_IMAGES_DIR = 'quotes_images'


# Get all image files in the current directory
def get_image_files(image_dir):
    supported_formats = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
    return [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.lower().endswith(supported_formats)]

# Create a class for the slideshow
class SlideshowApp:
    def __init__(self, root, image_files, delay=3000):
        self.root = root
        self.root.title("Image Slideshow")
        self.delay = delay  # Slideshow delay (milliseconds)

        # Set the window to fullscreen
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)  # Allow toggling fullscreen with the Escape key
        
        # Load the images
        self.images = cycle([Image.open(img) for img in image_files])

        #Create canvas to display the images
        self.canvas = tk.Canvas(root, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Get screen size
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Initialize image variable to keep reference
        self.current_image = None
        self.next_image = None

        # Start the slideshow
        self.show_next_image()

    def show_next_image(self):
        # Get the next image from the iterator
        img = next(self.images)

        # Get image dimensions
        img_width, img_height = img.size
        
        # Calculate new dimensions while maintaining aspect ratio
        aspect_ratio = img_width / img_height
        if self.screen_width / self.screen_height > aspect_ratio:
            # Fit image to screen height
            new_height = self.screen_height
            new_width = int(new_height * aspect_ratio)
        else:
            # Fit image to screen width
            new_width = self.screen_width
            new_height = int(new_width / aspect_ratio)

        # Resize image to fit the window
        img = img.resize((new_width, new_height), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        # Update the canvas
        self.canvas.config(width=self.screen_width, height=self.screen_height)
        self.canvas.create_image(self.screen_width // 2, self.screen_height // 2, image=img_tk)

        self.current_image = img_tk

        self.root.after(self.delay, self.show_next_image)  # Change the image after a delay

    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))
        return "break"

# Main function to start the slideshow
def start_slideshow():
    image_files = get_image_files(IMAGES_DIR)
    quote_image_files = get_image_files(QUOTES_IMAGES_DIR)

    image_files = image_files + quote_image_files
    if not image_files:
        print("No images found!") 
        return

    random.shuffle(image_files)
    
    print(image_files)
    root = tk.Tk()
    app = SlideshowApp(root, image_files, delay=5000)  # 3000 ms delay between images
    root.mainloop()

if __name__ == "__main__":
    start_slideshow()

