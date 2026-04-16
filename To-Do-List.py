tasks = []

def add_task():
    task_name = input("Masukkan tugas: ")
    tasks.append(task_name)

def show_tasks():
    if not tasks:
        print("Tidak ada tugas")
        return
    
    for index, task in enumerate(tasks):
        print(f"{index}: {task}")

def delete_task():
    try:
        index = int(input("Masukkan index tugas: "))
        tasks.pop(index)
    except (ValueError, IndexError):
        print("Input tidak valid")

def show_menu():
    print("\n=== TO DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def main():
    while True:
        show_menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid")

main()