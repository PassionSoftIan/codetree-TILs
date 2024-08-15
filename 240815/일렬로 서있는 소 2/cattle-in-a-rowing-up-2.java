import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int arr[] = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int count = 0;
        for (int i = 0; i < N-2; i++) {
            for(int j = i+1; j < N-1; j++) {
                if (arr[i] > arr[j]) {
                    continue;
                }
                for(int k = j+1; k < N; k++) {
                    if (arr[j] > arr[k]) {
                        continue;
                    }

                    count++;

                }
            }
        }

        System.out.print(count);
    }
}