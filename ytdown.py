from tkinter import *
from pytube import *
import ffmpeg   
import os

# make the winodow tkinter
window = Tk()

# base
window.geometry('500x220')   # ok might need to change later
window.resizable(0,0)
window.title('Simple YouTube Downloader')

#to hold the link
link = StringVar()

# we need to get a link 
linkEntry = Entry(window,width=70,textvariable=link).place(x=30,y=80)

# now need to write the download function 
def download():

    # first get data with YouTube(url)
    yt = YouTube(str(link.get()))
    #print(yt.title)                         # OK

    # need naming
    title = yt.title

    # split to easily recognise
    x = title.split(' ')
    audiofilename = x[0] + 'a'
    videofilename = x[0] + 'v'
    outputfilename = title + '.mkv'

    #try to download
    #YouTube(str(link.get())).streams.first().download()  # downloaded but no audio !!!  # adaptive streams have audio and video separte need to download both
     # video
      # audio  only downloaded ! rewriting occur clips replaced
    #OK
    print('ffmpeg start')
    output = ffmpeg.output(ffmpeg.input(yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=videofilename)), ffmpeg.input(yt.streams.filter(only_audio=True).first().download(filename=audiofilename)),outputfilename,vcodec='copy',acodec='aac',strict='experimental')
    output.run()
    print('ffmpeg stop')
    #now need to join two streams , ffmpeg-python can do that i know

    # error because we gave str need to give ffmpeg.input

    #Ok

    # need to delete two files
    removeaud = audiofilename + '.mp4'
    removevid = videofilename + '.mp4'
    os.remove(removeaud)
    os.remove(removevid)

# we need a button widget from tkinter
Button(window,text='Download',command=download).place(x=195,y=120)




window.mainloop()  # tkinter need mainloop to initialize


# ok some small errors and some videos on youtube can't download at all (in any video downloader)
 # done (will fix file error later.)