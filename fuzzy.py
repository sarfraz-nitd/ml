def union(A,B):
    u={}

    for i in A.keys():
        #if B.has_key(i):
        if i in B:
            u[i]=max(A[i],B[i])
    return u

def intersection(A,B):
    v={}

    for i in A.keys():
        #if B.has_key(i):
        if i in B:
            v[i]=min(A[i],B[i])
    return v

def complement(A):
    Ac={}

    for i in A.keys():
        Ac[i]=round(1-A[i],1)
    return Ac

def a_product(A,B):
    p={}

    for i in A.keys():
        #if B.has_key(i):
        if i in B:
            p[i]=round(A[i]*B[i],2)
    return p
    
def a_sum(A,B):
    s={}

    for i in A.keys():
        #if B.has_key(i):
        if i in B:
            s[i]=round(A[i]+B[i]-A[i]*B[i],2)
    return s


A={"a":0.2,"b":0.5,"c":0.8}
B={"a":0.8,"b":0.6,"c":0.4}
C={"a":0.1,"b":0.7,"c":0.2}
print("set A : ",A)
print( "set B : ",B)
print ("set C : ",C)

print (":::Operations on fuzzy sets:::")

print ("union of set A and B : AUB = ",union(A,B))
print ("intersection of set A and B : A^B = ",intersection(A,B))
print ("complement of set A is : Ac = ",complement(A))
print ("complement of set B is : Bc = ",complement(B))
print ("algebraic product of sets A and B is : A*B = ",a_product(A,B)     )
print ("algebraic sum of sets A and B is : A+B = ",a_sum(A,B))

print (":::properties of fuzzy sets:::")
print ("1. Idempotent laws : ")
print ("1.1 AUA=A")
print ("A = ",A)
print ("AUA = ",union(A,A))
print ("1.2 A^A=A")
print ("A = ",A)
print ("A^A = ",intersection(A,A))

print ("2. Commutative laws : ")
print ("2.1 AUB=BUA")
print ("AUB = ",union(A,B))
print ("BUA = ",union(B,A))
print ("2.2 A^B=B^A")
print ("A^B = ",intersection(A,B))
print ("B^A = ",intersection(B,A))

print ("3. Associative laws : ")
print ("3.1 (AUB)UC = AU(BUC)")
print ("(AUB)UC = ",union(union(A,B),C))
print ("AU(BUC) = ",union(A,union(B,C)))
print ("3.2 (A^B)^C = A^(B^C)")
print ("(A^B)^C = ",intersection(intersection(A,B),C))
print ("A^(B^C) = ",intersection(A,intersection(B,C)))

print ("4. Absorption laws : ")
print ("4.1 AU(A^B)=A")
print ("A = ",A)
print ("AU(A^B) = ",union(A,intersection(A,B)))
print ("4.2 A^(AUB)=A")
print ("A = ",A)
print ("A^(AUB) = ",intersection(A,union(A,B)))

print ("5. Distributive laws : ")
print ("5.1 AU(B^C) = (AUB)^(AUC)")
print ("AU(B^C) = ",union(A,intersection(B,C)))
print ("(AUB)^(AUC) = ",intersection(union(A,B),union(A,C)))
print ("5.2 A^(BUC) = (A^B)U(A^C)")
print ("A^(BUC) = ",intersection(A,union(B,C)))
print ("(A^B)U(A^C) = ",union(intersection(A,B),intersection(A,C)))

print ("6. Involution law : ")
print ("A'' = A")
print ("A = ",A)
print ("A'' = ",complement(complement(A)))

print ("7. De-morgan's laws : ")
print ("7.1 (AUB)' = A'^B'")
print ("(AUB)' = ",complement(union(A,B)))
print ("A'^B' = ",intersection(complement(A),complement(B)))
print ("7.2 (A^B)' = A'UB'")
print ("(A^B)' = ",complement(intersection(A,B)))
print ("A'UB' = ",union(complement(A),complement(B)))

print ("8. Identity laws : ")
p={"a":0,"b":0,"c":0}
u={"a":1,"b":1,"c":1}
print ("empty set p = ",p)
print ("universal set u = ",u)
print ("8.1 AUp = A")
print ("A = ",A)
print ("AUp = ",union(A,p))
print ("8.2 AUu = u")
print ("u = ",u)
print ("AUu = ",union(A,u))
print ("8.3 A^p = p")
print ("p = ",p)
print ("A^p = ",intersection(A,p))
print ("8.4 A^u = A")
print ("A = ",A)
print ("AUu = ",intersection(A,u))

print ("9. Complement laws : ")
print ("9.1 AUA' != u")
print ("AUA' = ",union(A,complement(A)))
print ("u = ",u)
print ("9.2 A^A' != p")
print ("A^A' = ",intersection(A,complement(A)))
print ("p = ",p)
