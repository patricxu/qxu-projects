#http://blog.codinglabs.org/articles/prime-test.html
def compute_power(a, p, m):
    result = 1
    p_bin = bin(p)[2:]
    length = len(p_bin)
    for i in range(0, length):
        result = result**2 % m
        if p_bin[i] == '1':
            result = result * a % m
 
    return result
    
def prime_test_fermat(p):
    if p == 1:
        return False
    if p == 2:
        return True   
    d = compute_power(2, p - 1, p)
    if d == 1:
        return True
    return False
    
print(prime_test_fermat(7)) #True
print(prime_test_fermat(11)) #True
print(prime_test_fermat(15)) #False
print(prime_test_fermat(121)) #False
print(prime_test_fermat(561)) #True
print(prime_test_fermat(6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151)) #True    