import java.util.*;

public class Main {

    public static void repeat(int N) {
        for (int i = 0; i < N; i++) {
            System.out.println("12345^&*()_");
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rowNum = sc.nextInt();
        repeat(rowNum);
    }
}