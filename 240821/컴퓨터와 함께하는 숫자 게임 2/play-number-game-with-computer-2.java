import java.util.*;

public class Main {

    public static long M;
    public static long a;
    public static long b;

    public static int minCount = 60;
    public static int maxCount = 0;

    public static void find(long target) {
        long left = 1;
        long right = M;

        int count = 0;

        while (left <= right) {
            count++;

            long mid = (left + right) / 2;

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

        M = sc.nextLong();

        a = sc.nextLong();
        b = sc.nextLong();

        for (long i = a; i <= b; i++) {
            find(i);
        }
        System.out.print(minCount + " " + maxCount);
    }
}