import os,time,pwinput

admin = 'me'
pw = 'him'
user = []
pw1 = []

class Gmail:
    def __init__(self, dari, kepada, subjek, tulis):
        self.dari = dari
        self.kepada = kepada
        self.subjek = subjek
        self.tulis = tulis
        self.next = None

    def display(self):
        print("Dari : ", self.dari)
        print("Kepada : ", self.kepada)
        print("Subjek : ", self.subjek)
        print("Tulis email : ", self.tulis)
        print("========================================")

class Mengisi:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def add(self):
        while True:
            dari = input("Dari ('exit' untuk melihat pesan): ")
            if dari == "exit":
                break
            kepada = (input("Kepada : "))
            subjek = (input("Subjek : "))
            tulis = input("Tulis email : ")
            mail = Gmail(dari, kepada, subjek, tulis)
            if self.head is None:
                self.head = mail
                self.tail = mail
            else:
                self.tail.next = mail
                self.tail = mail

            self.history.append("===============================")
            self.history.append(f"Dari : {dari}")
            self.history.append(f"Kepada : {kepada}")
            self.history.append("===============================")

    def newdel(self):
        while True:
            delnew = input("Hapus atau bikin ulang? (delete/new/exit) :")
            if delnew == "delete":
                subjek = input("Masukkan subjek yang ingin dihapus ('exit' jika ingin kembali) : ")
                if subjek == "exit":
                    break
                temp = self.head
                prev = None
                while temp is not None:
                    if temp.subjek == subjek:
                        if prev is None:
                            self.head = temp.next
                        else:
                            prev.next = temp.next
                        del temp
                        print(f"Subjek {subjek} berhasil dihapus.")
                        self.history.append(f"Subjek yang dihapus : {subjek}")
                        self.show()
                        break
                    prev = temp
                    temp = temp.next
                else:
                    print(f"Subjek {subjek} tidak ada.")
            elif delnew == "new":
                self.add()
                self.show()
            elif delnew == "exit":
                return
            else:
                print("Terjadi kesalahan, silahkan input ulang sesuai perintah yang ada")

    def show(self):
        temp = self.head
        while temp is not None:
            temp.display()
            temp = temp.next

Email = Mengisi()

while True:
        try:
            nama = input("Enter your username : ")
            pw = pwinput.pwinput(prompt="Enter your password : ")
            if nama == admin and pw == pw:
                print("Succesfully Logged in")
                Email.add()
                Email.show()
                Email.newdel()
                break
            else :
                print ("Masukkan dengan benar")
        except: print("Data tidak ditemukan")

print("History : ")
for i in Email.history:
    print(i)
