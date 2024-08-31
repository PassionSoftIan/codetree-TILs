/*
시간 복잡도를 N+K로 해야 풀림.

N과 K가 100,000라서 N*K로 풀면 시간초과 발생.
*/


import java.util.*;

public class Main {

    public static int N;
    public static int K;

    public static int[] arr;
    public static int[][] change;

    public static HashSet<Integer>[] set;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        arr = new int[N];
        change = new int[K][2];
        set = new HashSet[N];

        for (int i = 0; i < N; i++) {
            arr[i] = i;
            set[i] = new HashSet<>();
            set[i].add(i);
        }

        for (int i = 0; i < K; i++) {
            change[i][0] = sc.nextInt();
            change[i][1] = sc.nextInt();
        }

        for (int i = 0; i < 3*K; i++) {
            int changeNum = i % K;

            int a = change[changeNum][0] - 1;
            int b = change[changeNum][1] - 1;

            set[arr[a]].add(b);
            set[arr[b]].add(a);

            int check = arr[a];
            arr[a] = arr[b];
            arr[b] = check;
        }

        for (int i = 0; i < N; i++) {
            System.out.println(set[i].size());
        }
    }
}