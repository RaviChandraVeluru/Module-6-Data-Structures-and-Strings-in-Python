from idlelib.debugobj_r import StubObjectTreeItem

result = {"Harsha": 80, "Hari": 75, "Thasif": 30, "Lokesh": 89, "Ravi":92, "Alice":85}
search_student = input("Enter the Student's name: ")
if search_student in result:
    print(search_student + "\'s marks: ", result[search_student])
else:
    print("Student Not Found.")