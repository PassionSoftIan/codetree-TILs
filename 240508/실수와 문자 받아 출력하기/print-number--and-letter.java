import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        String a;
        double b,c;

        Scanner sc = new Scanner(System.in);

        a = sc.next();
        b = sc.nextDouble();
        c = sc.nextDouble();

        System.out.printf("%s\n%.2f\n%.2f", a,b,c);
    }
}