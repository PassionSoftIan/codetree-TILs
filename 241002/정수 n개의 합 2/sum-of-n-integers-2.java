import java.util.*;

public class Main {

    public static int N;
    public static int K;

    public static int[] nums;

    public static int[] prefixSum;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();
        
        nums = new int[N];
        prefixSum = new int[N+1];

        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }

        prefixSum[1] = nums[0];

        for (int i = 2; i < N; i++) {
            prefixSum[i] = prefixSum[i-1] + nums[i-2];
        }

        int maxResult = Integer.MIN_VALUE;
        for (int i = K; i < N; i++) {
            maxResult = Math.max(maxResult, prefixSum[i] - prefixSum[i-K]);
        }

        System.out.print(maxResult);
    }
}