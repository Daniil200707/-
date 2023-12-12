import pygame
from button import Button
# from level import Level

# ------------ Початкові налаштування ------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

waiting_time = 0

BG = [pygame.image.load("resource/Pictures/level 1.0.png"), pygame.image.load("resource/Pictures/level 1.1.png"),
      pygame.image.load("resource/Pictures/level 1.2.png"), pygame.image.load("resource/Pictures/level 1.3.png"),
      pygame.image.load("resource/Pictures/level 1.4.png")]
BG_ANIMATE = [
    pygame.image.load("resource/Pictures/level 1.0.0.png"),
    pygame.image.load("resource/Pictures/level 1.0.1.png"),
    pygame.image.load("resource/Pictures/level 1.0.2.png"),
    pygame.image.load("resource/Pictures/level 1.0.3.png"),
    pygame.image.load("resource/Pictures/level 1.0.4.png"),
    pygame.image.load("resource/Pictures/level 1.0.5.png"),
    pygame.image.load("resource/Pictures/level 1.0.6.png"),
    pygame.image.load("resource/Pictures/level 1.0.7.png"),
    pygame.image.load("resource/Pictures/level 1.0.8.png"),
    pygame.image.load("resource/Pictures/level 1.0.9.png"),
    pygame.image.load("resource/Pictures/level 1.0.png")
]
BG_ANIMATE2 = [
    pygame.image.load("resource/Pictures/level 1.4.png"),
    pygame.image.load("resource/Pictures/level 1.4.0.png"),
    pygame.image.load("resource/Pictures/level 1.4.1.png"),
    pygame.image.load("resource/Pictures/level 1.4.2.png"),
    pygame.image.load("resource/Pictures/level 1.4.3.png"),
    pygame.image.load("resource/Pictures/level 1.4.4.png"),
    pygame.image.load("resource/Pictures/level 1.4.5.png"),
    pygame.image.load("resource/Pictures/level 1.4.6.png"),
    pygame.image.load("resource/Pictures/level 1.4.7.png"),
    pygame.image.load("resource/Pictures/level 1.4.8.png"),
    pygame.image.load("resource/Pictures/level 1.4.9.png")
]

pygame.init()
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

cursor_image = pygame.image.load("resource/Pictures/Game Cursor.png")

animation_count = 0

def animate_a_background(animation=True, count=1):
    global animation_count

    if count == 1:

        if animation_count >= 60:
            animation = False

        if animation:
            screen.blit(BG_ANIMATE[animation_count // 6], (0, 0))
            animation_count += 1
    if count == 2:

        if animation_count >= 60:
            animation_count = 0
            animation = False

        if animation:
            screen.blit(BG_ANIMATE2[animation_count // 6], (0, 0))
            animation_count += 1

x = 0
x2 = 1280
x3 = 1280
x4 = 1280
x5 = 1280
full_screen = False
main_click = pygame.mixer.Sound("resource/Music/Click.mp3")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font('resource/Fonts/font.ttf', size)

def enable_screensaver(level):
    if level == 1:
        global running
        global waiting_time
        global screen
        global full_screen
        global x
        global x2
        global x3
        global x4
        global x5
        pygame.display.set_caption("Screensaver")

        melody_path = "resource/Music/Den`s monologue.mp3"
        pygame.mixer.music.load(melody_path)

        # Настройка зацикливания мелодии
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play(loops=0)

        screen.fill("black")
        while running:
            if x2 > 0:
                screen.blit(BG[0], (x, 0))
            elif x3 > 0:
                screen.blit(BG[1], (x2, 0))
            elif x4 > 0:
                screen.blit(BG[2], (x3, 0))
            elif x5 > 0:
                screen.blit(BG[3], (x4, 0))
            else:
                screen.blit(BG[4], (x5, 0))

            screensaver_mouse_pos = pygame.mouse.get_pos()

            screensaver_button = Button(image=pygame.image.load("resource/Pictures/Skip Rect.png"), pos=(1180, 620),
                                        a_text_input="Пропустити", a_font=get_font(5), base_color="#d7fcd4",
                                        hovering_color="White")
            screensaver_button.change_color(screensaver_mouse_pos)
            screensaver_button.update(screen)

            # ------------ Обробка подій ------------
            screensaver_events = pygame.event.get()
            for screensaver_event in screensaver_events:
                if screensaver_event.type == pygame.QUIT:
                    running = False
                elif screensaver_event.type == pygame.MOUSEBUTTONDOWN:
                    if screensaver_button.check_for_input(screensaver_mouse_pos):
                        pygame.mixer.Sound.play(main_click)
                        running = False
                elif screensaver_event.type == pygame.KEYDOWN:
                    if screensaver_event.key == pygame.K_f:
                        # Переключение полноэкранного режима при нажатии клавиши 'f'
                        full_screen = not full_screen
                        if full_screen:
                            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

            if pygame.mouse.get_focused():
                language_pos = pygame.mouse.get_pos()
                pygame.transform.scale(cursor_image, (100, 100))
                cursor_image.get_rect()

                screen.blit(cursor_image, language_pos)

            waiting_time += 0.04
            print(waiting_time)
            if waiting_time <= 10:
                animate_a_background()
            if waiting_time >= 48:
                if x2 >= 0:
                    x -= 3
                    screen.blit(BG[1], (x2, 0))
                    x2 -= 3
            if waiting_time >= 69:
                if x3 >= 0:
                    x2 -= 3
                    screen.blit(BG[2], (x3, 0))
                    x3 -= 3
            if waiting_time >= 99:
                if x4 >= 0:
                    x3 -= 3
                    screen.blit(BG[3], (x4, 0))
                    x4 -= 3
            if waiting_time >= 121:
                if x5 >= 0:
                    x4 -= 3
                    screen.blit(BG[4], (x5, 0))
                    x5 -= 3
            if waiting_time >= 180:
                animate_a_background(count=2)
            if waiting_time >= 181:
                running = False

            clock.tick(60)
            pygame.display.update()

        pygame.quit()

def level_1():
    enable_screensaver(1)
    print("hello")
