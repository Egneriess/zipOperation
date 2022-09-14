import zipfile

path = input('Enter Path:')
savePath = input('Enter Decompression Path:')

try:
    z = zipfile.ZipFile(path, 'r')
    z.extractall(path=savePath)
    z.close()
except:
    print("Decompression Error")
else:
    print("Decompression Complete")
