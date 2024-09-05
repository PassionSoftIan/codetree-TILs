import java.util.*;

public class Main {

    public static int N;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        int maxResult = -100000001;

        int result = 0;
        for (int i = 0; i < N; i++) {
            if (result < 0) {
                result = 0;
            }
            result += sc.nextInt();
            maxResult = Math.max(maxResult, result);
        }
        System.out.print(maxResult);        
    }
}