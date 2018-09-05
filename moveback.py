import os, shutil

path = os.path.abspath('json/in')
arch = os.path.abspath('json/arch_in')
for root, dirs, files in os.walk(arch):
    for f in files:
        shutil.move(os.path.join(arch, f), os.path.join(path, f))
