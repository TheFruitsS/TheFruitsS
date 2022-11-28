from os import path

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

fil = StrPath('/home/dimitarvili/Downloads/VioletaProjects/Python OOP/Exercise: Iterators and Generators/testgen.csv')
csvgen = csv_reader(fil)