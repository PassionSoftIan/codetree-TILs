import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static HashMap<String, String> map = new HashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        for (int i = 1; i <= N; i++) {
            String str = sc.next();
            String index = String.valueOf(i);
            map.put(str, index);
            map.put(index, str);
        }

        for (int i = 0; i < M; i++) {
            String check = sc.next();
            System.out.println(map.get(check));
        }
    }
}