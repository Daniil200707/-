import pygame
from button import Button
# from level import Level
from map import Map
import levels

# ------------ Початкові налаштування ------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

waiting_time = 0

BG = pygame.image.load("resource/Pictures/background.jpg")
WAIT_BG = pygame.image.load("resource/Pictures/Wait Rect.png")

pygame.init()
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
full_screen = False

cursor_image = pygame.image.load("resource/Pictures/Game Cursor.png")

gear_animation = [
                  pygame.image.load("resource/Pictures/1.png"), pygame.image.load("resource/Pictures/2.png"),
                  pygame.image.load("resource/Pictures/3.png"), pygame.image.load("resource/Pictures/4.png"),
                  pygame.image.load("resource/Pictures/5.png"), pygame.image.load("resource/Pictures/6.png"),
                  pygame.image.load("resource/Pictures/7.png"), pygame.image.load("resource/Pictures/8.png"),
                  pygame.image.load("resource/Pictures/9.png"), pygame.image.load("resource/Pictures/10.png")
                  ]
# Инициализация звука
pygame.mixer.init()

# Загрузка мелодии
melody_path = "resource/Music/Main.mp3"
pygame.mixer.music.load(melody_path)

# Настройка зацикливания мелодии
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play(loops=-1)

main_click = pygame.mixer.Sound("resource/Music/Click.mp3")
gear_sound = pygame.mixer.Sound("resource/Music/Gear.mp3")

player = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
player1 = pygame.Vector2(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3)
font = pygame.font.SysFont('couriernew', 50)

animation_count = 1

