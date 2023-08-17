#include <stdio.h>
#include <conio.h>
#include <graphics.h>

// Bezier curve function
int bezier(int p0, int p1, int p2, int p3, double t) {
    double t2 = t * t;
    double t3 = t2 * t;
    
    // Bezier basis functions
    double b1 = -t3 + 3 * t2 - 3 * t + 1;
    double b2 = 3 * t3 - 6 * t2 + 3 * t;
    double b3 = -3 * t3 + 3 * t2;
    double b4 = t3;
    
    // Calculate and return the point on the Bezier curve
    return (int) (b1 * p0 + b2 * p1 + b3 * p2 + b4 * p3);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TC\\BGI"); // Update the path according to your setup
    
    int p0x = 100, p0y = 100; // Start point
    int p1x = 150, p1y = 300; // Control point 1
    int p2x = 300, p2y = 50;  // Control point 2
    int p3x = 400, p3y = 200; // End point
    
    double t;
    int x, y;
    
    setcolor(WHITE);
    line(p0x, p0y, p1x, p1y); // Draw the control lines in white
    line(p2x, p2y, p3x, p3y);
    
    setcolor(YELLOW);
    for (t = 0; t <= 1; t += 0.01) {
        x = bezier(p0x, p1x, p2x, p3x, t);
        y = bezier(p0y, p1y, p2y, p3y, t);
        putpixel(x, y, YELLOW);
    }
    
    getch();
    closegraph();
    return 0;
}

