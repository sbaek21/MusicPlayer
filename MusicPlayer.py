import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time 
import math


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title("Music Player")
root.geometry("400x480")

pygame.mixer.init()

list_of_songs = ['music/City.wav']
list_of_covers = ['img/city.jpg']
n = 0


def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name[6:-3]
    song_name_label = tkinter.Label(text= stripped_string,bg="#222222", fg="white")
    song_name_label.place(relx=0.4,rely=0.6)



def progress():
    a = pygame.mixer.Sound(f"{list_of_songs[n]}")
    song_len = a.get_length()*3
    for i in range(0,math.ceil(song_len)):
        time.sleep(0.3)
        progressbar.set(pygame.mixer.music.get_pos()/100000)

def threading():
    t1 = Thread(target=progress)
    t1.start()

def play_music():
    threading()
    global n
    current_song = n
    if n > 2:
        n=0
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)
    get_album_cover(song_name, n)
    #print("PLAY")
    n+=1
def pause_music():
    pygame.mixer.music.pause()
def unpause_music():
    pygame.mixer.music.unpause()

def rewind_music():
    pygame.mixer.music.rewind()
def skip_forward():
    play_music()
def skip_backward():
    global n
    n -= 2
    play_music()
def volume(value):
    #print(value)
    pygame.mixer.music.set_volume(value)




#Buttons
play_button = customtkinter.CTkButton(master=root, text="⏹️", command = play_music, width =1)
play_button.place(relx=0.4,rely=0.7,anchor=tkinter.CENTER)

pause_button = customtkinter.CTkButton(master=root, text="⏸️", command = pause_music, width = 1)
pause_button.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

unpause_button = customtkinter.CTkButton(master=root, text="▶️", command = unpause_music, width = 1)
unpause_button.place(relx=0.6,rely=0.7,anchor=tkinter.CENTER)

rewind_button = customtkinter.CTkButton(master=root, text="🔁", command = rewind_music, width =1)
rewind_button.place(relx=0.3,rely=0.7,anchor=tkinter.CENTER)


skip_f = customtkinter.CTkButton(master=root, text="⏭️", command = skip_forward, width=2)
skip_f.place(relx=0.8,rely=0.7,anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text="⏮️", command = skip_backward, width=2)
skip_b.place(relx=0.2,rely=0.7,anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210)
slider.place(relx=0.5,rely=0.78,anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color="#9df593", width=250)
progressbar.place(relx=0.5,rely=0.85,anchor=tkinter.CENTER)



root.mainloop()