"""
This test case will verify if the provided exercise solution by a student for the Signature.py is correct.

The goal of this tutorial is to learn how to create text-based unformatted transactions.
However, in real scenario, we need to use a more specific and useful format for transactions (next tutorial).


Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run this test file and observe the results.

"""

from Signature import *

if __name__ == '__main__':

    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()

    data = [
        'Alex pays 2 coin to mike',
        'Alex pays 1.2 coins to Mara',
        'Mike pays 0.6 coin to Alex'
        ]



    # TODO 1: Complete the test case 1
    # Create a test case to sign data using alex's signature
    # and then try to verify it using the same (alex's) signature
    # As data is signed by alex signature, it should be successfully verified by alex's key

    # Test case 1: write your code here:
    for msg in data:
        alex_sig = sign(msg.encode('utf-8'), alex_prv)
        if verify(msg.encode('utf-8'), alex_sig, alex_pbc):
            print('Test case 1: Signature is verified successfully for msg: ' + msg)
        else:
            print('Test case 1: Signature is not verified failed for msg: ' + msg)




    # TODO 2: Complete the test case 2
    # Create a test case to sign data using alex's signature
    # and then try to verify it using mike's signature
    # As data is signed by alex signature, it should not be successfully verified by mike's (or any other key) key

    # Test case 2: write your code here:
    for msg in data:
        alex_sig = sign(msg.encode('utf-8'), alex_prv)
        if verify(msg.encode('utf-8'), alex_sig, mike_pbc):
            print('Test case 2: Signature is verified failed for msg: ' + msg)
        else:
            print('Test case 2: Signature is not verified successfully for msg: ' + msg)