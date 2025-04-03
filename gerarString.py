#Gambiarra para colocar vários argumentos no windows

out = open("string.txt", "w", encoding="UTF-8")
x = range(35)
for i in x:
    out.write('''"magicparser ({0}).log" '''.format(i+1))