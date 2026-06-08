#include <stdio.h>

struct Sensor {
    int id;
    float medicion;
};

int main()
{
    struct Sensor mi_sensor = {1, 25.5};
    printf("ID sensor: %d\nMedición sensor: %d\n", mi_sensor.id, mi_sensor.medicion);
    
    return 0;
}