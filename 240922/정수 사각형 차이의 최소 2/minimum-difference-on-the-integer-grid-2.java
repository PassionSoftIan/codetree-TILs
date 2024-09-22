import java.util.*;

public class Main {
    public static int N;
    public static int[][] arr;
    public static boolean[][] visited;

    public static int[] dx = {1, 0}; // 오른쪽 혹은 아래로만 이동
    public static int[] dy = {0, 1}; 

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        arr = new int[N][N];

        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;

        // 격자의 값 입력 받기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
                minVal = Math.min(minVal, arr[i][j]); // 최솟값
                maxVal = Math.max(maxVal, arr[i][j]); // 최댓값
            }
        }

        int result = maxVal - minVal;

        // 이진 탐색 시작 (최댓값과 최솟값의 차이를 이진 탐색으로 줄여나감)
        int left = 0, right = maxVal - minVal;
        while (left <= right) {
            int mid = (left + right) / 2;

            boolean canReach = false;

            // 최솟값을 기준으로 가능한 범위를 정함
            for (int start = minVal; start + mid <= maxVal; start++) {
                int low = start;
                int high = start + mid;

                visited = new boolean[N][N];
                if (arr[0][0] >= low && arr[0][0] <= high) {
                    canReach = dfs(0, 0, low, high); // DFS로 도착 가능한지 체크
                }

                if (canReach) break;
            }

            // 가능한 범위였다면 차이를 줄여봄
            if (canReach) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // 최종 결과 출력
        System.out.println(result);
    }

    // DFS를 사용하여 (0,0)에서 (N-1,N-1)까지 범위 내에서 이동할 수 있는지 확인
    public static boolean dfs(int x, int y, int low, int high) {
        if (x == N - 1 && y == N - 1) {
            return true;
        }

        visited[x][y] = true;

        for (int i = 0; i < 2; i++) { // 오른쪽 또는 아래로만 이동
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
                if (arr[nx][ny] >= low && arr[nx][ny] <= high) {
                    if (dfs(nx, ny, low, high)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}