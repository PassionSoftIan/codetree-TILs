import java.util.*;

public class Main {

    public static int N;

    public static long[] dp;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        dp = new long[1001];

        dp[1] = 1;
        dp[2] = 3;

        for (int i = 3; i <= N; i++) {
            dp[i] = ((2 * dp[i-2]) + dp[i-1]) % 10007;
        }

        System.out.print(dp[N]);
    }
}