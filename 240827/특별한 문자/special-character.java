import java.util.*;

public class Main {

    public static LinkedHashMap<Character, Integer> countCheck = new LinkedHashMap<>();

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        char[] chars = str.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            char check = chars[i];
            if(!countCheck.containsKey(check)) {
                countCheck.put(check, 1);
            }
            else {
                countCheck.put(check, countCheck.get(check) + 1);
            }
        }

        String result = "None";

        for (Character check : countCheck.keySet()) {
            if (countCheck.get(check).equals(1)) {
                result = String.valueOf(check);
                break;
            }
        }
        System.out.print(result);
    }
}