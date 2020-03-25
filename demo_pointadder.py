import pyperclip
text = pyperclip.paste()

# TODO: separate lines and add stars
lines = text.split('\n')
val = []
for i, line in enumerate(lines):
    val.append('* ' + line)
text = '\n'.join(val)

pyperclip.copy(text)