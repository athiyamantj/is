package training.ECC;

import java.io.*;
import java.net.*;
import java.util.*;

public class UserA {
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

        System.out.println("Enter the private key na: ");
        int nA = sc.nextInt();

        int[] G = {gx, gy};
        int[] pA = ecc.scalmul(nA, G, a, p);

        System.out.println("Alice's public key - " + pA[0] + " " + pA[1]);

        ServerSocket serverSocket = new ServerSocket(5000);
        Socket socket = serverSocket.accept();
        System.out.println("Bob connected!!!");

        DataInputStream dis = new DataInputStream(socket.getInputStream());
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

        int Bx = dis.readInt();
        int By = dis.readInt();

        System.out.println("Bob's public key - " + Bx + " " + By);

        dos.writeInt(pA[0]);
        dos.writeInt(pA[1]);
        dos.flush();

        int[] Ba = {Bx, By};
        int[] ss = ecc.scalmul(nA, Ba, a, p);

        System.out.println("Shared secret key - " + ss[0] + " " + ss[1]);

        int key = ss[0] % 256;

        System.out.println("Enter message to send to Bob: ");
        sc.nextLine(); 
        String message = sc.nextLine();

        String encrypted = xorEncrypt(message, key);
        dos.writeUTF(encrypted);
        System.out.println("Encrypted message sent: " + encrypted);

        String encryptedReply = dis.readUTF();
        String decryptedReply = xorEncrypt(encryptedReply, key);
        System.out.println("Encrypted reply: " + encryptedReply);
        System.out.println("Decrypted reply: " + decryptedReply);

        socket.close();
        serverSocket.close();
    }

    public static String xorEncrypt(String text, int key) {
        char[] chars = text.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            chars[i] = (char) (chars[i] ^ key);
        }
        return new String(chars);
    }
}
