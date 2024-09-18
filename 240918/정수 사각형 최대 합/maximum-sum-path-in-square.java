import java.util.*;

public class Main {

    public static int N;
    public static int[][] arr;
    public static int[][] dp;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        arr = new int[N][N];
        dp = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        dp[0][0] = arr[0][0];

        for (int i = 1; i < N; i++) {
            dp[i][0] = dp[i-1][0] + arr[i][0];
            dp[0][i] = dp[0][i-1] + arr[0][i];
        }

        for (int i = 1; i < N; i++) {
            for (int j = 1; j < N; j++) {
                dp[i][j] = Math.max(arr[i][j] + dp[i-1][j], arr[i][j] + dp[i][j-1]);
            }
        }

        System.out.print(dp[N-1][N-1]);
    }
}