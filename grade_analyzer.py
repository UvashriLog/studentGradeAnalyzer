def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages


def classify_grades(averages):
    # Grading thresholds (local variables)
    A_threshold = 90
    B_threshold = 75
    C_threshold = 60

    classified = {}
    for name, avg in averages.items():
        if avg >= A_threshold:
            grade = "A"
        elif avg >= B_threshold:
            grade = "B"
        elif avg >= C_threshold:
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
        "Alice": [85, 90, 78, 92],
        "Bob": [70, 75, 65, 80],      # Adjusted scores (now passes)
        "Clara": [95, 98, 94, 98]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)