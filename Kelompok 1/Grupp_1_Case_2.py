import pandas as pd
import matplotlib.pyplot as plt

class Mahasiswa:
    def __init__(self, nama, id, nilai):
        self.nama = nama
        self.id = id
        self.nilai = nilai

    def hitung_rata_rata(self):
        if len(self.nilai) == 0:
            return 0
        return sum(self.nilai) / len(self.nilai)

    def kategori_nilai(self):
        rata_rata = self.hitung_rata_rata()
        if rata_rata >= 80:
            return "Excellent"
        elif 60 <= rata_rata < 80:
            return "Good"
        else:
            return "Needs Improvement"

data_mahasiswa = [
    Mahasiswa("Hafizah Halizah", "20231001", [85, 78, 90]),
    Mahasiswa("Ilman", "20231002", [70, 75, 72]),
    Mahasiswa("Felicia", "20231003", [88, 92, 95]),
    Mahasiswa("Abdus Somad", "20231004", [55, 60, 58])
]

df = pd.DataFrame({
    "Nama": [m.nama for m in data_mahasiswa],
    "ID": [m.id for m in data_mahasiswa],
    "Rata-rata": [m.hitung_rata_rata() for m in data_mahasiswa],
    "Kategori": [m.kategori_nilai() for m in data_mahasiswa]
})

print(df)

kategori_counts = df["Kategori"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(kategori_counts, labels=kategori_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Distribusi Kategori Nilai Mahasiswa")
plt.show()