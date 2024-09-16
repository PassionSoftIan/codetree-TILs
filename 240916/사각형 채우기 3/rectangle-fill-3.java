import java.util.*;
import java.math.BigInteger;

public class Main {

    public static int N;

    public static BigInteger[] dp;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        dp = new BigInteger[1001];

        dp[1] = new BigInteger("2");
        dp[2] = new BigInteger("7");
        dp[3] = new BigInteger("22");
        dp[4] = new BigInteger("71");
        
        BigInteger MOD = new BigInteger("1000000007");
        
        for (int i = 4; i <= N; i++) {
            dp[i] = dp[i-1].multiply(new BigInteger("3"))
                           .add(dp[i-2])
                           .subtract(dp[i-3])
                           .mod(MOD);
        }

        System.out.print(dp[N]);
    }
}