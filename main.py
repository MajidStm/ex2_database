
number_of_users = input("Enter number of Users:")
number_of_users = int(number_of_users)
dictionary_list =[]

for x in range (number_of_users):
    user_name= input("user.name:")
    user_age= input("user.age:")
    user_age = int(user_age)
    new_user_data = { "name":user_name ,"age": user_age}
    dictionary_list.append(new_user_data)

input_name = input("Enter name to search :")
data =next((x for x in dictionary_list if x["name"] == input_name ),None)  

if(data != None): print(data)
else : print("There is no user with given name !")
