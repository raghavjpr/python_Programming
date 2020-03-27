import operator
STUDENT_NAMES = ('sunil', 'Ishan', 'Raghav', 'Billy', 'Mat')
STUDENT_MATH_MARKS = (19, 18, 20, 10, 9)
STUDENT_CHEMISTRY_MARKS = (17, 19, 0, 10, 15)

STUDENT_COUNT = len(STUDENT_NAMES)

summary = []
for i in range(0, STUDENT_COUNT):
  total = STUDENT_MATH_MARKS[i] + STUDENT_CHEMISTRY_MARKS[i]
  summary.append((STUDENT_NAMES[i], total))

a = sorted(summary, key = operator.itemgetter(1), reverse= True)
for k in a:
  print(k[0], k[1])
