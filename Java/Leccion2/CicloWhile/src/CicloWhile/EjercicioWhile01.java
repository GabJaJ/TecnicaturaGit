
package CicloWhile;


public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0;//inferencia de tipos
        while(conteo <= 7) {
            System.out.println("conteo = " + conteo); 
            conteo++; // vamos aumentando en uno la variable
        }
        
        var contador = 0;
        do{                 //ciclo DoWhile 
            System.out.println("contador = " + contador);
            contador++;   //para que no entre en un ciclo infinito
        }while(contador < 7); // en Dowhile es necesario finalizar con el ";" punto y coma
        
        for(var contando = 0; contando < 7; contando++) {
            System.out.println("contando = " + contando);
        }    //en ciclo FOR podemos trabajar sin llaves "{}" en caso de que sea una linea simple
        
        
        
        //for(var contador = 7; contador > 0; contador--) para decremento
        
        for(var contando = 0; contando < 7; contando++) {
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break;
            }
            
        }  
        
        
        for(var contando = 0; contando < 7; contando++) {
            if(contando % 2 != 0){
                continue;
            }
            System.out.println("contando = " + contando);
        }  
    }
}
