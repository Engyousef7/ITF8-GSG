def main():
    user_name = input("Enter your name: ")
    age = input("Enter your age: ")
    Date_of_Birth = input("Enter your date of birth (YYYY-MM-DD): ")
    content = f"User Name: {user_name}\nAge: {age}\nDate of Birth: {Date_of_Birth}"
    file_name = "user_info.txt"
    with open(file_name, "w") as file:
        file.write(content)

    print(f"User information has been saved to {file_name}")

if __name__ == "__main__":
    main()