import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        float ft = 30.48f;

        float a = sc.nextFloat();

        System.out.printf("%.1f", a*ft);

        sc.close();

    }
}