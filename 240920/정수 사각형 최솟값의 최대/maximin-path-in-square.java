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
            dp[0][i] = Math.min(dp[0][i-1], arr[0][i]);
            dp[i][0] = Math.min(dp[i-1][0], arr[i][0]);
        }

        for (int i = 1; i < N; i++) {
            for (int j = 1; j < N; j++) {
                dp[i][j] = Math.min(Math.max(dp[i-1][j], dp[i][j-1]), arr[i][j]);
            }
        }

        System.out.print(dp[N-1][N-1]);
    }
}