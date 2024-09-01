/*
1. 종이가 2N장 있다.
2. 각 종이에는 M개의 알파벳이 한 줄 적혀있다.
3. 알파벳은 A, T, G, C 의 조합으로 작성되어 있다.
4. A그룹과 B그룹 각각 N장의 종이로 구성 되어 있다.
5. M개의 자리 중 3개의 자리를 골라 A와 B로 나뉘는 규칙을 찾는다.
6. 

*/


import java.util.*;

public class Main {

    public static int N;
    public static int M;

    public static String[] A;
    public static String[] B;

    public static HashSet<String> setA;
    public static HashSet<String> setB;

    public static int isSperated() {
        for (String code : setA) {
            if (setB.contains(code)) {
                return 0;
            }
        }
        return 1;
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        A = new String[N];
        B = new String[N];

        for (int i = 0; i < N; i++) {
            A[i] = sc.next();
        }

        for (int i = 0; i < N; i++) {
            B[i] = sc.next();
        }

        int count = 0;
        for (int i = 0; i < M-2; i++) {
            for (int j = i+1; j < M-1; j++) {
                for (int k = j+1; k < M; k++) {
                    setA = new HashSet<>();
                    setB = new HashSet<>();

                    for (int l = 0; l < N; l++) {
                        String codeA = A[l].substring(i, i+1) + A[l].substring(j, j+1) + A[l].substring(k, k+1);
                        String codeB = B[l].substring(i, i+1) + B[l].substring(j, j+1) + B[l].substring(k, k+1);
                        setA.add(codeA);
                        setB.add(codeB);
                    }
                    count += isSperated();
                }
            }
        }
        System.out.print(count);
    }
}