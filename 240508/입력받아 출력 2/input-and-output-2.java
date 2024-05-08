import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int s, e;

        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("-");
        s = sc.nextInt();
        e = sc.nextInt();

        System.out.printf("%d%d", s, e);
    }
}