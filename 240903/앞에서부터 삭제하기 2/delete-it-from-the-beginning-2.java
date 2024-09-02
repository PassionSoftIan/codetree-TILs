import java.util.*;

public class Main {

    public static int N;
    public static int[] arr;
    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static int maxSum;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
            maxSum += arr[i];
        }

        int K = 0;

        float maxResult = 0;

        while (K <= N-3) {
            maxSum -= arr[K];

            int tempSum = maxSum;

            for (int i = K+1; i < N; i++) {
                pq.add(arr[i]);
            }

            tempSum -= pq.poll();

            float avg = (tempSum / (N - (K + 2)));

            maxResult = Math.max(maxResult, avg);

            K += 1;
        }

        System.out.printf("%.2f", maxResult);
    }
}