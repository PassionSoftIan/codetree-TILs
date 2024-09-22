import java.util.*;

class Pair {
    int minNum, maxNum, minResult;

    public Pair(int minNum, int maxNum, int minResult) {
        this.minNum = minNum;
        this.maxNum = maxNum;
        this.minResult = minResult;
    }

    @Override
    public String toString() {
        return "(" + " " + String.valueOf(minNum) + " " + String.valueOf(maxNum) + " " + String.valueOf(minResult) + " " + ")";
    }
}

public class Main {
    public static int[] dy = {0, 1};
    public static int[] dx = {1, 0};

    public static int N;

    public static int[][] arr;
    public static Pair[][] dp;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        arr = new int[N][N];
        dp = new Pair[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        dp[0][0] = new Pair(arr[0][0], arr[0][0], 0);

        for (int i = 1; i < N; i++) {
            
            int colMinNum = Math.min(dp[0][i-1].minNum, arr[0][i]);
            int colMaxNum = Math.max(dp[0][i-1].maxNum, arr[0][i]);
            dp[0][i] = new Pair(colMinNum, colMaxNum, Math.abs(colMaxNum - colMinNum));

            int rowMinNum = Math.min(dp[i-1][0].minNum, arr[i][0]);
            int rowMaxNum = Math.max(dp[i-1][0].maxNum, arr[i][0]);
            dp[i][0] = new Pair(rowMinNum, rowMaxNum, Math.abs(rowMaxNum - rowMinNum));
        }

        for (int i = 1; i < N; i++) {
            for (int j = 1; j < N; j++) {
                int fromRowMinNum = dp[i-1][j].minNum;
                int fromRowMaxNum = dp[i-1][j].maxNum;
                int fromRowMinResult = dp[i-1][j].minResult;


                int fromColMinNum = dp[i][j-1].minNum;
                int fromColMaxNum = dp[i][j-1].maxNum;
                int fromColMinResult = dp[i][j-1].minResult;

                int arrRowMinNum = Math.min(fromRowMinNum, arr[i][j]);
                int arrRowMaxNum = Math.max(fromRowMaxNum, arr[i][j]);
                int arrRowMinResult = Math.abs(arrRowMaxNum - arrRowMinNum);

                int arrColMinNum = Math.min(fromColMinNum, arr[i][j]);
                int arrColMaxNum = Math.max(fromColMaxNum, arr[i][j]);
                int arrColMinResult = Math.abs(arrColMaxNum - arrColMinNum);

                if (arrRowMinResult > arrColMinResult) {
                    Pair pair = new Pair(arrColMinNum, arrColMaxNum, arrColMinResult);
                    dp[i][j] = pair;
                }
                else if (arrRowMinResult == arrColMinResult) {
                    if (fromColMaxNum < fromRowMaxNum) {
                        Pair pair = new Pair(arrColMinNum, arrColMaxNum, arrColMinResult);
                        dp[i][j] = pair;                        
                    }
                    else {
                        Pair pair = new Pair(arrRowMinNum, arrRowMaxNum, arrRowMinResult);
                        dp[i][j] = pair;                          
                    }
                }
                else {
                    Pair pair = new Pair(arrRowMinNum, arrRowMaxNum, arrRowMinResult);
                    dp[i][j] = pair;                    
                }
            }
        }
        System.out.print(dp[N-1][N-1].minResult);
    }
}