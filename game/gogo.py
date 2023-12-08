import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
NUM_ROWS = 4
NUM_STUDENTS_PER_ROW = 6
STUDENT_WIDTH, STUDENT_HEIGHT = 64, 64
STUDENT_GAP = 64
TEACHER_WIDTH, TEACHER_HEIGHT = 60, 60
ENTER_KEY = pygame.K_RETURN
TEACHER_SPEED = 1.4
CHEATER_TIME_LIMIT = 10000 

LEVELS_CONFIG = [
    {"cheaters": (2, 6), "need_help": (2, 6), "time_limit": 30},
    {"cheaters": (6, 10), "need_help": (2, 7), "time_limit": 25},
    {"cheaters": (10, 15), "need_help": (2, 5), "time_limit": 20}
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cheating Student Game")

background_image = pygame.image.load("background.jpeg").convert_alpha()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
student_image = pygame.image.load("student.png").convert_alpha()
cheating_student_image = pygame.image.load("cheating_student.png").convert_alpha()
teacher_image = pygame.image.load("teacher.png").convert_alpha()
student_needs_help_image = pygame.image.load("student_needs_help.png").convert_alpha()
student_needs_help_image = pygame.transform.scale(student_needs_help_image, (STUDENT_WIDTH // 2 + 30, STUDENT_HEIGHT // 2 ))
success_image = pygame.image.load("success.png").convert_alpha()
loss_image = pygame.image.load("loss.png").convert_alpha()
menu_bg_image = pygame.image.load("menubg.jpg").convert_alpha()
menu_bg_image = pygame.transform.scale(menu_bg_image, (WIDTH, HEIGHT))
play_button_image = pygame.image.load("play.jpg").convert_alpha()
play_button_rect = play_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
quit_button_image = pygame.image.load("quit.jpg").convert_alpha()
quit_button_rect = quit_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

current_level = 0
game_over = False
success = False
game_start_time = 0
cheater_spotted_times = {}

caught_cheaters_count = 0
helped_students_count = 0
start_time = 0

font_path = "pixel.otf"
pygame.font.init()
font = pygame.font.Font(font_path, 16)

def setup_level(level_index):
    global classroom, students_needing_help, cheating_students, cheater_spotted_times, game_start_time, start_time
    classroom = ["Student"] * (NUM_ROWS * NUM_STUDENTS_PER_ROW)
    cheaters_range = LEVELS_CONFIG[level_index]["cheaters"]
    need_help_range = LEVELS_CONFIG[level_index]["need_help"]
    cheating_students = random.sample(range(NUM_ROWS * NUM_STUDENTS_PER_ROW), random.randint(*cheaters_range))
    students_needing_help = random.sample(range(NUM_ROWS * NUM_STUDENTS_PER_ROW), random.randint(*need_help_range))
    cheater_spotted_times = {student: pygame.time.get_ticks() for student in cheating_students}
    game_start_time = pygame.time.get_ticks()
    start_time = time.time()

def display_classroom():
    screen.blit(background_image, (0, 0))
    for row in range(NUM_ROWS):
        for col in range(NUM_STUDENTS_PER_ROW):
            x = col * (STUDENT_WIDTH + STUDENT_GAP) + STUDENT_GAP
            y = row * (STUDENT_HEIGHT + STUDENT_GAP) + STUDENT_GAP
            student_index = row * NUM_STUDENTS_PER_ROW + col
            student_image_to_draw = cheating_student_image if student_index in cheating_students else student_image
            screen.blit(student_image_to_draw, (x, y))
            if student_index in students_needing_help:
                help_image_x = x + STUDENT_WIDTH - student_needs_help_image.get_width() // 2 
                help_image_y = y
                screen.blit(student_needs_help_image, (help_image_x, help_image_y))
    screen.blit(teacher_image, (teacher_x, teacher_y))

def is_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def game_over_screen():
    screen.fill(WHITE)
    final_image = success_image if success else loss_image
    screen.blit(final_image, (0, 0))
    result_text = font.render(f"Cheaters caught: {caught_cheaters_count}, Students helped: {helped_students_count}", True, (0, 0, 0))
    screen.blit(result_text, (10, HEIGHT - 40))
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()
    sys.exit()

def wait_for_enter():
    enter_pressed = False
    while not enter_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == ENTER_KEY:
                enter_pressed = True

def main_menu():
    font = pygame.font.Font(None, 36)
    play_text = font.render("       ", True, (255, 255, 255))
    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    quit_text = font.render("        ", True, (0, 0, 0))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    pixel_font = pygame.font.Font("pixel.otf", 18)

    names_text = "\n".join(
        ["Gizatova Elzhana", "Manatkyzy Zhanel", "Tolegenov Dias", "Seilkhan Ilyas", "Alimzhan Damir"])
    names_rendered = pixel_font.render(names_text, True, (255, 255, 255))

    names_rect = names_rendered.get_rect(bottomright=(WIDTH - 45, HEIGHT - 10))


    while True:
        screen.blit(menu_bg_image, (0, 0))
        screen.blit(play_text, play_rect.topleft)
        screen.blit(quit_text, quit_rect.topleft)
        screen.blit(names_rendered, names_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_rect.collidepoint(x, y):
                    return True
                elif quit_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

def display_counters_and_timer():
    current_time = time.time()
    elapsed_time = current_time - start_time
    timer_text = font.render(f"Time: {int(elapsed_time)}s", True, (0, 0, 0))
    cheaters_text = font.render(f"Cheaters caught: {caught_cheaters_count}", True, (0, 0, 0))
    helped_text = font.render(f"Students helped: {helped_students_count}", True, (0, 0, 0))
    level_text = font.render(f"Level: {current_level + 1}", True, (0, 0, 0))
    

    screen.blit(timer_text, (10, HEIGHT - 40))
    screen.blit(cheaters_text, (10, HEIGHT - 80))
    screen.blit(helped_text, (10, HEIGHT - 120))
    screen.blit(level_text, (10, HEIGHT - 160))

def main():
    global teacher_x, teacher_y, game_over, success, current_level, cheating_students, classroom, caught_cheaters_count, helped_students_count, start_time
    if not main_menu():
        pygame.quit()
        sys.exit()
    setup_level(current_level)
    teacher_x, teacher_y = WIDTH - TEACHER_WIDTH - 10, HEIGHT - TEACHER_HEIGHT - 10

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            teacher_x -= TEACHER_SPEED
        elif keys[pygame.K_RIGHT]:
            teacher_x += TEACHER_SPEED
        elif keys[pygame.K_UP]:
            teacher_y -= TEACHER_SPEED
        elif keys[pygame.K_DOWN]:
            teacher_y += TEACHER_SPEED

        teacher_x = max(0, min(teacher_x, WIDTH - TEACHER_WIDTH))
        teacher_y = max(0, min(teacher_y, HEIGHT - TEACHER_HEIGHT))

        teacher_rect = pygame.Rect(teacher_x, teacher_y, TEACHER_WIDTH, TEACHER_HEIGHT)
        for i, student_state in enumerate(classroom):
            student_x = (i % NUM_STUDENTS_PER_ROW) * (STUDENT_WIDTH + STUDENT_GAP) + STUDENT_GAP
            student_y = (i // NUM_STUDENTS_PER_ROW) * (STUDENT_HEIGHT + STUDENT_GAP) + STUDENT_GAP
            student_rect = pygame.Rect(student_x, student_y, STUDENT_WIDTH, STUDENT_HEIGHT)

            if is_collision(teacher_rect, student_rect):
                if i in cheating_students:
                    if cheater_spotted_times[i] == 0:
                        cheater_spotted_times[i] = pygame.time.get_ticks()
                    elif pygame.time.get_ticks() - cheater_spotted_times[i] > CHEATER_TIME_LIMIT:
                        game_over = True
                        success = False
                        break
                    else:
                        print(f"Teacher: Student {i + 1} is cheating! Press Enter to catch the cheater.")
                        wait_for_enter()
                        cheating_students.remove(i)
                        classroom[i] = "Student"
                        cheater_spotted_times[i] = 0
                        caught_cheaters_count += 1
                elif i in students_needing_help:
                    print(f"Teacher: Student {i + 1} needs help. Press Enter to assist the student.")
                    wait_for_enter()
                    students_needing_help.remove(i)
                    classroom[i] = "Student"
                    helped_students_count += 1

        display_classroom()
        display_counters_and_timer()
        pygame.display.update()

        if not cheating_students and not students_needing_help:
            if current_level < len(LEVELS_CONFIG) - 1:
                current_level += 1
                setup_level(current_level)
                print(f"Level up! Now starting level {current_level + 1}.")
            else:
                success = True
                game_over = True

        if pygame.time.get_ticks() - game_start_time >= LEVELS_CONFIG[current_level]["time_limit"] * 1000:
            print(f"Time's up for level {current_level + 1}!")
            game_over = True
            break

    game_over_screen()

if __name__ == "__main__":
    print("Welcome to the Cheating Student Game!")
    print("The teacher is coming to check the exams.")
    main()