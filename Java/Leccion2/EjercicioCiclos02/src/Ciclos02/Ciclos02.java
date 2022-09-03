/*
Ejercicio 2: Leer un numero e identificar si es positivo o 
negativo. El proceso se repetira hasta que se introduzca
un cero "0" con 
*/

package Ciclos02;

import javax.swing.JOptionPane;


public class Ciclos02 {
       public static void main(String[] args) {
        

        
        var numero  = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")); //JopcionPane trabaja con tipos string
        while(numero != 0){ //Mientras el numero sea igual a cero o positivo
            if(numero > 0){
                    JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
                } 
                else{
                     JOptionPane.showMessageDialog(null, "El numero "+numero+" es NEGATIVO");

                }
               numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
           }
            JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa");
    }
}
