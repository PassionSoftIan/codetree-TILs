import java.util.*;

public class Main {

    public static int N;
    public static int K;

    public static int[] arr = new int[100001];
    public static HashMap<Integer, Integer> numCheck = new HashMap<>();

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        for (int i = 0; i < N; i++) {
            arr[i] += sc.nextInt();
        }

        int result = 0;

        for (int i = 0; i < N; i++) {
            int num = arr[i];
            int pair = K - num;

            if (numCheck.containsKey(pair)) {
                result += numCheck.get(pair);
            }

            if (!numCheck.containsKey(num)) {
                numCheck.put(num, 1);
            }
            else {
                numCheck.put(num, numCheck.get(num) + 1);
            }
        }
        System.out.print(result);
    }
}