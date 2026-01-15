#Encryption function
def encrypt_char(shift1, shift2):
    # Lowercase letters split into two halves
    l1 = "abcdefghijklm"
    l2 = "nopqrstuvwxyz"
    # Uppercase letters split into two halves
    u1 = "ABCDEFGHIJKLM"
    u2 = "NOPQRSTUVWXYZ"
    Evalue = "" # This will store the encrypted text

    # Read the original text from file
    with open("raw_text.txt", "r") as file:
        txt = file.read()
    # Go through each character in the text
    for c in txt:
        # If the character is lowercase
        if c.islower():
            if c in l1:
                # If the character is lowercase
                idx = l1.index(c)
                new_idx = (idx + (shift1 * shift2)) % 13
                Evalue += l1[new_idx]
            elif c in l2:
                # Shift characters in the second half backward
                idx = l2.index(c)
                new_idx = (idx - (shift1 + shift2)) % 13
                Evalue += l2[new_idx]

        # If the character is uppercase
        elif c.isupper():
            # Shift uppercase first half backward
            if c in u1:
                idx = u1.index(c)
                new_idx = (idx - shift1) % 13
                Evalue += u1[new_idx]
            elif c in u2:
                # Shift uppercase second half forward using square of shift2
                idx = u2.index(c)
                new_idx = (idx + (shift2 ** 2)) % 13
                Evalue += u2[new_idx]
        else:
            Evalue += c # Keep spaces, numbers, and symbols unchanged

    with open("encrypted.txt", "w") as file:
        file.write(Evalue)

#Decryption function
def decrypt_char(shift1, shift2):
    # Same letter groups used for reversing the encryption
    l1 = "abcdefghijklm"
    l2 = "nopqrstuvwxyz"
    u1 = "ABCDEFGHIJKLM"
    u2 = "NOPQRSTUVWXYZ"
    Dvalue = "" # This will store the decrypted text

    # Read the encrypted text from file
    with open("encrypted.txt", "r") as file:
        txt = file.read()
    # Go through each character and reverse the encryption steps
    for c in txt:
        # Reverse shift for the whole decryption process
        if c.islower():
            if c in l1:
                idx = l1.index(c)
                new_idx = (idx - (shift1 * shift2)) % 13
                Dvalue += l1[new_idx]
            elif c in l2:
                idx = l2.index(c)
                new_idx = (idx + (shift1 + shift2)) % 13
                Dvalue += l2[new_idx]
        elif c.isupper():
            if c in u1:
                idx = u1.index(c)
                new_idx = (idx + shift1) % 13
                Dvalue += u1[new_idx]
            elif c in u2:
                idx = u2.index(c)
                new_idx = (idx - (shift2 ** 2)) % 13
                Dvalue += u2[new_idx]
        else:
            Dvalue += c

    # Write the decrypted text to a file
    with open("decrypted.txt", "w") as file:
        file.write(Dvalue)


#Verification Function to check if decryption worked correctly
def verify():
    with open("raw_text.txt") as f1, open("decrypted.txt") as f2:
        if f1.read() == f2.read():
            print("Decryption successful. Files match.")
        else:
            print("Decryption failed. Files do not match.")


# MAIN PROGRAM

while True:
    # Show menu options and user intraction code
    print("1. Encrypt        2. Decrypt      3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        # Take shift values and encrypt the file
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
        encrypt_char(shift1, shift2)

    elif choice== "2":
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
        decrypt_char(shift1, shift2)
        verify()
    
    elif choice=="3":
        # Exit the program
        break

    else:
        # Handle invalid menu input
        print("please enter valid number")
