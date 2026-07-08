"""Dictionaries (key-value pairs) and sets (unique, unordered collections)."""

user = {"name": "Davian", "role": "student", "active": True}

# Access, update, safe access with .get()
print(user["name"])
user["role"] = "contractor"
print(user.get("email", "no email on file"))

# Iterate keys, values, items
for key, value in user.items():
    print(f"{key} -> {value}")

# Sets: unique values, fast membership tests, set algebra
skills_a = {"python", "sql", "flutter"}
skills_b = {"python", "javascript"}

print(skills_a & skills_b)   # intersection
print(skills_a | skills_b)   # union
print(skills_a - skills_b)   # difference
print("sql" in skills_a)     # O(1) membership test

# dict.setdefault and defaultdict-style counting
word_counts = {}
for word in "the cat sat on the mat the cat ran".split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(word_counts)
