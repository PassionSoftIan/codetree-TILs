import java.util.*;

class Pair implements Comparable<Pair> {
    int start, end;

    public Pair(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public int compareTo(Pair pair) {
        return this.end - pair.end;
    }
}

public class Main {

    public static int N;

    public static Pair[] meeting;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        meeting = new Pair[N];

        for (int i = 0; i < N; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();

            meeting[i] = new Pair(start, end);
        }

        Arrays.sort(meeting);

        int maxResult = 1;

        int now = meeting[0].end;
        for (int i = 1; i < N; i++) {
            int start = meeting[i].start;
            int end = meeting[i].end;

            if (start >= now) {
                now = end;
                maxResult++;
            }
        }
        System.out.print(maxResult);
    }
}