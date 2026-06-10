# Server2 šalje Serveru1 vreme poslednje izmene svog data.txt. Server1 proverava da li je njegov fajl noviji.
# Ako jeste, ispisuje poruku: „Server1 ima noviju verziju“. Ako nije, ispisuje „Server2 ima noviju verziju“ ili „Fajlovi su sinhronizovani“ ako je vreme isto.

import os
import socket

def vreme_izmene(putanja):
    return os.path.getmtime(putanja)

def main():
    moje_vreme = vreme_izmene("data2.txt")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 5000))
    s.listen(1)

    print("Server2 ceka konekciju...")

    conn, addr = s.accept()
    print(f"Povezan sa {addr}")

    vreme_server1 = float(conn.recv(1024).decode())

    conn.sendall(str(moje_vreme).encode())

    conn.close()
    s.close()


if __name__ == "__main__":
    main()