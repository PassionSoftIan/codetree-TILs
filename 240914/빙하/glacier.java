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

    public static int iceBerg = 0;

    public static int lastIceBerg = 0;

    public static int T = 0;

    public static boolean canGo(int ny, int nx) {
        return 0 <= ny && ny < N && 0 <= nx && nx < M && !visited[ny][nx];
    }

    public static void push(int n, int m) {
        visited[n][m] = true;
        q.add(new Pair(n, m));
    }

    public static int BFS() {
        int tempIceBerg = 0;

        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int n = pair.n;
            int m = pair.m;

            for (int k = 0; k < 4; k++) {
                int ny = n + dy[k];
                int nx = m + dx[k];

                if (canGo(ny, nx)) {
                    if (arr[ny][nx] == 1) {
                        visited[ny][nx] = true;
                        iceBerg--;
                        tempIceBerg++;
                        arr[ny][nx] = 0;
                    }
                    else {
                        push(ny, nx);
                    }
                }
            }
        }
        return tempIceBerg;
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
                if (arr[i][j] == 1) {
                    iceBerg++;
                }
            }
        }

        while (iceBerg != 0) {
            T++;
            visited = new boolean[N][M];
            push(0, 0);
            lastIceBerg = BFS();
        }
        System.out.print(T + " " + lastIceBerg);
    }
}