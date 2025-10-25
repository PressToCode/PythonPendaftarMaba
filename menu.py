import validator

# Untuk Mahasiswa (Dictionary)
# Format {<NIM>:[<NAMA>,<PRODI>,<IPK>]}
listMaba = {235150700111021:['Muhammad Olfat Faiz', 'Teknologi Informasi', '4.0']}

# Opsi 01) Tambah Mahasiswa
def optionOne():
    print('\nMenambahkan Mahasiswa:')
    while True:
        name = input('Nama: ')
        if validator.nameValidator(name):
            break
        print('Input Invalid!\n')

    while True:
        nim = input('Nim: ')
        if (validator.numberValidator(nim)) and (validator.lengthValidator(nim, 15)):
            break
        print('Input Invalid! (Syarat: Angka 15 digit!)\n')

    while True:
        prodi = input('Prodi: ')
        if validator.nameValidator(prodi):
            break
        print('Input Invalid!\n')

    while True:
        ipk = input('IPK: ')
        if (validator.numberValidator(ipk)) or (validator.floatValidator(ipk)):
            break
        print('Input Invalid!\n')

    # NIM tidak akan duplikat, akan di override
    listMaba[int(nim)] = [name, prodi, ipk]

# Opsi 02) Tampilkan Semua Mahasiswa
def optionTwo():
    if len(listMaba) == 0:
        print('Data Mahasiswa Kosong...\n')
        return

    print('\nList Semua Mahasiswa:')
    for (nim,detail) in listMaba.items():
        print("Nama\t:" + detail[0])
        print("NIM\t\t:" + str(nim))
        print("Prodi\t:" + detail[1])
        print("IPK\t\t:" + detail[2] + "\n")

# KISS Principle (Keep It Simple, St*pid)
def findMahasiswaByNIM(prompt):
    nim = input('Input NIM Mahasiswa ' + prompt + ': ')

    if not validator.numberValidator(nim):
        print('Input Invalid! Kembali ke menu...\n')
        return None, None

    nim = int(nim)
    detail = listMaba.get(nim)

    if detail is None:
        print('Mahasiswa tidak ditemukan!\n')
        return None, None

    return nim, detail

# Opsi 03) Mencari Mahasiswa Berdasarkan NIM
def optionThree():
    nim, detail = findMahasiswaByNIM('yang Dicari')

    if detail is None:
        return

    print('Detail Mahasiswa:')
    print('Nama\t:' + detail[0])
    print('NIM\t\t:' + str(nim))
    print('Prodi\t:' + detail[1])
    print('IPK\t\t:' + detail[2] + "\n")

# Opsi 04) Menghapus Mahasiswa Berdasarkan NIM
def optionFour():
    nim, detail = findMahasiswaByNIM('yang Dicari')

    if detail is None:
        return

    listMaba.pop(int(nim))
    print(detail[0] + ' dengan NIM ' + str(nim) + ' Berhasil Dihapus\n')