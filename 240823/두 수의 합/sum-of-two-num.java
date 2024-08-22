import java.util.*;

public class Main {

    public static int N;
    public static long K;

    public static HashMap<Long, Long> check = new HashMap<>();

    public static ArrayList<Long> nums = new ArrayList<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextLong();

        int result = 0;

        for (int i = 0; i < N; i++) {
            long num = sc.nextLong();
            if (check.containsKey(num)) {
                check.put(num, check.get(num) + 1);
            }
            else {
                check.put(num, 1L);
            }
            nums.add(num);
        }

        for (int i = 0; i < N; i++) {
            long num = nums.get(i);
            long pair = K - num;

            if (check.containsKey(num) && check.containsKey(pair) && check.get(num) > 0 && check.get(pair) > 0) {
                result += 1;
                check.put(num, check.get(num) - 1);
                check.put(pair, check.get(pair) - 1);
            }
        }
        System.out.print(result);
    }
}