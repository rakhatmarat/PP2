import pygame
import os

pygame.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Music Player")

def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song(current_index):
    current_index = (current_index + 1) % len(songs)
    play_music(songs[current_index])
    return current_index

def prev_song(current_index):
    current_index = (current_index - 1) % len(songs)
    play_music(songs[current_index])
    return current_index

songs = ["s2.wav", "s1.mp3"]

current_song_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(songs[current_song_index])
            elif event.key == pygame.K_RIGHT:
                current_song_index = next_song(current_song_index)
            elif event.key == pygame.K_LEFT:
                current_song_index = prev_song(current_song_index)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 100:
                    current_song_index = next_song(current_song_index)

    pygame.display.update()
pygame.quit()
