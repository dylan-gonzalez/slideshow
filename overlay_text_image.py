import os
from PIL import Image, ImageDraw, ImageFont

FONT_SIZE=20
FONT = "fonts/Crimson_Text/CrimsonText-Regular.ttf"

# Function to wrap text to fit within the image width
def wrap_text(text, max_width, draw, font):
    # Split the text into individual words
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        # Calculate the width of the current line with the next word
        test_line = current_line + word + " "
        text_bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        
        if text_width <= max_width:
            current_line = test_line
        else:
            # If the line is too wide, add it to the list and start a new line
            lines.append(current_line)
            current_line = word + " "
    
    # Add the last line
    if current_line:
        lines.append(current_line)
    
    return lines

def overlay_text_on_images_in_directory(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Add more formats if needed
            image_path = os.path.join(input_dir, filename)
            overlay_text_on_image(image_path, filename, output_path=os.path.join(output_dir, filename)) 

def overlay_text_on_image(image_path, text, output_path='output_image.jpg'):
    # Open the image
    image = Image.open(image_path).convert("RGB")
    
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Load a font (you can change the path to a different font)
    try:
        font = ImageFont.truetype(FONT, FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if custom font not available

    # Get image size
    width, height = image.size
    
    #Calculate text bounding box
    #bbox = draw.textbbox((0, 0), text, font=font)
    #text_width = bbox[2] - bbox[0]
    #text_height = bbox[3] - bbox[1]
    
    # Calculate position (bottom right corner)
    #position = (width - text_width - 10, height - text_height - 10)  # 10 pixels from the edges
    
    # Draw the text on the image
    max_width = width - 200  # Leave some padding on the sides
    wrapped_lines = wrap_text(text, max_width, draw, font)
    #draw.text(position, text, fill="white", font=font)

    line_height = font.getbbox('A')[3]  # Use getbbox() for line height
    line_spacing = int(line_height * 1.5)
    total_text_height = len(wrapped_lines) * (line_height + line_spacing)

    y_text = height - 40 - total_text_height

    # Draw each line of the wrapped text
    for i, line in enumerate(wrapped_lines):
        text_bbox = draw.textbbox((0, 0), line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x_text = (width - text_width) // 2
        draw.text((x_text, y_text), line, font=font, fill=(255, 255, 255))

        y_text += line_height + line_spacing
    
    # Save the edited image
    image.save(output_path)

# Example usage
input_directory = 'images'  # Directory with images
output_directory = 'images/images_with_text'  # Directory to save edited images

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

overlay_text_on_images_in_directory(input_directory, output_directory) 
