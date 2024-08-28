import java.util.*;

class Person implements Comparable<Person> {
    String name;
    int height;
    int weight;

    public Person(String name, int height, int weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    @Override
    public int compareTo(Person person) {
        if (this.height != person.height) {
            return this.height - person.height;
        }
        return person.weight - this.weight;
    }

    @Override
    public String toString() {
        return this.name + " " + this.height + " " + this.weight;
    }
}

public class Main {

    public static int N;

    public static Person[] people;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        people = new Person[N];

        for (int i = 0; i < N; i++) {
            String name = sc.next();
            int height = sc.nextInt();
            int weight = sc.nextInt();

            people[i] = new Person(name, height, weight);
        }

        Arrays.sort(people);

        for (Person person : people) {
            System.out.println(person);
        }
    }
}