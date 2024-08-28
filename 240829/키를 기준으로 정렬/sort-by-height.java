import java.util.*;

class People implements Comparable<People> {
    String name;
    int height;
    int weight;

    public People(String name, int height, int weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    @Override
    public int compareTo(People person) {
        return this.height - person.height;
    }

    @Override
    public String toString() {
        return name + " " + height + " " + weight;
    }
}

public class Main {

    public static int N;

    public static People[] checkPerson;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        checkPerson = new People[N];

        for (int i = 0; i < N; i++) {
            String name = sc.next();
            int height = sc.nextInt();
            int weight = sc.nextInt();

            checkPerson[i] = new People(name, height, weight);
        }

        Arrays.sort(checkPerson);

        for (People person : checkPerson) {
            System.out.println(person);
        }

    }
}