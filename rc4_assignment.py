def ksa(key):
    # Khởi tạo mảng S từ 0 đến 9
    S = list(range(10))
    j = 0
    for i in range(10):
        j = (j + S[i] + key[i % len(key)]) % 10
        S[i], S[j] = S[j], S[i]
    return S


def prga(S, length):
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 10
        j = (j + S[i]) % 10
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 10
        keystream.append(S[t])
    return keystream


def main():
    K = [2, 4, 1, 7]
    text = "cybersecurity"

    # 1. Khởi tạo KSA
    S = ksa(K)
    print(f"Mảng S sau KSA: {S}")

    # 2. Tạo dòng khóa PRGA
    keystream = prga(S, len(text))
    print(f"Dòng khóa (Keystream) cho {len(text)} ký tự: {keystream}")

    # 3. Mã hóa (XOR)
    cipher = []
    print("\nChi tiết mã hóa:")
    for i in range(len(text)):
        m_t = ord(text[i])  # Lấy mã ASCII
        k_t = keystream[i]
        c_t = m_t ^ k_t  # Phép XOR bitwise
        cipher.append(c_t)
        print(f"Ký tự '{text[i]}' (ASCII: {m_t}) XOR {k_t} = {c_t}")

    print(f"\nBản mã C(t) cuối cùng (Decimal): {cipher}")


if __name__ == "__main__":
    main()