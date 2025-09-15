def encrypt(plaintext: str, shift: int) -> str:
    """
    Функция encrypt возвращает входную строку plaintext,
    зашифрованную шифром Цезаря на входной сдвиг shift
    по ascii-кодам отдельных символов строки
    """
    total_symbols = 126 - 31
    output = ''

    interval_begin = 32
    interval_end = 126
    for symbol in plaintext:

        if interval_begin <= ord(symbol) <= interval_end:
            output += chr((ord(symbol) - interval_begin + shift) % total_symbols + interval_begin)
        else:
            output += symbol

    return output

def decrypt(ciphertext: str, shift: int) -> str:
    """
    Функция decrypt возвращает строку ciphertext,
    расшифрованную шифром Цезаря на входной сдвиг shift
    по ascii-кодам отдельных символов строки
    путем вызова функции encrypt со сдвигом  -shift,
    то есть шифрует на противоположный сдвиг
    """
    return encrypt(ciphertext, -shift)
