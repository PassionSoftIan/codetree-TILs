import java.util.*;

class Dot implements Comparable<Dot> {

    int num, dist;

    public Dot(int num, int dist) {
        this.num = num;
        this.dist = dist;
    }

    @Override
    public int compareTo(Dot dots) {

        if (this.dist == dots.dist) {
            return this.num - dots.num;
        }
        return this.dist - dots.dist;
    }
}

public class Main {

    public static int N;

    public static Dot[] dots;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        dots = new Dot[N];

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int dist = Math.abs(x) + Math.abs(y);
            dots[i] = new Dot(i+1, dist);
        }

        Arrays.sort(dots);

        for (Dot dot : dots) {
            System.out.println(dot.num);
        }
    }
}