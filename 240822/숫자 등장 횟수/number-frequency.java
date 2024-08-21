import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static HashMap<Integer, Integer> nums = new HashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();

            if (!nums.containsKey(num)) {
                nums.put(num, 1);
            }
            else {
                nums.put(num, nums.get(num) + 1);
            }
        }
        for (int i = 0; i < M; i++) {
            int check = sc.nextInt();
            if (!nums.containsKey(check)) {
                System.out.print(0);
            }
            else {
                System.out.print(nums.get(check) + " ");
            }
        }
    }
}