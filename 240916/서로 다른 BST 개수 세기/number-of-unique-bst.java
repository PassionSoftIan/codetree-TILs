/*
1. 왼쪽에 있는 모든 노드들의 값이 해당 노드 보다 작다.
2. 오른쪽에 있는 모든 노드들의 값은 해당 노드 보다 크다.
*/


import java.util.*;

public class Main {

    public static int N;

    public static int[] dp;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        dp = new int[20];

        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 5;

        for (int i = 4; i <= N; i++) {
            for (int j = 0; j < i; j++) {
                dp[i] += dp[j] * dp[i-j-1];
            }
        }

        System.out.print(dp[N]);
    }
}