def animate_a_gear(animation=True):
    global animation_count

    if animation_count >= 60:
        animation_count = 1

    if animation:
        screen.blit(gear_animation[animation_count // 6], (100, 260))
        if animation_count % 6 == 0:
            pygame.mixer.Sound.play(gear_sound)
        animation_count += 1

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font('resource/Fonts/font.ttf', size)

pygame.mouse.set_visible(False)

def enable_options():
    global running
    global full_screen
    global screen
    pygame.display.set_caption("Options")

    while running:
        screen.fill("black")
        screen.blit(BG, (0, 0))

        option_mouse_pos = pygame.mouse.get_pos()

        options_text = get_font(100).render("Параметри", True, "#ffffff")
        options_rect = options_text.get_rect(center=(640, 100))

        language_button = Button(image=pygame.image.load("resource/Pictures/Language Rect.png"), pos=(640, 250),
                                 a_text_input="Мова", a_font=get_font(75), base_color="#d7fcd4",
                                 hovering_color="White")
        language_back = Button(image=pygame.image.load("resource/Pictures/Back Rect.png"), pos=(640, 550),
                               a_text_input="Повернутись", a_font=get_font(75), base_color="#d7fcd4",
                               hovering_color="White")

        screen.blit(options_text, options_rect)

        language_button.change_color(option_mouse_pos)
        language_button.update(screen)
        language_back.change_color(option_mouse_pos)
        language_back.update(screen)

        # ------------ Обробка подій ------------
        option_events = pygame.event.get()
        for option_event in option_events:
            if option_event.type == pygame.QUIT:
                running = False
            elif option_event.type == pygame.MOUSEBUTTONDOWN:
                if language_button.check_for_input(option_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    enable_language()
                if language_back.check_for_input(option_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    main()
            elif option_event.type == pygame.KEYDOWN:
                if option_event.key == pygame.K_f:
                    # Переключение полноэкранного режима при нажатии клавиши 'f'
                    full_screen = not full_screen
                    if full_screen:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        if pygame.mouse.get_focused():
            options_pos = pygame.mouse.get_pos()
            pygame.transform.scale(cursor_image, (100, 100))
            cursor_image.get_rect()

            screen.blit(cursor_image, options_pos)

        pygame.display.update()

    pygame.quit()

def enable_language():
    global running
    global full_screen
    global screen
    pygame.display.set_caption("Language")

    screen.fill("red")

    while running:
        screen.blit(BG, (0, 0))

        language_mouse_pos = pygame.mouse.get_pos()

        language_text = get_font(100).render("Мова", True, "#ffffff")
        language_rect = language_text.get_rect(center=(640, 100))

        ukraine_button = Button(image=pygame.image.load("resource/Pictures/Ukraine Rect.png"), pos=(640, 250),
                                a_text_input="Український", a_font=get_font(75), base_color="#d7fcd4",
                                hovering_color="White")
        language_back = Button(image=pygame.image.load("resource/Pictures/Back Rect.png"), pos=(640, 550),
                               a_text_input="Повернутись", a_font=get_font(75), base_color="#d7fcd4",
                               hovering_color="White")

        screen.blit(language_text, language_rect)

        ukraine_button.change_color(language_mouse_pos)
        ukraine_button.update(screen)
        language_back.change_color(language_mouse_pos)
        language_back.update(screen)

        # ------------ Обробка подій ------------
        language_events = pygame.event.get()
        for language_event in language_events:
            if language_event.type == pygame.QUIT:
                running = False
            elif language_event.type == pygame.MOUSEBUTTONDOWN:
                if ukraine_button.check_for_input(language_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                elif language_back.check_for_input(language_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    enable_options()
            elif language_event.type == pygame.KEYDOWN:
                if language_event.key == pygame.K_f:
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

        pygame.display.update()

    pygame.quit()

def wait(level_number):
    global running
    global waiting_time
    global screen
    global full_screen
    pygame.display.set_caption("Wait")

    screen.fill("black")
    while running:
        screen.blit(WAIT_BG, (0, 0))

        play_mouse_pos = pygame.mouse.get_pos()

        play_back = Button(image=pygame.image.load("resource/Pictures/Back Rect.png"), pos=(640, 360),
                           a_text_input="Перший крок винахідника", a_font=get_font(27), base_color="#d7fcd4",
                           hovering_color="White")

        play_back.update(screen)

        animate_a_gear()

        # ------------ Обробка подій ------------
        play_events = pygame.event.get()
        for play_event in play_events:
            if play_event.type == pygame.QUIT:
                running=False
            elif play_event.type == pygame.KEYDOWN:
                if play_event.key == pygame.K_f:
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

        waiting_time += 0.06
        if waiting_time >= 10:
            if level_number == 1:
                levels.level_1()
                pass

        clock.tick(60)
        pygame.display.update()

    pygame.quit()


def play():
    # levels = Level()
    # current_level = levels.get_level()

    global running
    global full_screen
    global screen
    pygame.display.set_caption("Play")

    screen.fill("orange")

    while running:
        screen.blit(BG, (0, 0))

        play_mouse_pos = pygame.mouse.get_pos()

        play_text = get_font(25).render("Глава 1 - Перший Крок на Шляху Винаходів", True, "#ffffff")
        play_rect = play_text.get_rect(center=(640, 100))

        map1 = Map(640, 360, pygame.image.load("resource/Pictures/Map Rect.png"))
        level_1_button = Button(image=pygame.image.load("resource/Pictures/Enabled Level Rect.png"), pos=(500, 300),
                                a_text_input="1",
                                a_font=get_font(10), base_color="#000000", hovering_color="White")
        play_back = Button(image=pygame.image.load("resource/Pictures/Back Rect.png"), pos=(640, 600),
                           a_text_input="Повернутись", a_font=get_font(75), base_color="#d7fcd4",
                           hovering_color="White")

        screen.blit(play_text, play_rect)

        map1.update(screen)
        level_1_button.change_color(play_mouse_pos)
        level_1_button.update(screen)
        play_back.change_color(play_mouse_pos)
        play_back.update(screen)

        # ------------ Обробка подій ------------
        play_events = pygame.event.get()
        for play_event in play_events:
            if play_event.type == pygame.QUIT:
                running = False
            elif play_event.type == pygame.MOUSEBUTTONDOWN:
                if level_1_button.check_for_input(play_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    pygame.mixer.music.stop()
                    wait(1)
                elif play_back.check_for_input(play_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    main()
            elif play_event.type == pygame.KEYDOWN:
                if play_event.key == pygame.K_f:
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

        pygame.display.update()

    pygame.quit()

def main():
    global running
    global screen
    global full_screen

    pygame.display.set_caption("Menu")

    # --------------- Головний цикл гри --------------
    while running:
        screen.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Головне меню", True, "#ffffff")
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("resource/Pictures/Play Rect.png"), pos=(640, 250),
                             a_text_input="Грати",
                             a_font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("resource/Pictures/Options Rect.png"), pos=(640, 400),
                                a_text_input="Параметри",
                                a_font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("resource/Pictures/Quit Rect.png"), pos=(640, 550),
                             a_text_input="Вихід",
                             a_font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        # ------------ Обробка подій ------------
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            # ------------- Логіка гри --------------
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    running = False
                elif options_button.check_for_input(menu_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    enable_options()
                elif play_button.check_for_input(menu_mouse_pos):
                    pygame.mixer.Sound.play(main_click)
                    play()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # Переключение полноэкранного режима при нажатии клавиши 'f'
                    full_screen = not full_screen
                    if full_screen:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            elif event.type == pygame.constants.USEREVENT:
                # При завершении мелодии, начнем ее заново
                pygame.mixer.music.rewind()
        # ----------- Оновлення екрану ----------

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            pygame.transform.scale(cursor_image, (100, 100))
            cursor_image.get_rect()

            screen.blit(cursor_image, pos)

        pygame.display.update()

    # ------------- Вихід з гри ------------
    pygame.quit()

if __name__ == "__main__":
    main()
