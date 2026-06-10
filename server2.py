# Server2 šalje Serveru1 vreme poslednje izmene svog data.txt. Server1 proverava da li je njegov fajl noviji.
# Ako jeste, ispisuje poruku: „Server1 ima noviju verziju“. Ako nije, ispisuje „Server2 ima noviju verziju“ ili „Fajlovi su sinhronizovani“ ako je vreme isto.

import hashlib
import socket

def hashiranje(putanja):
    sha256 = hashlib.sha256()
    with open(putanja, "rb") as f:
        for blok in iter(lambda: f.read(4096), b""):
            sha256.update(blok)
    return sha256.hexdigest()

def main():
    moj_hash = hashiranje("data2.txt")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 5000))
    s.listen(1)

    print("Server2 ceka konekciju...")

    conn, addr = s.accept()
    print(f"Povezan sa {addr}")

    hash_server1 = conn.recv(1024).decode()

    conn.sendall(moj_hash.encode())

    conn.close()
    s.close()


if __name__ == "__main__":
    main()