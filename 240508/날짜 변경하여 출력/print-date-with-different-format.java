import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int y, m, d;

        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("\\.");
        y = sc.nextInt();
        m = sc.nextInt();
        d = sc.nextInt();

        System.out.print(m + "-" + d + "-" + y);
    }
}