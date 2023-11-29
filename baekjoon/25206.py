course_list = []
credit_sum = 0.0
grade_score_sum = 0.0
avar_result = 0.0
grade_score_adapter = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
    "P": 0.0
}

for i in range(0, 20):
    raw_input_str = input()
    input_array = raw_input_str.split(" ")
    course_list.append({
        "name": input_array[0],
        "credit": float(input_array[1]),
        "grade": input_array[2]
    })

for course in course_list:
    if course["grade"] == "P":
        pass
    else:
        credit_sum += course["credit"]
        grade_score_sum += (course["credit"] * grade_score_adapter[course["grade"]])

avar_result = grade_score_sum / credit_sum
print("{:.6f}".format(avar_result))
