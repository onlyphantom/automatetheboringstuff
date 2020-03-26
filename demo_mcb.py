"""Example Usage:
- ig: instagram.com/officialsamuel/
- fb: fb.com/onlyphantom
- github: github.com/onlyphantom
1. To save current clipboard content to a key called 'book'
    - python demo_mcb.pyw -s 'fb'
2. To print all stored keys
    - python demo_mcb.pyw -l
3. To retrieve stored content by key (into clipboard)
    - python demo_mcb.pyw -k 'fb'
5. To delete stored content by key
    - python demo_mcb.pyw -d 'fb'
4. To delete all stored keys and their content
    - python demo_mcb.pyw -d
"""

import shelve, pyperclip, argparse

parser = argparse.ArgumentParser(prog="Multiclipboard", description="Saves and loads pieces of text to the clipboard.")
g = parser.add_mutually_exclusive_group()
g.add_argument('-l', '--list', default=False, action="store_true", help='List all keywords')
g.add_argument('-s', '--save', help='Saves clipboard to keyword')
g.add_argument('-k', '--keyword', help='Loads keyword to clipboard')
g.add_argument('-d', '--delete', nargs='?', const=' ', help="Delete keyword or keywords")
args = vars(parser.parse_args())

with shelve.open('mcb', 'c') as mcb:
    if args['list']:
        print(str(list(mcb.keys())))
    elif args['save'] is not None:
        mcb[args['save']] = pyperclip.paste()
    elif args['keyword'] is not None:
        pyperclip.copy(mcb[args['keyword']])
    else:
        if args['delete'] == ' ':
            mcb.clear()
        else:
            mcb.pop(args['delete'], None)
