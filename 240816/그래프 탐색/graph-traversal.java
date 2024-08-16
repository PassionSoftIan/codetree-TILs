import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static ArrayList<ArrayList<Integer>> edge = new ArrayList<>();

    public static boolean[] visited;

    public static int count;

    public static void DFS(int start) {

        for (int vertex : edge.get(start)) {
            if (!visited[vertex]) {
                visited[vertex] = true;
                count++;
                DFS(vertex);
            }
        }
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        for (int i = 0; i < (N+1); i++) {
            edge.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();

            edge.get(s).add(e);
            edge.get(e).add(s);
        }

        visited = new boolean[N+1];

        visited[1] = true;
        DFS(1);

        System.out.print(count);
    }
}