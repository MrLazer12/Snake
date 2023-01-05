import os, shutil, time
print("Drag and drop your file here")
pyPath = input()
print("Drag and drop your icon here")
ico = input()
os.system(f'pyinstaller "{pyPath}" --icon "{ico}" --onefile')

time.sleep(0.2)
os.remove("main.spec")#stergerea fail cu setari pentru convertirea in exe
shutil.rmtree("build")#stergerea mapa build generata, care contine failuri pentru convertirea in exe

print("SuccesfuIIy created your exe!")