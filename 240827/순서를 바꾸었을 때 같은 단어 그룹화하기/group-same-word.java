import java.util.*;

public class Main {

    public static int N;

    public static HashMap<String, Integer> countCheck = new HashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        sc.nextLine();
        
        for (int i = 0; i < N; i++) {
            String str = sc.nextLine();
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            
            String sortedStr = new String(chars);

            countCheck.put(sortedStr, countCheck.getOrDefault(sortedStr, 0) + 1);
        }

        int max_count = 0;

        for (int count : countCheck.values()) {
            max_count = Math.max(max_count, count);
        }

        System.out.print(max_count);
    }
}