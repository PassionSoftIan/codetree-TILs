import java.util.*;

public class Main {

    public static int N;

    public static int[] cars;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        cars = new int[N];

        for (int i = 0; i < N; i++) {
            int price = sc.nextInt();
            cars[i] = price;
        }

        int maxProfit = 0;
        int minPrice = cars[0];

        for (int i = 0; i < N; i++) {
            int profit = cars[i] - minPrice;

            if (profit > maxProfit) {
                maxProfit = profit;
            }

            if (minPrice > cars[i]) {
                minPrice = cars[i];
            }
        }
        System.out.print(maxProfit);
    }
}