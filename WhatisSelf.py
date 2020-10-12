#code dimulai
# code pertaanyan dan tambahan keguanaan self

class Reviewer:

    def __init__(self, nama, kelas):

        self.nama = nama

        self.kelas = kelas

    def review(self):

        print("Reviewer " + self.nama + " bertanggung jawab di kelas " + self.kelas)

#code tambahan 
    def cobaSelf(self):
         nama = "Saya"
         return (f"Nama dengan self {self.nama}, nama tanpa self {nama}" )




reviewer = Reviewer("Aku", "Python")
print(reviewer.cobaSelf())

'''
mencoba self di luar class dengan hapus tanda "#" pada print di bawah , akan terjadi error
yaitu NameError: name 'self' is not defined
'''
#print(self.nama)

#code selesai 
