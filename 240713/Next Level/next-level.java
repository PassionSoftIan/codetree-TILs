import java.util.*;

class User {

    String id;
    int lv;

    public User() {
        this.id = "codetree";
        this.lv = 10;
    }

    public User(String id, int lv) {
        this.id = id;
        this.lv = lv;
    }

}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        User user = new User();

        System.out.println("user " + user.id + " lv " + user.lv);

        String id = sc.next();
        int lv = sc.nextInt();

        User userChanged = new User(id, lv);
        
        System.out.println("user " + userChanged.id + " lv " + userChanged.lv);
    }
}