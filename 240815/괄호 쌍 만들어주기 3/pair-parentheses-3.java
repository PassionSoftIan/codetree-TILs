import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        int N = str.length();

        int count = 0;

        for (int i = 0; i < N; i++) {
            if (str.charAt(i) == ')') {
                continue;
            }
            for (int j = i+1; j < N; j++) {
                if (str.charAt(j) == ')') {
                    count += 1;
                }
            }
        }

        System.out.print(count);


    }
}