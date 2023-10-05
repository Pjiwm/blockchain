#!/usr/bin/env python3
"""
The goal of this exercise is to complete the TXBlock class. We want be able to correctly store and
load a block on disk. You have already completed every required modules seperately in the previous tutorials.
In this exercise, you have to integrate all the previously created modules, and ensure
all components are properly working together.

In addition, we would also like to see details of a transaction. For this part, check the assignment
for Transaction.py file

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run the test of this exercise located in same folder.

To test run 'TxBlock_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * Check previous tutorials for more information on this topic
"""

from BlockChain import CBlock
from Signature import generate_keys, sign, verify

from Transaction import Tx

class TxBlock (CBlock):

    # TODO 1: Initialize the block
    # Each block contains a list for the data and a hash value to previous block
    def __init__(self, previousBlock):
        super().__init__([], previousBlock)

    # TODO 2: Append the transaction to the data list
    def addTx(self, Tx_in):
        self.data.append(Tx_in)


    # TODO 3: Check the validity of each transaction in the data list
    # and check the validity of other blocks in the chain to make the cchain tamper-proof
    # Expected return value is true or false
    def is_valid(self):
        return super().is_valid() and all([Tx.is_valid() for Tx in self.data])
