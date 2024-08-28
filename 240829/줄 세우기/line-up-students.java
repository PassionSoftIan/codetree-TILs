import java.util.*;

class Student implements Comparable<Student> {
    int height, weight, number;

    public Student (int height, int weight, int number) {
        this.height = height;
        this.weight = weight;
        this.number = number;
    }

    @Override
    public int compareTo(Student student) {
        if (this.height != student.height) {
            return student.height - this.height;
        }
        else if (this.weight != student.weight) {
            return student.height - this.height;
        }
        return this.number - student.number;
    }

    @Override
    public String toString() {
        return this.height + " " + this.weight + " " + this.number;
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

        for (int i = 1; i < N + 1; i++) {
            int height = sc.nextInt();
            int weight = sc.nextInt();
            int number = i;

            students[i-1] = new Student(height, weight, number);
        }

        Arrays.sort(students);

        for (Student student : students) {
            System.out.println(student);
        }
    }
}