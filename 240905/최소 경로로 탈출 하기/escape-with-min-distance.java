import java.util.*;

class Coordinate {
    int n, m, dist;

    public Coordinate(int n, int m, int dist) {
        this.n = n;
        this.m = m;
        this.dist = dist;
    }
}

public class Main {
    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;
    public static int M;

    public static int[][] arr;
    public static int[][] visited;

    public static Queue<Coordinate> q = new LinkedList<>();

    public static boolean isRange(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < M;
    }

    public static boolean canGo(int ny, int nx) {
        if (!isRange(ny, nx)) {
            return false;
        }
        if (visited[ny][nx] == -1 && arr[ny][nx] == 1) {
            return true;
        }
        return false;
    }

    public static void push(int n, int m, int dist) {
        if (visited[n][m] == -1) {
            visited[n][m] = dist;
        }
        else {
            visited[n][m] = Math.min(visited[n][m], dist);
        }
        q.add(new Coordinate(n, m, dist));
    }

    public static void BFS() {
        while (!q.isEmpty()) {
            Coordinate coordi = q.poll();
            int n = coordi.n;
            int m = coordi.m;
            int dist = coordi.dist;

            for (int i = 0; i < 4; i++) {
                int ny = n + dy[i];
                int nx = m + dx[i];
                if (canGo(ny, nx)) {
                    push(ny, nx, dist + 1);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N][M];
        visited = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
                visited[i][j] = -1;
            }
        }

        push(0, 0, 0);
        BFS();

        System.out.print(visited[N-1][M-1]);
    }
}