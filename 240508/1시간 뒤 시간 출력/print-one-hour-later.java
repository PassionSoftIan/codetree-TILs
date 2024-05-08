import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int h, m;

        Scanner sc = new Scanner(System.in);
        sc.useDelimiter(":");
        h = sc.nextInt();
        m = sc.nextInt();

        System.out.print((h+1) + ":" + m);


    }
}