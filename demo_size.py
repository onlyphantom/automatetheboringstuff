import os

totalSize = 0
par = os.getcwd()
print(par)
allfiles = os.listdir(par)
for f in allfiles:
    totalSize += os.path.getsize(os.path.join(par, f))

print(totalSize)