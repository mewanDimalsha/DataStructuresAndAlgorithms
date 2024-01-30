/** 
 * Reg: E/19/111 Galappaththi M.D.
 * Reg: E/19/003 Abeysinghe A.M.H.P.
 */
 
 

import java.util.Scanner;

public class Solution {

    static void swap(int []d, int i, int j) { 
        int tmp = d[i]; 
        d[i] = d[j]; 
        d[j] = tmp;
        }

    static int [] selection_sort(int [] data,int size) {
    int n = size;
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (data[j] < data[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            swap(data, i, minIndex);
        }
    }
    return data;
    }
    static int binarySearch(int sortedArray[], int value)
    {
        int low = 0, high = sortedArray.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
 
            if (sortedArray[mid] == value)
                return mid;
 
            if (sortedArray[mid] < value)
                low = mid + 1;

            else
                high = mid - 1;
        }

        return -1;
    }
    public static void main(String args[] ) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int reqNumber = scanner.nextInt();
        int size = scanner.nextInt();

        int[] values = new int[size];
        
        for (int i = 0; i < size; i++) {
            values[i] = scanner.nextInt();
        }
        int index = binarySearch(selection_sort(values, size), reqNumber);
        if ((index!=-1)) {
            System.out.println("Bicorn Horn is present at index "+index);
        }
        else{
            System.out.println("Bicorn Horn is not found!");
        }
        
    }
}