import java.util.*;

public class Main {

    public static int N;
    public static int K;
    public static int[] arr = new int[100001];

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int result = 0;

        for (int i = 0; i < N; i++) {
            HashMap<Integer, Integer> numCheck = new HashMap<>();
            int firstNum = arr[i];
            int target = K - firstNum;

            for (int j = i + 1; j < N; j++) {
                int secondNum = arr[j];
                int thirdNum = target - secondNum;

                if (numCheck.containsKey(thirdNum)) {
                    result += numCheck.get(thirdNum);
                }

                if (!numCheck.containsKey(secondNum)) {
                    numCheck.put(secondNum, 1);
                } else {
                    numCheck.put(secondNum, numCheck.get(secondNum) + 1);
                }
            }
        }
        System.out.print(result);
    }
}