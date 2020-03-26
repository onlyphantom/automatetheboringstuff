"""Example usage
1. Passing Address: python demo_mapit.py -a 'Park+Royale+Jl.+Gatot+Subroto'
2. Use clipboard values: python demo_mapit.py 
"""
import webbrowser, argparse, pyperclip
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address')
args = vars(parser.parse_args())

address = args['address'] or pyperclip.paste()
uri = f'https://www.google.com/maps/place/{address}'
print("URI:", uri)

webbrowser.open(uri)