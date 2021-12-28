import pygame
import numpy as np
import os
import tkinter
import tkinter.filedialog
import ast

np.set_printoptions(threshold=np.inf)

pygame.init()
pygame.font.init()

file_name = "PAINT"

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH + 500, HEIGHT))
pygame.display.set_caption(file_name)

DROPPER = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "dropper.png")), (40, 40))
SS_RECT = WIN.subsurface(pygame.Rect(0, 0, WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (127, 0, 255)
BROWN = (100, 70, 36)


def prompt_file_save(file_text):
    top = tkinter.Tk()
    top.withdraw()
    file = tkinter.filedialog.asksaveasfile()
    file.write(file_text)
    file.close()


def prompt_file_open():
    top = tkinter.Tk()
    top.withdraw()
    file_path = tkinter.filedialog.askopenfilename()
    file = open(file_path, "r")
    array_text = ""
    dict_text = ""
    for i in range(151):
        if i < 150:
            array_text += file.readline()
            array_text = array_text.replace("[", "")
            array_text = array_text.replace("]", "")
            array_text = array_text.replace("\n", "")
        else:
            dict_text += file.readline()
    array_text = array_text.replace(".", ",")
    x = array_text.split(", ")
    array_data = []
    temp = ""
    for i in x:
        for j in i:
            if j.isdecimal():
                temp += j
        array_data.append(int(temp))
        temp = ""
    actual_array = np.zeros((50, 50))
    index = 0
    for i in range(50):
        for j in range(50):
            actual_array[i][j] = array_data[index]
            index += 1
    dict_data = ast.literal_eval(dict_text)
    file.close()
    return actual_array, dict_data


def prompt_save_img():
    top = tkinter.Tk()
    top.withdraw()
    file_path = tkinter.filedialog.asksaveasfilename()
    return file_path


def draw_grid(r_active, g_active, b_active, r_text, g_text, b_text, selected_color, dropper_active):
    WIN.fill(WHITE)
    pygame.draw.line(WIN, BLACK, (0, 0), (0, HEIGHT), 1)
    pygame.draw.line(WIN, BLACK, (0, 0), (WIDTH, 0), 1)
    pygame.draw.line(WIN, BLACK, (WIDTH, 0), (WIDTH, HEIGHT), 1)
    pygame.draw.line(WIN, BLACK, (0, HEIGHT), (WIDTH, HEIGHT), 1)

    pygame.draw.rect(WIN, BLACK, (1000, 50, 75, 75))

    pygame.draw.rect(WIN, RED, (1075, 50, 75, 75))
    pygame.draw.rect(WIN, BLACK, (1075, 50, 75, 75), 1)

    pygame.draw.rect(WIN, GREEN, (1150, 50, 75, 75))
    pygame.draw.rect(WIN, BLACK, (1150, 50, 75, 75), 1)

    pygame.draw.rect(WIN, BLUE, (1225, 50, 75, 75))
    pygame.draw.rect(WIN, BLACK, (1225, 50, 75, 75), 1)

    pygame.draw.rect(WIN, ORANGE, (1000, 125, 75, 75))
    pygame.draw.rect(WIN, BLACK, (1000, 125, 75, 75), 1)

    pygame.draw.rect(WIN, YELLOW, (1075, 125, 75, 75))
    pygame.draw.rect(WIN, BLACK, (1075, 125, 75, 75), 1)

    pygame.draw.rect(WIN, PURPLE, (1150, 125, 75, 75))
    pygame.draw.rect(WIN, BLACK, (1150, 125, 75, 75), 1)

    pygame.draw.rect(WIN, BROWN, (1225, 125, 75, 75))
    pygame.draw.rect(WIN, BLACK, (1225, 125, 75, 75), 1)

    font = pygame.font.SysFont("Comic Sans", 30)

    R_text = font.render("R:", False, BLACK)
    G_text = font.render("G:", False, BLACK)
    B_text = font.render("B:", False, BLACK)

    WIN.blit(R_text, (920, 250))
    WIN.blit(G_text, (1070, 250))
    WIN.blit(B_text, (1220, 250))

    red_input_rect = pygame.Rect(950, 250, 100, 50)
    green_input_rect = pygame.Rect(1100, 250, 100, 50)
    blue_input_rect = pygame.Rect(1250, 250, 100, 50)

    if not r_active:
        pygame.draw.rect(WIN, BLACK, red_input_rect, 1)
    else:
        pygame.draw.rect(WIN, (142, 142, 142), red_input_rect)
        pygame.draw.rect(WIN, BLACK, red_input_rect, 1)
    if not g_active:
        pygame.draw.rect(WIN, BLACK, green_input_rect, 1)
    else:
        pygame.draw.rect(WIN, (142, 142, 142), green_input_rect)
        pygame.draw.rect(WIN, BLACK, green_input_rect, 1)
    if not b_active:
        pygame.draw.rect(WIN, BLACK, blue_input_rect, 1)
    else:
        pygame.draw.rect(WIN, (142, 142, 142), blue_input_rect)
        pygame.draw.rect(WIN, BLACK, blue_input_rect, 1)

    red_text = font.render(r_text, False, 30)
    WIN.blit(red_text, (955, 250))

    green_text = font.render(g_text, False, 30)
    WIN.blit(green_text, (1105, 250))

    blue_text = font.render(b_text, False, 30)
    WIN.blit(blue_text, (1255, 250))

    pygame.draw.rect(WIN, BLACK, (1100, 350, 100, 50), 1)
    ok_text = font.render("OK", False, 30)
    WIN.blit(ok_text, (1125, 350))

    pygame.draw.rect(WIN, BLACK, (1075, 550, 150, 50), 1)
    clear_text = font.render("CLEAR", False, 30)
    WIN.blit(clear_text, (1100, 550))

    pygame.draw.rect(WIN, selected_color, (1250, 450, 50, 50))
    pygame.draw.rect(WIN, BLACK, (1250, 450, 50, 50), 1)
    selected_color_text = font.render("SELECTED COLOR:", False, 30)
    WIN.blit(selected_color_text, (960, 450))

    pygame.draw.rect(WIN, BLACK, (950, 650, 150, 50), 1)
    open_text = font.render("OPEN", False, 30)
    WIN.blit(open_text, (985, 650))

    pygame.draw.rect(WIN, BLACK, (1200, 650, 150, 50), 1)
    save_text = font.render("SAVE", False, 30)
    WIN.blit(save_text, (1230, 650))

    pygame.draw.rect(WIN, BLACK, (1050, 750, 200, 50), 1)
    save_img_text = font.render("SAVE IMAGE", False, 30)
    WIN.blit(save_img_text, (1053, 750))

    if not dropper_active:
        pygame.draw.rect(WIN, BLACK, (1250, 350, 50, 50), 1)
    else:
        pygame.draw.rect(WIN, (142, 142, 142), (1250, 350, 50, 50))
        pygame.draw.rect(WIN, BLACK, (1250, 350, 50, 50), 1)
    WIN.blit(DROPPER, (1255, 355))


def update_grid(pixel_data, CUSTOM_COLOR_ID):
    for i in range(50):
        for j in range(50):
            if pixel_data[i][j] == 0:
                pygame.draw.rect(WIN, WHITE, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            if pixel_data[i][j] == 1:
                pygame.draw.rect(WIN, BLACK, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] == 2:
                pygame.draw.rect(WIN, RED, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] == 3:
                pygame.draw.rect(WIN, GREEN, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] == 4:
                pygame.draw.rect(WIN, BLUE, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] == 5:
                pygame.draw.rect(WIN, ORANGE, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] == 6:
                pygame.draw.rect(WIN, YELLOW, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] == 7:
                pygame.draw.rect(WIN, PURPLE, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] == 8:
                pygame.draw.rect(WIN, BROWN, (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))
            elif pixel_data[i][j] > 8:
                pygame.draw.rect(WIN, CUSTOM_COLOR_ID[pixel_data[i][j]],
                                 (WIDTH // 50 * j, HEIGHT // 50 * i, WIDTH // 50, HEIGHT // 50))


def main():
    run = True
    clock = pygame.time.Clock()
    pixel_data = np.zeros((50, 50))
    CURRENT_COLOR = 1
    r_active = False
    g_active = False
    b_active = False
    r_text = ""
    g_text = ""
    b_text = ""
    r_value = 0
    g_value = 0
    b_value = 0
    custom_id = 8
    selected_color = BLACK
    dropper_active = False
    CUSTOM_COLOR_ID = {}

    while run:
        clock.tick(120)
        draw_grid(r_active, g_active, b_active, r_text, g_text, b_text, selected_color, dropper_active)
        update_grid(pixel_data, CUSTOM_COLOR_ID)
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed() == (True, False, False) and x < WIDTH and not dropper_active:
                pixel_data[y // (HEIGHT // 50)][x // (WIDTH // 50)] = CURRENT_COLOR
            elif pygame.mouse.get_pressed() == (False, False, True) and x < WIDTH and not dropper_active:
                pixel_data[y // (HEIGHT // 50)][x // (WIDTH // 50)] = 0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x > WIDTH:
                if 1000 < x < 1075 and 50 < y < 125:
                    CURRENT_COLOR = 1
                    selected_color = BLACK
                elif 1075 < x < 1150 and 50 < y < 125:
                    CURRENT_COLOR = 2
                    selected_color = RED
                elif 1150 < x < 1225 and 50 < y < 125:
                    CURRENT_COLOR = 3
                    selected_color = GREEN
                elif 1225 < x < 1300 and 50 < y < 125:
                    CURRENT_COLOR = 4
                    selected_color = BLUE
                elif 1000 < x < 1075 and 125 < y < 200:
                    CURRENT_COLOR = 5
                    selected_color = ORANGE
                elif 1075 < x < 1150 and 125 < y < 200:
                    CURRENT_COLOR = 6
                    selected_color = YELLOW
                elif 1150 < x < 1225 and 125 < y < 200:
                    CURRENT_COLOR = 7
                    selected_color = PURPLE
                elif 1225 < x < 1300 and 125 < y < 200:
                    CURRENT_COLOR = 8
                    selected_color = BROWN
                elif 1075 < x < 1225 and 550 < y < 600:
                    for i in range(50):
                        for j in range(50):
                            pixel_data[i][j] = 0
                elif 1200 < x < 1350 and 650 < y < 700:
                    arr_text = str(pixel_data)
                    dict_text = str(CUSTOM_COLOR_ID)
                    prompt_file_save(arr_text + "\n" + dict_text)
                elif 950 < x < 1100 and 650 < y < 700:
                    pixel_data, CUSTOM_COLOR_ID = prompt_file_open()
                elif 1050 < x < 1250 and 750 < y < 800:
                    path = prompt_save_img()
                    screenshot = pygame.Surface((WIDTH, HEIGHT))
                    screenshot.blit(SS_RECT, (0, 0, WIDTH, HEIGHT))
                    pygame.image.save(screenshot, path + ".jpg")
                if 1250 < x < 1300 and 350 < y < 400:
                    dropper_active = True
                else:
                    dropper_active = False
                if 950 < x < 1050 and 250 < y < 300:
                    r_active = True
                else:
                    r_active = False
                if 1100 < x < 1200 and 250 < y < 300:
                    g_active = True
                else:
                    g_active = False
                if 1250 < x < 1350 and 250 < y < 300:
                    b_active = True
                else:
                    b_active = False
                if 1100 < x < 1200 and 350 < y < 400:
                    custom_id += 1
                    CURRENT_COLOR = custom_id
                    if r_text.isdecimal():
                        r_value = int(r_text)
                    if g_text.isdecimal():
                        g_value = int(g_text)
                    if b_text.isdecimal():
                        b_value = int(b_text)
                    CUSTOM_COLOR_ID[custom_id] = (r_value, g_value, b_value)
                    selected_color = (r_value, g_value, b_value)
                    r_text = ""
                    g_text = ""
                    b_text = ""
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x < WIDTH:
                if dropper_active:
                    CURRENT_COLOR = pixel_data[y // (HEIGHT // 50)][x // (WIDTH // 50)]
                    if CURRENT_COLOR == 0:
                        selected_color = WHITE
                    if CURRENT_COLOR == 1:
                        selected_color = BLACK
                    if CURRENT_COLOR == 2:
                        selected_color = RED
                    if CURRENT_COLOR == 3:
                        selected_color = GREEN
                    if CURRENT_COLOR == 4:
                        selected_color = BLUE
                    if CURRENT_COLOR == 5:
                        selected_color = ORANGE
                    if CURRENT_COLOR == 6:
                        selected_color = YELLOW
                    if CURRENT_COLOR == 7:
                        selected_color = PURPLE
                    if CURRENT_COLOR == 8:
                        selected_color = BROWN
                    if CURRENT_COLOR > 8:
                        selected_color = CUSTOM_COLOR_ID[CURRENT_COLOR]
                    dropper_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if r_active:
                        r_text = r_text[:-1]
                    elif g_active:
                        g_text = g_text[:-1]
                    elif b_active:
                        b_text = b_text[:-1]
                else:
                    if r_active:
                        r_text += event.unicode
                    elif g_active:
                        g_text += event.unicode
                    elif b_active:
                        b_text += event.unicode
        pygame.display.update()


main()
