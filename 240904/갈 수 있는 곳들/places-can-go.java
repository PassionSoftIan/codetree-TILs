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
    public static int K;

    public static int[][] arr;

    public static int count;

    public static Queue<Pair> q = new LinkedList<>();

    public static boolean isRange(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N;
    }

    public static boolean canGo(int ny, int nx) {
        if (isRange(ny, nx) && arr[ny][nx] == 0) {
            return true;
        }
        return false;
    }

    public static void push(int n, int m) {
        count++;
        arr[n][m] = 1;
        q.add(new Pair(n, m));
    }

    public static void BFS() {

        while (!q.isEmpty()) {
            Pair coordi = q.poll();
            for (int i = 0; i < 4; i++) {
                int ny = coordi.n + dy[i];
                int nx = coordi.m + dx[i];
                
                if (canGo(ny, nx)) {
                    push(ny, nx);
                }
            }
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        count = 0;

        for (int i = 0; i < K; i++) {

            int n = sc.nextInt();
            int m = sc.nextInt();

            if (arr[n-1][m-1] == 1) {
                continue;
            }
            push(n-1, m-1);
            BFS();
        }
        System.out.print(count);
    }
}