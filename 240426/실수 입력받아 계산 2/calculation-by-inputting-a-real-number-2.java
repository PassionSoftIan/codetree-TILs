import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        double a;

        Scanner sc = new Scanner(System.in);
        a = sc.nextDouble();
        sc.close();

        System.out.printf("%.2f", a+1.5);

    }
}