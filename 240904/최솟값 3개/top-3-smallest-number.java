import java.util.*;

public class Main {

    public static int N;

    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            pq.add(num);

            if (pq.size() >= 3) {
                int num1 = pq.poll();
                int num2 = pq.poll();
                int num3 = pq.peek();
                System.out.println((long)num1*num2*num3);

                pq.add(num1);
                pq.add(num2);
            }
            else {
                System.out.println(-1);
            }
        }
    }
}