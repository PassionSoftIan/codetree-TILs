import java.util.*;

public class Main {

    public static int N;
    public static int K;

    public static int[] arr;

    public static HashMap<Integer, Integer> map = new HashMap<>();

    public static ArrayList<Integer> nums = new ArrayList<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        arr = new int[100001];

        int result = 0;

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            arr[num] += 1;
            nums.add(num);
            map.put(num, K-num);
        }

        for (int i = 0; i < N; i++) {
            int num = nums.get(i);

            if (arr[num] > 0) {
                if (map.containsKey(map.get(num))) {
                    arr[num] -= 1;
                    arr[map.get(num)] -= 1;
                    result += 1;
                }
            }
        }
        System.out.print(result);
    }
}