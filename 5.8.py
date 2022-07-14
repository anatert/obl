'''names = ['Admin', 'john', 'sara', 'brad']
if names:
    for name in names:
        if name.lower() == 'admin':
            print("Hello " + name + ", would you like to see a status report?")
        else:
            print("Hello " + name.title() + ", thank you for logging in again")
else:
    print("We need to find some users!")'''

'''current_users = ['John', 'sara', 'brandon', 'Nina', 'Ben']
lower_current_users = [user.lower() for user in current_users]

new_users = ['Nina', 'john', 'kurt', 'inna', 'arthur']
for user in new_users:
    if user.lower() in lower_current_users:
        print(user + 'Такое имя уже есть')
    else:
        print(user + ' Имя свободно')'''

numbers = [str(i) for i in range(1,10)]
for number in numbers:
  if number == "1":
      print(number + 'st')
  elif number == '2' or number == '3':
      print(number + 'nd')
  else:
      print(number + 'th')
