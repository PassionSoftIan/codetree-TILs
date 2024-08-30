import java.util.*;

public class Main {

    public static int N;

    public static TreeMap<Integer, Integer> map = new TreeMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();

            if (!map.containsKey(num)) {
                map.put(num, i+1);
            }
        }

        for (Integer key : map.keySet()) {
            System.out.println(key + " " + map.get(key));
        }
    }
}