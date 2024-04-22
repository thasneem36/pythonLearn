list = []
for i in range(1,6):
    user = int(input(f"enter the data {i} "))
    list.append(user)
    
sum_list=sum(list)
print(f"Sum of your intger data {sum_list}")
print(f"Averge of your intger data {sum_list/len(list)}")