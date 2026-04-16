tasks = []

def do(x, y=None):
    if x == 1:
        t = input("Masukkan tugas: ")
        tasks.append(t)
    elif x == 2:
        for i in range(len(tasks)):
            print(str(i) + ":" + tasks[i])
    elif x == 3:
        i = int(input("Index: "))
        tasks.pop(i)
    else:
        print("Error")

while True:
    print("1.Tambah 2.Lihat 3.Hapus 4.Keluar")
    a = int(input())
    if a == 4:
        break
    do(a)