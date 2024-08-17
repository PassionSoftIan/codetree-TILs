import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static ArrayList<Integer> result = new ArrayList<>();

    public static void backTracking(int depth, int start) {
        if (depth == M) {
            for (int num : result) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i <= N; i++) {
            result.add(i);
            backTracking(depth+1, i+1);
            result.remove(result.size() - 1);
        }

    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        backTracking(0, 1);
    }
}