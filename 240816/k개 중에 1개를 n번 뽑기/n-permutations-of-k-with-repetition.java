import java.util.*;

public class Main {

    public static ArrayList<Integer> result = new ArrayList<>();
    public static int K;
    public static int N;

    public static void backtracking(int depth) {
        if (depth == N) {
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= K; i++) {

            result.add(i);
            backtracking(depth+1);
            result.remove(result.size() - 1);

        }


    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        K = sc.nextInt();
        N = sc.nextInt();

        backtracking(0);

    }
}