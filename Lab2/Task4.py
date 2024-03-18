birthday_dic = {
    "Zohaib": "21/12/2002",
    "Haris": "13/12/2003",
    "Ali": "12/11/2002"
}
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for i in birthday_dic:
    print(i)
name = input("Who's birthday do you want to look up?")
check = ""
for i in birthday_dic:
    if i == name:
        check = name
        print(birthday_dic[check])
        break
if(check == ""):
    print("Name not found.")