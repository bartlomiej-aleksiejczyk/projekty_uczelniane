import java.io.File;

public class Z3 {
    public static <t> void wypiszbezrozszerzenia(File plik,String rozszerzenie) {
        String[] etap1 = plik.list((katalog, nazwa)-> (new File((katalog.toString())+"/"+nazwa)).isFile());
        for(String element: etap1){
            if (element.endsWith(rozszerzenie)==false){
                System.out.print(element);
            }
        }
    }
    public static void main(String[] args) {
        File plik= new File(".");
        wypiszbezrozszerzenia(plik,".iml");


    }
}
