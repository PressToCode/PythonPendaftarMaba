import re

# Validasi Nama berupa huruf dan spasi saja
def nameValidator(name) -> bool:
    if re.fullmatch(r'[A-Za-z ]+', name.strip()):
        return True
    else:
        return False

def numberValidator(number) -> bool:
    if number.isdigit():
        return True
    else:
        return False

def lengthValidator(input, length) -> bool:
    if len(input) == length:
        return True
    else:
        return False

def floatValidator(float) -> bool:
    if re.fullmatch(r'^-?(\d+(\.\d*)?|\.\d+)$', float):
        # RegEx mengecek jika angka seperti 2.5 atau .5
        return True
    else:
        return False