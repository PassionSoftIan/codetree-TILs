import java.util.*;

public class Main {

    public static int N;

    public static HashSet<Integer> set = new HashSet<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            set.add(sc.nextInt());
        }

        System.out.print(set.size());
    }
}