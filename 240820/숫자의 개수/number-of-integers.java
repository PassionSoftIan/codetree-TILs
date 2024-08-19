import java.util.*;

public class Main {

    public static int N;
    public static int M;
    
    public static int[] arr;

    public static int lowerBound(int target) {

        int left = 0;
        int right = N-1;

        int minIdx = N;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] >= target) {
                right = mid - 1;
                // minIdx = Math.min(minIdx, mid);
                minIdx = mid;

            }
            else {
                left = mid + 1;
            }
        }

        return minIdx;

    }

    public static int upperBound(int target) {

        int left = 0;
        int right = N-1;

        int minIdx = N;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] > target) {
                right = mid - 1;
                // minIdx = Math.min(minIdx, mid);
                minIdx = mid;
            }
            else {
                left = mid + 1;
            }
        }

        return minIdx;
    }


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {
            int num = sc.nextInt();
            System.out.println(upperBound(num) - lowerBound(num));
        }
        
    }
}