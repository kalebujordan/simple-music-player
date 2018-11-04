from pygame import mixer
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from random import randrange
import time

root = Tk()
root.title("Music Player")
root.geometry("400x400")
root.configure(background="#345")
root.iconbitmap('1.ico')
root.resizable(False, False)

class Iris():
	def __init__(self):
		mixer.init()
		mixer.music.set_volume(0.5)
		self.pstate=0
		self.songs = []
		self.song_number = 0

	def pick_color(self):
		bcolor = colorchooser.askcolor()
		bcolor = bcolor[1]
		root.configure(background=bcolor)

	def open_file(self):
		self.songs = []
		musics = filedialog.askopenfilenames()
		for song in musics:
			if song.endswith('.mp3'):
				self.songs.append(song)
			else:
				continue
		for song in self.songs:
			print(song)

	def load_music(self):
		music_file = filedialog.askopenfilename()
		self.music_file = music_file
		print(music_file)

	def get_songname(self, song_dir):
		playing_song = song_dir
		playing_song = playing_song.split('/')
		playing_song = playing_song[-1]
		playing_song = playing_song.split('.')
		playing_song = playing_song[-2]
		song_playing_l.configure(text=playing_song)
		print(playing_song)

	def s_play(self, songname):
		mixer.music.load(songname)
		mixer.music.play(0)

	def s_play_get(self, current):
		Iris().get_songname(current)
		Iris().s_play(current)


	def play(self):
		if self.songs:
			current = self.songs[self.song_number]
			Iris().s_play_get(current)	
		else:
			Iris().s_play_get(self.music_file)

	def pause(self):
		if self.pstate == 0:
			pause_b.configure(bg='red')
			mixer.music.pause()
			self.pstate+=1
		else:
			pause_b.configure(bg='green')
			mixer.music.unpause()
			self.pstate-=1


	def volume(self, level):
		if level:
			volume_amount = mixer.music.get_volume()
			if volume_amount>=0:
				v_color = randrange(100, 999)
				v_color = '#' + str(v_color)
				volume_b.configure(bg=v_color)
				volume_amount = float(level)
				volume_amount/=100
				mixer.music.set_volume(volume_amount)

	def next_(self):
		plen = len(self.songs)
		if self.song_number<plen-1:
			self.song_number+=1
			current = self.songs[self.song_number]
			Iris().s_play_get(current)

	def back_(self):
		plen = len(self.songs)
		if self.song_number>0:
			self.song_number-=1
			current = self.songs[self.song_number]
			Iris().s_play_get(current)
		
iris = Iris()



play_b = Button(root, text='play', command=iris.play, width=15)
volume_b = Scale(root, from_=100, to=0, bg="#234", width=15, command=iris.volume)
volume_b.set(50)
song_playing_l = Label(root, bg='blue', font=('Arial', 10))
pause_b  = Button(root, text="Pause", bg='green', width=15, command=iris.pause)
play_b = Button(root, text='play', command=iris.play, width=10)
next_b = Button(root, text='next', command=iris.next_, bg='red', width=10)
back_b = Button(root, text='back', command=iris.back_, bg='green', width=10)

def initializer():
	volume_b.place(x=0, y=280)
	pause_b.place(x=165, y=325)
	back_b.place(x=100, y=350)
	next_b.place(x=260, y=350)
	play_b.place(x=180, y=350)
	song_playing_l.place(x=10, y=100)

set_info = initializer()

menubar = Menu(root)
root.config(menu = menubar)
filemenu = Menu(menubar)
loadmenu = Menu(menubar)
menubar.add_cascade(label = 'Home', menu = filemenu)
menubar.add_cascade(label="Load", menu=loadmenu)
loadmenu.add_command(label='Load Music', command=iris.load_music)
loadmenu.add_command(label='Load playlist', command=iris.open_file)
loadmenu.add_command(label='Load Folder')
filemenu.add_command(label="background", command=iris.pick_color)
filemenu.add_command(label="settings")
filemenu.add_command(label="Exit", command=root.destroy)


root.mainloop()