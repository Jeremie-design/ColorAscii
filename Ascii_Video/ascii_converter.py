from PIL import Image

CHAR_RAMP = "@%#*+=-:. "
CHAR_ASPECT_RATIO = 1.0


def image_to_ascii_colored(
    image: Image.Image, width_chars: int, height_chars: int
) -> list[list[tuple[str, tuple[int, int, int, int]]]]:
    
    new_width = max(1, width_chars)
    new_height = max(1, int(height_chars * CHAR_ASPECT_RATIO))

    resized = image.resize((new_width, new_height)).convert("RGBA")
    pixels = list(resized.getdata())

    ascii_frame = []
    for row_index in range(new_height):
        row = pixels[row_index * new_width : (row_index + 1) * new_width]
        row_chars = []
        for r, g, b, a in row:
            brightness = (r + g + b) / 3
            char_index = int(brightness / 255 * (len(CHAR_RAMP) - 1))
            row_chars.append((CHAR_RAMP[char_index], (r, g, b, a)))
        ascii_frame.append(row_chars)

    return ascii_frame