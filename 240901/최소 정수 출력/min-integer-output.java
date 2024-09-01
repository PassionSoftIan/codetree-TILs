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
            if (num != 0) {
                pq.add(num);
            }
            else {
                if (pq.isEmpty()){
                    System.out.println(0);
                }
                else {
                    System.out.println(pq.poll());
                }
            }
        }
    }
}