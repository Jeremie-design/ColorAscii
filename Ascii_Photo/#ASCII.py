from PIL import Image, ImageDraw, ImageFont

CHARS = "$@B%8&WM#*oahkbUYXzcvunxrjft?-_+~<>i!lI;:,\"^`'. "
CHAR_ARRAY = list(CHARS)
CHAR_LENGTH = len(CHAR_ARRAY)
SCALE_FACTOR = 0.4
CHAR_WIDTH = 8
CHAR_HEIGHT = 18
CHAR_ASPECT_RATIO = CHAR_WIDTH / CHAR_HEIGHT

def get_char(brightness):
    index = int(brightness * CHAR_LENGTH / 256)
    return CHAR_ARRAY[index]

while True:
    try:
        file_name = input("What is the file? (e.g., nemo.webp): ").strip()
        image = Image.open(file_name).convert("RGBA")
        break
    except FileNotFoundError:
        print("File not found. Try again.")

font = ImageFont.truetype("arial.ttf", 20)
width, height = image.size
print("Original size:", width, height)
new_width = int(SCALE_FACTOR * width)
new_height = int(SCALE_FACTOR * height * CHAR_ASPECT_RATIO)
image = image.resize((new_width, new_height))
width, height = image.size
print("ASCII size:", width, height)

pixels = image.load()
output_image = Image.new("RGBA", (CHAR_WIDTH * width, CHAR_HEIGHT * height), color=(0, 0, 0, 255))
draw = ImageDraw.Draw(output_image)

with open("output.txt", "w") as text_file:
    for y in range(height):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            brightness = int((red + green + blue) / 3)
            character = get_char(brightness)
            text_file.write(character)
            draw.text((x * CHAR_WIDTH, y * CHAR_HEIGHT), character, font=font, fill=(red, green, blue))
        text_file.write("\n")

output_image.save("output.png")
print("Converted")
