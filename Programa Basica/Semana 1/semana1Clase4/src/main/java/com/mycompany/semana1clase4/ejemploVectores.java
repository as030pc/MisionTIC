
package com.mycompany.semana1clase4;

public class ejemploVectores {

    public static void main(String[] args) {
        int[] la_matriz = new int[5];
        int la_matriz2[] = new int[3]; //creacion de la matriz
        
        la_matriz[0] = 5;              // inicializacion de la matriz
        la_matriz[1] = 32;
        la_matriz[2] = -7;
        la_matriz[3] = 12;
        la_matriz[4] = 8;
        
        
        
        System.out.println(la_matriz[4]);
        System.out.println(la_matriz[0]);
        
        //Para mostrar todos los elementos de la matriz
        
        for(int i=0; i<5; i++) {
            System.out.print(la_matriz[i] + " ");
            
        }
        
        int[] otra_matriz = {46, 32, -7, 12, 8}; //Otra manera de crear e inicializar una matriz
        for(int i=0;i <otra_matriz.length;i++) {
            System.out.print(otra_matriz[i] + " ");
        }

    }
    
}
