FILENAME = "./classwork_analysis.txt"

"""
def create_dict(filename):
    student_dict = dict()
    with open(filename) as file:
        file_content = file.read()
        collections = file_content.split("\n*****\n");
        for index in range(len(collections) - 1): # minus 1 because the last element will always be a list with an empty string
            student_message_list = collections[index].split("\n")
            student = student_message_list[0]
            student_dict[student] = student_message_list[1:]
    return student_dict
"""

def create_dict(filename):
    student_dict = dict()
    with open(filename) as file:
        file_content = file.read()
        collections = file_content.split("\n*****\n");
        for index in range(len(collections) - 1): # minus 1 because the last element will always be a list with an empty string
            student_message_list = collections[index].split("\n")
            student = student_message_list[0]
            student_dict[student] = len(student_message_list) - 1
    return student_dict

def get_max_and_avg(a_dict):
    max = 0
    sum = 0
    for student in a_dict:
        count = a_dict[student]
        sum += count
        if count > max:
            max = count
    return max, sum // len(a_dict)

def print_students_dict(a_dict):
    for student in a_dict:
        print(student, ": ", a_dict[student], sep="")

def main():
    a_dict = create_dict(FILENAME)
    print_students_dict(a_dict)
    print("\nMax:", get_max_and_avg(a_dict)[0])
    print("Avg:", get_max_and_avg(a_dict)[1])

if __name__ == "__main__":
    main()