import re
# Vigenere encryption
def vigenere_encryption(plaintext, key):
    #remove all non-alphabetic characters with a for loop
    for i in range(len(plaintext)):
        plaintext[i] = re.sub(r'[^a-zA-ZåäöÅÄÖ]', '', plaintext[i])
    while '' in plaintext:
        plaintext.remove('')
    plaintext="".join(plaintext)  
    # loop through the plaintext
    for ke in key :
        ke= list(ke * (len(plaintext) // len(ke) + 1))
        # make a list of the ciphertext
        ciphertext = []
        # loop through the plaintext
        for i in range(len(plaintext)):
            #make sure that the key 
            # make sure the letter is lowercase
            p = plaintext[i].lower()
            k = ke[i].lower()
            # make sure the letter is a letter
            if not p.isalpha():
                continue
            # make sure the letter is in the alphabet
            if ord(p) < ord('a') and ord(p) != ord('å') and ord(p) != ord('ä') and ord(p) != ord('ö') :
                continue
            # get the index of the letter in the alphabet
            if p=='å':
                p=26
            elif p=='ä':
                p=27
            elif p=='ö':
                p=28
            else:
                p = ord(p) - ord('a')
            # get the index of the letter in the key
            if k=='å':
                k=26
            elif k=='ä':
                k=27
            elif k=='ö':
                k=28
            else:
                k = ord(k) - ord('a')
            c = (p + k) % 29
            # add the letter to the ciphertext
            if c==26:
                ciphertext.append('å')
            elif c==27:
                ciphertext.append('ä')
            elif c==28:
                ciphertext.append('ö')
            else:
                ciphertext.append(chr(c + ord('a')))
            #return the ciphertext
    return ''.join(ciphertext)


#Vigenere decryption algorithm
def vigenere_decryption(ciphertext, key):
    # make a list of the plaintext
    ciphertext=ciphertext.split('\n')
    plaintext = []
    for cipher in ciphertext :
        # loop through the ciphertext
        for ke in key :
            ke= list(ke * (len(cipher) // len(ke) + 1))
            # loop through the plaintext
            for i in range(len(cipher)):
                #make sure that the key 
                # make sure the letter is lowercase
                ciph = cipher[i].lower()
                k = ke[i].lower()
                #make sure that the cipher is a letter
                if not ciph.isalpha() or ciph==' ' or ciph=='\t' or ciph=='\r' or ciph=='\n':
                    print("je suis la")
                    continue
                # get the index of the letter in the alphabet
                if ciph=='å':
                    ciph=26
                elif ciph=='ä':
                    ciph=27
                elif ciph=='ö':
                    ciph=28
                else:
                    ciph = ord(ciph) - ord('a')
                    # get the index of the letter in the key
                if k=='å':
                    k=26
                elif k=='ä':
                    k=27
                elif k=='ö':
                    k=28
                else:
                    k = ord(k) - ord('a')
                # do the vigenere algorithm
                c = (ciph - k) % 29
                # add the letter to the ciphertext
                if c==26:
                    plaintext.append('å')
                elif c==27:
                    plaintext.append('ä')
                elif c==28:
                    plaintext.append('ö')
                else:
                    plaintext.append(chr(c + ord('a')))
            plaintext.append('\n')
    return ''.join(plaintext)

def main():
    # get the plaintext
    plain = open("groupX.plain","r")
    plaintext = plain.readlines()
    # get the key
    k = open("groupX.key","r")
    key = k.readlines()
    # encrypt the plaintext
    f=open("vig_groupX.crypto","w")
    ciphertext = vigenere_encryption(plaintext, key)
    f.write(ciphertext)
    
    # decrypt the ciphertext
    plaintext = vigenere_decryption(ciphertext, key)
    print("The plaintext is: " + plaintext)


# call the main function
main()
