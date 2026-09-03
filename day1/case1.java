//i/p=[7,3,9,2,8]
//o/p=second largest number is 8

import java.util.Arrays;
import java.util.Collections;

public class case1 {
    public static void main(String[] args) {
        Integer[] arr = {7, 3, 9, 2, 8};  //--------O(1)
        
        Arrays.sort(arr, Collections.reverseOrder());  //--------O(n log n)
        
        System.out.println("Second largest number is: " + arr[1]);  //--------O(1)
    }
}

//total time complexity=O(n log n)






