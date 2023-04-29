import os,time,pwinput

admin = 'admin'
pw = '123'
user = 'user@gmail.com'
pw1 = '456'

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
        self.size = 0

    def clear(self):
        os.system('cls')
        time.sleep(1)

    def add(self):
        while True:
            print("-) Ketik 'new' untuk membuat pesan")
            print("-) Ketik 'other' untuk menu lain")
            opsi = input("Ketik? : ")
            if opsi == "other":
                Email.clear()
                break
            elif opsi == "new":
                dari = (input ("Dari : "))
                kepada = (input("Kepada : "))
                subjek = (input("Subjek : "))
                tulis = input("Tulis email : ")
                mail = Gmail(dari, kepada, subjek, tulis)
                Email.clear()
                if self.head is None:
                    self.head = mail
                    self.tail = mail
                    self.size += 1
                else:
                    self.tail.next = mail
                    self.tail = mail
                    self.size += 1
                self.history.append(f"Subjek : {subjek}")

            else :
                Email.clear()
                print("Masukkan dengan benar")

    def newdel(self):
        while True:
            print("-) Ketik 'delete' untuk menghapus pesan")
            print("-) Ketik 'return' untuk kembali ke menu sebelumnya")
            print("-) Ketik 'exit' untuk keluar")
            delnew = input("Pesan baru/Hapus/Keluar? : ")
            if delnew == "delete":
                Email.clear()
                print("Ketik 'return' untuk kembali")
                print("===============================================")
                print("*NOTE")
                print("Tulis 'subjek pesan' untuk menghapus sebuah pesan")
                subjek = input("Masukkan subjek pesan : ")
                if subjek == "return":
                    break
                temp = self.head
                prev = None
                while temp is not None:
                    if temp.subjek == subjek:
                        if prev is None:
                            self.head = temp.next
                            self.size -= 1
                        else:
                            prev.next = temp.next
                        del temp
                        print(f"Subjek {subjek} berhasil dihapus.")
                        self.history.append(f"Subjek yang dihapus : {subjek}")
                        Email.clear()
                        self.show()
                        break
                    prev = temp
                    temp = temp.next
                else:
                    print(f"Subjek {subjek} tidak ada.")
            elif delnew == "return":
                Email.clear()
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

    def histo(self):
        while True:
            print("History : ")
            for a in Email.history:
                print(a)
            choice = input("History di sorting (y/n) : ")
            if choice == "y":
                subject = Email.history
                sorting = quicksort(subject)
                print(sorting)
            elif choice == "n":
                Email.clear()
                break
            else:
                print("Masukkan dengan benar")

    def menuAdmin(self):
        while True:
            print ('1.Search Subject')
            print ('2.History')
            print ('3.Return')
            crud = (input("Input Pilihan : "))
            if crud == "1":
                Email.clear()
                subjek = Email.history
                search = input("Cari : ")
                result = jump_search(subjek, search)
                if result == -1:
                    print(f"Ada subjek '{search}' di dalam pesan Email")
                else:
                    print(f"Tidak ada subjek 2'{search}' di dalam pesan Email")

            elif crud == "2":
                Email.clear()
                Email.histo()

            elif crud == "3":
                Email.clear()
                break
            else:
                Email.clear()
                print ("Pilihan tidak ada")

Email = Mengisi()

def jump_search(arr, x):
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0
        while arr[min(step, n)-1] < x:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1
        while arr[prev] < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev] == x:
            return prev
        return -1

def quicksort(history):
    if len(history) <= 1:
        return history
    else:
        pivot = history[0]
        left_pivot = [title for title in history[1:] if title.lower() < pivot.lower()]
        right_pivot = [title for title in history[1:] if title.lower() >= pivot.lower()]
        return quicksort(left_pivot) + [pivot] + quicksort(right_pivot)

while True :
    print ("""
    Log In sebagai:
    1.) Register User
    2.) Login User
    3.) Login Admin
    4.) Selesai/Keluar
    """)

    choice = (input("Masukkan pilihan yang anda inginkan (1-4) : "))
    if choice == '1' :
        print('Sign Up')
        mainuser = input("Create your username : ")
        mainpass = input("Create your password : ")
        print('Log In')
        username = input("Enter your username : ")
        password = pwinput.pwinput("Enter your password : ")

        if username==mainuser and password==mainpass :
            Email.clear()
            print("Succesfully Logged In")
            Email.add()
            Email.show()
            Email.newdel()
        else:
            Email.clear()
            print("Your username or password is incorrect")

    elif choice == '2' :
        while True:
            try:
                nama = input("Enter your username : ")
                pw = pwinput.pwinput("Enter your password : ")
                if nama == user and pw == pw1:
                    Email.clear()
                    print("Succesfully Logged in")
                    Email.add()
                    Email.show()
                    Email.newdel()
                    break
                else :
                    print ("Masukkan dengan benar")
            except:
                print("Data tidak ditemukan")

    elif choice == '3' :
        while True:
            try:
                nama = input("Enter your username : ")
                pw = pwinput.pwinput("Enter your password : ")
                if nama == admin and pw == pw:
                    Email.clear()
                    print("Succesfully Logged in")
                    Email.menuAdmin()
                    break
                else :
                    print ("Masukkan dengan benar")
            except:
                print("Data tidak ditemukan")

    elif choice == '4' :
        print("Anda berhasil keluar")
        break
        
    else :
        Email.clear()
        print("Masukkan dengan benar")
