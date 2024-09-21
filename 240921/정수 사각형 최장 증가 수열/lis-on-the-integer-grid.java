import java.util.*;

public class Main {
    public static int dy[] = {0, 1, 0, -1};
    public static int dx[] = {1, 0, -1, 0};

    public static int N;

    public static int[][] arr;

    public static int[][] dp;

    public static boolean[][] visited;

    public static boolean canGo(int ny, int nx, int n, int m) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx] && arr[n][m] < arr[ny][nx];
    }

    public static void check(int ny, int nx, int count) {
        visited[ny][nx] = true;
        dp[ny][nx] = Math.max(dp[ny][nx], count);
    }

    public static void DFS(int n, int m, int count) {

        for (int k = 0; k < 4; k++) {
            int ny = n + dy[k];
            int nx = m + dx[k];

            if (canGo(ny, nx, n, m)) {
                check(ny, nx, count);
                DFS(ny, nx, count + 1);
            }
        }
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

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                visited = new boolean[N][N];
                check(i, j, 1);
                DFS(i, j, 2);
            }
        }

        int maxResult = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                maxResult = Math.max(dp[i][j], maxResult);
            }
        }

        System.out.print(maxResult);
    }
}