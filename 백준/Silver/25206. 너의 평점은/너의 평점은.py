total_credit = 0
total_score = 0
for _ in range(20):
    subject, credit, score = map(str, input().split())
    credit = float(credit)
    if score == 'P':
        continue
    total_credit += credit
    if score == 'A+':
        total_score += (4.5*credit)
    elif score == 'A0':
        total_score += (4*credit)
    elif score == 'B+':
        total_score += (3.5*credit)
    elif score == 'B0':
        total_score += (3*credit)
    elif score == 'C+':
        total_score += (2.5*credit)
    elif score == 'C0':
        total_score += (2*credit)
    elif score == 'D+':
        total_score += (1.5*credit)
    elif score == 'D0':
        total_score += (1*credit)
print(total_score / total_credit)
