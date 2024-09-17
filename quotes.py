from PIL import Image, ImageDraw, ImageFont

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

FONT_SIZE = 120
IMAGE_WIDTH = 3840
IMAGE_HEIGHT = 2160
FONT = "Crimson_Text/CrimsonText-Regular.ttf"
FONT_AUTHOR = "Crimson_Text/CrimsonText-Italic.ttf"
FONT_AUTHOR_SIZE = 100

quotes = [
    "\nLearning never exhausts the mind.\n\n",
    "\nNothing strengthens authority so much as silence.\n\n",
    "\nTears come from the heart and not from the brain.\n\n",
    "\nAs a well-spent day brings happy sleep, so a life well spent brings happy death.\n\n",
    "\nI have been impressed with the urgency of doing. Knowing is not enough; we must apply. Being willing is not enough; we must do.\n\n",
    "\nThe human foot is a masterpiece of engineering and a work of art.\n\n",
    "\nThe beginnings and ends of shadow lie between the light and darkness and may be infinitely diminished and infinitely increased. Shadow is the means by which bodies display their form. The forms of bodies could not be understood in detail but for shadow.\n\n",
    "\nNature is the source of all true knowledge. She has her own logic, her own laws, she has no effect without cause nor invention without necessity.\n\n",
    "\nTime stays long enough for anyone who will use it.\n\n",
    "\nScience is the captain, and practice the soldiers.\n\n",
    "\nMarriage is like putting your hand into a bag of snakes in the hope of pulling out an eel.\n\n",
    "\nHe who loves practice without theory is like the sailor who boards ship without a rudder and compass and never knows where he may cast.\n\n",
    "\nWater is the driving force of all nature.\n\n",
    "\nHe who wishes to be rich in a day will be hanged in a year.\n\n",
    "\nWhy does the eye see a thing more clearly in dreams than the imagination when awake?\n\n",
    "\nA beautiful body perishes, but a work of art dies not.\n\n",
    "\nOur life is made by the death of others.\n\n",
    "\nIn rivers, the water that you touch is the last of what has passed and the first of that which comes; so with present time.\n\n",
    "\nYou can have no dominion greater or less than that over yourself.\n\n",
    "\nTime abides long enough for those who make use of it.\n\n",
    "\nWhere the spirit does not work with the hand, there is no art.\n\n",
    "\nExperience never errs; it is only your judgments that err by promising themselves effects such as are not caused by your experiments.\n\n",
    "\nThe function of muscle is to pull and not to push, except in the case of the genitals and the tongue.\n\n",
    "\nMedicine is the restoration of discordant elements; sickness is the discord of the elements infused into the living body.\n\n",
    "\nJust as courage imperils life, fear protects it.\n\n",
    "\nThe human bird shall take his first flight, filling the world with amazement, all writings with his fame, and bringing eternal glory to the nest whence he sprang.\n\n",
    "\nJust as food eaten without appetite is a tedious nourishment, so does study without zeal damage the memory by not assimilating what it absorbs.\n\n",
    "\nNecessity is the mistress and guide of nature. Necessity is the theme and inventress of nature, her curb and her eternal law.\n\n",
    "\nIntellectual passion drives out sensuality.\n\n",
    "\nMen of lofty genius when they are doing the least work are most active.\n\n",
    "\nAll knowledge which ends in words will die as quickly as it came to life, with the exception of the written word: which is its mechanical part.\n\n",
    "\nThe greatest deception men suffer is from their own opinions.\n\n",
    "\nI love those who can smile in trouble, who can gather strength from distress, and grow brave by reflection. 'Tis the business of little minds to shrink, but they whose heart is firm, and whose conscience approves their conduct, will pursue their principles unto death.\n\n",
    "\nIron rusts from disuse; water loses its purity from stagnation... even so does inaction sap the vigor of the mind.\n\n",
    "\nArt is never finished, only abandoned.\n\n",
    "\nPoor is the pupil who does not surpass his master.\n\n",
    "\nThere are three classes of people: those who see, those who see when they are shown, those who do not see.\n\n",
    "\nWhile I thought that I was learning how to live, I have been learning how to die.\n\n",
    "\nThe noblest pleasure is the joy of understanding.\n\n",
    "\nAll our knowledge has its origins in our perceptions.\n\n",
    "\nWhere there is shouting, there is no true knowledge.\n\n",
    "\nThe smallest feline is a masterpiece.\n\n",
    "\nMen of lofty genius sometimes accomplish the most when they work least, for their minds are occupied with their ideas and the perfection of their conceptions, to which they afterwards give form.\n\n",
    "\nWho sows virtue reaps honor.\n\n",
    "\nI have offended God and mankind because my work didn't reach the quality it should have.\n\n",
    "\nHe who is fixed to a star does not change his mind.\n\n",
    "\nBlinding ignorance does mislead us. O! Wretched mortals, open your eyes!\n\n",
    "\nIt's easier to resist at the beginning than at the end.\n\n",
    "\nHuman subtlety will never devise an invention more beautiful, more simple or more direct than does nature because in her inventions nothing is lacking, and nothing is superfluous.\n\n",
    "\nKnowledge of the past and of the places of the earth is the ornament and food of the mind of man.\n\n",
    "\nPainting is concerned with all the 10 attributes of sight; which are: Darkness, Light, Solidity and Colour, Form and Position, Distance and Propinquity, Motion and Rest.\n\n",
    "\nEvery action needs to be prompted by a motive.\n\n",
    "\nThe truth of things is the chief nutriment of superior intellects.\n\n",
    "\nLife well spent is long.\n\n",
    "\nThe natural desire of good men is knowledge.\n\n",
    "\nI have always felt it is my destiny to build a machine that would allow man to fly.\n\n",
    "\nYou do ill if you praise, but worse if you censure, what you do not understand.\n\n",
    "\nThe senses are of the earth, the reason stands apart from them in contemplation.\n\n",
    "\nI have wasted my hours.\n\n",
    "\nNature never breaks her own laws.\n\n"
]

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
def create_quote_image(quote, image_size=(IMAGE_WIDTH, IMAGE_HEIGHT), output_folder="quotes_images"):
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
        font = ImageFont.load_default()  # Fallback to default font if custom font not available
    
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
            y_text += line_spacing * 1.75
        else:
            y_text += line_spacing

    middle = image_size[0] // 2
    draw.text((middle, image_size[1] * 0.8), "Leonardo Da Vinci", font=font_author, fill=(255,255,255))
    
    # Save the image
    output_path = f"{output_folder}/quote_{quotes.index(quote)+1}.png"
    img.save(output_path)
    print(f"Saved: {output_path}")

# Create images for all quotes
import os
if not os.path.exists("quotes_images"):
    os.makedirs("quotes_images")

for quote in quotes:
    create_quote_image(quote)
