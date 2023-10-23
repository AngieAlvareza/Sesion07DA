def file_write(fname):
    with open(fname, "w") as myfile:
        myfile.write("Ejercicios Python\n")
        myfile.write("Ejercicios Java")

def file_read(fname):
    with open(fname, "r") as txt:
        print(txt.read())

file_write('abc.txt')
file_read('abc.txt')
