import java.util.*;

public class Main {


    public static int N;
    public static int M;

    public static int[][] arr;
    public static int[][] dp;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N][M];
        dp = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                dp[i][j] = 1;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int y = i + 1; y < N; y++) {
                    for (int x = j + 1; x < M; x++) {
                        if (arr[y][x] > arr[i][j]) {
                            dp[y][x] = Math.max(dp[y][x], dp[i][j] + 1);
                        }
                    }
                }
            }
        }

        int maxCount = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                maxCount = Math.max(maxCount, dp[i][j]);
            }
        }
        
        System.out.print(maxCount);
    }
}