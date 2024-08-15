import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        char arr[][] = new char[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.next().charAt(0);
            }
        }

        int count = 0;

        for (int i = 1; i < N-2; i++) {
            for (int j = 1; j < M-2; j++) {
                if (arr[i][j] == arr[0][0]) {
                    continue;
                }
                for (int k = i+1; k < N-1; k++) {
                    for (int l = j+1; l < M-1; l++) {
                        if ((arr[i][j] != arr[k][l]) && (arr[k][l] != arr[N-1][M-1])) {
                            count++;
                        }
                    }
                }
            }
        }
        System.out.print(count);
    }
}