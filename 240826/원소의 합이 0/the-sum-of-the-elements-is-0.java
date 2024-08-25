import java.util.*;

public class Main {

    public static int N;

    public static int[] A;
    public static int[] B;
    public static int[] C;
    public static int[] D;

    public static HashMap<Integer, Integer> sumCheck = new HashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        A = new int[N];
        B = new int[N];
        C = new int[N];
        D = new int[N];
        for(int i = 0; i < N; i++) A[i] = sc.nextInt();
        for(int i = 0; i < N; i++) B[i] = sc.nextInt();
        for(int i = 0; i < N; i++) C[i] = sc.nextInt();
        for(int i = 0; i < N; i++) D[i] = sc.nextInt();

        int result = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int num = A[i] + B[j];
                sumCheck.put(num, sumCheck.getOrDefault(num, 0) + 1);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int num = C[i] + D[j];
                if (sumCheck.getOrDefault(-num, 0) != 0) {
                    result += sumCheck.getOrDefault(-num, 0);
                }
            }
        }
        System.out.print(result);
    }
}