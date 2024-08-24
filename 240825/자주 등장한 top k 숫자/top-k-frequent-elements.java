import java.util.*;

public class Main {

    public static int N;
    public static int K;

    public static HashMap<Integer, Integer> countCheck = new HashMap<>();

    public static ArrayList<Integer> arr = new ArrayList<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner (System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            if (!countCheck.containsKey(num)) {
                countCheck.put(num, 1);
            }
            else {
                countCheck.put(num, countCheck.get(num) + 1);
            }
        }

        int maxCount = 0;

        for (Integer key : countCheck.keySet()) {
            maxCount = Math.max(maxCount, countCheck.get(key));
        }

        for (Integer key : countCheck.keySet()) {
            if (maxCount == countCheck.get(key)) {
                arr.add(key);
            }
        }

        arr.sort(null);

        for (int i = arr.size() - 1; i >= 0; i--) {
            System.out.print(arr.get(i) + " ");
        }
    }
}