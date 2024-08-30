import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static HashSet<Integer> setN = new HashSet<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            setN.add(num);
        }

        M = sc.nextInt();

        for (int i = 0; i < M; i++) {
            int num = sc.nextInt();
            if (setN.contains(num)) {
                System.out.println(1);
            }
            else {
                System.out.println(0);
            }
        }
    }
}