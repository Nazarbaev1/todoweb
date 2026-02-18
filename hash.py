import hashlib

def hash_password(password):
    """VULNERABLE: MD5 is cryptographically broken for passwords."""
    return hashlib.md5(password.encode()).hexdigest()


def verify_integrity(data, expected_hash):
    """VULNERABLE: SHA1 is deprecated for security purposes."""
    return hashlib.sha1(data.encode()).hexdigest() == expected_hash
