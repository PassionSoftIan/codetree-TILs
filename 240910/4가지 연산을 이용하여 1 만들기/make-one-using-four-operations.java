import java.util.*;

class Pair {
    int num, count;

    public Pair(int num, int count) {
        this.num = num;
        this.count = count;
    }
}

public class Main {

    public static int N;
    public static Queue<Pair> q = new LinkedList<>();
    public static int result = 0;
    public static boolean[] visited;

    public static int first(int num) {
        return num - 1;
    }

    public static int second(int num) {
        return num + 1;
    }

    public static int third(int num) {
        if (num % 2 == 0) {
            return num / 2;
        }
        return -1;
    }

    public static int fourth(int num) {
        if (num % 3 == 0) {
            return num / 3;
        }
        return -1;
    }

    public static void push(int num, int count) {
        if (num >= 1 && num <= 1000000 && !visited[num]) {  // 범위 내의 숫자만 큐에 넣음
            visited[num] = true; // 방문 처리
            q.add(new Pair(num, count));
        }
    }

    public static void BFS() {
        while (!q.isEmpty()) {
            Pair pair = q.poll();
            int num = pair.num;
            int count = pair.count;

            if (num == 1) {
                result = count;
                return;
            }

            push(first(num), count + 1);
            push(second(num), count + 1);

            if (third(num) != -1) {
                push(third(num), count + 1);
            }

            if (fourth(num) != -1) {
                push(fourth(num), count + 1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        visited = new boolean[1000001]; // 방문 배열 초기화

        push(N, 0);
        BFS();
        
        System.out.print(result);
    }
}