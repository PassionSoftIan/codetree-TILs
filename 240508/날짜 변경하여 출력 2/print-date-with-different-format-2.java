import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int m, d, y;

        Scanner sc = new Scanner(System.in);
        sc.useDelimiter("-");
        m = sc.nextInt();
        d = sc.nextInt();
        y = sc.nextInt();

        System.out.print(y + "." + m + "." + d);

    }
}