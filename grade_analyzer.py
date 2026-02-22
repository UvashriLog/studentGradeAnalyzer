def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages


def classify_grades(averages):
    classified = {}

    for name, avg in averages.items():
        if avg >= 90:
            grade = "A"
        elif 75 <= avg <= 89:
            grade = "B"
        elif 60 <= avg <= 74:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")

    passed = 0
    total = len(classified)

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1

        print(f"{name:<10} | Avg: {avg:<6} | Grade: {grade} | Status: {status}")

    failed = total - passed

    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


# ===== Main Block =====
if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 78, 92],   # 86.25 → B
        "Bob": [70, 75, 65, 80],     # 72.5  → C
        "Clara": [95, 98, 94, 98]    # 96.25 → A
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)