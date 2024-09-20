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

        dp[0][N-1] = arr[0][N-1];

        for (int i = 1; i < N; i++) {
            dp[i][N-1] = dp[i-1][N-1] + arr[i][N-1];
        }

        for (int i = N-2; i >= 0; i--) {
            dp[0][i] = dp[0][i+1] + arr[0][i];
        }

        for (int i = 1; i < N; i++) {
            for (int j = N-2; j >= 0; j--) {
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j+1]) + arr[i][j];
            }
        }

        System.out.print(dp[N-1][0]);
    }
}