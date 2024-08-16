import java.util.*;
import java.io.*;

public class Main {

    public static int K;
    public static int N;
    public static ArrayList<Integer> result = new ArrayList<>();
    public static StringBuilder sb = new StringBuilder();

    public static void backTracking(int depth) {
        if (depth == N) {
            for (int i = 0; i < N; i++) {
                sb.append(result.get(i)).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= K; i++) {
            if (depth >= 2 && i == result.get(result.size() - 1) && i == result.get(result.size() - 2)) {
                continue;
            }
            result.add(i);
            backTracking(depth + 1);
            result.remove(result.size() - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        // BufferedReader를 사용하여 입력을 받습니다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // StringTokenizer를 사용하여 한 줄에서 두 개의 숫자를 분리하여 읽습니다.
        StringTokenizer st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        // 백트래킹 시작
        backTracking(0);

        // StringBuilder에 저장된 결과를 한 번에 출력합니다.
        System.out.print(sb.toString());
    }
}