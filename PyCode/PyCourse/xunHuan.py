#for循环
tem_list=[36.5,37.5,38.5]
for temp in tem_list:
    print(temp)

tem_dict = {"001":36.5,"002":37.5,"003":38.5}
print(tem_dict.keys())
print(tem_dict.values())
print(tem_dict.items())

for id,temp in tem_dict.items():
    if temp>=38:
        print(id)

for i in range(5,10):
    print(i)

for n in range(1,10,2):
    print(n)

num=0
total=0
while num<5:
    total+=num
    num+=1
print(total)