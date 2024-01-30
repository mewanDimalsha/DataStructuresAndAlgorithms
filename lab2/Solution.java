import java.util.*;

public class Solution {

    static void swap(int []d, int i, int j) { 
        int tmp = d[i]; 
        d[i] = d[j]; 
        d[j] = tmp;
        }
    static void swaps(String []value, int i,int j) { 
        String tmp = value[i]; 
        value[i] = value[j]; 
        value[j] = tmp;
        }        

    static void bubble_sort(int [] data, String [] names)  {
        int t = 0;
        int n= data.length;
        String [] selectedNames = new String[n];
        boolean swapped;
    
        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                if (data[j] < data[j + 1]) {
                    swap(data, j, j + 1);
                    swaps(names, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) {
                break; // If no swaps were made, the array is already sorted
            }
        }
        for (int i = 0; i < n ; i++) {
            if (data[i]>500) {
                selectedNames[t]= names[i];
                t++;
            }
        }
            System.out.print("[");
            for (int i = 0; i < names.length; i++) {
                System.out.print("'" + names[i] + "'");
                if (i < names.length - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");
            System.out.println(Arrays.toString(data));
            
            for (int i = 0; i <selectedNames.length; i++) {
                if (!(selectedNames[i] == null)) {
                    System.out.print(selectedNames[i]);
                    System.out.print('\n'); 
                }
            }
        }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int size = scanner.nextInt();

        String [] names = new String[size];
        int[] values = new int[size];

        for (int i = 0; i < size; i++) {
            names[i] = scanner.next();
        }

        for (int i = 0; i < size; i++) {
            values[i] = scanner.nextInt();
        }

        bubble_sort(values,names);

    }
}