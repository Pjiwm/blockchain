#!/usr/bin/env python3
"""
Transaction Class

The goal of this exercise is to learn how to complete transaction class.
A transaction is composed of a list of Inputs and a list of outputs, and few methods.
add_input() and add_output(), and sign() are already completed in the previous tutorials and exercise.
In this hoemwork, we will add another method is_valid() to the class. With this method, we can
validate a transaction.

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run the test of this tutorial located in same folder.

To test run 'Transactions_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
"""

from Signature import sign, verify

class Tx:
    inputs = None
    outputs =None
    sigs = None
    reqd = None

    # TODO 1: Complete the method
    # These three methods are already done in the previous tutorials
    # you can copy and paste the previous codes here
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []
        self.reqd = []

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))

    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))

    # TODO 2: Complete the method
    # We would like to have another method to add extra required signature if needded (e.g. escrow)
    # with this method, we can specify other required signature to the transaction by adding the
    # public key of the required signature
    # If this signature is needed, later we can check if the transaction is also signed by that person/party.
    def add_reqd(self, addr):
        self.reqd.append(addr)

    def data(self):
        tx_data=[]
        tx_data.append(self.inputs)
        tx_data.append(self.outputs)
        tx_data.append(self.reqd)
        return tx_data

    def pbc_keys(self):
        pbc_keys = []
        pbc_keys.extend([pbc_key for pbc_key, _ in self.inputs])
        pbc_keys.extend(self.reqd)
        return pbc_keys

    # TODO 3: Complete the method
    # This method is also already done in the previous tutorials.
    # you can copy and paste the previous codes here
    def sign(self, private):
        self.sigs.append(sign(self.data(), private))


    # TODO 4: Complete the method
    # This method is used to validate a transaction.
    # To validate a transaction, we must check few important things:
    #   1 -  Every entery in inputs need to be signed by the relevant sender, and
    #   2 -  If an extra required signature is needed, the signature need to be verified too, and
    #   3 -  The total amount of outputs must not exceed the total amount of inputs.
    def is_valid(self):
        return self.is_balance_valid() and self.are_signatures_valid() and self.has_required_signatures()

    def are_signatures_valid(self):
        sig_valid_for_all_keys = all(
            any(verify(self.data(), s, pub_key) for s in self.sigs)
            for pub_key in self.pbc_keys()
        )
        return sig_valid_for_all_keys

    def has_required_signatures(self):
        for pub_key in self.pbc_keys():
            is_valid = any(verify(self.data(), s, pub_key) for s in self.sigs)
            if not is_valid:
                return False
        return True

    def is_balance_valid(self):
        total_in = sum(amount for _, amount in self.inputs)
        total_out = sum(amount for _, amount in self.outputs)
        inputs_valid = all(amount >= 0 for _, amount in self.inputs)
        outputs_valid = all(amount >= 0 for _, amount in self.outputs)
        return total_out <= total_in and inputs_valid and outputs_valid
