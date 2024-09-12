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
    public static int M;

    public static int[][] arr;
    public static boolean[][] visited;

    public static Pair[] startPoint;

    public static Queue<Pair> q = new LinkedList<>();

    public static ArrayList<Pair> lst = new ArrayList<>();
    public static Stack<Pair> result = new Stack<>();

    public static int tempAns;
    public static int ans = 0;

    public static boolean canGo(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx] && arr[ny][nx] == 0;
    }

    public static void push(int n, int m) {
        tempAns++;
        visited[n][m] = true;
        q.add(new Pair(n, m));
    }

    public static void BFS() {
        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int n = pair.n;
            int m = pair.m;

            for (int k = 0; k < 4; k++) {
                int ny = n + dy[k];
                int nx = m + dx[k];

                if (canGo(ny, nx)) {
                    push(ny, nx);
                }
            }
        }
    }

    public static void backTracking(int depth, int start) {
        if (depth == M) {
            for (Pair stone : result) {
                arr[stone.n][stone.m] = 0;
            }

            visited = new boolean[N][N];
            tempAns = 0;

            for (int i = 0; i < K; i++) {
                push(startPoint[i].n, startPoint[i].m);
            }

            BFS();
            ans = Math.max(ans, tempAns);

            for (Pair stone : result) {
                arr[stone.n][stone.m] = 1;
            }
            return;
        }

        for (int i = start; i < lst.size(); i++) {
            Pair pair = lst.get(i);
            int stoneN = pair.n;
            int stoneM = pair.m;

            result.push(new Pair(stoneN, stoneM));
            backTracking(depth+1, i+1);
            result.pop();
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 1) {
                    lst.add(new Pair(i, j));
                }
            }
        }

        startPoint = new Pair[K];

        for (int i = 0; i < K; i++) {
            int row = sc.nextInt() - 1;
            int col = sc.nextInt() - 1;

            startPoint[i] = new Pair(row, col);

        }

        backTracking(0, 0);

        System.out.print(ans);
    }
}