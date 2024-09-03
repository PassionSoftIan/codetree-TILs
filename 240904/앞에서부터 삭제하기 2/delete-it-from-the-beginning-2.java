import java.util.*;

public class Main {

    public static int N;
    public static int[] arr;
    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int K = N-3;

        pq.add(arr[N-1]);

        int total = arr[N-1];

        float maxResult = 0;

        for (int i = N-2; i >= 1; i--) {
            pq.add(arr[i]);

            total += arr[i];

            maxResult = Math.max(maxResult, (double) (total - pq.peek()) / (pq.size() - 1));
        }
        System.out.printf("%.2f", maxResult);
    }
}