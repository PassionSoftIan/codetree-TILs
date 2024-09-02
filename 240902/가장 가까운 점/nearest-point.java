import java.util.*;

// class Pair implements Comparable<Pair> {

//     int x, y;

//     public Pair(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }

//     @Override
//     public int compareTo(Pair p) {

//     }
// }

public class Main {

    public static int N;
    public static int M;

    public static PriorityQueue<Pair> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            pq.add(new Pair(x, y));
        }

        System.out.print(pq);

    }
}