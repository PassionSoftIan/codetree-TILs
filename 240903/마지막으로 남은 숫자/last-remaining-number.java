import java.util.*;

public class Main {

    public static int N;

    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            pq.add(-sc.nextInt());
        }

        while (pq.size() >= 2) {

            int num1 = -pq.poll();
            int num2 = -pq.poll();

            int diff = num1 - num2;

            if (diff != 0) {
                pq.add(-diff);
            }
        }

        if (pq.isEmpty()) {
            System.out.print(-1);
        }
        else {
            System.out.print(-pq.poll());
        }
    }
}