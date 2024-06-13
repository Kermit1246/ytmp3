import os
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, messagebox
from pytube import YouTube

#dl
def DL(link, dl_folder):
    audio = YouTube(link).streams.filter(only_audio=True).first()
    return audio.download(output_path=dl_folder)

#convert
def convert():
    url, dl_folder = url_entry.get(), folder_path.get()
    if not url:
        return messagebox.showerror("Error", "Please enter a YouTube URL")
    if not dl_folder:
        return messagebox.showerror("Error", "Please select a download folder")
    try:
        output_file = DL(url, dl_folder)
        new_file = os.path.splitext(output_file)[0] + '.mp3'
        os.rename(output_file, new_file)
        messagebox.showinfo("Success", f"Downloaded and saved audio as MP3: {new_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

#fl
def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# tk
root = Tk()
root.title("YT to MP3")
root.resizable(False, False)

url_label = Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

folder_label = Label(root, text="Download Folder:")
folder_label.grid(row=1, column=0, padx=10, pady=10)

folder_path = StringVar()
folder_entry = Entry(root, textvariable=folder_path, width=50)
folder_entry.grid(row=1, column=1, padx=10, pady=10)

folder_button = Button(root, text="Browse", command=select_folder)
folder_button.grid(row=1, column=2, padx=10, pady=10)

download_button = Button(root, text="Convert", command=convert)
download_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
