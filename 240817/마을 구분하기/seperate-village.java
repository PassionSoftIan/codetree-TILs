import java.util.*;

public class Main {

    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;

    public static int[][] arr;

    public static int v_count = 0;

    public static int p_count;

    public static int[][] visited;

    public static ArrayList<Integer> result = new ArrayList<>();

    public static boolean canGo(int ny, int nx) {
        if (0 <= ny && ny < N && 0 <= nx && nx < N && arr[ny][nx] == 1 && visited[ny][nx] == 0) {
            return true;
        }
        return false;
    }

    public static void DFS(int n, int m) {

        p_count++;

        for (int k = 0; k < 4; k++) {
            int ny = n + dy[k];
            int nx = m + dx[k];

            if (canGo(ny, nx)) {
                visited[ny][nx] = 1;
                DFS(ny, nx);
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

        visited = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 1 && visited[i][j] == 0) {
                    visited[i][j] = 1;
                    v_count++;
                    p_count = 0;
                    DFS(i, j);
                    result.add(p_count);
                }
            }
        }

        result.sort(null);

        System.out.println(v_count);

        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }
}