 /*Rotation w.r.t the centroid*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <graphics.h>

void drawTriangle(int x1, int y1, int x2, int y2, int x3, int y3) {
line(x1, y1, x2, y2);
line(x2, y2, x3, y3);
line(x3, y3, x1, y1);
}

void rotateTriangle(int x1, int y1, int x2, int y2, int x3, int y3, float angle) {
    // Calculate centroid
int centroid_x = (x1 + x2 + x3) / 3;
int centroid_y = (y1 + y2 + y3) / 3;

    // Convert angle from degrees to radians
float radian = angle * (M_PI / 180.0);

    // Apply rotation transformation to each vertex
int new_x1 = centroid_x + (x1 - centroid_x) * cos(radian) - (y1 - centroid_y) * sin(radian);
int new_y1 = centroid_y + (x1 - centroid_x) * sin(radian) + (y1 - centroid_y) * cos(radian);
int new_x2 = centroid_x + (x2 - centroid_x) * cos(radian) - (y2 - centroid_y) * sin(radian);
int new_y2 = centroid_y + (x2 - centroid_x) * sin(radian) + (y2 - centroid_y) * cos(radian);
int new_x3 = centroid_x + (x3 - centroid_x) * cos(radian) - (y3 - centroid_y) * sin(radian);
int new_y3 = centroid_y + (x3 - centroid_x) * sin(radian) + (y3 - centroid_y) * cos(radian);

    // Draw the rotated triangle
setcolor(CYAN);
drawTriangle(new_x1, new_y1, new_x2, new_y2, new_x3, new_y3);
}

int main() {
int gd, gm;
gd = DETECT;
initgraph(&gd, &gm, "");

    // Coordinates of the original triangle
int x1 = 200, y1 = 200;
int x2 = 100, y2 = 300;
int x3 = 300, y3 = 300;

    // Draw the original triangle
drawTriangle(x1, y1, x2, y2, x3, y3);

    // Rotate the triangle by 30 degrees
float angle = 30.0;
rotateTriangle(x1, y1, x2, y2, x3, y3, angle);

delay(50000); // Delay for 5 seconds to see the result

closegraph();

return 0;
}

