"""Control flow: conditionals and loops."""

score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} -> grade {grade}")

# for loop over a range and over an iterable
for i in range(3):
    print("range i:", i)

for ch in "abc":
    print("char:", ch)

# while loop with break/continue
n = 0
while True:
    n += 1
    if n % 2 == 0:
        continue        # skip even numbers
    if n > 7:
        break            # stop the loop entirely
    print("odd n:", n)

# for/else: the else clause runs only if the loop was NOT broken out of
for i in range(5):
    if i == 10:
        break
else:
    print("loop finished without break")
