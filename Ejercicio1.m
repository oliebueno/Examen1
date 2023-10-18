//Ejercicio 2.1
#import <Foundation/Foundation.h>

// Función que rota una cadena de caracteres dado una cadena de caracteres y un entero
NSString *rotar(NSString *w, int k) {
    NSString *cadena = w; //Cadena de caracteres
    int movimiento; //Veces que se rotara la cadena de caracteres
    int tam = [cadena length];

    movimiento = k % tam; //Se calcula este modulo para no hacer rotaciones imnecesarias

    //Si la cadena no rota. devuelve la cadena original
    if(movimiento == 0) {
        return cadena;
    }else { //Rota la cadena la cantidad de veces que el usuario indico
        int i = movimiento;
        while(i > 0) {
            NSString *uno = [cadena substringToIndex:1];    
            cadena = [cadena substringFromIndex:1];
            cadena = [cadena stringByAppendingString:uno];
            i = i - 1;
        }
        return cadena;
    }
}

//Programa principal
int main(int argc, char *argv[]) {
    
    // Se para administrar la memoria de los objetos que se marcan como autoliberados, como los NSString
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    // Se verificar que se hayan ingresado dos argumentos
    if (argc != 3) {
        NSLog(@"Se requieren dos argumentos: una cadena y un número");
        return 1;
    }
        
    // Se convertir el primer argumento en un objeto NSString
    NSString *w = [NSString stringWithUTF8String:argv[1]];

    // Se convertir el segundo argumento en un entero
    int k = atoi(argv[2]);

    // Llamar a la función rotar con la cadena y el número
    NSString *ro = rotar(w, k);
    
    // Imprime el resultado
    NSLog(@"El resultado es: %@", ro);
    
    [pool drain];
    return 0;
}
