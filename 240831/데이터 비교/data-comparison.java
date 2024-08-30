import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static int[] arrM;

    public static HashSet<Integer> setN = new HashSet<>();
    public static HashSet<Integer> setM = new HashSet<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        
        for (int i = 0; i < N; i++) {
            setN.add(sc.nextInt());
        }

        M = sc.nextInt();

        arrM = new int[M];

        for (int i = 0; i < M; i ++) {
            int num = sc.nextInt();
            arrM[i] = num;
            setM.add(num);
        }

        for (int i = 0; i < M; i++) {
            if (setN.contains(arrM[i])) {
                System.out.print(1 + " ");
            }
            else {
                System.out.print(0 + " ");
            }
        }
    }
}