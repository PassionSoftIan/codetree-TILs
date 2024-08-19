import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] arr;

    public static int left;
    public static int right;

    public static int upperBound(int target) {

        left = 0;
        right = N - 1;

        int minIdx = N;

        while (left <= right) {

            int mid = (left + right) / 2;

            if (arr[mid] > target) {
                right = mid - 1;
                minIdx = Math.min(minIdx, mid);
            }

            else {
                left = mid + 1;
            }

        }
        return minIdx;
    }

    public static int lowerBound(int target) {

        left = 0;
        right = N - 1;

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
        return minIdx;
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

        Arrays.sort(arr, 0, N);

        for (int i = 0; i < M; i++) {
            int l = sc.nextInt();
            int r = sc.nextInt();

            System.out.println(upperBound(r) - lowerBound(l));
        }
    }
}