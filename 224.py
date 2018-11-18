def char_count(s,dic):
    for c in s:
        if not  c.isalpha():
            continue
        c = c.lower()
        dic[c] = dic.get(c,0) + 1


d1 = {}
char_count("Python is a programming language", d1)
print(d1)

char_count("想去爬山？去紫金山还是老山",d1)
print(d1["山"])