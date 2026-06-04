"""Why you NEVER store plaintext passwords, and how bcrypt hashing works."""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "correct horse battery staple"

# Hashing is one-way and salted - the same password hashes differently
# every time, and you can never recover the original from the hash.
hash1 = pwd_context.hash(password)
hash2 = pwd_context.hash(password)
print("hash 1:", hash1)
print("hash 2:", hash2)
print("hashes differ even for the same password:", hash1 != hash2)

# Verification checks a plaintext attempt against a stored hash
print("correct password verifies:", pwd_context.verify(password, hash1))
print("wrong password fails:", pwd_context.verify("wrong password", hash1))
