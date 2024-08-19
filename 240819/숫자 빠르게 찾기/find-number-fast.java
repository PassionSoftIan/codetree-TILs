import java.util.*;

public class Main {

    public static int N;
    public static int M;
    public static int[] arr;

    public static int start;
    public static int end;
    public static int mid;

    public static void find(int T) {

        int result = -1;

        while (start <= end) {
            mid = (start + end) / 2;

            if (arr[mid] == T) {
                result = mid + 1;
                break;
            }
            else if (arr[mid] > T) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        System.out.println(result);
        return;
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
            int num = sc.nextInt();
            start = 0;
            end = arr.length - 1;
            find(num);
        }

    }
}