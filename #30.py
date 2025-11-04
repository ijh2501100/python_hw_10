#30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
for subject, score in choi.items():
    if score >= 90:
        print(subject)