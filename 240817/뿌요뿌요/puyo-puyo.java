import java.util.*;

public class Main {

    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;

    public static int[][] arr;

    public static int max_block_size = 0;

    public static int block_count = 0;

    public static int temp_count;

    public static boolean[][] visited;

    public static boolean canGo(int ny, int nx) {
        if (0 <= ny && ny < N && 0 <= nx && nx < N && visited[ny][nx] == false) {
            return true;
        }
        return false;
    }

    public static void DFS(int n, int m) {
        temp_count++;

        for (int k = 0; k < 4; k++) {
            int ny = n + dy[k];
            int nx = m + dx[k];

            if (canGo(ny, nx)) {
                if (arr[n][m] == arr[ny][nx]) {
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

        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j] == false) {
                    visited[i][j] = true;
                    temp_count = 0;
                    DFS(i, j);
                    if (temp_count >= 4) {
                        block_count++;
                    }
                    max_block_size = Math.max(max_block_size, temp_count);
                }
            }
        }
        System.out.print(block_count + " " + max_block_size);
    }
}