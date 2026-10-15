import hashlib

# Prompt user for the flag
flag = input("Enter the flag: ")

# Compute SHA256 hash of the input
sha256_hash = hashlib.sha256(flag.encode()).hexdigest()

# Print the hash
print("SHA256 hash:", sha256_hash)