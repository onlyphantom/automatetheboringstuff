import argparse, pyperclip

PASSWORDS = {
    'fb': 'fb01KHFhTxFtjVB6',
    'gmail': 'gmailQyKAxiVtjV',
    'luggage': 43210
}

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--account')
args = vars(parser.parse_args())
print(args)

def retri(account):
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print("Password for " + account + ' copied to clipboard.')
    else:
        print('No account named ', account)

if __name__ == '__main__':
    retri(args['account'])
