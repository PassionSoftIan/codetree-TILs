import java.util.*;

public class Main {

    public static final int MAX_NUM = 100000;

    public static int N;
    public static int ans = MAX_NUM;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i <= MAX_NUM; i++) {
            int remainder = N - (5 * i);
            if (remainder >= 0 && remainder % 2 == 0) {
                ans = Math.min(ans, i + (remainder / 2));
            }
        }

        if (ans == MAX_NUM) {
            ans = -1;
        }

        System.out.print(ans);
    }
}