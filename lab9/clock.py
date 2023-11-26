import pygame
import sys
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock Simulation")

hour_arrow = pygame.image.load("left-hand.png")
minute_arrow = pygame.image.load("right-hand.png")
clock_image = pygame.image.load("mickeyclock.jpeg")

clock_image = pygame.transform.scale(clock_image, (300, 300))
minute_arrow = pygame.transform.scale(minute_arrow, (300, 300))
hour_arrow = pygame.transform.scale(hour_arrow, (300, 300))

def draw_clock():
    screen.blit(clock_image, (CENTER_X - clock_image.get_width() // 2, CENTER_Y - clock_image.get_height() // 2))

def draw_arrow(image, angle, length):
    rotated_arrow = pygame.transform.rotate(image, -angle)
    rotated_arrow_rect = rotated_arrow.get_rect(center=(CENTER_X, CENTER_Y))
    screen.blit(rotated_arrow, rotated_arrow_rect)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        current_time = datetime.now().time()
        hours = current_time.hour
        minutes = current_time.minute

        hour_angle = (hours % 12 + minutes / 60) * 30
        minute_angle = minutes * 6

        draw_clock()
        draw_arrow(hour_arrow, hour_angle, 50)
        draw_arrow(minute_arrow, minute_angle, 100)

        pygame.display.flip()

        pygame.time.Clock().tick(1)

if __name__ == "__main__":
    main()
