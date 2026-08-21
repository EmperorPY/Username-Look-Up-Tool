import requests


def menu():
    print("\nUSERNAME LOOKUP TOOL\n")
    print("1. Minecraft")
    print("2. GitHub")
    print("3. Exit")

    choice = input("> ").strip()
    return choice


while True:

    choice = menu()

    if choice == "1":

        username = input("Enter Minecraft username: ").strip()

        minecraft_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"

        response = requests.get(minecraft_url)

        if response.status_code == 200:
            data = response.json()

            print("User found - cannot use this username!\n")
            print(f"Username: {data['name']}\n")
            print(f"UUID: {data['id']}\n")

        else:
            print("User not found - Username is available!\n")

    elif choice == "2":

        username = input("Enter GitHub username: ").strip()

        github_url = f"https://api.github.com/users/{username}"

        response = requests.get(github_url)

        if response.status_code == 200:
            data = response.json()

            print("User found - cannot use this username!")
            print(f"Username: {data['login']}\n")
            print(f"ID: {data['id']}\n")
            print(f"Avatar URL: {data['avatar_url']}\n")
            print(f"Profile URL: {data['html_url']}\n")

        else:
            print("User not found - Username is available!\n")

    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid choice!")
        continue