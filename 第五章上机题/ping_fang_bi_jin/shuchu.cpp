#include <iostream>
#include <fstream>
#include <cmath>

int main() {
    // 打开输出文件流
    std::ofstream fout("data5.txt");

    // 生成x坐标值，计算对应的y值，并输出到文件
    for (int i = 0; i < 1000; ++i) {
        double xi = -M_PI + i * 2.0 * M_PI / 1000.0;
        double yi = 0.98786214*xi-0.15527141*xi*xi*xi+0.00564312*xi*xi*xi*xi*xi;
        fout << xi << " " << yi << std::endl;
    }

    // 关闭输出文件流
    fout.close();

    return 0;
}


