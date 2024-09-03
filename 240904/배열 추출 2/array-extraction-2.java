import java.util.*;

class Pair implements Comparable<Pair> {
    int realNum, absNum;

    public Pair(int realNum, int absNum) {
        this.realNum = realNum;
        this.absNum = absNum;
    }

    @Override
    public int compareTo(Pair pair) {
        if (this.absNum == pair.absNum) {
            return this.realNum - pair.realNum;
        }
        else {
            return this.absNum - pair.absNum;
        }
    }
}

public class Main {

    public static int N;

    public static PriorityQueue<Pair> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int realNum = sc.nextInt();
            int absNum = Math.abs(realNum);

            if (realNum == 0) {
                if (!pq.isEmpty()) {
                    System.out.println(pq.poll().realNum);
                }
                else {
                    System.out.println(0);
                }
            }
            else {
                pq.add(new Pair(realNum, absNum));
            }
        }
    }
}