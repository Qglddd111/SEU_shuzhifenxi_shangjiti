set terminal pngcairo size 800,600
set output 'merged_test.png'
set title 'compare'
set xlabel 'x'
set ylabel 'y'

# 设置布局和边距
#set multiplot layout 1,1 margins 0.05, 0.95, 0.1, 0.9 spacing 0.05

# 绘制第一条线（从数据文件中读取）
plot 'taylor_expansion5.txt' with lines lt 1 lc rgb "blue" title "Function 1", \
     sin(x) with lines title 'sin(x)'
