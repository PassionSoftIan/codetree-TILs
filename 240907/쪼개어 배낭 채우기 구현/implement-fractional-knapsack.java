import java.util.*;

class Pair implements Comparable<Pair> {
    int weight;
    int price;
    double perValue;

    public Pair(int weight, int price, double perValue) {
        this.weight = weight;
        this.price = price;
        this.perValue = perValue;
    }

    @Override
    public int compareTo(Pair pair) {
        return Double.compare(pair.perValue, this.perValue);
    }
}

public class Main {

    public static int N;
    public static int M;

    public static Pair[] values;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        values = new Pair[N];

        for (int i = 0; i < N; i++) {
            int weight = sc.nextInt();
            int price = sc.nextInt();

            values[i] = new Pair(weight, price, (double) price/weight);

        }

        Arrays.sort(values);

        int tempWeight = 0;
        double maxValue = 0;
        for (int i = 0; i < N; i++) {
            int weight = values[i].weight;
            int price = values[i].price;
            double perValue = values[i].perValue;

            if (M == tempWeight) {
                break;
            }

            if (M - tempWeight >= weight) {
                tempWeight += weight;
                maxValue += price;
            }
            else {
                maxValue += (M - tempWeight) * perValue;
                tempWeight = M;
            }
        }
        System.out.printf("%.3f", maxValue);
    }
}