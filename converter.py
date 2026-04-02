import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, 'ffmpeg.exe')
    return "ffmpeg.exe"

def select_input():
    file = filedialog.askopenfilename(
        filetypes=[("Media files", "*.mp4 *.avi *.mkv *.mov")]
    )
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file)

def select_output():
    output_format = format_var.get()
    file = filedialog.asksaveasfilename(
        defaultextension=f".{output_format}",
        filetypes=[(output_format.upper(), f"*.{output_format}")]
    )
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file)

def convert():
    input_file = input_entry.get()
    output_file = output_entry.get()
    output_format = format_var.get()

    if not input_file or not output_file:
        messagebox.showerror("Ошибка", "Выберите файлы!")
        return

    ffmpeg_path = get_ffmpeg_path()

    try:
        command = [ffmpeg_path, "-i", input_file]

        # логика форматов
        if output_format == "mp4":
            command += ["-vcodec", "libx264", "-acodec", "aac", "-preset", "slow", "-crf", "28"]
        elif output_format == "avi":
            command += ["-vcodec", "mpeg4"]
        elif output_format == "mkv":
            command += ["-vcodec", "libx264"]
        elif output_format == "mov":
            command += ["-vcodec", "libx264", "-acodec", "aac", "-preset", "slow", "-crf", "28"]

        command.append(output_file)

        subprocess.run(command, check=True)
        messagebox.showinfo("Готово", "Конвертация завершена!")

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


# GUI
root = tk.Tk()
root.title("Видео конвертер")
root.geometry("500x300")

tk.Label(root, text="Входной файл:").pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()

tk.Button(root, text="Выбрать", command=select_input).pack()

tk.Label(root, text="Формат вывода:").pack()

format_var = tk.StringVar(value="mp4")

formats = ["mp4", "avi", "mkv", "mov"]

format_menu = tk.OptionMenu(root, format_var, *formats)
format_menu.pack()

tk.Label(root, text="Выходной файл:").pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()

tk.Button(root, text="Сохранить как", command=select_output).pack()

tk.Button(root, text="Конвертировать", command=convert, bg="green", fg="white").pack(pady=20)

root.mainloop()