group_counter = int(input())
total_People = 0

musala_expedition = 0
monblan_expedition = 0
kilimandjaro_expedition = 0
k2_expedition = 0
everest_expedition = 0

musala_percent = 0
monblan_percent = 0
kilimandjaro_percent = 0
k2_percent = 0
everest_percent = 0

for x in range(group_counter):
    each_group_count = int(input())

    total_People += each_group_count

    if each_group_count <= 5:
        musala_expedition += each_group_count

    elif each_group_count > 5 and each_group_count <= 12:
        monblan_expedition += each_group_count

    elif each_group_count > 12 and each_group_count <= 25:
        kilimandjaro_expedition += each_group_count

    elif each_group_count > 25 and each_group_count <= 40:
        k2_expedition += each_group_count

    elif each_group_count > 40:
        everest_expedition += each_group_count


musala_percent = (musala_expedition / total_People) * 100
monblan_percent = (monblan_expedition / total_People) * 100
kilimandjaro_percent = (kilimandjaro_expedition / total_People) * 100
k2_percent = (k2_expedition / total_People) * 100
everest_percent = (everest_expedition / total_People) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
