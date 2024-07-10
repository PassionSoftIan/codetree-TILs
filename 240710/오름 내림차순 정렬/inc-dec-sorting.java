import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];

        for(int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        Arrays.sort(nums);

        for(int num : nums){
            System.out.print(num + " ");
        }

        System.out.println();

        Integer[] nums2 = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(nums2, Collections.reverseOrder());

        for(int num2 : nums2){
            System.out.print(num2 + " ");
        }
    }
}