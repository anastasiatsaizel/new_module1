def get_name():
    while True:
        name = input("Enter your name: ")

        if not name:
            print("Name input is empty")
        else:
            return name


def get_phone():
    while True:
        tel = input("Enter your phone number: ")

        if not tel:
            print("Phone number input is empty")

        elif not tel.isdigit():
            print("Invalid input")

        elif len(tel) != 9:
            print("Invalid amount of numbers")

        else:
            return tel


def get_email():
    while True:
        mail = input("Enter your email address: ")

        if not mail:
            print("Email input is empty")

        elif "@" not in mail or "." not in mail:
            print("Invalid email")

        else:
            return mail

# # 1

def add_contact():

    name = get_name()
    tel = get_phone()
    mail = get_email()

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

    search = input("Enter name or phone number of renewal contact: ")

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    found = False
    # пока что мы не нашли нужный контакт

    with open("contacts.txt", "w", encoding="utf-8") as file:

        for line in lines:

            if search in line:
                name = get_name()
                tel = get_phone()
                mail = get_email()

                file.write(f"Name: {name} | Telephone number: {tel} |Email: {mail}\n")
                found = True

            else:
                file.write(line)

    if found:
        print("Contact updated")
    else:
        print("Contact not found")

# 5

def show_contacts():

    with open("contacts.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines.sort()

    print(lines)

# проходимся по каждому контакту из списка и выводим их
    for contact in lines:
        print(contact.strip())

# obálka кода - main
def main():

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
            break

        else:
            print("Invalid option")

main()