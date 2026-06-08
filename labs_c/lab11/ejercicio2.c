#include <stdio.h>

void duplicarValor(int *numero) {
    *numero *= 2;
}

int main()
{
    int voltaje = 12;

    printf("Valor de voltaje: %d\n", voltaje);
    duplicarValor(&voltaje);

    printf("Valor actual de voltaje: %d\n", voltaje);
    return 0;
}