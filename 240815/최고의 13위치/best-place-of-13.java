import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int arr[][] = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        int max_count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N-2; j++) {
                int count = 0;
                for (int k = 0; k < 3; k++) {
                    if (arr[i][j+k] == 1) {
                        count++;
                    }
                }
                max_count = Math.max(max_count, count);
            }
        }

        System.out.print(max_count);

    }
}