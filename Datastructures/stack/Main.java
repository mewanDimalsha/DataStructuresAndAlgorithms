import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();
        int Z = sc.nextInt();
        int[][] matrix = new int[X][Y];
        for (int i = 0; i < X; i++) {
            for (int j = 0; j < Y; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        rotateMatrix(X, Y, Z, matrix);
    }

    static void rotateMatrix(int X, int Y, int Z, int[][] matrix) {
        int numRings = Math.min(X, Y) / 2;
        for (int i = 0; i < numRings; i++) {
            List<Integer> temp = new ArrayList<>();
            for (int j = i; j < Y - i; j++)
                temp.add(matrix[i][j]);
            for (int j = i + 1; j < X - i; j++)
                temp.add(matrix[j][Y - i - 1]);
            for (int j = i + 1; j < Y - i; j++)
                temp.add(matrix[X - i - 1][Y - j - 1]);
            for (int j = i + 1; j < X - i - 1; j++)
                temp.add(matrix[X - j - 1][i]);

            Collections.rotate(temp, Z % temp.size());

            int idx = 0;
            for (int j = i; j < Y - i; j++)
                matrix[i][j] = temp.get(idx++);
            for (int j = i + 1; j < X - i; j++)
                matrix[j][Y - i - 1] = temp.get(idx++);
            for (int j = i + 1; j < Y - i; j++)
                matrix[X - i - 1][Y - j - 1] = temp.get(idx++);
            for (int j = i + 1; j < X - i - 1; j++)
                matrix[X - j - 1][i] = temp.get(idx++);
        }

        printMatrix(X, Y, matrix);
    }

    static void printMatrix(int X, int Y, int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}
