
import numpy as np

# Helper function
def ismember(A, B):
    return [ np.sum(a == B) for a in A ]

def pskmod(x, M, phi=0, ctype="gray"):
    m = np.array(range(M))
   
    if sum(ismember(np.array(ismember(x, m)) == 0, True)) > 0:
        print("pskmod: all elements of X must be integers in the range [0,%d-1]" % M)
       
    constellation = np.exp(1j*2*np.pi*m/M+1j*phi)
   
    if (ctype.lower() == "bin"): # non-graycoding
        y = [constellation[xx] for xx in x]
    elif (ctype.lower() == "gray"): # graycoding
        (m ^ np.right_shift(m, 1))
        b = (m ^ np.right_shift(m, 1)).argsort()
        y = [constellation[xx] for xx in b[x]]
   
    return y

def pskdemod(x, M, phi=0, ctype="gray"):
    m = np.array(range(M))
    
    idx = np.mod(np.round((np.angle(x) - phi) * M/2/np.pi), M) + 1
    
    if (ctype.lower() == "bin"):
        y = idx-1
    elif (ctype.lower() == "gray"):
        constmap = m ^ np.right_shift(m, 1)
        y = [constmap[int(xx)] for xx in idx-1]
        
    return y

def qammod(x, M):
    m = np.array(range(M))
   
    if sum(ismember(np.array(ismember(x, m)) == 0, True)) > 0:
        print("qammod: all elements of X must be integers in the range [0,%d-1]" % M)
        return
    
    c = np.sqrt(M)
    if (not (c == int(c) and np.log2(c) == int(np.log2(c)))):
        print("qammod: M must be square and a power of 2")
        return
    
    b = -2 * np.mod (x, (c)) + c - 1
    a = 2 * np.floor (x / (c)) - c + 1
    y = a + 1j*b
    return (y)


def qamdemod(y, M):
    c = np.sqrt(M)
    if (not (c == int(c) and np.log2(c) == int(np.log2(c)))):
        print("qamdemod: M must be square and a power of 2")
        return
    
    x = qammod(range(M), M)
    z = np.zeros(np.size(y))
    for k in range(np.size(y)):
        z[k] = np.argmin(abs(  y[k] - x ))
    
    return z
