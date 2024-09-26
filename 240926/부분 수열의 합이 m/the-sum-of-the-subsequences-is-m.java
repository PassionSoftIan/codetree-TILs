import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] nums;
    public static int[] dp;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        nums = new int[N];
        dp = new int[M+1];

        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }

        for (int i = 0; i < M+1; i++) {
            dp[i] = 101;
        }

        dp[0] = 0;

        for (int i = 0; i < N; i++) {
            for (int j = M; j >= 0; j--) {
                if (j >= nums[i]) {
                    if (dp[j - nums[i]] == -1) {
                        continue;
                    }

                    dp[j] = Math.min(dp[j], dp[j - nums[i]] + 1);
                }
            }
        }

        if (dp[M] == 101) {
            System.out.print(-1);
        }
        else {
            System.out.print(dp[M]);  
        }
    }
}