import java.util.*;

class Student implements Comparable<Student> {

    String name;
    int kor, eng, math;

    public Student(String name, int kor, int eng, int math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    @Override
    public int compareTo (Student student) {
        if (this.kor != student.kor) {
            return student.kor - this.kor;
        }
        else if (this.eng != student.eng) {
            return student.eng - this.eng;
        }
        return student.math - this.math;
    }

    @Override
    public String toString () {
        return name + " " + kor + " " + eng + " " + math;
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
            String name = sc.next();
            int kor = sc.nextInt();
            int eng = sc.nextInt();
            int math = sc.nextInt();

            students[i] = new Student(name, kor, eng, math);
        }

        Arrays.sort(students);

        for (Student student : students) {
            System.out.println(student);
        }
    }
}