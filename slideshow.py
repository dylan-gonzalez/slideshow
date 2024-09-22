import os
import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk, ImageEnhance
import random
import gc

IMAGES_DIR = '/home/slideshow/slideshow/images'
QUOTES_IMAGES_DIR = '/home/slideshow/slideshow/quotes_images/1920x1080'

# Get all image files in the current directory
def get_image_files(image_dir):
    supported_formats = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
    return [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.lower().endswith(supported_formats)]

# Create a class for the slideshow
class SlideshowApp:
    def __init__(self, root, image_files, delay=3000, fade_duration=1000, fade=True):
        self.root = root
        self.root.title("Image Slideshow")
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.overrideredirect(1)

        self.delay = delay  # Slideshow delay (milliseconds)
        self.fade_duration = fade_duration  # Fade duration (milliseconds)
        self.fade = fade

        # Set the window to fullscreen
        self.root.attributes('-fullscreen', False)
        self.root.bind("<Escape>", self.toggle_fullscreen)  # Allow toggling fullscreen with the Escape key

        # Get screen size
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Load the images
        #self.images = cycle([Image.open(img) for img in image_files])
        self.images = cycle(image_files)

        # Create canvas to display the images
        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.config(width=self.screen_width, height=self.screen_height)
        
        # Initialize image variables to keep references
        self.current_image = None 
        self.current_image_tk = None 
        self.next_image = None

        # Start the slideshow
        self.root.after(100, self.show_next_image)

    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))
        return "break"

    def display_image(self, img):
        """Display the image centered on the canvas."""
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image((self.canvas.winfo_width()) // 2, (self.canvas.winfo_height()) // 2, image=img_tk, anchor=tk.CENTER)
        self.root.update()
        # Keep a reference to prevent garbage collection
        self.current_image_tk = img_tk
        self.current_image = img

    def apply_fade(self, img, alpha):
        """Apply fade effect by changing the image opacity."""
        img = img.convert("RGBA")
        alpha_channel = img.split()[3].point(lambda p: p * alpha)  # Adjust the alpha channel
        img.putalpha(alpha_channel)
        return img

    def show_next_image(self):
        # Get the next image from the iterator
        img_path = next(self.images)
        img = Image.open(img_path)
        print(f'img: {img}')

        # Resize image to fit while maintaining aspect ratio
        img_width, img_height = img.size
        #print(f"Original image dimensions: {img_width}x{img_height}")

        aspect_ratio = img_width / img_height
        if self.screen_width / self.screen_height > aspect_ratio:
            new_height = self.screen_height
            new_width = int(new_height * aspect_ratio)
        else:
            new_width = self.screen_width
            new_height = int(new_width / aspect_ratio)

        img = img.resize((new_width, new_height), Image.LANCZOS)
        #print(f"Adjusted image dimensions: {new_width}x{new_height}")

        if self.current_image:
            if self.fade:
                # Fade out the current image
                self.fade_out(self.current_image, 1.0, 0.0, self.fade_duration)
            else:
                print("deleting canvas")
                self.current_image.close()
                self.canvas.delete("all")

        # Store the next image for the fade-in effect
        self.next_image = img
        if self.fade:
            self.fade_in(self.next_image, 0.0, 1.0, self.fade_duration)
        else:
            self.display_image(self.next_image)
        
        # Schedule the next image
        self.root.after(self.delay + self.fade_duration, self.show_next_image)
        gc.collect()

    def fade_out(self, img, start_alpha, end_alpha, duration):
        """Fade out effect."""

        steps = 20
        interval = duration // steps
        for i in range(steps):
            alpha = start_alpha - (start_alpha - end_alpha) * (i / steps)
            img_fade = self.apply_fade(img, alpha)
            self.display_image(img_fade)

    def fade_in(self, img, start_alpha, end_alpha, duration):
        """Fade in effect."""
        steps = 20
        interval = duration // steps
        for i in range(steps):
            alpha = start_alpha + (end_alpha - start_alpha) * (i / steps)
            img_fade = self.apply_fade(img, alpha)
            self.display_image(img_fade)
        
    def on_closing():
        print("Exiting gracefully...")
        root.destroy()  # Close the Tkinter window
        sys.exit(0)  # Exit the program

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
    app = SlideshowApp(root, image_files, delay=30000, fade_duration=1000, fade=False)
    root.mainloop()

if __name__ == "__main__":
    start_slideshow()

