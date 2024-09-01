import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            pq.add(-num);
        }
        
        for (int i = 0; i < M; i++) {
            pq.add(-(-pq.poll() - 1));
        }

        System.out.print(-pq.peek());
    }
}