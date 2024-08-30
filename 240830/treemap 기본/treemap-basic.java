import java.util.*;
import java.util.Map.Entry;

public class Main {

    public static int N;

    public static TreeMap<Integer, Integer> map = new TreeMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            String cmd = sc.next();

            if (cmd.equals("add")) {
                int k = sc.nextInt();
                int v = sc.nextInt();
                map.put(k, v);    
            }
            else if (cmd.equals("find")) {
                int k = sc.nextInt();
                if (map.containsKey(k)) {
                    System.out.println(map.get(k));
                }
                else {
                    System.out.println("None");
                }
                
            }
            else if (cmd.equals("remove")) {
                int k = sc.nextInt();
                if (map.containsKey(k)) {
                    map.remove(k);
                }
            }
            else if (cmd.equals("print_list")) {
                Iterator<Entry<Integer, Integer>> elem = map.entrySet().iterator();
                if (elem.hasNext()) {
                    while(elem.hasNext()) {
                        Entry<Integer, Integer> entry = elem.next();
                        System.out.print(entry.getValue() + " ");
                    }                    
                }
                else {
                    System.out.println("None");
                }
                System.out.println();
            }
        }
    }
}