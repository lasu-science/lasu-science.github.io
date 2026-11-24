
clear;
clc;

// Constantes y parametros
g = 9.81;          // Gravedad [m/s^2]
rho = 1.225;       // Densidad del aire [kg/m^3]
A = 0.01;          // Area frontal [m^2]
Cd = 0.5;          // Coeficiente de arrastre

m0 = 10;           // Masa inicial [kg]
mdry = 6;          // Masa seca [kg]
mdot = 0.2;        // Caudal de propelente [kg/s]
Tmotor = 180;      // Empuje [N]

tburn = (m0-mdry)/mdot;

// Integracion temporal
dt = 0.01;
t = 0:dt:60;
N = length(t);

// Reservar memoria
y = zeros(1,N);
v = zeros(1,N);
m = zeros(1,N);
a = zeros(1,N);
T = zeros(1,N);
Fd = zeros(1,N);

// Condiciones iniciales
y(1) = 0;
v(1) = 0;

for i = 1:N-1

    // Masa y empuje instantaneos
    m(i) = max(mdry, m0-mdot*t(i));

    if t(i) < tburn then
        T(i) = Tmotor;
    else
        T(i) = 0;
    end

    // Resistencia aerodinamica con signo
    Fd(i) = 0.5*rho*A*Cd*v(i)*abs(v(i));

    // Segunda ley de Newton
    a(i) = (T(i)-m(i)*g-Fd(i))/m(i);

    // Euler explicito
    v(i+1) = v(i)+a(i)*dt;
    y(i+1) = y(i)+v(i)*dt;

end

m(N) = max(mdry, m0-mdot*t(N));
Fd(N) = 0.5*rho*A*Cd*v(N)*abs(v(N));
a(N) = (T(N)-m(N)*g-Fd(N))/m(N);

// Graficas
scf(0);
plot(t,y);
xtitle("Trayectoria vertical","Tiempo [s]","Altura [m]");
xgrid();

scf(1);
plot(t,v);
xtitle("Velocidad vertical","Tiempo [s]","Velocidad [m/s]");
xgrid();

scf(2);
plot(t,a);
xtitle("Aceleracion vertical","Tiempo [s]","Aceleracion [m/s^2]");
xgrid();

scf(3);
plot(t,m);
xtitle("Masa del cohete","Tiempo [s]","Masa [kg]");
xgrid();


// Reservar espacio para los resultados
h = zeros(1, length(t));
v = zeros(1, length(t));
a = zeros(1, length(t));

// Estado inicial
h(1) = h0;
v(1) = v0;

// Simulacion numerica
for i = 1:length(t)-1

    a(i) = (T - m*g)/m;

    v(i+1) = v(i) + a(i)*dt;

    h(i+1) = h(i) + v(i)*dt;

end

a($) = (T - m*g)/m;

// Graficar resultados
scf(0);
plot(t, h);
xtitle("Altura del cohete", "Tiempo [s]", "Altura [m]");
xgrid();

scf(1);
plot(t, v);
xtitle("Velocidad del cohete", "Tiempo [s]", "Velocidad [m/s]");
xgrid();

scf(2);
plot(t, a);
xtitle("Aceleracion del cohete", "Tiempo [s]", "Aceleracion [m/s^2]");
xgrid();
