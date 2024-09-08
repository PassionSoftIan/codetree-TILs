import java.util.*;

class Pair implements Comparable<Pair> {
    int score, time;

    public Pair(int score, int time) {
        this.score = score;
        this.time = time;
    }

    @Override
    public int compareTo(Pair pair) {
        if (this.time != pair.time) {
            return pair.time - this.time;
        }
        return pair.score - this.score;
    }
}

public class Main {

    public static int N;

    public static Pair[] bombs;

    public static PriorityQueue<Integer> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        bombs = new Pair[N];

        for (int i = 0; i < N; i++) {
            int score = sc.nextInt();
            int time = sc.nextInt();

            bombs[i] = new Pair(score, time);
        }

        Arrays.sort(bombs);

        int bombIdx = 0;
        int ans = 0;

        for (int t = 10000; t >= 1; t--) {
            while (bombIdx < N && bombs[bombIdx].time == t) {
                pq.add(-bombs[bombIdx].score);
                bombIdx++;
            }

            if(!pq.isEmpty()) {
                ans += -pq.poll();
            }
        }
        System.out.print(ans);
    }
}