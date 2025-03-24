import pygame
import sys
 
# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (0, 200, 0)

# Screen Setup
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Temperature Converter Game")
font = pygame.font.SysFont(None, 36)

# Variables
input_text = ""
result_text = ""
conversion_type = "Celsius to Fahrenheit"

def convert_temperature(temp, conv_type):
    try:
        temp = float(temp)
        if conv_type == "Celsius to Fahrenheit":
            return f"{(temp * 9/5 + 32):.2f} °F"
        else:
            return f"{((temp - 32) * 5/9):.2f} °C"
    except ValueError:
        return "Invalid Input!"

def draw_text(text, x, y, color=BLACK):
    screen.blit(font.render(text, True, color), (x, y))

# Game Loop
while True:
    screen.fill(WHITE)
    draw_text("Temperature Converter Game", 100, 20, BLUE)
    draw_text("Enter Temperature:", 50, 80)
    draw_text(f"{input_text}", 280, 80)
    draw_text(f"Conversion: {conversion_type}", 50, 130, GREEN)
    draw_text("Press SPACE to Switch | ENTER to Convert", 50, 170)
    draw_text("Result:", 50, 220)
    draw_text(result_text, 150, 220)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                result_text = convert_temperature(input_text, conversion_type)
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_SPACE:
                conversion_type = "Fahrenheit to Celsius" if conversion_type == "Celsius to Fahrenheit" else "Celsius to Fahrenheit"
            elif event.unicode.isdigit() or event.unicode in "-.":
                input_text += event.unicode

    pygame.display.flip()
