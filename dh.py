def power(a, b, p):
    if (b == 1):
        return a;
    else:
        return pow(a,b,p)
 
def dh_generatePublicKey(P,G,privateKey):
    #Your code for this function (copy from your lab5 submission)
    # P = 17
    # G = 4
    # privatekey = 3, alices private key she chose 
    # now we calculate her public key
    x = power (G,privateKey,P)
    return(x)
    
def dh_generateSecretKey(publicKey, privateKey, P):
    #Your code for this function (copy from your lab5 submission)
    x = power(publicKey,privateKey,P)

    return(x)
def main():
    P = 0; G = 0; x = 0; a = x;
    y = 0; b = 0;
    ka = 0; kb = 0;

    # Both the users will be agreed upon the public keys G and P
    P = 337; # A prime number P is taken
    print("The value of P: ", P);

    G = 3; # Primitive root for P, G is taken
    print("The value of G: ", G);

    # Alice will choose the private key a
    a = 7; # a is the chosen private key
    print("The private key a for Alice:", a);

     # <Enter code here which calls the appropriate function from above
    # to generate public key for Alice>
    ka = dh_generatePublicKey(P,G,a)


    # Bob will choose the private key b
    b = 11; # b is the chosen private key
    print("The private key b for Bob:", b);
    # <Enter code here which calls the appropriate function from above
    # to generate public key for Bob>
    kb = dh_generatePublicKey(P,G,b)


    # now we want to exchange keys
    # alice will give her key to bob and bob wil give his to alice. 

    tempA = ka # alices key 
    tempB = kb # bobs key 

    ka = tempB # # now alice has bobs key
    kb= tempA # now bob has Bobs key


    aliceSecretK = dh_generateSecretKey(ka,a,P)
    bobSecretK = dh_generateSecretKey(kb,b,P)

    # now that we have exchanged public keys, lets do their private shared key 

    # <Enter code here which calls the appropriate function from above
    # to generate secret keys for both Alice and Bob. Test that these keys
    # match>

    print("Secret key for the Alice is:", ka);
    print("Secret Key for the Bob is:", kb);

    

    if aliceSecretK == bobSecretK:
        print("Bob and alice have the same private shared key")
        print("shared key: ",aliceSecretK)
        print("bobs shared key :", bobSecretK)


if __name__ == '__main__':
    main()