import webbrowser as wb
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pyautogui
import subprocess
import requests
import pygame
import os
import cv2
from moviepy.editor import VideoFileClip

urlN  = 'https://www.netflix.com/mx/'
urlA  = 'https://www.primevideo.com/'
urlD  = 'https://www.disneyplus.com/es-mx'
urlH  = 'https://www.hbomax.com/mx/es'
urlC  = 'https://www.crunchyroll.com/es/'
urlAm = 'https://music.amazon.com.mx/'
urlS  = 'https://open.spotify.com/'
urlT  = 'https://tidal.com/'
urlDy = 'https://www.youtube.com/'

#Definicion del color de fondo

# Creación de ventana principal
window = tk.Tk()
window.config(bg="slate blue", cursor="spider")
# Pygame para reproducir musica
pygame.mixer.init()

# Largo y ancho de la ventana
width  = window.winfo_screenwidth()
height = window.winfo_screenheight()

espera = 200 #ms de espera

# Creación de funciones para cada servicio de streaming
def Netflix():
    wb.open_new(urlN) #Abre la url que se le manda como parámetro
    window.after(espera,pantallaCompleta) 

def Prime():
    wb.open_new(urlA)
    window.after(espera,pantallaCompleta)

def Disney():
    wb.open_new(urlD)
    window.after(espera,pantallaCompleta)

def HBO_MAX():
    wb.open_new(urlH)
    window.after(espera,pantallaCompleta)

def Crunchy():
    wb.open_new(urlC)
    window.after(espera,pantallaCompleta)

def PrimeMusic():
    wb.open_new(urlAm)
    window.after(espera,pantallaCompleta)

def Spotify():
    wb.open_new(urlS)
    window.after(espera,pantallaCompleta)

def Tidal():
    wb.open_new(urlT)
    window.after(espera,pantallaCompleta)

def Youtube():
    wb.open_new(urlDy)
    window.after(espera,pantallaCompleta)    
    
def pantallaCompleta():
    pyautogui.press("F11") 

def apagar():
    subprocess.call(['shutdown', "-h", "now"])

def cerrar():
    pygame.mixer.music.stop()
    pyautogui.keyDown("alt")
    pyautogui.press("F4")
    pyautogui.keyUp("alt")

def Salir():
    labelSalir = Label(window, text="ADIOS <3",
             fg="#fff",    # Foreground
             #bg=colorFondo,   # Background
             bg="slate blue",   # Background
             font=("Georgia",60))
    labelSalir.place(relx=0, rely=0, relheight=1, relwidth=1)
    window.after(5000, apagar)

def reinicio():
    subprocess.run(["reboot"])

def Conexion_Red(ssid, key):
    global labelConfig
    arch = '/etc/wpa_supplicant/wpa_supplicant.conf'
    subprocess.call(['sudo', "chmod", "777", arch])
    
    with open(arch, 'w') as fp:
        fp.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev')
    with open(arch, 'a') as fp:
        fp.write('\nupdate_config=1')
    with open(arch, 'a') as fp:
        fp.write('\ncountry=MX')
    with open(arch, 'a') as fp:
        fp.write('\nnetwork={ \n')
    with open(arch, 'a') as fp:
        fp.write('\tssid="{}" \n'.format(str(ssid)))
    with open(arch, 'a') as fp:
        fp.write('\tpsk="{}" \n'.format(str(key)))    
    with open(arch, 'a') as fp:
        fp.write('\tkey_mgmt=WPA-PSK')
    with open(arch, 'a') as fp:
        fp.write('\n}')
    labelConfig = Label(window, text="Empleando Configuración\nNecesita Reiniciar",                    
                    fg="#fff", bg="slate blue",font=("Georgia",60))
    labelConfig.place(relx=0, rely=0, relwidth=1, relheight=1)
    window.after(4000, reinicio)

