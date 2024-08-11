from itertools import combinations_with_replacement

def Combinations_With_Replacement(S, k):

    s = sorted(S)
    K = int(k)

    p = combinations_with_replacement(s, K)
    for j in p:
        print(''.join(j))
if __name__ == '__main__':
    S, k = list(input().split())

    result = Combinations_With_Replacement(S, k)