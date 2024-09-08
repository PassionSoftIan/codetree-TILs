import java.util.*;

public class Main {

    public static int N;

    public static TreeSet<Integer> ts = new TreeSet<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            String cmd = sc.next();

            if (cmd.equals("add")) {
                int num = sc.nextInt();
                ts.add(num);
            }
            else if (cmd.equals("remove")) {
                int num = sc.nextInt();
                ts.remove(num);
            }
            else if (cmd.equals("find")) {
                int num = sc.nextInt();
                if (ts.contains(num)) {
                    System.out.println("true");
                }
                else {
                    System.out.println("false");
                }
            }
            else if (cmd.equals("lower_bound")) {
                int num = sc.nextInt();
                Integer result = ts.ceiling(num);
                if (result != null) {
                    System.out.println(result);
                }
                else {
                    System.out.println("None");
                }
            }
            else if (cmd.equals("upper_bound")) {
                int num = sc.nextInt();
                Integer result = ts.higher(num);
                if (result != null) {
                    System.out.println(result);
                }
                else {
                    System.out.println("None");
                }
            }
            else if (cmd.equals("largest")) {
                if (!ts.isEmpty()) {
                    System.out.println(ts.last());
                }
                else {
                    System.out.println("None");
                }
            }
            else if (cmd.equals("smallest")) {
                if (!ts.isEmpty()) {
                    System.out.println(ts.first());
                }
                else {
                    System.out.println("None");
                }
            }
        }
    }
}