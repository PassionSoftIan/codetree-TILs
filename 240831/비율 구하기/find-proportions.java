import java.util.*;

public class Main {

    public static int N;

    public static TreeMap<String, Integer> colors = new TreeMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            String color = sc.next();

            colors.put(color, colors.getOrDefault(color, 0) + 1);
        }

        for (String color : colors.keySet()) {
            float percentage = (float) colors.get(color) / N * 100;
            System.out.printf("%s %.4f\n", color, percentage);
        }
    }
}