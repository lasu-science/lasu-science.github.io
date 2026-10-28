
clear;
clc;
clf;

// ==========================================
// 1. PARAMETROS DEL SISTEMA
// ==========================================

G = 1;
m = [1; 1; 1];

dt = 0.001;
Tfinal = 6.3259;
N = round(Tfinal / dt) + 1;
t = (0:N-1) * dt;

// Posiciones iniciales: una fila por cuerpo
r = [
   0.97000436, -0.24308753;
  -0.97000436,  0.24308753;
   0.0,         0.0
];

// Velocidades iniciales
v = [
   0.466203685,  0.43236573;
   0.466203685,  0.43236573;
  -0.932407370, -0.86473146
];

// Memoria para resultados
R = zeros(N, 3, 2);
V = zeros(N, 3, 2);
E = zeros(N, 1);

R(1,:,:) = matrix(r, 1, 3, 2);
V(1,:,:) = matrix(v, 1, 3, 2);

// ==========================================
// 2. ACELERACION GRAVITATORIA
// ==========================================

function a = gravedad(r, m, G)
    a = zeros(3, 2);

    for i = 1:3
        for j = 1:3
            if i <> j then
                dr = r(j,:) - r(i,:);
                d = sqrt(sum(dr.^2));

                // Evitar division por cero
                if d < 1e-10 then
                    error("Dos cuerpos estan demasiado cerca.");
                end

                a(i,:) = a(i,:) + G*m(j)*dr/(d^3);
            end
        end
    end
endfunction

// ==========================================
// 3. ENERGIA MECANICA TOTAL
// ==========================================

function Et = energia(r, v, m, G)
    Ec = 0;
    Ep = 0;

    for i = 1:3
        Ec = Ec + 0.5*m(i)*sum(v(i,:).^2);

        for j = i+1:3
            dr = r(j,:) - r(i,:);
            d = sqrt(sum(dr.^2));
            Ep = Ep - G*m(i)*m(j)/d;
        end
    end

    Et = Ec + Ep;
endfunction

// ==========================================
// 4. INTEGRACION: VELOCITY VERLET
// ==========================================

a = gravedad(r, m, G);
E(1) = energia(r, v, m, G);

for k = 1:N-1

    // Actualizar posiciones
    rnew = r + v*dt + 0.5*a*dt^2;

    // Calcular aceleraciones en las posiciones nuevas
    anew = gravedad(rnew, m, G);

    // Actualizar velocidades
    vnew = v + 0.5*(a + anew)*dt;

    // Avanzar el estado
    r = rnew;
    v = vnew;
    a = anew;

    // Guardar resultados
    R(k+1,:,:) = matrix(r, 1, 3, 2);
    V(k+1,:,:) = matrix(v, 1, 3, 2);
    E(k+1) = energia(r, v, m, G);

end

// ==========================================
// 5. GRAFICAR LAS TRAYECTORIAS
// ==========================================

scf(0);
clf();

plot( ...
    matrix(R(:,1,1), -1, 1), ...
    matrix(R(:,1,2), -1, 1), "r", ...
    matrix(R(:,2,1), -1, 1), ...
    matrix(R(:,2,2), -1, 1), "g", ...
    matrix(R(:,3,1), -1, 1), ...
    matrix(R(:,3,2), -1, 1), "b");

xgrid();
xlabel("x");
ylabel("y");
title("Problema de los tres cuerpos - Velocity Verlet");
legend("Cuerpo 1", "Cuerpo 2", "Cuerpo 3");

// ==========================================
// 6. ERROR RELATIVO DE ENERGIA
// ==========================================

E0 = E(1);
errorE = abs((E - E0) / E0);

scf(1);
clf();
plot(t, errorE);
xgrid();
xlabel("Tiempo");
ylabel("|(E - E0) / E0|");
title("Error relativo de energia mecanica");

disp("Energia inicial:");
disp(E0);

disp("Maximo error relativo de energia:");
disp(max(errorE));
