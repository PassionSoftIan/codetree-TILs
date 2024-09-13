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

    public static int[][] arr;
    public static boolean[][] visited;
    
    public static int K;

    public static int U;
    public static int D;

    public static Queue<Pair> q = new LinkedList<>();

    public static Stack<Pair> stk = new Stack<>();

    public static ArrayList<Pair> coordinate = new ArrayList<>();

    public static int maxResult = 0;

    public static boolean height(int n, int m, int ny, int nx) {
        int dist = Math.abs(arr[n][m] - arr[ny][nx]);
        return U <= dist && dist <= D;
    }

    public static boolean canGo(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < N && !visited[ny][nx];
    }

    public static void push(int n, int m) {
        visited[n][m] = true;
        q.add(new Pair(n, m));
    }

    public static int BFS() {
        int count = 0;

        while (!q.isEmpty()) {
            count++;

            Pair pair = q.poll();

            int n = pair.n;
            int m = pair.m;

            for (int k = 0; k < 4; k++) {
                int ny = n + dy[k];
                int nx = m + dx[k];

                if (canGo(ny, nx) && height(n, m, ny, nx)) {
                    push(ny, nx);
                }
            }
        }
        return count;
    }

    public static void backTracking(int depth, int start) {
        if(depth == K) {
            visited = new boolean[N][N];
            for (Pair pair : stk) {
                int n = pair.n;
                int m = pair.m;

                push(n, m);
            }
            maxResult = Math.max(maxResult, BFS());
            return;
        }

        for (int i = start; i < coordinate.size(); i++) {
            stk.push(coordinate.get(i));
            backTracking(depth + 1, i+1);
            stk.pop();
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();

        U = sc.nextInt();
        D = sc.nextInt();

        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
                coordinate.add(new Pair(i, j));
            }
        }

        backTracking(0, 0);

        System.out.print(maxResult);
    }
}