import binascii
import ecdsa
import random
from ecdsa import SigningKey, VerifyingKey

USERS = ["Alice", "Bob", "Charlie", "Dave"]

def sha256_2_string(string_to_hash):
    """ Returns the SHA256^2 hash of a given string input
    in hexadecimal format.

    Args:
        string_to_hash (str): Input string to hash twice

    Returns:
        str: Output of double-SHA256 encoded as hexadecimal string.
    """

    import hashlib
    first_sha = hashlib.sha256(string_to_hash.encode("utf8"))
    second_sha = hashlib.sha256(first_sha.digest())
    return second_sha.hexdigest()

def sign_message(message, sk, parity_bit):
    while True:
        signature = sk.sign(message.encode("utf-8"))
        hex_signature = signature.hex()
        sig_to_int = int(hex_signature, 16)
        if (sig_to_int % 2) == parity_bit:
            return hex_signature

def is_message_signed(message, hex_sig, secret_key_hex):
    # Decode signature to bytes, verify it
    try:
        signature = binascii.unhexlify(hex_sig)
        pk = SigningKey.from_string(binascii.unhexlify(secret_key_hex)).get_verifying_key()
    except binascii.Error:
        print("binascii error; invalid key")
        return False
    try:
        return pk.verify(signature, message.encode("utf-8"))
    except ecdsa.keys.BadSignatureError:
        print("signature error; invalid signature")
        return False

def verify_key(recovered_key_hex, challenge):
    for line in challenge.splitlines():
        line_challenge = line.split("; Signature: ")
        assert(len(line_challenge) == 2)
        message = line_challenge[0]
        signature = line_challenge[1]
        if not is_message_signed(message, signature, recovered_key_hex):
            return False
        print("Verified signature successfully")
    return True


def get_key_from_challenge(challenge):
    signature = []
    for line in challenge.splitlines():
        line_challenge = line.split("; Signature: ")
        assert (len(line_challenge) == 2)
        message = line_challenge[0]
        signature.append(line_challenge[1])
        # print(message, signature)

    binary_sig = []
    for sig in signature:
        binary_sig.append(bin(int(sig, 16))[2:].zfill(8))


    sec_key = []

    for sig in binary_sig:
        sec_key.append(sig[-1])
    sec_key = ''.join(sec_key)
    # print(sec_key)
    return hex(int(sec_key, 2))[2:]
    # TODO Problem 3 - Use this to reconstruct Rafael's Key


def test_code():
    # You can use this function to test your code
    challenge_text = open("challenge").read().strip()
    sk_hex = get_key_from_challenge(challenge_text)

    print(sk_hex)
    print(len(sk_hex))
    print(verify_key(sk_hex, challenge_text)) # should print True

test_code()
