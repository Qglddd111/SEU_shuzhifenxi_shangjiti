#include <iostream>
#include <cmath>
#include <fstream>

const double PI = 3.14159265358979323846;

// 计算阶乘
double factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

// 计算泰勒展开的值
double taylorExpansion(double x, int n) {
    double result = 0;
    int n_tem;
    if (n==1)
        n_tem=0;
    else if (n==2)
        n_tem=0;
    else if (n==3)
        n_tem=1;
    else if (n==4)
        n_tem=1;
    else if (n==5)
        n_tem=2;
    else n_tem=2;
    for (int i = 0; i <= n_tem; ++i) {
        double numerator = std::pow(-1, i) * std::pow(x, 2*i+1);
        double denominator = factorial(2*i + 1);
        result += numerator / denominator;
    }
    return result;
}

int main() {
    int n;
    std::cout << "请输入展开的次数 n：";
    std::cin >> n;

    std::ofstream outputFile("taylor_expansion5.txt");
    if (!outputFile.is_open()) {
        std::cout << "无法打开文件！" << std::endl;
        return 1;
    }

    // 绘制泰勒展开的图像
    int numPoints = 1000;  // 绘制的点数
    double stepSize = 2 * PI / numPoints;
    for (int i = 0; i < numPoints; ++i) {
        double x = -PI + i * stepSize;
        double y = taylorExpansion(x, n);
        outputFile << x << " " << y << std::endl;
        
    }

    outputFile.close();

    std::cout << "图像已保存到 taylor_expansion.txt" << std::endl;

    return 0;

}
