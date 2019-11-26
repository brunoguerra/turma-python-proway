a = [6,2,4,0,10,20,12,14,16,18]
b = [5,15,25,0,10,20]

a_dif = []
for item_a in a:
    if not item_a in b:
        a_dif.append(item_a)

print(a_dif)

a_dif_b_for_comprehensive = [item for item in a if item not in b]
print(a_dif_b_for_comprehensive)