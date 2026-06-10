# Server2 šalje Serveru1 vreme poslednje izmene svog data.txt. Server1 proverava da li je njegov fajl noviji.
# Ako jeste, ispisuje poruku: „Server1 ima noviju verziju“. Ako nije, ispisuje „Server2 ima noviju verziju“ ili „Fajlovi su sinhronizovani“ ako je vreme isto.

#prvo se pokrece server2 pa server1

import os
import socket

def vreme_izmene(putanja):
    return os.path.getmtime(putanja)

def main():
    moje_vreme = vreme_izmene("data1.txt")
    # moje_vreme = vreme_izmene("data2.txt") # ovde ce biti sinhronizovani

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 5000))

    s.sendall(str(moje_vreme).encode())

    vreme_server2 = float(s.recv(1024).decode())

    if moje_vreme > vreme_server2:
        print("Server1 ima noviju verziju")
    elif moje_vreme < vreme_server2:
        print("Server2 ima noviju verziju")
    else:
        print("Fajlovi su sinhronizovani")

    s.close()

if __name__ == "__main__":
    main()