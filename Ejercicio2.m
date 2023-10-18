//Ejercicio 2.1
#import <Foundation/Foundation.h>
#include <stdio.h>
#include <stdlib.h>

int N; // Tamño de la matriz

//Función que traspone una matriz cuadrada
void transponer(int A[N][N], int AT[N][N]) {
    int i = 0;
    int j = 0;
    while (i < N) {
        while (j < N) {
            AT[i][j] = A [j][i];
            j = j + 1;
        }
        i = i + 1;
        j = 0;
    }
};

//Función que ejecuta el producto cruz de dos matrices cuadradas 
void producto(int A[N][N], int AT[N][N], int C[N][N]) {
    int i = 0;
    int j = 0;
    int k = 0;
    while (i < N) {
        while (j < N) {
            C[i][j] = 0;
            while (k < N) {
                C[i][j] = C[i][j] + A[i][k] * AT[k][j];
                k = k + 1;
            }
            k = 0;
            j = j + 1;
        }
        j = 0;
        i = i + 1;
    }
};


// Función que imprime una matriz
void imprimir(int A[N][N]) {
    int i = 0;
    int j = 0;
    while (i < N) {
        while (j < N) {
            printf("%d ", A[i][j]);
            j = j + 1;
        }
        i = i + 1;
        j = 0;
        printf("\n");
    }
};

void introducir(int A[N][N]) {
    printf("Introduce los elementos de la matriz separados con un espacio:\n");
    int i = 0;
    int j = 0;
    while (i < N) {
        while (j < N) {
            scanf("%d", &A[i][j]);
            j = j + 1;
        }
        i = i + 1;
        j = 0;
        printf("\n");
    }
}

int main(int argc, char *argv[]) {

    // Se verifica que se haya pasado un argumento
    if (argc < 2) {
        printf("Error: se debe pasar el tamaño de la matriz como argumento\n");
        return 1;
    }
    // Convertir el argumento a un entero
    N = atoi(argv[1]);

    // Se verifica que el valor sea válido y mayor que cero
    if (N <= 0) {
        printf("Error: el tamaño de la matriz debe ser un número positivo\n");
        return 1;
    }

    // Se definen las matrices a usar
    int A[N][N], AT[N][N], C[N][N];

    // Se llena la matriz
    introducir(A);
    // Se traspone la matriz
    transponer(A, AT);
    // Se multiplica A con su traspuesta
    producto(A, AT, C);
    // Se imprime el la matriz resultante
    imprimir(C);
}