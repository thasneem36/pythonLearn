#number or string type anything divide every single letter and store a list attribute

store_num = []
store_str = []

num_data = ["1","2","3","4","5","6","7","8","9","0"]

#select option 
print("Enter the multipule data < 1 >\nEnter the one data < 2 >")
input_option = input("< 1 > OR < 2 > - ")
print("< ",input_option," >")
print("============")

if input_option == "1":
    
    input_type = input("::) ")
    for i in input_type:
    
        if i in num_data:
            con_int=int(i)
            store_num.append(con_int)
    
        else:
            con_str=str(i)
            store_str.append(con_str)

else:
    while True:
        
        input_type = input("::) ")
        if input_type == "":
            break
        
        for i in input_type:
    
            if i in num_data:
                con_int=int(i)
                store_num.append(con_int)
    
            else:
                con_str=str(i)
                store_str.append(con_str)
        
    
    

#output of y
print()
print("show of your input :) ",input_type)
print()

#filter the word
print("the filter of your word as a string :) ",store_str)
print()
print("the filter of your word as a integer or Number :) ",store_num)
print()
        
        