import hashlib
import time

data = input("Enter the data to hash: ").encode()


start_md5 = time.time()
md5_hash = hashlib.md5(data).hexdigest()
end_md5 = time.time()


start_sha = time.time()
sha256_hash = hashlib.sha256(data).hexdigest()
end_sha = time.time()

print("\n--- Hash Results ---")
print("Input Data:", data.decode())

print("\nMD5 Hash:")
print(md5_hash)
print("Length:", len(md5_hash), "characters")
print("Time Taken:", end_md5 - start_md5, "seconds")

print("\nSHA-256 Hash:")
print(sha256_hash)
print("Length:", len(sha256_hash), "characters")
print("Time Taken:", end_sha - start_sha, "seconds")