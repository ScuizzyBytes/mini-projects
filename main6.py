# 1 - copy()
people: list[str] =  ['misha', 'araik', 'eblan']
copy_people: list[str] = people.copy()
copy_people.remove('araik')

print(people)
print(copy_people)

# 2 - count()
people1: list[str] = ['Mario', 'Araik', 'Araik']
copys = people.count('Araik')

print(copys)

# 3 - extend()
people2: list[str] = ['Mario', 'Araik', 'Araik']
extend_people: list[str] = ['apple', 'orange']

people.extend(extend_people)

print(people)

# 4 - insert()
people4: list[str] = [1, 2, 3, 4, 5]
people4.insert(0, 0)

print(people4)

people5: list[str] = ['Mario', 'Araik', 'Araik']
people5.pop(0)

print(people5)

# 5 - remove()
people6: list[str] = ['Mario', 'Araik', 'Araik']
people6.remove('Mario')

print(people6)

# 6 - reverse()
people7: list[str] = ['Mario', 'Araik', 'Araik']
people7.reverse()

print(people7)

# 7 - sort()
people8: list[str] = ['Maadario', 'araik', 'Ratmir', 'Misha', 'dima']
people8.sort(key=lambda name: name.lower())

print(people8)



