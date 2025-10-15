# Elliptic Curve Cryptography (ECC) Key Exchange - Python version

def inverse_mod(k, p):
    """Compute modular multiplicative inverse of k mod p."""
    k = (k % p + p) % p
    for x in range(1, p):
        if (k * x) % p == 1:
            return x
    return 1


def point_add(P, Q, a, p):
    """Elliptic curve point addition."""
    INF = None
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return INF

    if x1 == x2 and y1 == y2:
        if y1 == 0:
            return INF
        m = ((3 * x1 * x1 + a) * inverse_mod(2 * y1, p)) % p
    else:
        m = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3 % p, y3 % p)


def scalar_mult(k, P, a, p):
    """Perform scalar multiplication k*P using double-and-add."""
    INF = None
    R = INF
    Q = P
    while k > 0:
        if k & 1:
            R = point_add(R, Q, a, p)
        Q = point_add(Q, Q, a, p)
        k >>= 1
    return R


def point_to_string(P):
    """Return string representation of a point."""
    return "∞" if P is None else f"({P[0]},{P[1]})"


def main():
    p = 11
    a, b = 7, 10
    G = (2, 7)

    print(f"Elliptic Curve: y^2 = x^3 + {a}x + {b} mod {p}")
    print(f"Base Point G = {point_to_string(G)}")

    alice_key = int(input("Enter Alice's private key (integer): "))
    bob_key = int(input("Enter Bob's private key (integer): "))

    PA = scalar_mult(alice_key, G, a, p)
    PB = scalar_mult(bob_key, G, a, p)

    S1 = scalar_mult(alice_key, PB, a, p)
    S2 = scalar_mult(bob_key, PA, a, p)

    print("\n--- Results ---")
    print("Alice Private Key:", alice_key)
    print("Bob Private Key:", bob_key)
    print("Alice Public Key:", point_to_string(PA))
    print("Bob Public Key:", point_to_string(PB))
    print("Shared Secret (Alice):", point_to_string(S1))
    print("Shared Secret (Bob):", point_to_string(S2))


if __name__ == "__main__":
    main()
