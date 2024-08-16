import java.util.*;

public class Main {

    public static int[] dy = {0, 1};
    public static int[] dx = {1, 0};

    public static int N;
    public static int M;

    public static int[][] arr;

    public static boolean[][] visited;

    public static boolean isRange(int ny, int nx) {
        if (0 <= ny && ny < N && 0 <= nx && nx < M) {
            return true;
        }
        return false;
    }

    public static void DFS(int n, int m) {
        
        for (int k = 0; k < 2; k++) {
            int ny = n + dy[k];
            int nx = m + dx[k];

            if (isRange(ny, nx)) {
                if (arr[ny][nx] == 1 && visited[ny][nx] == false) {
                    visited[ny][nx] = true;
                    DFS(ny, nx);
                }
            }
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N][M];

        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        visited[0][0] = true;

        DFS(0, 0);

        if (visited[N-1][M-1]) {
            System.out.print(1);
        }
        else {
            System.out.print(0);
        };
    }
}