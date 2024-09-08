import java.util.*;

public class Main {

    public static int N;

    public static TreeSet<Integer> A = new TreeSet<>();

    public static int[] B;

    public static ArrayList<Integer> throwB = new ArrayList<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        B = new int[2*N+1];

        for (int i = 0; i < N; i++) {
            int card = sc.nextInt();
            B[card] = 1;
            throwB.add(card);
        }

        for (int i = 1; i <= 2*N; i++) {
            if (B[i] == 0) {
                A.add(i);
            }
        }

        int maxScore = 0;

        for (int i = 0; i < N; i++) {
            int bCard = throwB.get(i);

            if (A.higher(bCard) != null) {
                A.remove(A.higher(bCard));
                maxScore++;
            }
        }

        System.out.print(maxScore);
    }
}