from abc import ABC, abstractmethod
import os

class GenericFile(ABC):
    @abstractmethod
    def get_path(self):
        pass



class TextAscii(GenericFile):

    def __init__(self,path):
        self.abs_path = path
        self.frecvente =0
        self.nume_fis_ascii =[]

    def get_path(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(self.abs_path))
        for root, subdirs, files in os.walk(ROOT_DIR):
            for file in os.listdir(root):
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    f = open(file_path, 'rb')
                    try:
                    # în content se va depune o listă de octeți
                        nrcar = 0
                        content = f.read()
                        nrcar = content.__len__()
                        ascii = 0
                        unicod = 0

                        for i in content:
                            if i<127 and i>9:
                                ascii+=1
                            if i==0:
                                unicod+=1
                        binar = nrcar - ascii - unicod
                        if(binar<ascii and ascii>unicod):
                            self.frecvente+=1
                            self.nume_fis_ascii.append(file_path.rsplit('/',1)[1])
                    finally:
                        f.close()
    def Print(self):
        print("Fisiere ASCII: ")
        for i in self.nume_fis_ascii:
            print(i)
        print("\nNr de fisiere ASCII: "+str(self.frecvente))
        print("\n===================================================\n")

class TextUnicod(GenericFile):

    def __init__(self,path):
        self.abs_path = path
        self.frecvente =0
        self.nume_fis_unicod =[]

    def get_path(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(self.abs_path))
        for root, subdirs, files in os.walk(ROOT_DIR):
            for file in os.listdir(root):
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    f = open(file_path, 'rb')
                    try:
                    # în content se va depune o listă de octeți
                        nrcar = 0
                        content = f.read()
                        nrcar = content.__len__()
                        unicod = 0

                        for i in content:
                            if i == 0:
                                unicod += 1
                        if (unicod / nrcar >= 0.3):
                            self.frecvente += 1
                            self.nume_fis_binar.append(file_path.rsplit('/', 1)[1])
                    finally:
                        f.close()

    def Print(self):
        print("Fisiere Unicod: ")
        for i in self.nume_fis_unicod:
            print(i)
        print("\nNr de fisiere unicod: "+str(self.frecvente))
        print("\n===================================================\n")

class TextBinar(GenericFile):

    def __init__(self,path):
        self.abs_path = path
        self.frecvente =0
        self.nume_fis_binar =[]

    def get_path(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(self.abs_path))
        for root, subdirs, files in os.walk(ROOT_DIR):
            for file in os.listdir(root):
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    f = open(file_path, 'rb')
                    try:
                    # în content se va depune o listă de octeți
                        nrcar = 0
                        content = f.read()
                        nrcar = content.__len__()
                        unicod = 0
                        frecvente = {}
                        for i in content:
                            if i not in frecvente:
                                frecvente[i] = 1
                            else:
                                frecvente[i] = frecvente[i]+1
                        toleranta = 0.1
                        ok = True
                        for i in frecvente:
                            if (frecvente[i]/nrcar > toleranta):
                                ok = False
                        if (ok == True):
                            self.frecvente += 1
                            self.nume_fis_binar.append(file_path.rsplit('/', 1)[1])
                    finally:
                        f.close()

    def Print(self):
        print("Fisiere binar: ")
        for i in self.nume_fis_binar:
            print(i)
        print("\nNr de fisiere binar: "+str(self.frecvente))
        print("\n===================================================\n")



if __name__=='__main__':
    path = "/home/student/Desktop/Resurse/graalvm-ce-java19-22.3.1/conf/security/policy/"
    ASCII = TextAscii(path)
    ASCII.get_path()
    ASCII.Print()

    Unicod = TextUnicod(path)
    Unicod.get_path()
    Unicod.Print()

    Binar = TextBinar(path)
    Binar.get_path()
    Binar.Print()