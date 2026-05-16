
# # 1

def add_contact():

    contacts = []

    while True:
        name = str(input("Enter your name: "))

        if len(name) == 0:
            print("Name input is empty: ")
        else:
            break

    while True:
        tel = str(input("Enter your phone number: "))

        if len(tel) == 0:
            print("Phone number input is empty: ")
        elif not tel.isdigit():
            print("Invalid input")
        elif len(tel) != 9:
            print("Invalid amount of numbers")
        else:
            break

    while True:

        mail = str(input("Enter your email address: "))

        if len(mail) == 0:
            print("Email input is empty : ")
        elif "@" not in mail or "." not in mail:
            print("Invalid email")
        else:
            break


    contacts.append(name)
    contacts.append(tel)
    contacts.append(mail)

    with open("contacts.txt", "a", encoding="utf-8") as file:
        file.write(f"Name: {name} | Telephone number: {tel} |Email: {mail}\n")

    print("Contact is successfully added")

# 2

def search_contact():

    while True:

        search_contact = input("Search for a name or phone number: ")
        file = open("contacts.txt", "r", encoding="utf-8")

        for line in file:
            if search_contact in line:
                print(line)
                return

        file.close()
        print("Contact not found")

# 3

def delete_contact():
    while True:

        delete_contact = input("Search for a name or phone number to delete: ")
        file = open("contacts.txt", "r", encoding="utf-8")
        lines = file.readlines()
        # сохраняет все строки файла пока он открыт
        file.close()

        new_file = []
        # создаем чтобы можно было сравнить длину file и new_file. Если меньше то выведем что контакт удален

        for line in lines:
            if delete_contact not in line:
                new_file.append(line)

        file = open("contacts.txt", "w", encoding="utf-8")
        for line in new_file:
            file.write(line)
        file.close()
        # записывает строки из new_file в файл. В new_file уже нет удаляемого контакта

        if len(lines) == len(new_file):
            print("Contact not found")
        else:
            print("Contact successfully deleted")
        break

# 4

def renew_contact():

    renew_contact = input("Enter name or phone number of renewal contact: ")
    file = open("contacts.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    for line in lines:

        if "Name: " + renew_contact in line or "Telephone number: " + renew_contact in line:
            name = input("Enter name of renewal contact: ")

            while True:
                tel = str(input("Enter phone number of renewal contact: "))

                if len(tel) == 0:
                    print("Phone number input is empty: ")
                elif not tel.isdigit():
                    print("Invalid input")
                elif len(tel) != 9:
                    print("Invalid amount of numbers")
                else:
                    break

            while True:

                mail = str(input("Enter email address of renewal contact: "))

                if len(mail) == 0:
                    print("Email input is empty : ")
                elif "@" not in mail or "." not in mail:
                    print("Invalid email")
                else:
                    break

            file = open("contacts.txt", "w", encoding="utf-8")

            for old_line in lines:
                if "Name: " + renew_contact in old_line or "Telephone number: " + renew_contact in old_line:
                    file.write("Name: " + name + " | Telephone number: " + tel + " | Email: " + mail + "\n")


                if renew_contact in old_line:
                    file.write("Name: " + name + " | Telephone number: " + tel + " | Email: " + mail + "\n")

                else:
                    file.write(old_line)

            file.close()

            print("Contact renewed successfully")
            break

    else:
        print("Contact not found")


# ЕПТА Я 3 ЧАСА БОРОЛАСЬ С ЭТИМ ОБНОВЛЕНИЕМ КОНТАКТА !!!!!!!!!!!!!

# 5

def show_contacts():

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines.sort()

    print(lines)

# проходимся по каждому контакту из списка и выводим их
    for contact in lines:
        print(contact.strip())

# obálka кода

while True:

    print("1 - Add a contact")
    print("2 - Search for a contact")
    print("3 - Delete contact")
    print("4 - Renew contact")
    print("5 - Show sorted contacts")
    print("6 - Exit")

    choice = input("Choose number from menu: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        renew_contact()

    elif choice == "5":
        show_contacts()

    elif choice == "6":
        print("Programme is over. See you soon!")

    else:
        print("Invalid menu option")