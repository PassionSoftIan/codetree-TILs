import java.util.*;

class Num implements Comparable<Num> {

    int idx, num;

    public Num(int idx, int num) {
        this.idx = idx;
        this.num = num;
    }

    @Override
    public int compareTo(Num nums) {
        if (this.num != nums.num) {
            return this.num - nums.num;
        }
        return this.idx - nums.idx;
    }
}

public class Main {

    public static int N;

    public static Num[] nums;

    public static int[] ranks;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        
        N = sc.nextInt();

        nums = new Num[N];

        for (int i = 0; i < N; i++) {
            nums[i] = new Num(i+1, sc.nextInt());
        }

        Arrays.sort(nums);

        ranks = new int[N];

        for (int i = 0; i < N; i++) {
            ranks[nums[i].idx - 1] = i+1; 
        }

        for (int i = 0; i < N; i++) {
            System.out.print(ranks[i] + " "); 
        }
    }
}