import java.util.*;

class Pair {
    int n, m, time, count;

    public Pair(int n, int m, int time, int count) {
        this.n = n;
        this.m = m;
        this.time = time;
        this.count = count;
    }
}

public class Main {
    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;
    public static int K;

    public static int[][] arr;
    public static boolean[][][] visited;

    public static Queue<Pair> q = new LinkedList<>();

    public static int result = -1;

    public static boolean canGo(int ny, int nx, int count) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx][count];
    }

    public static void push(int n, int m, int time, int count) {
        visited[n][m][count] = true;
        q.add(new Pair(n, m, time, count));
    }

    public static void BFS(int r2, int c2) {
        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int n = pair.n;
            int m = pair.m;
            int time = pair.time;
            int count = pair.count;

            if (n == r2 && m == c2) {
                result = time;  // 도착 시 시간을 저장
                return;         // 최단 경로이므로 바로 종료 가능
            }

            for (int k = 0; k < 4; k++) {
                int ny = n + dy[k];
                int nx = m + dx[k];

                if (canGo(ny, nx, count)) {
                    if (arr[ny][nx] == 1 && count < K) {
                        // 벽을 없애고 이동
                        push(ny, nx, time + 1, count + 1);
                    } else if (arr[ny][nx] == 0) {
                        // 벽이 없으면 그냥 이동
                        push(ny, nx, time + 1, count);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        arr = new int[N][N];
        visited = new boolean[N][N][K + 1];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        int r1 = sc.nextInt() - 1, c1 = sc.nextInt() - 1;
        int r2 = sc.nextInt() - 1, c2 = sc.nextInt() - 1;

        // BFS 시작
        push(r1, c1, 0, 0);
        BFS(r2, c2);

        // 결과 출력
        System.out.print(result);
    }
}