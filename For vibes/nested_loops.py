# niet zelf gedaan!
scores = [
    [45, 67, 88],   
    [90, 53, 77],   
    [100, 82, 61]   
]

student_score_labels = []

for i, student in enumerate(scores, start=1):
    per_student = []
    print(f"Student {i}:")
    for cijfer in student:
        match cijfer:
            case s if 0 <= s <= 50:
                label = "slecht"
            case s if 51 <= s <= 70:
                label = "voldoende"
            case s if 71 <= s <= 90:
                label = "goed"
            case s if 91 <= s <= 100:
                label = "uitmuntend"
        print(f"Student {i}:")
        per_student.append(label)
        print(f"  Score {cijfer}: {label}")
    student_score_labels.append(per_student)

# optioneel: print de labels per student als lijst
print("\nLabels per student:", student_score_labels)
