import os

path = os.getcwd()
dirlist = os.listdir(path)

for dir in dirlist:
    if os.path.isdir(dir):
        i = 0
        for filename in os.listdir(os.path.join(path,dir)):
            if filename.endswith('.html'):
                os.rename(os.path.join(path, dir, filename),os.path.join(path, dir, (dir+str(i)+'.html')))
                i += 1
