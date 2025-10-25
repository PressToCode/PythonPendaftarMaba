import validator
import menu

# Untuk Menu
listMenu = {1:'Tambah Mahasiswa', 2:'Tampilkan Semua Mahasiswa', 3:'Cari Mahasiswa Berdasarkan NIM', 4:'Hapus Mahasiswa Berdasarkan NIM', 5:'Keluar'}

# Pesan Awal Menampilkan Menu yang Tersedia
def menus():
    print('Silahkan Pilih Menu:')
    for(number,text) in listMenu.items():
        print(f'{number}) {text}')

# Memproses Input
def processMenu(input):
    # Validasi Input merupakan Angka
    if not validator.numberValidator(input):
        print('Input Invalid!\n')
        return

    input = int(input)
    # Jika memilih salah satu menu
    if input == 5:
        exit()
    elif input == 4:
        menu.optionFour()
        return
    elif input == 3:
        menu.optionThree()
        return
    elif input == 2:
        menu.optionTwo()
        return
    elif input == 1:
        menu.optionOne()
        return
    else:
        # Jika input angka bukan salah satu menu
        print('Input Invalid!\n')

# Main
if __name__ == '__main__':
    while True:
        menus()
        processMenu(input('Pilih Menu (1-5): '))