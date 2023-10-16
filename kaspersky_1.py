s = input().split()
s_out = []

n = int(input())

data = [input().lower() for i in range(n)]

prep = '.,;:!?'

#print(s)
#print(data)

for i in s:
    i = i.lower()
    if i[-1] in prep:
        if i[0:-1] in data:
            s_out.append("." * len(i))
        else:
            s_out.append("~" * len(i[0:-1]) + ".")
    elif i in data:
        s_out.append("." * len(i))
    else:
        s_out.append("~" * len(i))

print(" ".join(s))
print(".".join(s_out))
# print("~~~...~~...............~~~.~~~~~~~~~.~~........")
