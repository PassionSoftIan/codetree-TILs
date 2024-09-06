import java.util.*;

class Pair {
    int n, m, count, usedK;

    public Pair(int n, int m, int count, int usedK) {
        this.n = n;
        this.m = m;
        this.count = count;
        this.usedK = usedK; // 1번 이동을 사용한 횟수
    }
}

public class Main {

    // 상하좌우
    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    // 대각선 (장기 마 이동을 위한 8방향)
    public static int[] horseDy = {-2, -2, -1, -1, 1, 1, 2, 2};
    public static int[] horseDx = {-1, 1, -2, 2, -2, 2, -1, 1};

    public static int K;
    public static int N;
    public static int M;

    public static int[][] arr;
    public static int[][][] visited;

    public static Queue<Pair> q = new LinkedList<>();

    public static boolean canGo(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < M && arr[ny][nx] == 0;
    }

    public static void push(int n, int m, int count, int usedK) {
        visited[n][m][usedK] = count;
        q.add(new Pair(n, m, count, usedK));
    }

    public static void BFS() {
        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int n = pair.n;
            int m = pair.m;
            int count = pair.count;
            int usedK = pair.usedK;

            // 2번 이동: 상하좌우로 이동
            for (int i = 0; i < 4; i++) {
                int ny = n + dy[i];
                int nx = m + dx[i];
                if (canGo(ny, nx) && visited[ny][nx][usedK] == -1) {
                    push(ny, nx, count + 1, usedK);
                }
            }

            // 1번 이동: K번을 넘지 않도록 체크하면서 대각선 이동
            if (usedK < K) {
                for (int i = 0; i < 8; i++) {
                    int ny = n + horseDy[i];
                    int nx = m + horseDx[i];
                    if (canGo(ny, nx) && visited[ny][nx][usedK + 1] == -1) {
                        push(ny, nx, count + 1, usedK + 1);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        K = sc.nextInt();
        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N][M];
        visited = new int[N][M][K + 1]; // 1번 이동을 사용한 횟수에 따른 방문 체크

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
                for (int k = 0; k <= K; k++) {
                    visited[i][j][k] = -1; // 아직 방문하지 않은 상태
                }
            }
        }

        // 시작점 방문
        push(0, 0, 0, 0);
        BFS();

        // 도착점의 최소 이동 횟수 구하기
        int result = Integer.MAX_VALUE;
        for (int k = 0; k <= K; k++) {
            if (visited[N - 1][M - 1][k] != -1) {
                result = Math.min(result, visited[N - 1][M - 1][k]);
            }
        }

        // 결과 출력
        if (result == Integer.MAX_VALUE) {
            System.out.println("-1"); // 도달할 수 없는 경우
        } else {
            System.out.println(result);
        }
    }
}