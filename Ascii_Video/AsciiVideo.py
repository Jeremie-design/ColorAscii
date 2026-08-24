import cv2
import pygame
import sys


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FONT_SIZE = 12
BACKGROUND_COLOR = (20, 20, 20)

CHARS = "@%#*+=-:. "

video_path = input("Enter the path to your video file: ").strip()
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Could not open file")
    sys.exit()


fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30
clock = pygame.time.Clock()



pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("ASCII Video")


font = pygame.font.SysFont( "Menlo", FONT_SIZE)
char_width = font.size("@")[0]
char_height = font.get_height()

columns = WINDOW_WIDTH // char_width
rows = WINDOW_HEIGHT // char_height


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    success, frame = cap.read()
    if not success:
        break

    small_frame = cv2.resize(frame,(columns, rows))
    screen.fill(BACKGROUND_COLOR)

    for y in range(rows):
        for x in range(columns):
            blue, green, red = small_frame[y, x]
            blue = int(blue)
            green = int(green)
            red = int(red)

            brightness = (red + green + blue) // 3
            char_index = (brightness * (len(CHARS) - 1)) // 255
            char = CHARS[char_index]

            text = font.render(char,True,(red, green, blue))
            screen.blit(text,(x * char_width, y * char_height))

    pygame.display.flip()
    clock.tick(fps)
cap.release()
pygame.quit()

