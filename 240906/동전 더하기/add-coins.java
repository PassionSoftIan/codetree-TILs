import java.util.*;

public class Main {

    public static int N;
    public static int K;
    
    public static int[] coins;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        coins = new int[N];

        for (int i = 0; i < N; i++) {
            coins[i] = sc.nextInt();
        }

        int count = 0;

        for (int i = N-1; i >= 0; i--) {
            count += K / coins[i];
            K %= coins[i];
        }
        System.out.print(count);
    }
}