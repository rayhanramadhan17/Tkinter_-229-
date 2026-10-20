import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x480")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 14, "bold")
)
judul.grid(row=0, column=0, columnspan=2, pady=15)

mapel = [
    "Nilai Matematika",
    "Nilai Bahasa Indonesia",
    "Nilai Bahasa Inggris",
    "Nilai Fisika",
    "Nilai Kimia",
    "Nilai Biologi",
    "Nilai Sejarah",
    "Nilai Geografi",
    "Nilai Ekonomi",
    "Nilai Informatika"
]

for i, nama_mapel in enumerate(mapel, start=1):
    label = tk.Label(root, text=nama_mapel)
    label.grid(row=i, column=0, padx=15, pady=4, sticky="w")

    entry = tk.Entry(root, width=20)
    entry.grid(row=i, column=1, padx=10, pady=4)

def hasil_prediksi():
    hasil.config(text="Hasil Prediksi Prodi: Teknologi Informasi")

button = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
button.grid(row=11, column=0, columnspan=2, pady=15)

hasil = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    fg="black"
)
hasil.grid(row=12, column=0, columnspan=2, pady=5)

root.mainloop()

