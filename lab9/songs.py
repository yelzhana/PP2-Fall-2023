import pygame
import os
import random

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

white = (255, 255, 255)
black = (0, 0, 0)

music_dir = r"C:\Users\ACER\pp1\pp2\lab9\musics"
songs = os.listdir(music_dir)
current_song_index = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_music()
            elif event.key == pygame.K_s:  # Stop
                stop_music()
            elif event.key == pygame.K_n:  # Next
                next_song()
            elif event.key == pygame.K_b:  # Previous
                prev_song()

    screen.fill(white)
    text = font.render("Press P to Play, S to Stop, N for Next, B for Previous", True, black)
    screen.blit(text, (20, 150))

    pygame.display.flip()

pygame.quit()
