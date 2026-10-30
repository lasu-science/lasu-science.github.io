clear;
clc;

// Sobrevuelo hiperbolico en el modelo de dos cuerpos (Luna-nave).
// Todas las distancias estan en metros y las velocidades en m/s.
muLuna = 4.9048695e12;       // Parametro gravitacional lunar [m^3/s^2]
radioLuna = 1.7374e6;        // Radio medio lunar [m]
altitudPerilunio = 100e3;    // Altitud minima sobre la superficie [m]
velocidadInfinita = 1.6e3;   // Velocidad asintotica relativa a la Luna [m/s]

radioPerilunio = radioLuna + altitudPerilunio;
excentricidad = 1 + radioPerilunio * velocidadInfinita^2 / muLuna;
parametroOrbital = radioPerilunio * (1 + excentricidad);

// Se dibuja el tramo entre -90 y +90 grados de anomalia verdadera.
numeroPuntos = 1201;
anomalia = linspace(-%pi / 2, %pi / 2, numeroPuntos);
distancia = parametroOrbital ./ (1 + excentricidad * cos(anomalia));
xNave = distancia .* cos(anomalia);
yNave = distancia .* sin(anomalia);

// Circulo lunar a escala, con el mismo numero de puntos que la trayectoria.
anguloLuna = linspace(0, 2 * %pi, numeroPuntos);
xLuna = radioLuna * cos(anguloLuna);
yLuna = radioLuna * sin(anguloLuna);

scf(0);
plot2d([xNave' xLuna'], [yNave' yLuna'], [2 5]);
xtitle("Sobrevuelo lunar hiperbolico (modelo de dos cuerpos)", ...
       "Distancia X respecto al centro lunar [m]", ...
       "Distancia Y respecto al centro lunar [m]");
xgrid();

// Iguala la escala de ambos ejes: una misma distancia ocupa lo mismo en X e Y.
ejes = gca();
ejes.data_bounds = [-6e6, -6e6; 6e6, 6e6];
isoview("on");
