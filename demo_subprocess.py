"""Usage
Specific to OS X (MacOS) and local configuration
"""
import subprocess

with open('hello.txt', 'w') as f:
    f.write('Hello from Subprocess!')

v = subprocess.Popen(['open','/System/Applications/Calendar.app'])
w = subprocess.Popen(['open', 'hello.txt'])
x = subprocess.Popen(['open','/Applications/R.app'])
y = subprocess.Popen(['/Users/samuel/.virtualenvs/py38/bin/python', '/Users/samuel/Documents/Work/corgi/boringstuff/demo_mapit.py', '-a', 'Park Royale Jl Gatot Subroto'])
z = subprocess.Popen(['open', '/System/Volumes/Data/usr/local/Cellar/python@3.8/3.8.1/IDLE 3.app'])
