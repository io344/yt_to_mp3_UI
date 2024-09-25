from pytubefix import YouTube
from pytubefix.exceptions import PytubeFixError
#from pydub import AudioSegment
import os
import tkinter as tk
import validators
from tkinter import filedialog

root = tk.Tk()
root.title("YT TO MP3")
root.geometry('320x300')

root.resizable(False, False)

def browse_dir():
    selected_directory = filedialog.askdirectory()
    return selected_directory

def yt_to_mp3():
    try:
        yt_url = input.get()
        if yt_url.find("watch") == -1:
            return
        if not yt_url.strip():
            return
        if not validators.url(yt_url):
            return

        yt = YouTube(yt_url, 'MWEB')
        label.config(text="Please select a directory:")
        dl_path = browse_dir()
        # if directory not specified
        if not dl_path:
            label.config(text=orig_label)
            return

        label.config(text=f"Saving at {dl_path}...", wraplength=200)
        process_mp3_dl(yt, dl_path)
        #process_dl_mp3(yt, dl_path)
        input.delete(0, tk.END)
        change_label()
    except PytubeFixError as p:
        label.config(text=f'Problem occurred: {p}')
        return
    except:
        label.config(text="Network problem!")
        return

'''def process_dl_mp3(yt, dl_path):
    root.update_idletasks()
    stream = yt.streams.get_audio_only()
    dld_stream = stream.download(output_path=dl_path)
    mp3_file = os.path.splitext(dld_stream)[0] + '.mp3'
    audio = AudioSegment.from_file(dld_stream)
    audio.export(mp3_file, format='mp3')
    os.remove(dld_stream)'''

def process_mp3_dl(yt, dl_path):
    root.update_idletasks()
    stream = yt.streams.get_audio_only()
    stream.download(mp3=True, output_path=dl_path)


def change_label():
    label.config(text="Dl completed!")
    root.after(2000, revert_label)

def revert_label():
    label.config(text=orig_label)

def on_button_click():
    button.grid_remove()
    input.grid_remove()
    label1.grid_remove()
    root.update_idletasks()
    yt_to_mp3()
    label1.grid(row=2, column=0, padx=10, pady=10)
    input.grid(row=3,column=0,padx=10,pady=10)
    button.grid(row=4,column=0,padx=10,pady=10)

orig_label = 'Yt to Mp3'
label = tk.Label(root, text=orig_label, font=("Arial",15,"bold"))
label.grid(row=1,column=0,padx=10,pady=10)

label1 = tk.Label(root, text="Enter URL below:", font=("Arial", 10))
label1.grid(row=2,column=0,padx=10,pady=10)

input = tk.Entry(root, width=50)
input.grid(row=3,column=0,padx=10,pady=10)

button = tk.Button(root, text='Download', font="Arial", command=on_button_click)
button.grid(row=4,column=0,padx=10,pady=10)

root.mainloop()

