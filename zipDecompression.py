import zipfile
import sys

def zipDecompression():
    if len(sys.argv) <= 1:
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
        finally:
            input()
    else:
        path = sys.argv[1]
        savePath = sys.argv[2]

        try:
            z = zipfile.ZipFile(path, 'r')
            z.extractall(path=savePath)
            z.close()
        except:
            print("Decompression Error")
        else:
            print("Decompression Complete")

if __name__ == "__main__":
    zipDecompression()
