import java.util.*;

class Student implements Comparable<Student> {
    int height, weight, num;

    public Student(int height, int weight, int num) {
        this.height = height;
        this.weight = weight;
        this.num = num;
    }

    @Override
    public int compareTo(Student students) {
        if (this.height != students.height) {
            return this.height - students.height;
        }
        return this.weight - students.weight;
    }

    @Override
    public String toString() {
        return this.height + " " + this.weight + " " + this.num;
    }
}

public class Main {

    public static int N;

    public static Student[] students;

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        students = new Student[N];

        for (int i = 0; i < N; i++) {
            int height = sc.nextInt();
            int weight = sc.nextInt();
            int num = i+1;

            students[i] = new Student(height, weight, num);
        }

        Arrays.sort(students);

        for (Student student : students) {
            System.out.println(student);
        }
    }
}