def main():
    student_info = {"name":"Bob", "age":"20", "grade":"A"}

    print(student_info["age"])

    student_info["grade"] = "A+"
    
    if student_info["gender"]:
        return True
    else:
        return False

    del student_info["age"]

main()