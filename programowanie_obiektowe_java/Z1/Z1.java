import java.time.LocalTime;
import java.util.Arrays;

public class Z1 {
    public class ArrayUtil{
        public static <t extends Comparable> boolean jestPailandromem(t[] tablica) {
            t[] tablicapomocnicza = tablica.clone();
            int j = 0;
            for (int i = tablica.length - 1; i >= 0; i--) {
                tablicapomocnicza[j] = tablica[i];
                j++;
            }
            for(int k =0; k<tablica.length;k++){
                //System.out.println(tablica[k]);
                //System.out.println(tablicapomocnicza[k]);
                if(!tablica[k].equals(tablicapomocnicza[k])) return false;
            }
            return true;
        }
    }
    public static void main(String[] args) {
        Integer[] tablica_próbna={1,2,2,1};
        System.out.println(ArrayUtil.jestPailandromem(tablica_próbna));
        Arrays.parallelSort(tablica_próbna);
        System.out.println(ArrayUtil.jestPailandromem(tablica_próbna));
        LocalTime[] tablica_localt ={LocalTime.of(21,11),LocalTime.of(11,11),LocalTime.of(21,11)};
        System.out.println(ArrayUtil.jestPailandromem(tablica_localt));
        Arrays.sort(tablica_localt);
        System.out.println(ArrayUtil.jestPailandromem(tablica_localt));
    }
}

