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
        }

        int minResult = 0;

        while (pq.size() != 1) {
            int first = pq.poll();
            int second = pq.poll();

            int numSum = first + second;
            minResult += numSum;

            pq.add(numSum);
        }
        System.out.print(minResult);
    }
}