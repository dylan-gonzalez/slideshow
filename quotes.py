from PIL import Image, ImageDraw, ImageFont
import json
import os

'''
https://www.brainyquote.com/authors/leonardo-da-vinci-quotes (page 1)

let xpath = "//a[@title='view quote']/div"
let result = document.evaluate(xpath, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);

arr = [];

// Loop through all matching divs
for (let i = 0; i < result.snapshotLength; i++) {
    arr.push(result.snapshotItem(i).textContent);
}

console.log(arr)
'''

FONT_SIZE = 80#120
IMAGE_WIDTH = 1920#3840
IMAGE_HEIGHT = 1080#2160
FONT = "fonts/Crimson_Text/CrimsonText-Regular.ttf"
FONT_AUTHOR = "fonts/Crimson_Text/CrimsonText-Italic.ttf"
FONT_AUTHOR_SIZE = 60#100

def convert_quotes_to_json(quotes, author):
    quotes_dict = [{"quote": quote.strip(), "author": author} for i, quote in enumerate(quotes)]
    return json.dumps(quotes_dict, indent=4)

# Function to wrap text to fit within the image width
def wrap_text(text, font, max_width, draw):
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

# Function to create an image for each quote
def create_quote_image(quote, author, image_size=(IMAGE_WIDTH, IMAGE_HEIGHT), output_folder="quotes_images"):
    # Create a black background
    img = Image.new('RGB', image_size, color=(0, 0, 0))
    
    # Initialize drawing context
    draw = ImageDraw.Draw(img)
    
    # Load a font (you can change the path to a different font)
    try:
        font = ImageFont.truetype(FONT, FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if custom font not available

    try:
        font_author = ImageFont.truetype(FONT_AUTHOR, FONT_AUTHOR_SIZE)
    except IOError:
        font_author = ImageFont.load_default()  # Fallback to default font if custom font not available
    
    # Wrap the text to fit within the image width
    max_width = image_size[0] - 200  # Leave some padding on the sides
    wrapped_lines = wrap_text(quote, font, max_width, draw)
    
    # Calculate total height of the text block
    line_height = font.getbbox('A')[3]  # Use getbbox() for line height
    line_spacing = int(line_height * 1.5)
    total_text_height = len(wrapped_lines) * (line_height + line_spacing)

    # Start drawing text from vertical center
    y_text = (image_size[1] - total_text_height) // 2
    
    # Draw each line of the wrapped text
    for i, line in enumerate(wrapped_lines):
        text_bbox = draw.textbbox((0, 0), line, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x_text = (image_size[0] - text_width) // 2
        draw.text((x_text, y_text), line, font=font, fill=(255, 255, 255))

        #draw.line((0, y_text, image_size[0], y_text), fill=(255, 0, 0), width=2)  # Red line with 2-pixel width

        #for some reason, the offset between the 1st and 2nd lines does not get applied properly
        if i == 0:
            y_text += line_spacing * 1.01
        else:
            y_text += line_spacing

    middle = image_size[0] // 2

    draw.text((middle, image_size[1] * 0.8), author, font=font_author, fill=(255,255,255))
    
    # Save the image
    output_dir = f"{output_folder}/{IMAGE_WIDTH}x{IMAGE_HEIGHT}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #file_path = output_dir + f"/quote_{quotes.index(quote)+1}.png"
    file_path = output_dir + f"/{author}_{quote[0:10]}.png"
    img.save(file_path)
    print(f"Saved: {file_path}")

dir_path = 'quotes_images'
# Create images for all quotes
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

quotes_file = open('quotes.json')
quotes = json.load(quotes_file)

for quote in quotes["quotes"]:
    if quote["author"] != "Leonardo Da Vinci":
        create_quote_image(quote=quote["quote"], author=quote["author"])

#json_output = convert_quotes_to_json(quotes, "Napoleon Bonaparte")
#print(json_output)
