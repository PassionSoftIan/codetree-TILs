import java.util.*;

public class Main {

    public static int N;

    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            String cmd = sc.next();
            if (cmd.equals("push")) {
                pq.add(sc.nextInt());
            }
            else if (cmd.equals("size")) {
                System.out.println(pq.size());
            }
            else if (cmd.equals("pop")) {
                System.out.println(pq.poll());
            }
            else if (cmd.equals("empty")) {
                if (pq.isEmpty()) {
                    System.out.println(1);
                }
                else {
                    System.out.println(0);
                }
            }
            else if (cmd.equals("top")) {
                System.out.println(pq.peek());
            }
        }





    }
}