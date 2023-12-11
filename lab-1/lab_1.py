# Шифр Цезаря, Савин Богдан ПИ(ю)-41
# русский, английский алфавит в нижнем регистре и пробел
BASE_ALPHABET = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя '

def shift_symbol(symbol: str, shift: int) -> str:
    num = BASE_ALPHABET.find(symbol)
    difference = num + shift - len(BASE_ALPHABET)
    if shift > 0 and difference >= 0:
        return BASE_ALPHABET[difference]
    if shift < 0 and difference < -len(BASE_ALPHABET):
        return BASE_ALPHABET[len(BASE_ALPHABET) + num + shift]
    return BASE_ALPHABET[num + shift]

if __name__ == '__main__':
    print('Шифр Цезаря для русского и английского алфавитов + пробел')
    n = input('Выберите сдвиг (по умолчанию -3): ')
    if n == "": n = -3 
    n = int(n)
    input_text = input('Введите сообщение: ')
    
    print(f'Исходный текст: {input_text}')
    print(f'Сдвиг: {n}\n')
    encrypted_text = ''
    # ENCRYPT
    for symbol in input_text:
        encrypted_text += shift_symbol(symbol, n)
    print(f'Зашифрованный текст: {encrypted_text}\n')

    # DECRYPT
    decrypted_text = ''
    for symbol in encrypted_text:
        decrypted_text += shift_symbol(symbol, -n)
    print(f'Расшифрованный текст: {decrypted_text}')