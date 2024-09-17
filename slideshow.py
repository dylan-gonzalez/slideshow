import os
import time
import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk

IMAGE_DIR = 'images'

# Get all image files in the current directory
def get_image_files():
    supported_formats = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
    return [os.path.join(IMAGE_DIR, file) for file in os.listdir(IMAGE_DIR) if file.lower().endswith(supported_formats)]

# Create a class for the slideshow
class SlideshowApp:
    def __init__(self, root, image_files, delay=3000):
        self.root = root
        self.root.title("Image Slideshow")
        self.delay = delay  # Slideshow delay (milliseconds)
        
        # Load the images
        self.images = cycle([ImageTk.PhotoImage(Image.open(img)) for img in image_files])
        
        # Create label to display the images
        self.label = tk.Label(root)
        self.label.pack()
        
        # Start the slideshow
        self.show_next_image()
    
    def show_next_image(self):
        # Get the next image from the iterator
        img = next(self.images)
        self.label.config(image=img)
        self.root.after(self.delay, self.show_next_image)  # Change the image after a delay

# Main function to start the slideshow
def start_slideshow():
    image_files = get_image_files()
    if not image_files:
        print("No images found in the current directory!")
        return
    
    root = tk.Tk()
    app = SlideshowApp(root, image_files, delay=3000)  # 3000 ms delay between images
    root.mainloop()

if __name__ == "__main__":
    start_slideshow()