def Configuracion_Red():
    labelTitulo = Label(window, text="Configuracion de Red",
             fg="#fff",    # Foreground            
             bg="slate blue",   # Background
             font=("Georgia",60))
    labelTitulo.place(relx=0.3, rely=0.05)
    botonClose.place(relx=0.9, rely=0.9) # Posición del botón de cerrar

    # Llamado de cada botón
    botonNetflix.place_forget()
    botonPrime.place_forget()
    botonDisney.place_forget()
    botonHBO_MAX.place_forget()
    botonCrunchy.place_forget()
    botonPrimeMusic.place_forget()
    botonSpotify.place_forget()
    botonTidal.place_forget()    
    botonYoutube.place_forget()
    botonConfiguracion.place_forget()
    botonSalir.place_forget()
    botonUsb.place_forget()

    labelSSID = Label(window, text="Red", 
                        fg="#fff",    # Foreground
                        #bg=colorFondo,   # Background
                        bg="slate blue",   # Background
                        font=("Georgia",40))
    labelSSID.place(relx=0.25, rely=0.35) 
    
    entrySSID.place(relx=0.45, rely=0.35, relheight=0.05, relwidth=0.25)

    labelPWD = Label(window, text="Contraseña", 
                        fg="#fff",    # Foreground                        
                        bg="slate blue",   # Background
                        font=("Georgia",40))
    labelPWD.place(relx=0.25, rely=0.55) 

    entryPWD.place(relx=0.45, rely=0.55, relheight=0.05, relwidth=0.25)

    botonConnect.pack()
    botonConnect.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)

def USB():
    # Llamado de cada botón
    botonNetflix.place_forget()
    botonPrime.place_forget()
    botonDisney.place_forget()
    botonHBO_MAX.place_forget()
    botonCrunchy.place_forget()
    botonPrimeMusic.place_forget()
    botonSpotify.place_forget()
    botonTidal.place_forget()    
    botonYoutube.place_forget()
    botonConfiguracion.place_forget()
    botonSalir.place_forget()
    botonUsb.place_forget()

    labelBienvenida.place_forget()
    botonConnect.place_forget()
    
    
    botonClose.place(relx=0.9, rely=0.9) # Posición del botón de cerrar

    botonMusica.pack()
    botonImagenes.pack()
    botonVideo.pack()

    botonMusica.place(relx=0.2,  rely=0.4)
    botonImagenes.place(relx=0.7,  rely=0.4)
    botonVideo.place(relx=0.45, rely=0.4)

def Musica():
    musicPlayer = tk.Toplevel()    
    musicPlayer.config(bg="slate blue", cursor="spider") #Se define el color de la mini interfaz
    musicPlayer.geometry("%dx%d" % (width, height))

    labelMusica = Label(window, text="DinamitaMusic", #Se define el nombre de la ventana
                        fg="#fff",    # Foreground                        
                        bg="slate blue",   # Background
                        font=("Georgia",60))
    labelMusica.place(relx=0.3, rely=0.05) #Posición de la ventana

    botonClose = tk.Button(musicPlayer,  # Botón para cerrar 
                            text = "Regresar",
                            command = musicPlayer.destroy,
                            bg="#000",  
                            borderwidth= 0.1,
                            fg="#fff",                            
                            cursor="heart",
                            font=("Georgia", 18))
    botonClose.place(relx=0.9, rely=0.9) # Posición del botón de cerrar
    musicPlayer.focus()
    musicPlayer.grab_set() # Función para que el usuario no pueda utilizar la ventana principal

    # Función para agregar canciones de la memoria USB
    def añadir():
        canciones = filedialog.askopenfilenames(initialdir="/media/pepito/Roja/Music",title="Elige una canción",filetypes=(("mp3","*.mp3"),("allfiles","*.*")))
        #camiar la extension del nombre de la cancion for cancion in canciones:
        for cancion in canciones:
    
            cancion=cancion.replace("C:/Users/User/Downloads/","")
            cancion=cancion.replace(".mp3","")
    
        #añadir cancion a la pantalla
            pantalla.insert (END, cancion)
            
        cancion= pantalla.get(ACTIVE)
        cancion=f'{cancion}.mp3'
    
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play(loops=0)
    
    def siguiente():
        #obtener el numero de tuple de la cancion que esta sonando
        proxima = pantalla.curselection()
        #añadir uno al numero de cancion
        proxima = proxima[0]+1
    
        if proxima >= pantalla.size():
            proxima = 0 
        #obtener titulo de cancion 
        cancion= pantalla.get(proxima)	
    
        cancion= f'{cancion}.mp3'
    
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play(loops=0)
    
        pantalla.selection_clear(0,END)
        #activar nueva barra a la siguiente cancion
        pantalla.activate(proxima)
        #mostrar la barra
        last = None
        pantalla.selection_set(proxima, last)
    
    global paused
    paused=False
    
    def pause(is_paused):
        global paused
        paused = is_paused
        if paused:
            pygame.mixer.music.unpause()
            paused=False 
        else:
            pygame.mixer.music.pause()
            paused=True

    #Pantalla
    pantalla= Listbox(musicPlayer, bg="lightblue", fg ="blue", width= 100, selectbackground= "white", selectforeground="black") 
    pantalla.pack(pady=150)
    #Botones
    Siguiente_Cancion= tk.Button(musicPlayer, text="Siguiente", command= siguiente, #ventana, texto del boton, accion 
                         bg="#000", borderwidth= 0.1, #color de fondo, grosor del boton
                         fg="#fff",
                         cursor="heart",
                         font=("Georgia", 18)) #tamaño y fuente de letra
    Siguiente_Cancion.pack()
    Siguiente_Cancion.place(relx=0.5, rely=0.35) #posicion del boton
    

    pausa= tk.Button(musicPlayer, text="Pausa", command=lambda: pause(paused), #botón pausa
                     bg="#000",borderwidth= 0.1,
                     fg="#fff",
                     cursor="heart",
                     font=("Georgia", 18))
    pausa.pack()
    pausa.place(relx=0.65, rely=0.35)

    buscar = tk.Button(musicPlayer, text = "Buscar Canciones", command=añadir, #boton buscar cancion
                       bg="#000", borderwidth= 0.1,
                       fg="#fff",
                       cursor="heart",
                       font=("Georgia", 18))
    buscar.pack()
    buscar.place(relx=0.30, rely=0.35)
    
    
    musicPlayer.attributes('-fullscreen', True)
    
