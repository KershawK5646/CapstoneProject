'''
START DATE: 02/10/20

This python program will work to process log in credentials.
Steps for this process:
1. User enters U-name & PW
2. Program takes the data and salts/ hashes
3. Pass the U-name to the DAO
4. DAO searches DB for the matching hashed U-Name & returns hashed PW.
5. Compare hashes for PW
6. Issue a True/False state based on PW matches.

If match, allow through to welcome screen
If fail, kick back with error message.
'''

def main():

    # THESE ARE DUMMY VALUES
    uName = "admin"
    password = "password"