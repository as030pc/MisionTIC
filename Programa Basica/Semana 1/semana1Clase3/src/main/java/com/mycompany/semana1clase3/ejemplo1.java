
package com.mycompany.semana1clase3;
import java.util.Scanner;

public class ejemplo1 {

    public static void main(String[] args) {
        /*
        //Manejo de string
        String nombre = "Juan";
        System.out.println("");
        System.out.println("El nombre tiene "+nombre.length()+ " caracteres");
        System.out.println("La segunda letra de: "+ nombre + "es:" +nombre.charAt(2));
       
        //Para pedir informacion por consola
        Scanner sc = new Scanner(System.in);
        System.out.println("Favor escriba su nombre");  // Se usa para crear un input
        String nombre2 = sc.nextLine();
        System.out.println("Bienvenido " + nombre2);
        
        
        //Uso de swith
        
        Scanner scanner2 = new Scanner(System.in);
        System.out.println("Ingrese un dia de la semana");
        
        int v = scanner2.nextInt();
        
        String dia;
       
        switch (v) {
            case 1:
                dia = "Lunes";
                break;
            case 2:
                dia = "Martes";
                break;
            case 3:
                dia = "Miercoles";
             break;
             
           
            
                
            default:
                dia = "Dia Incorrecto";
        }
        
        System.out.println("El dia de la semana es "+ dia);
        
        */
        

        
        /*
        // Ciclos
        
        //1.While y Do -WHILE
 
        System.out.println(Math.random()*100);
        
        // refundicion para convertir a entero
        int aleatorio = (int)(Math.random()*100);
        int numero = 0;
        int intentos =0;
        Scanner entra = new Scanner(System.in);
        
        while (numero != aleatorio) {
        intentos++;
            System.out.println("Escriba un numero");
            numero = entra.nextInt();
            
            if(aleatorio<numero) {
                System.out.println("El numero secreto es menor");
            }
            else if (aleatorio > numero) {
                System.out.println("El numero secreto es mayor");
            }     
        
        }
        
        System.out.println("Reto logrado");
        */
        
        
        // 2. Ciclo for
        for (int numero =1;numero<=100; numero++) {
            System.out.print(numero+ " ");
        }
        
        int numero = 1;
        while(numero <=100) {
            System.out.println(numero);
            numero++;
        }
        
        
    }
    
}
