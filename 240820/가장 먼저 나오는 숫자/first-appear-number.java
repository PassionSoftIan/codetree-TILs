import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] arr;

    public static void find(int target) {
        int left = 0;
        int right = N - 1;

        int minIdx = N;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] >= target) {
                right = mid - 1;
                minIdx = Math.min(minIdx, mid);
            } 
            else {
                left = mid + 1;
            }
        }

        if (arr[minIdx] != target) {
            System.out.println(-1);
        }
        else {
            System.out.println(minIdx + 1);
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {
            int x = sc.nextInt();

            find(x);
        }

    }
}