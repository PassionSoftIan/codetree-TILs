import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] coins;

    public static int[] dp;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        coins = new int[N];

        dp = new int[M+1];

        for (int i = 0; i < N; i++) {
            coins[i] = sc.nextInt();
        }

        for (int i = 0; i <= M; i++) {
            dp[i] = Integer.MAX_VALUE;
        }

        dp[0] = 0;

        for (int i = 1; i <= M; i++) {
            for (int j = 0; j < N; j++) {
                if (coins[j] <= i) {
                    if (dp[i - coins[j]] == -1) {
                        continue;
                    }

                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        if (dp[M] == -1) {
            System.out.print(-1);
        }
        else {
            System.out.print(dp[M]);
        }
    }
}