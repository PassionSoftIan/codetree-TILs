import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] dp = new int[1001];

        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 1;
        dp[4] = 1;


        for (int i = 5; i <= N; i++) {
            dp[i] = (dp[i-2] + dp[i-3]) % 10007;
        }

        System.out.print(dp[N]);
    }
}