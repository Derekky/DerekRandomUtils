# Workaround to include multiple arguments in Windows
# If it were Linux, I could simply write "filename*.log"

out = open("string.txt", "w", encoding="UTF-8")
x = range(35)
for i in x:
    out.write('''"filename ({0}).log" '''.format(i+1))