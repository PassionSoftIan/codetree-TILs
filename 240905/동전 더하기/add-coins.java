import java.util.*;

public class Main {

    public static int N;
    public static int K;
    
    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        for (int i = 0; i < N; i++) {
            pq.add(-sc.nextInt());
        }

        int count = 0;

        while (K != 0) {
            int coin = -pq.poll();

            if (coin <= K) {
                K -= coin;
                pq.add(-coin);
                count++;
            }
        }
        System.out.print(count);
    }
}