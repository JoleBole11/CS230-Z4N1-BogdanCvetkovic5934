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
    moj_hash = hashiranje("data1.txt")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 5000))

    s.sendall(moj_hash.encode())

    hash_server2 = s.recv(1024).decode()

    if moj_hash >= hash_server2:
        print("Server1 ima noviju verziju")
    elif moj_hash <= hash_server2:
        print("Server2 ima noviju verziju")
    else:
        print("Fajlovi nisu identični")

    s.close()

if __name__ == "__main__":
    main()