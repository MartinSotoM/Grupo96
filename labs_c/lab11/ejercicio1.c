#include <stdio.h>

int main()
{
    int N, contador = 0;
    printf("Ingrese un valor límite:");
    scanf("%d", &N);

    for (int i = 0; i <= N; i++) {
        if (i%2 == 0){
            printf("Números pares: %d\n",i);
            contador += 1;
        }
    }

    printf("\nCantidad total de pares: %d", contador);

    return 0;
}