
# This tutorial is already done in lesson 3
# You can copy and paste the completed signature module

"""Asymmetric Cryptography -> Digital Signature: Tutorial 4

The goal of this tutorial is to learn how to sign and verify messages using asymmetric keys.
In this implementation the passed message as an argument is a string that needs to be converted to a byte object.
When signing a message the RSA sign-function requires a specific hash like SHA256, and padding such as PSS.
Be aware that verification must use the same algorithms values to correctly verify the signature.

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run the test of this tutorial located in same folder.

To test run 'Signature_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on this topic:
    https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
"""

from cryptography.exceptions import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keys():
    private = rsa.generate_private_key(65537, 2048)
    public = private.public_key()
    return private, public

def sign(message, private_key):
    return private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False