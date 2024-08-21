import java.util.*;

public class Main {

    public static int N;

    public static HashMap<String, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        int maxCount = 0;

        for (int i = 0; i < N; i++) {
            String str = sc.next();
            if (map.containsKey(str)) {
                int checkCount = map.get(str);
                map.put(str, checkCount + 1);
                maxCount = Math.max(maxCount, checkCount + 1);
            }
            else {
                map.put(str, 1);
                maxCount = Math.max(maxCount, 1);
            }
        }
        System.out.print(maxCount);
    }
}