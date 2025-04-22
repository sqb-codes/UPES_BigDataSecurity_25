import hashlib

def compute_hash(data):
	# SHA - Secure Hash Algorithm - 256 bit
	# it generates fixed length 64-character hexadecimal string (256 bits)
	return hashlib.sha256(data.encode()).hexdigest()

orignal_data = "Transaction amount = $5000"
orignal_hash = compute_hash(orignal_data)

storage = {
	"data" : orignal_data,
	"hash" : orignal_hash
}

# create a validation check
def verify_integrity(stored_data, stored_hash):
	return compute_hash(stored_data) == stored_hash

print("Valid data :",verify_integrity(storage["data"], storage["hash"]))
print(storage["hash"])

# Tampering simulation
storage["data"] = "Transaction amount = $950000"
print("After Tampering :",verify_integrity(storage["data"], storage["hash"]))