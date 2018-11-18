def print_data(x, **dic):
    print(x)
    for k,v in dic.items():
        print("{:6}{}".format(str(k) + ":",v))

print_data("PKU:",math = 114, phys = 247 , chem = 336, bio = 361)