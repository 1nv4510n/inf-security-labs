# Шифр Виженера, Савин Богдан ПИ(ю)-41
# русский алфавит в нижнем регистре и пробел
BASE_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '

def shift_symbol(symbol: str, shift: int) -> str:
    num = BASE_ALPHABET.find(symbol)
    difference = num + shift - len(BASE_ALPHABET)
    if shift > 0 and difference >= 0:
        return BASE_ALPHABET[difference]
    if shift < 0 and difference < -len(BASE_ALPHABET):
        return BASE_ALPHABET[len(BASE_ALPHABET) + num + shift]
    return BASE_ALPHABET[num + shift]

def text_crypt(text: str, key: str, is_encrypt: bool = False) -> str:
    mode = 1 if is_encrypt else -1
    result = ''
    for i in range(len(text)):
        symbol = text[i]
        shift = (BASE_ALPHABET.find(key[i]) + 1) % len(BASE_ALPHABET)
        result += shift_symbol(symbol, mode * shift)
    return result

if __name__ == '__main__':
    print('Шифр Виженера. Только для русского алфавита + пробела\n')
    input_text = input('Введите сообщение: ')
    encrypt_key = input('Введите ключ: ')
    encrypt_key *= len(input_text) // len(encrypt_key) + 1 # увеличение ключа до размера сообщения
    print(f'Исходный текст: {input_text}')
    print(f'Ключ: {encrypt_key}\n')

    result = text_crypt(input_text, encrypt_key, is_encrypt=True)
    print(f'Зашифрованный текст: {result}\n')

    result = text_crypt(result, encrypt_key, is_encrypt=False)
    print(f'Расшифрованный текст: {result}')