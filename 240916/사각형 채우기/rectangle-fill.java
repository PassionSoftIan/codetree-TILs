import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] dp = new int[1001];

        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        dp[4] = 5;

        for (int i = 5; i <= N; i++) {
            dp[i] = dp[i-2] + dp[i-1];
        }

        System.out.print(dp[N]);
    }
}