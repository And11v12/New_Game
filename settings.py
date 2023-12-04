SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def draw_text(text, shrift, color_text, posX, posY, screen):
    text_render = shrift.render(str(text), True, color_text)
    screen.blit(text_render, (posX, posY))