import tkinter as tk
from tkinter import filedialog, messagebox
import codecs
import os
import sys

def select_input_file():
    input_file = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt"), ("All files", "*.*")])
    if input_file:
        input_file_label.config(text=input_file)

def convert_to_utf8_srt():
    input_file = input_file_label.cget("text")

    if input_file == "dosya yolu":
        messagebox.showerror("Hata", "Lütfen giriş dosyasını seçin.")
        return

    output_file = os.path.splitext(input_file)[0] + "_utf8.srt"

    try:
        with codecs.open(input_file, 'r', encoding='iso-8859-9') as infile:
            content = infile.read()

        with codecs.open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(content)

        messagebox.showinfo("Başarılı", f"SRT dosyası başarıyla UTF-8 formatına dönüştürüldü.\nKaydedilen dosya: {output_file}")
    except Exception as e:
        messagebox.showerror("Hata", f"Dönüştürme sırasında bir hata oluştu: {e}")

# GUI oluşturma
if os.name == "nt":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Hidden")
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

root = tk.Tk()
root.title("Altyazı Uyum Aracı")
root.geometry("400x300")
root.configure(bg="#f9f9f9")

# Dosya
input_file_label = tk.Label(root, text="dosya yolu", bg="#f9f9f9", fg="#333", font=("Arial", 14), width=30, height=2, relief="solid")
input_file_label.pack(pady=40)

# Buton
select_button = tk.Button(root, text="dosya seç", command=select_input_file, bg="#333", fg="white", font=("Arial", 12), width=15, height=1, relief="flat")
select_button.pack(pady=10)

# Dönüştür
convert_button = tk.Button(root, text="Dönüştür", command=convert_to_utf8_srt, bg="#333", fg="white", font=("Arial", 12), width=15, height=1, relief="flat")
convert_button.pack(pady=10)

root.mainloop()
