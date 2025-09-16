def encrypt(plaintext: str, keyword: str) -> str:
    """
    Функция шифрует входную строку шифром Виженера с помощью ключевого слова
    """
    alphabet = sorted(list(set(('qwertyuiopasdfghjklzxcvbnm'))))
    assert len(alphabet) == 26
    a_ascii_code = ord('a')
    key_numbers = [ord(letter) - a_ascii_code for letter in keyword.lower() if letter in alphabet]


    total_symbols = 126 - 31
    output = ''

    interval_begin = 32
    interval_end = 126
    for i in range(len(plaintext)):
        symbol = plaintext[i]
        shift =  key_numbers[i % len(key_numbers)]

        if interval_begin <= ord(symbol) <= interval_end:
            output += chr((ord(symbol) - interval_begin + shift) % total_symbols + interval_begin)
        else:
            output += symbol

    return output

def decrypt(ciphertext: str, keyword: str) -> str:
    """
    Функция дешифрует входную строку шифром Виженера с помощью ключевого слова
    [шифрует с противоположным сдвигом]
    """
    alphabet = sorted(list(set(('qwertyuiopasdfghjklzxcvbnm'))))
    assert len(alphabet) == 26
    a_ascii_code = ord('a')
    key_numbers = [ord(letter) - a_ascii_code for letter in keyword.lower() if letter in alphabet]

    total_symbols = 126 - 31
    output = ''

    interval_begin = 32
    interval_end = 126
    for i in range(len(ciphertext)):
        symbol = ciphertext[i]
        shift = key_numbers[i % len(key_numbers)]

        if interval_begin <= ord(symbol) <= interval_end:
            output += chr((ord(symbol) - interval_begin - shift) % total_symbols + interval_begin)
        else:
            output += symbol

    return output