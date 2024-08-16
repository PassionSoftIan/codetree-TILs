import java.util.*;

public class Main {

    public static int N;

    public static ArrayList<Integer> result = new ArrayList<>();

    public static int count;

    public static boolean check() {

        for (int i = 0; i < N; i += result.get(i)) {

            if (i + result.get(i) - 1 >= N) {
                return false;
            }

            for (int j = i; j < i + result.get(i); j++) {
                if (!result.get(j).equals(result.get(i))) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void backTracking(int depth) {
        if (depth == N) {
            if (check()) {
                count++;
            }
            return;
        }

        for (int i = 1; i <= 4; i++) {
            result.add(i);
            backTracking(depth+1);
            result.remove(result.size() - 1);
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        backTracking(0);

        System.out.print(count);

    }
}