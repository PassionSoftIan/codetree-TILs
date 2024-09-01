import java.util.*;

public class Main {

    public static int NA;
    public static int NB;

    public static HashSet<Integer> setA = new HashSet<>();
    public static HashSet<Integer> setB = new HashSet<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        NA = sc.nextInt();
        NB = sc.nextInt();

        for (int i = 0; i < NA; i++) {
            int num = sc.nextInt();
            setA.add(num);
        }

        for (int i = 0; i < NB; i++) {
            int num = sc.nextInt();
            setB.add(num);
        }

        int countA = setA.size();
        for (Integer num : setA) {
            if (setB.contains(num)) {
                countA--;
            }
        }

        int countB = setB.size();
        for (Integer num : setB) {
            if (setA.contains(num)) {
                countB--;
            }
        }
        System.out.print(countA + countB);
    }
}