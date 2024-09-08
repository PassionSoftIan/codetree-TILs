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
    public static int[] dy = {-2, -1, 1, 2, 2, 1, -1, -2};
    public static int[] dx = {1, 2, 2, 1, -1, -2, -2, -1};

    public static int N;

    public static int[][] arr;
    public static boolean[][] visited;

    public static Queue<Pair> q = new LinkedList<>();

    public static int endY;
    public static int endX;

    public static int minResult;

    public static boolean canGo(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx];
    }

    public static void BFS() {

        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int n = pair.n;
            int m = pair.m;
            int count = pair.count;

            if (n == endY && m == endX) {
                minResult = count;
                return;
            }

            for (int k = 0; k < 8; k++) {
                int ny = n + dy[k];
                int nx = m + dx[k];

                if (canGo(ny, nx)) {
                    push(ny, nx, count+1);
                }
            }
        }
    }

    public static void push(int n, int m, int count) {
        visited[n][m] = true;
        q.add(new Pair(n, m, count));
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        visited = new boolean[N][N];

        int startY = sc.nextInt();
        int startX = sc.nextInt();

        endY = sc.nextInt();
        endX = sc.nextInt();

        minResult = -1;
        push(startY, startX, 0);
        BFS();

        System.out.print(minResult);
    }
}