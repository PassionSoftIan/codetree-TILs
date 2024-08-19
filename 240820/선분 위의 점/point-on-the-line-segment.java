import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] arr;

    public static int find(int left, int right, int target) {
        while (left <= right) {

            int mid = (left + right) / 2;

            if (mid == target) {
                return 1;
            }
            else if (mid < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }

        }
        return 0;
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
            int l = sc.nextInt();
            int r = sc.nextInt();

            int count = 0;
            for (int j = 0; j < N; j++) {
                int dot = arr[j];
                count += find(l, r, dot);
            }
            System.out.println(count);
        }
    }
}