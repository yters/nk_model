from random import randint, random, sample

N = 50
K = 25

m_K = []

for r in range(N):
    row = []
    for c in range(K):
        row += [randint(0, N-1)]
    m_K += [row]

def F(S):
    f = 0
    for i, n in enumerate(S):
        locus = n
        for j in range(K):
            locus += S[m_K[i][j]]
        f += locus
    return f

def d2b(D): return tuple([(D / 2**n) % 2 for n in range(N)])

def exchange(a0, a1):
    if F(a0[0]) > F(a1[0]):
        a1[0] = a0[0]
    elif F(a0[0]) < F(a1[0]):
        a0[0] = a1[0]

def crossover(a0, a1):
    nS0 = tuple([a0[0][i] if random() < 0.5 else a1[0][i] for i in range(N)])
    nS1 = tuple([a0[0][i] if random() < 0.5 else a1[0][i] for i in range(N)])
    a0[0] = nS0
    a1[0] = nS1
        
def mutate(a):
    nS = tuple([a[0][i] if random() > 0.1 else 1-a[0][i] for i in range(N)])
    a[0] = nS

def innovate(a):
    nS = tuple([a[0][i] if random() > 0.1 else 1 for i in range(N)])
    a[0] = nS

if __name__ == "__main__":
    A = 10
    agents = [[d2b(randint(0, 2**N-1))] for _ in range(A)]
    I = 100
    seen_max_F = 0
    global_max_F = F([1] * N)
    print "global max F:", global_max_F
    for _ in range(I):
        exchange(*sample(agents, 2))
        crossover(*sample(agents, 2))
        mutate(*sample(agents, 1))
        innovate(agents[0])
        curr_max_F = max([F(a[0]) for a in agents])
        if curr_max_F > seen_max_F:
            print curr_max_F
            seen_max_F = curr_max_F
    
