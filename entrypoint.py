import time

from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://kasucjusz:123@mongodbdarek-flxo2.mongodb.net/test?retryWrites=true&w=majority")


db = cluster["WirtualneMongoDB"]

#####################################   STUDENT
def create_student(first_name, last_name):
    post = {"first_name": first_name, "last_name": last_name}
    collection.insert_one(post)
    print(f"Created student {first_name} {last_name}")


def read_student(first_name, last_name):
    read = {"first_name": first_name, "last_name": last_name}
    print("Read student: " + collection.find_one(read))


def delete_user(first_name, last_name):
    delete = {"first_name": first_name, "last_name": last_name}
    collection.delete_one(delete)
    print(f"Deleted student {first_name} {last_name}")


def update_lastName_student(first_name, last_name):
    print("Insert new last nasme")
    new_last_name = input()
    newUpdate = {"$set": {"last_name": new_last_name}}
    update = {"first_name": first_name, "last_name": last_name}
    collection.update_one(update, newUpdate)
    print(f"Update student {first_name} {last_name}")


#####################################                   EMPOLOYEE

def create_employee(first_name, last_name, position):
    post = {"first_name": first_name, "last_name": last_name, "position": position}
    collection.insert_one(post)
    print(f"Created employee {first_name} {last_name} {position}")


def read_employee(first_name, last_name, position):
    read = {"first_name": first_name, "last_name": last_name, "postiion":position}
    print("Read employee: " + collection.find_one(read))


def delete_employee(first_name, last_name, position):
    delete = {"first_name": first_name, "last_name": last_name, "poistion":position}
    collection.delete_one(delete)
    print(f"Deleted employee {first_name} {last_name} {position}")

#####################################               SUBJECT

def create_subject(subject_name, max_number_of_participants, employee_id):
    t = time.localtime()
    created_date = time.strftime("%H:%M:%S", t)
    post = {"subject_name": subject_name, "max_number_of_participants": max_number_of_participants, "eployee_id":employee_id, "created_date":created_date}
    collection.insert_one(post)
    print(f"Created subject {subject_name} {max_number_of_participants} {employee_id}")


def delete_subject(subject_name, max_number_of_participants, employee_id):
    delete = {"first_name": first_name, "last_name": last_name}
    collection.delete_one(delete)
    print(f"Deleted student {first_name} {last_name}")


###########################CONSIOLE INPUT

print("Choose collection: 1 - Student, 2 - Employee, 3 - Subject")
colect = input()
if colect == "1":
    collection = db["Student"]
    print("Which actions would you like to take? 1 - Create, 2 - Read, 3 - update, 4 - delete")
    choose = input()
    print("Input name")
    first_name = input()
    print("Input last name")
    last_name = input()

    if choose == "1":
        create_student(first_name, last_name)
    elif choose == "2":
        read_student(first_name, last_name)
    elif choose == "3":
        update_lastName_student(first_name, last_name)
    elif choose == "4":
        delete_user(first_name, last_name)
if colect=="2":
    collection=db["Employee"]
    print("Which actions would you like to take? 1 - Create, 2 - Read,3 - delete")
    choose = input()
    print("Input name")
    first_name = input()
    print("Input last name")
    last_name = input()
    print("Input position")
    position=input()

    if choose == "1":
        create_employee(first_name, last_name, position)
    elif choose == "2":
        read_employee(first_name, last_name, position)
    elif choose == "3":
        delete_employee(first_name, last_name, position)

if colect=="3":
    collection=db["Subject"]
    print("Which actions would you like to take? 1 - Create")
    choose = input()
    print("subject_name")
    subject_name = input()
    print("max_number_of_participants")
    max_number_of_participants = input()
    print("employee_id")
    employee_id=input()

    if choose == "1":
        create_subject(subject_name, max_number_of_participants, employee_id)
