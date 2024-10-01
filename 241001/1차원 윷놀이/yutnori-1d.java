import java.util.*;

public class Main {

    public static int N;
    public static int M;
    public static int K;

    public static int[] turns;

    public static int[] players;

    public static ArrayList<Integer> result = new ArrayList<>();

    public static int maxResult = 0;

    public static void backTracking(int depth) {
        if (depth == N) {
            players = new int[K+1];
            for (int i = 0; i < result.size(); i++) {
                players[result.get(i)] += turns[i];
            }

            int result = 0;
            for (int i = 1; i < K+1; i++) {
                if (players[i] >= M-1) {
                    result++;
                }
            }

            maxResult = Math.max(result, maxResult);
            return;
        }

        for (int i = 1; i < K+1; i++) {
            result.add(i);
            backTracking(depth+1);
            result.remove(result.size() - 1);
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        K = sc.nextInt();

        turns = new int[N];

        for (int i = 0; i < N; i++) {
            turns[i] = sc.nextInt();
        }

        backTracking(0);

        System.out.print(maxResult);
    }
}