def Imagenes():
    input_images_path = "/media/pepito/Roja/Images"
    files_names = os.listdir(input_images_path)

    for file_name in files_names:
        image_path = input_images_path + "/" + file_name
        print(image_path)
        image = cv2.imread(image_path)
        if image is None:
            continue
        image = cv2.resize(image, (1280, 720), interpolation=cv2.INTER_CUBIC)
        
        cv2.imshow("Image", image)
        cv2.waitKey(1000)

    cv2.destroyAllWindows()

def Video():
    input_videos_path = "/media/pepito/Roja/Video"
    files_names = os.listdir(input_videos_path) 

    for file_name in files_names:
        video_path = os.path.join(input_videos_path, file_name)
        print(video_path)
        video = cv2.VideoCapture(video_path)
        if video is None:
            continue
    
        clip = VideoFileClip(video_path)
        clip.preview()

        while video.isOpened():
            ret, frame = video.read()
            if ret:
                cv2.imshow("Videos", frame)
                if cv2.waitKey(1) != -1:  # Presionar cualquier tecla para salir
                    break                    
            else:
                break                

        video.release()
        cv2.destroyAllWindows()   # Cerrar manualmente la ventana del video

def main():
    global botonConnect
    try:
        request = requests.get("http://www.google.com", timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        labelWifi = Label(window, image=img_nowifi,                       
                       bg="slate blue")
    else:
        labelWifi = Label(window, image=img_wifi,                       
                       bg="slate blue")
    labelWifi.place(relx=0.95, rely=0.05)

    labelTitulo.place(relx=0.3, rely=0.05)
    # Llamado de cada botón
    botonNetflix.pack()
    botonPrime.pack()
    botonDisney.pack()
    botonHBO_MAX.pack()
    botonCrunchy.pack()
    botonPrimeMusic.pack()
    botonSpotify.pack()
    botonTidal.pack()    
    botonYoutube.pack()
    botonConfiguracion.pack()
    botonUsb.pack()
    botonSalir.pack()
    
    botonNetflix.place(relx=0.2,  rely=0.2)
    botonPrime.place(relx=0.36,  rely=0.2)
    botonDisney.place(relx=0.52,  rely=0.2)
    botonHBO_MAX.place(relx=0.68,  rely=0.2)

    botonCrunchy.place(relx=0.2, rely=0.45)
    botonSpotify.place(relx=0.36, rely=0.45)
    botonPrimeMusic.place(relx=0.52, rely=0.45)
    botonTidal.place(relx=0.68, rely=0.45)

    botonYoutube.place(relx=0.2, rely=0.7)
    botonUsb.place(relx=0.36, rely=0.7)
    botonConfiguracion.place(relx=0.52, rely=0.7)
    botonSalir.place(relx=0.68, rely=0.7)   

    #Se oculta la pagina de bienvenida
    labelBienvenida.place_forget()
    botonConnect.place_forget()
    botonClose.place_forget()
    botonMusica.place_forget()
    botonVideo.place_forget()
    botonImagenes.place_forget()
    entrySSID.place_forget()
    entryPWD.place_forget()    
    labelSSID.place_forget()
    labelPWD.place_forget()
    
img_netflix = tk.PhotoImage(file="/home/pepito/Desktop/iconos/netflix.png")
img_prime   = tk.PhotoImage(file="/home/pepito/Desktop/iconos/prime.png")
img_disney  = tk.PhotoImage(file="/home/pepito/Desktop/iconos/disney.png")
img_hbo     = tk.PhotoImage(file="/home/pepito/Desktop/iconos/hbo.png")

img_crunchy = tk.PhotoImage(file="/home/pepito/Desktop/iconos/crunchy.png")
img_spotify = tk.PhotoImage(file="/home/pepito/Desktop/iconos/spotify.png")
img_primemusic=tk.PhotoImage(file="/home/pepito/Desktop/iconos/primemusic.png")
img_tidal   = tk.PhotoImage(file="/home/pepito/Desktop/iconos/tidal.png")

img_youtube = tk.PhotoImage(file="/home/pepito/Desktop/iconos/youtube.png")
img_config  = tk.PhotoImage(file="/home/pepito/Desktop/iconos/config.png")
img_salir   = tk.PhotoImage(file="/home/pepito/Desktop/iconos/salir.png")
img_wifi    = tk.PhotoImage(file="/home/pepito/Desktop/iconos/wifi.png")
img_nowifi  = tk.PhotoImage(file="/home/pepito/Desktop/iconos/nowifi.png")
img_usb  = tk.PhotoImage(file="/home/pepito/Desktop/iconos/usb.png")
img_musica  = tk.PhotoImage(file="/home/pepito/Desktop/iconos/musica.png")
img_fotos  = tk.PhotoImage(file="/home/pepito/Desktop/iconos/fotos.png")
img_video  = tk.PhotoImage(file="/home/pepito/Desktop/iconos/video.png")
#se guarda la imagen del boton
# Creación de los botones
botonNetflix = tk.Button(window, image=img_netflix, #ventana, imagen que tendrá el botón 
                         borderwidth=0, bg="slate blue", #grosor del botón, color de fondo
                         cursor="heart", #cursor 
                         command = Netflix) #acción que hará cuando se oprima el botón

botonPrime = tk.Button(window, image=img_prime,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                        command = Prime)

botonDisney = tk.Button(window, image=img_disney,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                        command = Disney)

botonHBO_MAX = tk.Button(window, image=img_hbo,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = HBO_MAX)    

botonCrunchy = tk.Button(window, image=img_crunchy,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Crunchy)


botonSpotify = tk.Button(window, image=img_spotify,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Spotify)

botonPrimeMusic=tk.Button(window, image=img_primemusic,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = PrimeMusic)

botonTidal=tk.Button(window, image=img_tidal,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Tidal)

botonYoutube = tk.Button(window, image=img_youtube,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Youtube)   

botonConfiguracion = tk.Button(window, image=img_config,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Configuracion_Red)

botonSalir = tk.Button(window, image=img_salir,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Salir)

botonUsb = tk.Button(window, image=img_usb,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = USB)

botonMusica = tk.Button(window, image=img_musica,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Musica)

botonImagenes = tk.Button(window, image=img_fotos,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Imagenes)

botonVideo = tk.Button(window, image=img_video,
                         borderwidth=0, bg="slate blue",
                         cursor="heart",
                         command = Video)

botonClose = tk.Button(window,
                            text = "Volver",
                            command = main,
                            bg="#000",  
                            borderwidth= 0.1,
                            fg="#fff",
                            cursor="heart",
                            font=("Georgia", 18))

botonConnect = tk.Button(window, text="Conectar",
                         command=lambda: Conexion_Red(entrySSID.get(), entryPWD.get()),
                         bg="#fff",  
                         borderwidth= 0.1,
                         fg="#000",
                         cursor="heart",
                         font=("Georgia", 40))                   

#Creacion de los label
labelBienvenida = Label(window, text="   Bienvenidos DinamitaTV",
                        fg="#fff",    # Foreground
                        bg="slate blue",   # Background
                        font=("Georgia",60))

labelTitulo = Label(window, text="         DinamitaTV",
                    fg="#fff",    # Foreground
                    bg="slate blue",   # Background
                    font=("Georgia",60))

entrySSID = Entry(window, font=("Georgia",34))
entryPWD = Entry(window, font=("Georgia",34), show="*")
labelSSID = Label(window, font=("Georgia",34))
labelPWD = Label(window, font=("Georgia",34))
# Geometria de la ventana
window.geometry("%dx%d" % (width, height))
# Atributos de la ventana, en este caso tiene que ser en pantalla completa
window.attributes('-fullscreen', True)
# Nombre de la ventana
window.title("Multimedia Center")

labelBienvenida.place(relx=0, rely=0, relheight=1, relwidth=1)
window.after(1000, main)

window.mainloop()
