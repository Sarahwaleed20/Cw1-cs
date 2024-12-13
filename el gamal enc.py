import random 

def is_prime(n): 
    "Check if a number is prime." 
    if n < 2: 
        return False 
    for i in range(2,int(n**0.5) + 1): 
        if n % i == 0: 
            return False 
    return True 

def generate_prime(): 
    "Generate a small prime number." 
    while True: 
        prime_candidate = random.randint(10, 100) 
        if is_prime(prime_candidate): 
            return prime_candidate 

def elgamal_keygen(): 
    "Generate ElGamal public and private keys." 
    p = generate_prime() 
    g = 2 
    x = random.randint(1, p - 1) 
    y = (g ** x) % p 
    return (p, g, y), x 

def elgamal_encrypt(public_key, plaintext): 
    "Encrypt the plaintext using the ElGamal algorithm." 
    p, g, y = public_key 
    k = random.randint(1, p - 2) 
    c1 = (g ** k) % p 
    c2 = (plaintext * (y ** k)) % p 
    return (c1, c2)  

def elgamal_decrypt(private_key, ciphertext, public_key): 
    "Decrypt the ciphertext using the ElGamal algorithm." 
    p, _, _ = public_key 
    c1, c2 = ciphertext 
    x = private_key 
    shared_secret = (c1 ** x) % p 
    shared_secret_inv = mod_inverse(shared_secret, p) 
    plaintext = (c2 * shared_secret_inv) % p 
    return plaintext 

def mod_inverse(a, p): 
    "Find the modular inverse of a under modulo p." 
    for i in range(1, p): 
        if (a * i) % p == 1: 
            return i 
    raise ValueError("Mod inverse does not exist")

if __name__ == "__main__":
    public_key, private_key = elgamal_keygen()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    plaintext = 42  
    ciphertext = elgamal_encrypt(public_key, plaintext)
    print("Ciphertext:", ciphertext)

    decrypted_plaintext = elgamal_decrypt(private_key, ciphertext, public_key)
    print("Decrypted Plaintext:", decrypted_plaintext)
