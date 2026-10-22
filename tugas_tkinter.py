import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x550")
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold")
)
judul.pack(pady=15)

mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Informatika",
    "Ekonomi",
    "Sosiologi",
    "Geografi"
]

input_nilai = []

for pelajaran in mapel:
    frame = tk.Frame(root)
    frame.pack(pady=3)

    label = tk.Label(frame, text=pelajaran, width=18, anchor="w")
    label.pack(side="left")

    entry = tk.Entry(frame, width=15)
    entry.pack(side="left")

    input_nilai.append(entry)

def hasil_prediksi():
    hasil.config(text="Hasil Prediksi: Teknologi Informasi")

tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)

