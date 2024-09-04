import java.util.*;

class Pair {
    int n, m;

    public Pair(int n, int m) {
        this.n = n;
        this.m = m;
    }
}

public class Main {

    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;
    public static int M;
    public static int[][] arr;
    public static boolean[][] visited;

    public static Queue<Pair> q = new LinkedList<>();

    public static boolean inRange(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < M;
    }

    public static boolean canGo(int ny, int nx) {
        if (!inRange(ny, nx)) {
            return false;
        }
        if (visited[ny][nx] == false && arr[ny][nx] == 1) {
            return true;
        }
        return false;
    }

    public static void push(int n, int m) {
        visited[n][m] = true;
        q.add(new Pair(n, m));
    }

    public static void BFS() {

        while (!q.isEmpty()) {
            Pair coordi = q.poll();
            int n = coordi.n;
            int m = coordi.m;

            for (int i = 0; i < 4; i++) {
                int ny = n + dy[i];
                int nx = m + dx[i];
                if (canGo(ny, nx)) {
                    push(ny, nx);
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

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        visited = new boolean[N][M];

        push(0, 0);
        BFS();

        if (visited[N-1][M-1]) {
            System.out.print(1);
        }
        else {
            System.out.print(0);
        }
    }
}