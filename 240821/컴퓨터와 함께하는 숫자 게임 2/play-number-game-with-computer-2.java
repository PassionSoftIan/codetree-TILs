import java.util.*;

public class Main {

    public static int M;
    public static int a;
    public static int b;

    public static long minCount = (long) Math.pow(10, 18) + 1;
    public static int maxCount = 0;

    public static void find(int target) {
        int left = 1;
        int right = M;

        int count = 0;

        while (left <= right) {
            count++;

            int mid = (left + right) / 2;

            if (target == mid) {
                minCount = Math.min(count, minCount);
                maxCount = Math.max(count, maxCount);
                return;
            }
            if (target < mid) {
                right = mid - 1;
            }
            if (target > mid) {
                left = mid + 1;
            }
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        M = sc.nextInt();

        a = sc.nextInt();
        b = sc.nextInt();

        for (int i = a; i <= b; i++) {
            find(i);
        }
        System.out.print(minCount + " " + maxCount);
    }
}