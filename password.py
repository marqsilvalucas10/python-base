#! /usr/bin/env python3

import sys, pyperclip
passwords = {'email':'jugue123',
        'faicebuqui':'jumento123',
        'insta':'caqui123'
        }

if len(sys.argv) < 2:
    print("Falta argumentos.")
    sys.exit()


account = sys.argv[1]
print("Escrito: "+account)
if account in passwords:
    pyperclip.copy(passwords[account])
    print(f'password for {account} copied to clipboard')
else:
    print(f'There is no account named {account}')

