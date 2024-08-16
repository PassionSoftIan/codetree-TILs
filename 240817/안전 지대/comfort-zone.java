import java.util.*;

public class Main {

    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;
    public static int M;

    public static int[][] arr;

    public static boolean[][] visited;

    public static int max_count = -1;

    public static int max_K = 0;

    public static boolean canGo(int ny, int nx) {
        if (0 <= ny && ny < N && 0 <= nx && nx < M && arr[ny][nx] > 0 && visited[ny][nx] == false) {
            return true;
        }
        return false;
    }

    public static void DFS(int n, int m) {

        for (int k = 0; k < 4; k++) {
            int ny = n + dy[k];
            int nx = m + dx[k];

            if (canGo(ny, nx)) {
                visited[ny][nx] = true;
                DFS(ny, nx);
            }
        }
    }


    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int k = 1; k < 100; k++) {
            int go = 0;
            visited = new boolean[N][M];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (arr[i][j] > 0) {
                        go++;
                        arr[i][j] -= 1;
                    }
                }
            }
            if (go == 0) {
                break;
            }
            else {
                int temp_count = 0;
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < M; j++) {
                        if (arr[i][j] > 0 && visited[i][j] == false) {
                            temp_count++;
                            visited[i][j] = true;
                            DFS(i,j);
                        }
                    }
                }
                if (max_count < temp_count) {
                    max_count = temp_count;
                    max_K = k;
                }
            }
        }
        System.out.print(max_K + " " + max_count);
    }
}