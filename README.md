# ColorAscii

This project converts images and video frames into colored ASCII art.
Images can be converted into ASCII output, while videos are processed frame by frame and displayed in a Pygame window. 

## Demo

https://github.com/user-attachments/assets/6699a859-be0c-49eb-bb20-21ce4e69a861

## How It Works
Each image or video frame is reduced to a smaller grid. Each position in that grid represents a portion of the original image.
For every pixel the program calculates its brightness from its red, green, and blue values:

```text
brightness = (red + green + blue) / 3
```
That brightness value (0–255) maps onto a fixed set of characters ordered from darkest to lightest
so darker areas render as heavier characters. Each character is then drawn in the pixel's original color.

## Setup
Requires Python 3.10+.
```bash
git clone https://github.com/Jeremie-design/ColorAscii.git
cd ColorAscii
pip install -r requirements.txt
```

## Project Structure
```
Ascii_Photo/
  AsciiPhoto.py    # Image ASCII (.txt + .png)
Ascii_Video/
  AsciiVideo.py    # Video ASCII playback in a Pygame window
  JoJo's Bizarre Adventure.py # Downloaded Jojo Video for testing  
requirements.txt
```
