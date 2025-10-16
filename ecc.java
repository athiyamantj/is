package training.ECC;

import java.math.BigInteger;

public class ecc {
    public static int modinv(int a, int p) {
        return BigInteger.valueOf(a).modInverse(BigInteger.valueOf(p)).intValue();
    }

    public static boolean isvalidpoint(int x, int y, int a, int b, int p) {
        int left = (y*y) % p;
        int right = ((x*x*x) + (a*x) + b) % p;

        if ((left+p)%p == (right+p)%p) return true;
        else return false;
    }

    public static int[] pointadd(int[] P, int[] Q, int a, int p) {
        if (P == null) return Q;
        if (Q == null) return P;

        int x1 = P[0], y1 = P[1];
        int x2 = Q[0], y2 = Q[1];

        if (x1 == x2) {
            if (y1 == y2) {
                int num = ((3*x1*x1) + a)%p;
                int den = (2*y1)%p;
                int lambda = (num * modinv(den, p)) % p;
                int x3 = ((lambda*lambda - 2*x1) % p + p) % p;
                int y3 = ((lambda * (x1 - x3) - y1) % p + p) % p;
                return new int[] {(x3+p)%p, (y3+p)%p}; 
            } else {
                return null;
            }
        } else {
            int num = (y2 - y1) % p;
            int den = (x2 -x1) % p;
            int l = (num * modinv(den, p)) % p;

            int x3 = ((l*l - x1 - x2) % p + p) % p;
            int y3 = ((l * (x1 - x3) - y1) % p + p) % p;
            return new int[] {(x3+p)%p, (y3+p)%p}; 
        }
    }

    public static int[] scalmul(int k, int[] P, int a, int p) {
        int[] result = null;
        int[] addend = P;

        while (k > 0) {
            if ((k & 1) == 1) result = pointadd(result, addend, a, p);
            addend = pointadd(addend, addend, a, p);
            k >>=1;
        }

        return result;
    }
}
