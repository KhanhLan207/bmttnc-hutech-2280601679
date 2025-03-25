
from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhap dữ liệu cần hash: ").encode('utf-8')
    hash_value = sha3(text)

    print("Chuỗi văn bản:", text.decode('utf-8'))
    print("Hash sha3-256:", hash_value.hex())

if __name__ == "__main__":
    main()
