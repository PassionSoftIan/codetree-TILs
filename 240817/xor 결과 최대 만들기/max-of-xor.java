import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] arr;

    public static ArrayList<Integer> result = new ArrayList<>();

    public static int maxXor = 0;

    public static void backTracking(int depth, int start) {
        if (depth == M) {
            int tempXor = 0;
            for (int num : result) {
                tempXor ^= num;
            }
            maxXor = Math.max(maxXor, tempXor);
            return;
        }

        for (int i = start; i < N; i++) {
            result.add(arr[i]);
            backTracking(depth+1, i+1);
            result.remove(result.size() - 1);
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

        backTracking(0, 0);

        System.out.print(maxXor);
    }
}