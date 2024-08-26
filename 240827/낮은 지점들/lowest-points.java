import java.util.*;

public class Main {

    public static int N;

    public static HashMap<Integer, Long> countCheck = new HashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            Long y = sc.nextLong();

            if (!countCheck.containsKey(x)) {
                countCheck.put(x, y);
            }
            else {
                Long minY = Math.min(y, countCheck.get(x));
                countCheck.put(x, minY);
            }
        }

        Long result = 0L;

        for (Long num : countCheck.values()) {
            result += num;
        }
        System.out.print(result);
    }
}