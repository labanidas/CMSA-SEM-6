//Rotate a triangle with coordinates (200,100), (100,300), (300,300) by 30 degrees with respect to the, a/ Origin b/ Centroid. 
//Code: 
/*Rotation w.r.t the origin*/
#include <stdio.h>
#include <math.h>
#include <graphics.h>

// Function to rotate a point (x, y) by angle theta
void rotatePoint(int* x, int* y, double theta) {
double radian = (theta * 3.14159) / 180.0;
int tempX = *x;
int tempY = *y;

    *x = round(tempX * cos(radian) - tempY * sin(radian));
    *y = round(tempX * sin(radian) + tempY * cos(radian));
}
// Function to rotate a triangle by angle theta
void rotateTriangle(int x1, int y1, int x2, int y2, int x3, int y3, double theta) {
    // Rotate each vertex of the triangle
rotatePoint(&x1, &y1, theta);
rotatePoint(&x2, &y2, theta);
rotatePoint(&x3, &y3, theta);

    // Draw the rotated triangle
setcolor(YELLOW); 
line(x1, y1, x2, y2);
line(x2, y2, x3, y3);
line(x3, y3, x1, y1);
}
int main() {
int gd, gm;
gd = DETECT;
    // Initialize graphics mode
initgraph(&gd, &gm, NULL);
    // Set color to white
setcolor(WHITE);
    // Define the coordinates of the triangle
int x1 = 300, y1 = 100;
int x2 = 400, y2 = 200;
int x3 = 200, y3 = 200;
    // Draw the original triangle
line(x1, y1, x2, y2);
line(x2, y2, x3, y3);
line(x3, y3, x1, y1);
    // Rotate the triangle by 30 degrees
double theta = 30;
rotateTriangle(x1, y1, x2, y2, x3, y3, theta);
    // Delay to see the result
delay(5000);
    // Close graphics mode
closegraph();
return 0;
}

