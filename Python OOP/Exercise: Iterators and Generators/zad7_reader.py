def read_next(*args):
    for el in args:
        for sec_el in el:
            yield sec_el

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)