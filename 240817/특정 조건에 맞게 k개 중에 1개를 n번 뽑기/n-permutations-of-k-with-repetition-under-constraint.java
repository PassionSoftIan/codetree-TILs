import java.util.*;

public class Main {

    public static int K;
    public static int N;

    public static ArrayList<Integer> result = new ArrayList<>();

    public static int check;

    public static void backTracking(int depth) {
        if (depth == N) {
            check = 1;
            for (int i = 0; i < N - 1; i++) {
                if (result.get(i) == result.get(i+1)) {
                    check++;
                }
                else {
                    check = 1;
                }
                if(check == 3) {
                    break;
                }
            }

            if (check < 3) {
                for (int i = 0; i < N; i++) {
                    System.out.print(result.get(i) + " ");
                }
                System.out.println();
                return;
            }
            return;
        }

        for (int i = 1; i <= K; i++) {
            result.add(i);
            backTracking(depth+1);
            result.remove(result.size() - 1);
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        K = sc.nextInt();
        N = sc.nextInt();

        backTracking(0);
    }
}