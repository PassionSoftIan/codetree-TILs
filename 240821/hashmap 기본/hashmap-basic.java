import java.util.*;

public class Main {

    public static int N;

    public static HashMap<Integer, Integer> M = new HashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            String cmd = sc.next();
            if (cmd.equals("add")) {
                int key = sc.nextInt();
                int value = sc.nextInt();
                M.put(key, value);
            }
            else if (cmd.equals("find")) {
                int key = sc.nextInt();
                if (M.containsKey(key)) {
                    System.out.println(M.get(key));
                }
                else {
                    System.out.println("None");
                }
            }
            else if (cmd.equals("remove")) {
                int key = sc.nextInt();
                M.remove(key);
            }
        }
    }
}