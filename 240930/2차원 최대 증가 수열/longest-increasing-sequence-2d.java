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

        dp[0][0] = 1;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int y = 0; y < i; y++) {
                    for (int x = 0; x < j; x++) {
                        if(dp[y][x] == 0) {
                            continue;
                        }
                        if (arr[y][x] < arr[i][j]) {
                            dp[i][j] = Math.max(dp[i][j], dp[y][x] + 1);
                        }
                    }
                }
            }
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                result = Math.max(result, dp[i][j]);
            }
        }
        
        System.out.print(result);
    }
}