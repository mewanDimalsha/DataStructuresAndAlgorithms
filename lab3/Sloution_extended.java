import java.util.*;
import java.util.Scanner;

public class Sloution_extended {

    static void swap(int [][]d, int i, int j) { 
        int tmp = d[i][0]; 
        int tmpIndex = d[i][1];
        d[i][0] = d[j][0]; 
        d[j][0] = tmp;
        d[i][1] = d[j][1]; 
        d[j][1] = tmpIndex;
        }

    static int [][] selection_sort(int [][] data,int size) {
    int n = size;
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (data[j][0] < data[minIndex][0]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            swap(data, i, minIndex);
        }
    }
    return data;
    }
    static int binarySearch(int sortedArray[][], int value)
    {
        int low = 0, high = sortedArray.length-1;
        while (low <= high) {
            int m = low + (high - low) / 2;
 
            if (sortedArray[m][0] == value)
                return sortedArray[m][1];
 
            if (sortedArray[m][0] < value)
                low = m + 1;

            else
                high = m - 1;
        }
        System.out.println(value);
        System.out.println(Arrays.deepToString(sortedArray));
        return -1;
    }
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        Scanner scanner = new Scanner(System.in);
        int reqNumber = scanner.nextInt();
        int size = scanner.nextInt();

        int[][] values = new int[size][2];
        int[] indexes = new int[size];
        
        for (int i = 0; i < size-1; i++) {
            values[i][0] = scanner.nextInt();
            values[i][1] = i;
        }
        int index = binarySearch(selection_sort(values, size), reqNumber);
        if ((index!=-1)) {
            System.out.println("Bicorn Horn is present at index "+(index+1));
        }
        else{
            System.out.println("Bicorn Horn is not found!");
        }
        
    }
}
