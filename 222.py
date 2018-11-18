def print_them(math,phys,chem,**others):
    form1 = "{:6}{}"
    print(form1.format("math:",math))
    print(form1.format("phys:",phys))
    print(form1.format("chem:",chem))
    print("other:",others)

uni = {"chem":336,"math":114,"phys":247,"bio":234}

print_them(**uni)