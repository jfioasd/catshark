import sys

prog = open(sys.argv[1]).read()

A, B = 0, 0
ptr = 0
while 1:
    if prog[ptr] == 'i':
        A += 1
    elif prog[ptr] == 'd':
        ptr += (A == 0)
        A -= (A != 0)
    elif prog[ptr] == 's':
        A, B = B, A
    elif prog[ptr] == 'o':
        print(A, B)

    elif prog[ptr] == 'h': # Debug instruction
        break

    ptr = (ptr+1) % len(prog)
