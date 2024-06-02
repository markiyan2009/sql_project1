from courses import Course
from students import Student
from connection import Connect
student = Student()
course = Course()
connect = Connect()
while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Видалити студента")
    print("6. Видалити курс")
    print("7. Зареєструвати студента на курс")
    print("8. Показати студентів на конкретному курсі")
    print("9. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Ім'я:")
        age = int(input("Вік:"))
        major = input("Опис:")
        student.add_student(name,age,major)
        print("Студента успішно додано")

    elif choice == "2":
        name = input("Назва:")
        instruction = input("Опис:")
        course.add_course(name,instruction)
        print("Курс успішно додано")

    elif choice == "3":
        print(student.get_students())
     
    elif choice == "4":
        print(course.get_courses())
    elif choice == "5":
        id = int(input("ID:"))
        student.delete_user(id)

    elif choice == "6":
        id = int(input("ID:"))
        course.delete_course(id)
        # Показати студентів на конкретному курсі
        id_student = int(input("ID студента:"))
        id_course = int(input("ID курсів:"))
        connect.add_conn(id_student,id_course)
    elif choice == "7":
        id_student = int(input("ID студента:"))
        id_course = int(input("ID курсу:"))
        
        connect.add_conn(id_student,id_course)
    elif choice == "8":
        id_course = int(input("ID курсу:"))
        connect.show_connection_by_course(id_course)

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")