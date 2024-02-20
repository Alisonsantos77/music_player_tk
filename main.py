# importando Tkinter
from tkinter import *
from tkinter import filedialog

# Importando pillow
from PIL import Image, ImageTk

#  Importando Pygame
import pygame
from pygame import mixer

# Importando OS
import os

# Cores ----------------------------------------------------------------
preto = '#000000'
azul_escuro = '#14213D'
amarelo = '#FCA311'
cinza = '#E5E5E5'
branco = '#FFFFFF'
rose_ebony = '#513b3c'

# Criando a janela --------------------------------

janela = Tk()
janela.title("Music Player")
janela.geometry('352x255')
janela.iconbitmap('window_icon.ico')
janela.configure(background=preto)
janela.resizable(width=FALSE, height=FALSE)

# Frames ----------------------------------------------------------------

frame_esquerda = Frame(janela, width=150, height=150, bg=branco)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela, width=350, height=150, bg=branco)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=404, height=100, bg=branco)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

# Configurando frame esquerdo ----------------------------------------------------------------
banner = Image.open('banner.png')
banner = banner.resize((130, 130))
banner = ImageTk.PhotoImage(banner)

# posicionando banner
l_logo = Label(frame_esquerda, height=130, image=banner, compound=LEFT,
               padx=0, anchor='nw', font=('ivy 16 bold'), bg=branco, fg=branco)
l_logo.place(x=18, y=15)

#  Criando funções --------------------------------


def play_music():
    rodando = listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()


def pause_music():
    mixer.music.pause()


def stop_music():
    rodando = 'Selecione uma musica'
    l_rodando['text'] = rodando
    mixer.music.stop()


def previous_music():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index - 1

    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0, END)

    exibir_lista()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando


def next_music():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index + 1

    if novo_index >= len(musicas):
        # Se for a última música
        mixer.music.rewind()
        listbox.select_clear(0, END)
        mixer.music.play()
        l_rodando['text'] = musicas[0]
        listbox.select_set(0)
    else:
        # Se não for a última música
        tocando = musicas[novo_index]
        mixer.music.load(tocando)
        listbox.select_clear(0, END)
        mixer.music.play()
        l_rodando['text'] = tocando
        listbox.select_set(novo_index)


def new_playlist():
    mixer.music.stop()

    new_dir = filedialog.askdirectory()

    if new_dir:
        global musicas
        # Atualiza o diretório de músicas com o diretório selecionado
        musicas = os.listdir(new_dir)
        # Limpa o Listbox
        listbox.delete(0, END)
        # Exibe a nova lista de músicas
        exibir_lista()

        tocando = musicas[0]
        mixer.music.load(os.path.join(new_dir, tocando))
        mixer.music.play()
        listbox.select_set(0)

def play_music():
    rodando = listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()


# Configurando frame direito --------------------------------


listbox = Listbox(frame_direita, selectmode=SINGLE, width=22,
                  height=10, font=('arial 9 bold'), bg=preto, fg=cinza)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

# Configurando frame baixo -------------------------
l_rodando = Label(frame_baixo, text='Selecione uma musica', width=50,
                  justify=LEFT, anchor='nw', font=('ivy 10'), bg=cinza, fg=azul_escuro)
l_rodando.place(x=0, y=1)

# Botões ----------------------------------------------------------------
img_anterior = Image.open('Skip_Back.png')
img_anterior = img_anterior.resize((30, 30))
img_anterior = ImageTk.PhotoImage(img_anterior)
b_anterior = Button(frame_baixo, command=previous_music, width=40, height=40, image=img_anterior, font=(
    'ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=azul_escuro, fg=amarelo)
b_anterior.place(x=38, y=35)

img_play = Image.open('Play.png')
img_play = img_play.resize((30, 30))
img_play = ImageTk.PhotoImage(img_play)
b_play = Button(frame_baixo, width=40, height=40, command=play_music, image=img_play, font=(
    'ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=azul_escuro, fg=amarelo)
b_play.place(x=84, y=35)

img_proxima = Image.open('Skip_Fwd.png')
img_proxima = img_proxima.resize((30, 30))
img_proxima = ImageTk.PhotoImage(img_proxima)
b_proxima = Button(frame_baixo, command=next_music, width=40, height=40, image=img_proxima, font=(
    'ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=azul_escuro, fg=amarelo)
b_proxima.place(x=130, y=35)

img_Pause = Image.open('Pause.png')
img_Pause = img_Pause.resize((30, 30))
img_Pause = ImageTk.PhotoImage(img_Pause)
b_Pause = Button(frame_baixo, command=pause_music, width=40, height=40, image=img_Pause, font=(
    'ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=azul_escuro, fg=amarelo)
b_Pause.place(x=176, y=35)

img_muted = Image.open('stop.png')
img_muted = img_muted.resize((30, 30))
img_muted = ImageTk.PhotoImage(img_muted)
b_muted = Button(frame_baixo, command=stop_music, width=40, height=40, image=img_muted, font=(
    'ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=azul_escuro, fg=amarelo)
b_muted.place(x=222, y=35)

img_playslist = Image.open('Library.png')
img_playslist = img_playslist.resize((30, 30))
img_playslist = ImageTk.PhotoImage(img_playslist)
b_playslist = Button(frame_baixo, command=new_playlist, width=40, height=40, image=img_playslist, font=(
    'ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=azul_escuro, fg=amarelo)
b_playslist.place(x=268, y=35)

os.chdir(r'C:\Users\aliso\Music\mscgol')
musicas = os.listdir()


def exibir_lista():
    listbox.delete(0, END)
    for i in musicas:
        listbox.insert(END, i)


exibir_lista()


# inicializando o mixer
mixer.init()

janela.mainloop()
