import hashlib

def sha256_hash(data): # Calculate the SHA-256 hash of an object
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()