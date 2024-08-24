import java.util.*;

class Pair implements Comparable<Pair> {
    int num, count;
    public Pair(int num, int count) {
        this.count = count;
        this.num = num;
    }
    @Override
    public int compareTo(Pair target) {
        if (count == target.count) {
            return target.num - num;
        }
        return target.count - count;
    }
}

public class Main {

    public static int N;
    public static int K;

    public static HashMap<Integer, Integer> countCheck = new HashMap<>();

    public static ArrayList<Pair> arr = new ArrayList<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner (System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            if (!countCheck.containsKey(num)) {
                countCheck.put(num, 1);
            }
            else {
                countCheck.put(num, countCheck.get(num) + 1);
            }
        }

        for (Integer key : countCheck.keySet()) {
            arr.add(new Pair(key, countCheck.get(key)));
        }

        arr.sort(null);

        for (int i = 0; i < K; i++) {
            System.out.print(arr.get(i).num + " ");
        }
    }
}