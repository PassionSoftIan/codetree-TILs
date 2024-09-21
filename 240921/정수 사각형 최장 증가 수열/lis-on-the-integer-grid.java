import java.util.*;

public class Main {
    public static int dy[] = {0, 1, 0, -1};
    public static int dx[] = {1, 0, -1, 0};

    public static int N;

    public static int[][] arr;

    public static int[][] dp;

    public static boolean canGo(int ny, int nx, int n, int m) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && arr[n][m] < arr[ny][nx];
    }

    public static int DFS(int n, int m) {
        if (dp[n][m] != 0) {
            return dp[n][m];
        }

        dp[n][m] = 1;

        for (int k = 0; k < 4; k++) {
            int ny = n + dy[k];
            int nx = m + dx[k];

            if (canGo(ny, nx, n, m)) {
                dp[n][m] = Math.max(dp[n][m], DFS(ny, nx) + 1);
            }
        }

        return dp[n][m];
    }

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

        int maxResult = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                maxResult = Math.max(maxResult, DFS(i, j));
            }
        }
        System.out.print(maxResult);
    }
}