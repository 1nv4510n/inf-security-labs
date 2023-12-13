# Шифр RSA, Савин Богдан ПИ(ю)-41
import random
import secrets
from math import sqrt

DEFAULT_BIT_LENGTH = 4

def get_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

def mod_inverse(a: int, m: int) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def isprime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

def generate_keypair(p: int, q: int, keysize: int) -> tuple:
    n_min = 1 << (keysize - 1)
    n_max = (1 << keysize) - 1
    primes = [2]
    start = 1 << (keysize // 2 - 1)
    stop = 1 << (keysize // 2 + 1)

    if start >= stop:
        return []

    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)

    while (primes and primes[0] < start):
        del primes[0]

    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if n_min <= p * q <= n_max]
        if q_values:
            q = random.choice(q_values)
            break
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = get_gcd(e, phi)

    while True:
        e = random.randrange(1, phi)
        g = get_gcd(e, phi)
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break
    return ((e, n), (d, n))

def encrypt_message(message: str, package: tuple) -> str:
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in message]
    return msg_ciphertext

def decrypt_message(message: str, package: tuple) -> str:
    d, n = package
    msg_plaintext = [chr(pow(c, d, n)) for c in message]
    return ''.join(msg_plaintext)

if __name__ == "__main__":
    print('Шифр RSA')
    bit_length = DEFAULT_BIT_LENGTH
    print(f'Количество бит: {DEFAULT_BIT_LENGTH}')
    p = secrets.randbits(512)
    q = secrets.randbits(512)
    public, private = generate_keypair(
        p, q, 2**bit_length)
    
    print(f'Ваш публичый ключ: {public}')
    print(f'Ваш приватный ключ: {private}')
    print('=' * 10)

    message = input("Введите сообщение: ")
    print([ord(c) for c in message])

    encrypted_msg = encrypt_message(message, public)
    print("Результат работы шифра:")
    print(''.join([str(i) for i in encrypted_msg]))

    print("Результат дешифровки: ")
    print(decrypt_message(encrypted_msg, private))