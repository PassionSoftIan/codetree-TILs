import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        int arr[] = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int max_count = 0;
        for (int i = 0; i < N; i++) {
            int count = 1;
            for (int j = 0; j < N; j++) {
                if (i == j) {
                    continue;
                }
                if (Math.abs(arr[i] - arr[j]) <= K && arr[i] >= arr[j]) {
                    count++;
                }
            }
            max_count = Math.max(max_count, count);
        }

        System.out.print(max_count);
    }
}