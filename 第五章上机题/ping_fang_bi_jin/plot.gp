set terminal pngcairo size 800,600
set output 'chaifen5.png'
set title 'n=5'
set xlabel 'x'
set ylabel 'y'
plot 'data5.txt' with lines lt 1 lc rgb 'blue' title "chaifen_5",\
     sin(x) with lines title 'sin(x)'