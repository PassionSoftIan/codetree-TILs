import java.util.*;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String a = sc.next();  // 입력된 2진법 문자열
        
        // 2진법 문자열에서 가장 왼쪽의 '0'을 '1'로 변경
        char[] binaryArray = a.toCharArray();
        for (int i = 0; i < binaryArray.length; i++) {
            if (binaryArray[i] == '0') {
                binaryArray[i] = '1';
                break;  // 첫 번째 '0'만 변경하고 종료
            }
        }
        
        // 변경된 2진 문자열을 정수로 변환
        String modifiedBinaryString = new String(binaryArray);
        int maxN = Integer.parseInt(modifiedBinaryString, 2);
        
        // 결과 출력
        System.out.println(maxN);
    }
}