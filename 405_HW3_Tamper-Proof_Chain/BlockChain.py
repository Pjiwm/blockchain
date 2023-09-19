#!/usr/bin/env python3
"""Block Integrity -> Tamper Proof Chain: Homework

The goal of this homework is to extend the behavior of a block to created a chain and securely link
them together using cryptography. In general, each block is used to hold a batch of transactions. In addition a cryptographic
hash of the previous block in the chain and some other needed values for computation.
In this homework each block will hold:
    * a string message (data)
    * its own block hash value
    * hash value of the previous block
    * nonce value which will be incremented when a block is mined

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run the test of this exercise located in same folder.

To test run 'Blockchain_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on this topic:
    https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/
"""
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import binascii

class CBlock:

    # TODO 1: Initialize the values of a block
    # Make sure you distinguish between the genesis block and other blocks
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock is not None:
            self.previousHash = previousBlock.computeHash()
        else:
            self.previousHash = None
        self.nonce = 0
        hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
        hasher.update(data.encode())
        self.hash = hasher.finalize()

    # TODO 2: Compute the cryptographic hash of the current block.
    # Be sure which values must be considered to compute the hash properly.
    # return the digest value
    def computeHash(self):
        data_bytes = self.data.encode()
        previous_hash_bytes = bytes(str(self.previousHash), 'utf-8') if self.previousHash else b''
        nonce_bytes = bytes(str(self.nonce), 'utf-8')
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(data_bytes)
        digest.update(previous_hash_bytes)
        digest.update(nonce_bytes)
        return digest.finalize()

    # TODO 3: Mine the current value of a block
    # Calculates a digest based on required values from the block, such as:
    # data, previousHash, nonce
    # Make sure to compute the hash value of the current block and store it properly
    def mine(self, leading_zeros):
        self.nonce = 0
        if self.previousBlock:
            self.previousHash = self.previousBlock.hash
        leading_zeros_str = '0' * leading_zeros
        self.hash = self.computeHash()
        while binascii.hexlify(self.hash).decode()[:leading_zeros] != leading_zeros_str:
            self.nonce += 1
            self.hash = self.computeHash()
        print(self.nonce)
    # TODO 4: Check if the current block contains valid hash digest values
    # Make sure to distinguish between the genesis block and other blocks
    # Make sure to compare both hash digest values:
    # The computed digest of the current block
    # The stored digest of the previous block
    # return the result of all comparisons as a boolean value
    def is_valid_hash(self):
        if self.previousBlock is None:
            return self.hash == self.computeHash()
        else:
            previous_hash = self.previousBlock.computeHash()
            return self.previousHash == previous_hash and self.hash == self.computeHash()