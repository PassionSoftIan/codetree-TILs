import java.util.*;

public class Main {

    public static int N;

    public static long[] dp;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        dp = new long[1001];

        dp[1] = 2;
        dp[2] = 7;
        dp[3] = 22;
        dp[4] = 71;
        
        for (int i = 4; i <= N; i++) {
            dp[i] = ((dp[i-1] * 3) + dp[i-2] - dp[i-3]) % 1000000007;
        }

        System.out.print(dp[N]);
    }
}