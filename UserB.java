package training.ECC;

import java.io.*;
import java.net.*;
import java.util.*;

public class UserB {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the p : ");
        int p = sc.nextInt();
        System.out.println("Enter the a : ");
        int a = sc.nextInt();
        System.out.println("Enter the b : ");
        int b = sc.nextInt();
        System.out.println("Enter the gx : ");
        int gx = sc.nextInt();
        System.out.println("Enter the gy : ");
        int gy = sc.nextInt();

        if (!ecc.isvalidpoint(gx, gy, a, b, p)) {
            System.out.println("Invalid points");
            return;
        }

        System.out.println("Enter the private key nb: ");
        int nB = sc.nextInt();

        int[] G = {gx, gy};
        int[] pB = ecc.scalmul(nB, G, a, p);

        System.out.println("Bob's public key - " + pB[0] + " " + pB[1]);

        Socket socket = new Socket("localhost", 5000);
        DataInputStream dis = new DataInputStream(socket.getInputStream());
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

        dos.writeInt(pB[0]);
        dos.writeInt(pB[1]);
        dos.flush();

        int Ax = dis.readInt();
        int Ay = dis.readInt();

        System.out.println("Alice's public key - " + Ax + " " + Ay);

        int[] Aa = {Ax, Ay};
        int[] ss = ecc.scalmul(nB, Aa, a, p);

        System.out.println("Shared secret key - " + ss[0] + " " + ss[1]);

        int key = ss[0] % 256;

        String encrypted = dis.readUTF();
        String decrypted = xorEncrypt(encrypted, key);
        System.out.println("Encrypted message from Alice: " + encrypted);
        System.out.println("Decrypted message: " + decrypted);

        System.out.println("Enter reply to Alice: ");
        sc.nextLine(); 
        String reply = sc.nextLine();
        String encryptedReply = xorEncrypt(reply, key);
        dos.writeUTF(encryptedReply);
        System.out.println("Encrypted reply sent: " + encryptedReply);

        socket.close();
    }

    public static String xorEncrypt(String text, int key) {
        char[] chars = text.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            chars[i] = (char) (chars[i] ^ key);
        }
        return new String(chars);
    }
}
