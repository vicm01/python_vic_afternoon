from main import Teacher


try:
    teacher_name = input("Enter name \n")
    teacher_email = input("Enter email \n")
    teacher_password = input("Enter password \n")

    Teacher.create(teach_name = teacher_name, teach_email = teacher_email, teach_password = teacher_password )
    print("Product Generated Successfully")
except:
    print("Failed to generate product")

