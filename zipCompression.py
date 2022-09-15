import zipfile
import sys

def zipCompression():
    if len(sys.argv) <= 1:
        path = input('Enter Path:')
        file = []
        f = ""
        while f != '/s':
            f = input('Enter File Path(Enter "/s" Stop):')
            file.append(f)
            z = zipfile.ZipFile(path, 'w', zipfile.ZIP_STORED)
        try:
            for i in file:
                z.write(i)
            z.close()
        except:
            print("Compression Error")
        else:
            print("Compression Complete")
        finally:
            z.close()
            input()
    else:
        path = sys.argv[1]
        file = sys.argv[2:len(sys.argv)]
        z = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
        try:
            for i in file:
                z.write(i)
        except:
            print("Compression Error")
        else:
            print("Compression Complete")
        finally:
            z.close()

if __name__ == "__main__":
    zipCompression()
