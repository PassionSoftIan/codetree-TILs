import java.util.*;

public class Main {

    public static int N;

    public static TreeMap<String, Integer> map = new TreeMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            String str = sc.next();
            map.put(str, map.getOrDefault(str, 0) + 1);
        }

        for (String key : map.keySet()) {
            System.out.println(key + " " + map.get(key));
        }
    }
}