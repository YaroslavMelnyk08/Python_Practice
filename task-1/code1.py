import re

string = input("\nВведіть щось: ")

let = ''.join([i for i in string if not i.isdigit()]) 

nums = re.findall(r'\d+', string) 
nums = [int(i) for i in nums] 

print("\nРядок без чисел:", let)
print("Масив чисел:", nums)

Let = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in let.split()) 
print("\nЗмінений рядок:", Let)
print("Максимальний елемент масиву:", max(nums)) 

nums.remove(max(nums)) 
numindex = [nums[i]**i for i in range(0,len(nums))]
print("Масив чисел, піднесені до степеню по їх індексу:", numindex)
print("\n")
