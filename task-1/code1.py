import re
string = input("\nВведіть масив: ")
let = ''.join([i for i in string if not i.isdigit()]) 
a = re.findall(r'\d+', string) 
a = [int(i) for i in a]
if len(let) <2:
    print("\nРядок не містить букви")
else:
    print("\n Без чисел: ", let)
print("Числа:", a)
if len(a) == 0:
    print("Масив не містить числа, подальші операції не можуть бути проведені")
else:
    print("Максимальний елемент масиву:", max(a))
Let = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in let.split())
print("\nРядок з велики буквами:", Let)
numindex = [a[i]**i for i in range(0,len(a))] 
print("Масив чисел, піднесені до степеню по їх індексу:", numindex)
print("\n")
