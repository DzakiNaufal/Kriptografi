import numpy as np

# ===============================
# Fungsi bantu konversi
# ===============================

def text_to_numbers(text):
    """Konversi huruf ke angka (A=0, ..., Z=25)"""
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    """Konversi angka ke huruf"""
    return ''.join(chr(num % 26 + ord('A')) for num in numbers)

# ===============================
# Hill Cipher: Enkripsi
# ===============================

def hill_encrypt(plaintext, K):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # padding jika ganjil
    nums = text_to_numbers(plaintext)
    ciphertext = []
    for i in range(0, len(nums), 2):
        block = np.array(nums[i:i+2])
        result = np.dot(K, block) % 26
        ciphertext.extend(result)
    return numbers_to_text(ciphertext)

# ===============================
# Mencari invers modulo
# ===============================

def mod_inverse(a, m):
    """Mencari invers dari a mod m"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# ===============================
# Invers matriks 2x2 mod 26
# ===============================

def matrix_mod_inverse(K, mod):
    det = int(np.round(np.linalg.det(K)))  # determinan
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError("Determinant tidak memiliki invers modulo 26")
    adj = np.array([[K[1,1], -K[0,1]],
                    [-K[1,0], K[0,0]]])
    inv_matrix = (det_inv * adj) % mod
    return inv_matrix

# ===============================
# Hill Cipher: Dekripsi
# ===============================

def hill_decrypt(ciphertext, K_inv):
    nums = text_to_numbers(ciphertext)
    plaintext = []
    for i in range(0, len(nums), 2):
        block = np.array(nums[i:i+2])
        result = np.dot(K_inv, block) % 26
        plaintext.extend(result)
    return numbers_to_text(plaintext)

# ===============================
# PROGRAM UTAMA (Input dari user)
# ===============================

print("=== Program Hill Cipher 2x2 ===")
plaintext = input("Masukkan plaintext (A-Z): ").strip().upper()

print("\nMasukkan matriks kunci 2x2 (hanya angka 0-25):")
a = int(input("K[0,0]: "))
b = int(input("K[0,1]: "))
c = int(input("K[1,0]: "))
d = int(input("K[1,1]: "))

K = np.array([[a, b],
              [c, d]])

# Proses enkripsi
ciphertext = hill_encrypt(plaintext, K)

# Hitung invers matriks K (mod 26)
K_inv = matrix_mod_inverse(K, 26)

# Proses dekripsi
decrypted = hill_decrypt(ciphertext, K_inv)

# ===============================
# Tampilkan hasil
# ===============================

print("\n=== HASIL ===")
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
print("Invers matriks K (mod 26):\n", K_inv)
print("Dekripsi  :", decrypted)
print("===============")