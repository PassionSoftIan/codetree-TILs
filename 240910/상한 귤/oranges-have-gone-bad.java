import java.util.*;

class Pair {
    int n, m, count;
    public Pair(int n, int m, int count) {
        this.n = n;
        this.m = m;
        this.count = count;
    }
}

public class Main {
    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;
    public static int K;

    public static int[][] arr;
    public static boolean[][] visited;

    public static int[][] info;

    public static Queue<Pair> q = new LinkedList<>();

    public static boolean canGo(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx] && arr[ny][nx] == 1;
    }

    public static void push(int n, int m, int count) {
        visited[n][m] = true;
        info[n][m] = count;
        q.add(new Pair(n, m, count));
    }

    public static void BFS() {
        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int n = pair.n;
            int m = pair.m;
            int count = pair.count;

            for (int i = 0; i < 4; i++) {
                int ny = n + dy[i];
                int nx = m + dx[i];

                if (canGo(ny, nx)) {
                    push(ny, nx, count+1);
                }
            }
        }
    }
 
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        arr = new int[N][N];
        visited = new boolean[N][N];
        info = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 0) {
                    info[i][j] = -1;
                }
                else if (arr[i][j] == 1) {
                    info[i][j] = -2;
                }
                else {
                    push(i, j, 0);
                }
            }
        }
        BFS();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(info[i][j] + " ");
            }
            System.out.println();
        }
    }
}