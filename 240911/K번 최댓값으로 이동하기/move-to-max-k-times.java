import java.util.*;

class Pair implements Comparable<Pair> {
    int n, m, num;

    public Pair(int n, int m, int num) {
        this.n = n;
        this.m = m;
        this.num = num;
    }

    @Override
    public int compareTo(Pair pair) {
        if (this.num != pair.num) {
            return pair.num - this.num;
        }
        else if (this.n != pair.n) {
            return this.n - pair.n;
        }
        return this.m - pair.m;
    }
}

public class Main {

    public static int[] dy = {0, 1, 0, -1};
    public static int[] dx = {1, 0, -1, 0};

    public static int N;
    public static int K;

    public static int[][] arr;
    public static boolean[][] visited;

    public static Queue<Pair> q;

    public static PriorityQueue<Pair> pq = new PriorityQueue<>();
    
    public static boolean canGo(int ny, int nx, int startNum) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx] && arr[ny][nx] < startNum;
    }

    public static void push(int n, int m, int num) {
        visited[n][m] = true;
        q.add(new Pair(n, m, num));
        pq.add(new Pair(n, m, num));
    }

    public static void BFS(int startNum) {

        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int n = pair.n;
            int m = pair.m;
            
            for (int k = 0; k < 4; k++) {
                int ny = n + dy[k];
                int nx = m + dx[k];

                if (canGo(ny, nx, startNum)) {
                    push(ny, nx, arr[ny][nx]);
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

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        int row = sc.nextInt() - 1;
        int col = sc.nextInt() - 1;

        int resultN = row+1;
        int resultM = col+1;

        for (int i = 0; i < K; i++) {
            visited = new boolean[N][N];
            q = new LinkedList<>();
            
            push(row, col, arr[row][col]);
            pq = new PriorityQueue<>();
            BFS(arr[row][col]);

            if (pq.isEmpty()) {
                break;
            }

            Pair next = pq.poll();

            row = next.n;
            col = next.m;

            resultN = row+1;
            resultM = col+1;
        }
        System.out.print(resultN + " " + resultM);
    }
}