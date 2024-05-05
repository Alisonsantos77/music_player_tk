# importando Tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
# Importando pillow
from PIL import Image, ImageTk

#  Importando Pygame
import pygame
from pygame import mixer

# Importando OS
import os

# Cores ----------------------------------------------------------------
preto = '#000000'
Royal_blue = '#00296B'
amarelo = '#ffd500'
Polynesian_blue = '#00509D'
Marian_blue = '#003F88'

# Criando a janela --------------------------------

janela = Tk()
janela.title("Music Player")
janela.geometry('450x255')
janela.iconbitmap('LogoICO.ico')
janela.configure(background=preto)
janela.resizable(width=FALSE, height=FALSE)

# Frames ----------------------------------------------------------------

frame_esquerda = Frame(janela, width=200, height=150, bg=Polynesian_blue)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela, width=500, height=150, bg=Polynesian_blue)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=420, height=100, bg=Polynesian_blue)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

# Configurando frame esquerdo ----------------------------------------------------------------
banner = Image.open('logo.png')
banner = banner.resize((150, 150))
banner = ImageTk.PhotoImage(banner)

# posicionando banner
l_logo = Label(frame_esquerda, height=300, image=banner, compound=LEFT,
               padx=0, anchor='nw', font=('ivy 16 bold'), bg=Polynesian_blue, fg=Polynesian_blue)
l_logo.place(x=20, y=10)

#  Criando funções --------------------------------

def play_music():
    # variavel recebe o arquivo ativo
    rodando = listbox.get(ACTIVE)
    listbox.select_set(0)
    # Altera e exibe em texto o arquivo ativo 
    l_rodando['text'] = rodando
    try:
        # Carrega o arquivo ativo
        mixer.music.load(rodando)
        # reproduz o arquivo ativo
        mixer.music.play()
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de música não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar a música: {e}")
        
        
def pause_music():
    mixer.music.pause()
    b_unpause.config(bg='blue') 


def stop_music():
    # após parar, altera o texto para selecione uma musica
    rodando = 'Selecione uma musica'
    l_rodando['text'] = rodando
    mixer.music.stop()

def unpause_music():
    mixer.music.unpause()
    b_unpause.config(bg=None) 

def previous_music():
    try:
        tocando = l_rodando['text']
        index = musicas.index(tocando)
        novo_index = index - 1

        if novo_index < 0:
            novo_index = len(musicas) - 1  # Volta ao último item se chegar ao início
        else:
            tocando = musicas[novo_index]
            mixer.music.load(tocando)
            listbox.select_clear(0,END)
            mixer.music.play()
            l_rodando['text'] = tocando
            listbox.select_set(novo_index)
    except ValueError:
        messagebox.showerror("Erro", "Música não encontrada na lista.")
        
def repeat_playlist():
    mixer.music.stop()
    # Abre cada música como um objeto de arquivo e enfileira para reprodução
    for musica in musicas:
        mixer.music.queue(open(musica, 'rb'))
    # Inicia a reprodução da primeira música na fila
    mixer.music.play()
    
def next_music():
    try:
        tocando = l_rodando['text']
        index = musicas.index(tocando)
        novo_index = index + 1

        if novo_index >= len(musicas):
            repeat_playlist()          
        else:
            # Se não for a última música
            tocando = musicas[novo_index]
            mixer.music.load(tocando)
            listbox.select_clear(0, END)
            mixer.music.play()
            l_rodando['text'] = tocando
            listbox.select_set(novo_index)
    except ValueError:
        print("Música não encontrada na lista.")

def new_playlist():
    global musicas
    mixer.music.stop()
    new_dir = filedialog.askdirectory()
    if new_dir:
        os.chdir(new_dir)
        musicas = os.listdir()
        listbox.delete(0, END)
        exibir_lista()
def repeat_music():
    mixer.music.stop()
    mixer.music.rewind()
    mixer.music.play()
    

    
# Configurando frame direito --------------------------------


listbox = Listbox(frame_direita, selectmode=SINGLE, width=33,
                height=10, font=('arial 9 bold'), bg=preto, fg=Polynesian_blue)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita, troughcolor=Royal_blue)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

# Configurando frame baixo -------------------------
l_rodando = Label(frame_baixo, text='Selecione uma musica', width=70,
                justify=LEFT, anchor='nw', font=('arial 9 bold'), bg=Royal_blue, fg=amarelo)
l_rodando.place(x=0, y=1)

# Botões ----------------------------------------------------------------
img_anterior = Image.open('Skip_Back.png')
img_anterior = img_anterior.resize((30, 30))
img_anterior = ImageTk.PhotoImage(img_anterior)
b_anterior = Button(frame_baixo, command=previous_music, width=40, height=40, image=img_anterior, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_anterior.place(x=38, y=35)

img_play = Image.open('Play.png')
img_play = img_play.resize((30, 30))
img_play = ImageTk.PhotoImage(img_play)
b_play = Button(frame_baixo, width=40, height=40, command=play_music, image=img_play, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_play.place(x=84, y=35)

img_proxima = Image.open('Skip_Fwd.png')
img_proxima = img_proxima.resize((30, 30))
img_proxima = ImageTk.PhotoImage(img_proxima)
b_proxima = Button(frame_baixo, command=next_music, width=40, height=40, image=img_proxima, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_proxima.place(x=130, y=35)

img_Pause = Image.open('Pause.png')
img_Pause = img_Pause.resize((30, 30))
img_Pause = ImageTk.PhotoImage(img_Pause)
b_Pause = Button(frame_baixo, command=pause_music, width=40, height=40, image=img_Pause, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_Pause.place(x=176, y=35)

img_unpause = Image.open('Unpause.png')
img_unpause = img_unpause.resize((30, 30))
img_unpause = ImageTk.PhotoImage(img_unpause)
b_unpause = Button(frame_baixo, command=unpause_music, width=40, height=40, image=img_unpause, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_unpause.place(x=222, y=35)

img_return = Image.open('Return.png')
img_return = img_return.resize((30, 30))
img_return = ImageTk.PhotoImage(img_return)
b_proxima = Button(frame_baixo, command=repeat_music, width=40, height=40, image=img_return, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_proxima.place(x=268, y=35)

img_muted = Image.open('stop.png')
img_muted = img_muted.resize((30, 30))
img_muted = ImageTk.PhotoImage(img_muted)
b_muted = Button(frame_baixo, command=stop_music, width=40, height=40, image=img_muted, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_muted.place(x=314, y=35)

img_playslist = Image.open('Library.png')
img_playslist = img_playslist.resize((30, 30))
img_playslist = ImageTk.PhotoImage(img_playslist)
b_playslist = Button(frame_baixo, command=new_playlist, width=40, height=40, image=img_playslist, relief=RAISED, overrelief=RIDGE, bg=Royal_blue)
b_playslist.place(x=360, y=35)


musicas = os.listdir()


def exibir_lista():
    listbox.delete(0, END)
    for i in musicas:
        listbox.insert(END, i)


exibir_lista()


# inicializando o mixer 
mixer.init()

janela.mainloop()
