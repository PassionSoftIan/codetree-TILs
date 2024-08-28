import java.util.*;

class Person implements Comparable<Person> {
    String name;
    int height;
    double weight;

    public Person(String name, int height, double weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }

    @Override
    public int compareTo(Person people) {
        return this.name.compareTo(people.name);
    }

    @Override
    public String toString() {
        return this.name + " " + this.height + " " + this.weight;
    }
}

public class Main {

    public static Person[] people;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        people = new Person[5];

        for (int i = 0; i < 5; i++) {

            String name = sc.next();
            int height = sc.nextInt();
            double weight = sc.nextDouble();

            people[i] = new Person(name, height, weight);
        }

        Arrays.sort(people);

        System.out.println("name");
        for (Person person : people) {
            System.out.println(person);
        }
        System.out.println();

        Arrays.sort(people, (p1, p2) -> p2.height - p1.height);

        System.out.println("height");
        for (Person person : people) {
            System.out.println(person);
        }
    }
}