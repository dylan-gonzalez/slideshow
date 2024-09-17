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
FONT = "fonts/Crimson_Text/CrimsonText-Regular.ttf"
FONT_AUTHOR = "fonts/Crimson_Text/CrimsonText-Italic.ttf"
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
    "\nNature never breaks her own laws.\n\n",
    "\nJust as courage is the danger of life, so is fear its safeguard.\n\n",
    "\nThe divisions of Perspective are 3, as used in drawing; of these, the first includes the diminution in size of opaque objects; the second treats of the diminution and loss of outline in such opaque objects; the third, of the diminution and loss of colour at long distances.\n\n",
    "\nFor, verily, great love springs from great knowledge of the beloved object, and if you little know it, you will be able to love it only little or not at all.\n\n",
    "\nAnyone who conducts an argument by appealing to authority is not using his intelligence; he is just using his memory.\n\n",
    "\nIt is better to imitate ancient than modern work.\n\n",
    "\nAs every divided kingdom falls, so every mind divided between many studies confounds and saps itself.\n\n",
    "\nThe painter who draws merely by practice and by eye, without any reason, is like a mirror which copies every thing placed in front of it without being conscious of their existence.\n\n",
    "\nAlthough nature commences with reason and ends in experience it is necessary for us to do the opposite, that is to commence with experience and from this to proceed to investigate the reason.\n\n",
    "\nEach man is always in the middle of the surface of the earth and under the zenith of his own hemisphere, and over the centre of the earth.\n\n",
    "\nThere is no object so large but that at a great distance from the eye it does not appear smaller than a smaller object near.\n\n",
    "\nWeight, force and casual impulse, together with resistance, are the four external powers in which all the visible actions of mortals have their being and their end.\n\n",
    "\nGood men by nature, wish to know. I know that many will call this useless work... men who desire nothing but material riches and are absolutely devoid of that of wisdom, which is the food and only true riches of the mind.\n\n",
    "\nMany are they who have a taste and love for drawing, but no talent; and this will be discernible in boys who are not diligent and never finish their drawings with shading.\n\n",
    "\nOur body is dependant on Heaven and Heaven on the Spirit.\n\n",
    "\nIn order to arrive at knowledge of the motions of birds in the air, it is first necessary to acquire knowledge of the winds, which we will prove by the motions of water in itself, and this knowledge will be a step enabling us to arrive at the knowledge of beings that fly between the air and the wind.\n\n",
    "\nTo such an extent does nature delight and abound in variety that among her trees there is not one plant to be found which is exactly like another; and not only among the plants, but among the boughs, the leaves and the fruits, you will not find one which is exactly similar to another.\n\n",
    "\nPeople talk to people who perceive nothing, who have open eyes and see nothing; they shall talk to them and receive no answer; they shall adore those who have ears and hear nothing; they shall burn lamps for those who do not see.\n\n",
    "\nThe Medici created and destroyed me.\n\n",
    "\nI have found that, in the composition of the human body as compared with the bodies of animals, the organs of sense are duller and coarser. Thus, it is composed of less ingenious instruments, and of spaces less capacious for receiving the faculties of sense.\n\n",
    "\nCommon Sense is that which judges the things given to it by other senses.\n\n",
    "\nBeyond a doubt truth bears the same relation to falsehood as light to darkness.\n\n",
    "\nThere are four Powers: memory and intellect, desire and covetousness. The two first are mental and the others sensual. The three senses: sight, hearing and smell cannot well be prevented; touch and taste not at all.\n\n",
    "\nIt seems that it had been destined before that I should occupy myself so thoroughly with the vulture, for it comes to my mind as a very early memory, when I was still in the cradle, a vulture came down to me, he opened my mouth with his tail and struck me a few times with his tail against my lips.\n\n",
    "\nHow many emperors and how many princes have lived and died and no record of them remains, and they only sought to gain dominions and riches in order that their fame might be ever-lasting.\n\n",
    "\nThe poet ranks far below the painter in the representation of visible things, and far below the musician in that of invisible things.\n\n",
    "\nMan and animals are in reality vehicles and conduits of food, tombs of animals, hostels of Death, coverings that consume, deriving life by the death of others.\n\n",
    "\nThe length of a man's outspread arms is equal to his height.\n\n",
    "\nThe spirit desires to remain with its body, because, without the organic instruments of that body, it can neither act, nor feel anything.\n\n",
    "\nThe mind of the painter must resemble a mirror, which always takes the colour of the object it reflects and is completely occupied by the images of as many objects as are in front of it.\n\n",
    "\nThe painter who is familiar with the nature of the sinews, muscles, and tendons, will know very well, in giving movement to a limb, how many and which sinews cause it; and which muscle, by swelling, causes the contraction of that sinew; and which sinews, expanded into the thinnest cartilage, surround and support the said muscle.\n\n",
    "\nExperience does not err. Only your judgments err by expecting from her what is not in her power.\n\n"
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
