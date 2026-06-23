import hashlib

def calculate_sha256(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("File not found!")
        return None


filename = input("Enter file name: ")

original_hash = calculate_sha256(filename)

if original_hash:
    print("\nOriginal SHA-256 Hash:")
    print(original_hash)

    print("\nNow modify the file slightly and save it.")
    input("Press Enter after modifying the file...")

    modified_hash = calculate_sha256(filename)

    print("\nModified SHA-256 Hash:")
    print(modified_hash)

    if original_hash == modified_hash:
        print("\nFile Integrity Status: File is unchanged.")
    else:
        print("\nFile Integrity Status: TAMPERING DETECTED!")