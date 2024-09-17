import os
import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk, ImageEnhance
import random

IMAGES_DIR = 'images'
QUOTES_IMAGES_DIR = 'quotes_images'

# Get all image files in the current directory
def get_image_files(image_dir):
    supported_formats = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
    return [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.lower().endswith(supported_formats)]

# Create a class for the slideshow
class SlideshowApp:
    def __init__(self, root, image_files, delay=3000, fade_duration=1000):
        self.root = root
        self.root.title("Image Slideshow")
        self.delay = delay  # Slideshow delay (milliseconds)
        self.fade_duration = fade_duration  # Fade duration (milliseconds)

        # Set the window to fullscreen
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)  # Allow toggling fullscreen with the Escape key

        # Get screen size
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Load the images
        self.images = cycle([Image.open(img) for img in image_files])

        # Create canvas to display the images
        self.canvas = tk.Canvas(root, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Initialize image variables to keep references
        self.current_image = None #For applying fade effects (PIL)
        self.current_image_tk = None #For showing the image once faded in (tk)
        self.next_image = None

        # Start the slideshow
        self.show_next_image()

    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))
        return "break"

    def apply_fade(self, img, alpha):
        """Apply fade effect by changing the image opacity."""
        print(type(img))
        img = img.convert("RGBA")
        alpha_channel = img.split()[3].point(lambda p: p * alpha)  # Adjust the alpha channel
        img.putalpha(alpha_channel)
        return img

    def show_next_image(self):
        # Get the next image from the iterator
        img = next(self.images)

        # Resize image to fit while maintaining aspect ratio
        img_width, img_height = img.size
        aspect_ratio = img_width / img_height
        if self.screen_width / self.screen_height > aspect_ratio:
            new_height = self.screen_height
            new_width = int(new_height * aspect_ratio)
        else:
            new_width = self.screen_width
            new_height = int(new_width / aspect_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)

        if self.current_image:
            # Fade out the current image
            self.fade_out(self.current_image, 1.0, 0.0, self.fade_duration)
        
        # Store the next image for the fade-in effect
        self.next_image = img
        self.fade_in(self.next_image, 0.0, 1.0, self.fade_duration)
        
        # Schedule the next image
        self.root.after(self.delay + self.fade_duration, self.show_next_image)

    def fade_out(self, img, start_alpha, end_alpha, duration):
        """Fade out effect."""

        print("fading out")
        steps = 10
        interval = duration // steps
        for i in range(steps):
            alpha = start_alpha - (start_alpha - end_alpha) * (i / steps)
            img_fade = self.apply_fade(img, alpha)
            img_tk = ImageTk.PhotoImage(img_fade)
            self.canvas.create_image(self.screen_width // 2, self.screen_height // 2, image=img_tk)
            self.root.update()
            self.root.after(interval)
            self.canvas.delete("all")
            self.current_image = img_tk  # Keep a reference to the image

    def fade_in(self, img, start_alpha, end_alpha, duration):
        """Fade in effect."""
        print('fading in')
        steps = 10
        interval = duration // steps
        for i in range(steps):
            alpha = start_alpha + (end_alpha - start_alpha) * (i / steps)
            img_fade = self.apply_fade(img, alpha)
            img_tk = ImageTk.PhotoImage(img_fade)
            self.canvas.create_image(self.screen_width // 2, self.screen_height // 2, image=img_tk)
            self.root.update()
            self.root.after(interval)
        
        # Keep a reference to the final image to prevent garbage collection
        self.current_image_tk = img_tk
        self.current_image = img

# Main function to start the slideshow
def start_slideshow():
    image_files = []
    image_files = get_image_files(IMAGES_DIR)
    quote_image_files = get_image_files(QUOTES_IMAGES_DIR)

    image_files = image_files + quote_image_files
    if not image_files:
        print("No images found!") 
        return

    random.shuffle(image_files)
    
    print(image_files)
    root = tk.Tk()
    app = SlideshowApp(root, image_files, delay=3000, fade_duration=1000)  # 5000 ms delay between images, 1000 ms fade duration
    root.mainloop()

if __name__ == "__main__":
    start_slideshow()

