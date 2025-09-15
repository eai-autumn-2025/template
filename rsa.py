def is_prime(n: int) -> bool:
    return n >= 2 and all(n % divider !=0 for divider in range(2,int(n**0.5)+1))

def gcd(a: int, b: int) -> int:
    while b !=0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e: int, phi:int) -> int:
    """
    ищет натуральное число, которое при умножении на e по модулю phi даёт 1
    с помощью последовательного перебора натуральных n
    """
    assert gcd(e, phi) == 1
    n = 0
    while (phi * n + 1) % e != 0:
        n+=1
    return (phi * n + 1)//e

    #return pow(e, -1, phi)

def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    генерирует открытый и закрытый ключи
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while gcd(e,phi) != 1:
        e+=1
    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key: tuple[int, int], text: str) -> list[int]:
    """
    шифрует входную строку с помощью закрытого ключа
    возвращает список зашифрованных ascii-кодов
    """

    e, n = public_key
    cipher_list = [None for _ in range(len(text))]
    for i in range(len(text)):
        #зашифровывает символ, находя остаток от деления на n его ascii-кода в степени e
        encrypted_symbol = pow(ord(text[i]), e, n)
        cipher_list[i] = encrypted_symbol
    return cipher_list

def decrypt(private_key: tuple[int, int], cipher_list: list[int]) -> str:
    """
    дешифрует входную строку с помощью закрытого ключа
    возвращает список зашифрованных ascii-кодов
    """
    d, n = private_key
    messege = ''
    for encrypted_symbol in cipher_list:
        #расшифровывает символ, находя остаток от деления на n его ascii-кода в степени d
        decrypted_symbol = pow(encrypted_symbol,d,n)
        messege+= chr(decrypted_symbol)
    return messege

