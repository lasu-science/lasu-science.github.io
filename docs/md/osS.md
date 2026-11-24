# Proyecto Solaris

## Informe de investigación conceptual

**Estado:** investigación preliminar  
**Fecha:** agosto de 2026  
**Naturaleza:** documento técnico-conceptual

---

## 1. Resumen ejecutivo

El Proyecto Solaris estudia una arquitectura espacial orientada a reducir la dependencia de grandes lanzamientos individuales mediante el desarrollo progresivo de infraestructura orbital modular, desplegable y energéticamente interconectada.

El principio general consiste en separar el problema espacial en distintos regímenes físicos y asignar a cada uno la tecnología más adecuada. La arquitectura estudiada combina:

- reducción de pérdidas atmosféricas mediante elevación previa;
- propulsión química para los incrementos de velocidad que todavía resulten necesarios;
- investigación de aceleración electromagnética externa;
- despliegue orbital mediante estructuras plegables, inflables y sistemas robóticos;
- grandes superficies solares;
- transmisión de energía mediante radiación electromagnética;
- láseres orbitales;
- velas solares y velas impulsadas por haces;
- radiadores de gran superficie;
- estructuras estabilizadas o desplegadas mediante rotación.

El objetivo no es sustituir inmediatamente al cohete convencional, sino determinar hasta qué punto una arquitectura modular puede trasladar parte de las funciones tradicionalmente realizadas por una única etapa de lanzamiento hacia infraestructura terrestre y orbital.

La hipótesis central es:

> **La infraestructura espacial puede crecer a partir de pequeños módulos funcionales si el diseño prioriza una elevada relación entre capacidad desplegada y masa de lanzamiento.**

---

# 2. Antecedentes y motivación

La investigación comenzó con el problema de mantener un vehículo sobre un punto terrestre situado fuera del ecuador.

Se consideró inicialmente la posibilidad de mantener un satélite sobre una posición fija a latitud aproximada de 34°51'33.8" S, mediante control continuo de su velocidad y dirección.

Una órbita geoestacionaria convencional exige necesariamente una órbita ecuatorial. Sin embargo, un vehículo puede permanecer sobre una determinada región terrestre mediante una combinación de fuerzas no gravitacionales, siempre que se proporcione continuamente la aceleración necesaria para compensar la dinámica orbital natural.

Esto conduce a una conclusión importante:

> Una órbita no ecuatorial puede ser mantenida artificialmente, pero deja de ser una órbita geoestacionaria kepleriana convencional y pasa a ser una trayectoria controlada activamente.

Se estudió inicialmente propulsión iónica para realizar estas correcciones. El análisis mostró rápidamente que, para mantener indefinidamente una posición no ecuatorial, el propelente y la masa del sistema de propulsión pueden superar ampliamente la masa de la carga útil.

La vela solar apareció entonces como alternativa por no requerir propelente convencional. Sin embargo, su aceleración está condicionada por la dirección de la radiación incidente.

La geometría Sol–vela se convirtió así en una restricción fundamental.

---

# 3. Propulsión fotónica y energía externa

La presión de radiación sobre una superficie perfectamente reflectante puede aproximarse mediante:

\[
P_{\rm rad}=\frac{2I}{c}.
\]

La fuerza correspondiente es:

\[
F=P_{\rm rad}A.
\]

Por tanto, la aceleración específica depende directamente de la relación superficie/masa:

\[
\frac{F}{m}
=
\frac{2I}{c}\frac{A}{m}.
\]

La variable de diseño fundamental para una vela es, por tanto, \(A/m\).

Esto llevó a estudiar una arquitectura en la que la fuente de energía no estuviera necesariamente instalada sobre el vehículo.

Durante la iluminación solar directa, la vela puede utilizar radiación solar. Durante eclipses o cuando la geometría orbital resulte desfavorable, una infraestructura externa podría proporcionar un haz dirigido.

Los láseres orbitales fueron considerados como posible solución debido a que permiten transferir energía y momento sin una conexión física entre la fuente y el vehículo.

Esta idea es conceptualmente similar al principio de propulsión por haces de energía empleado en propuestas de velas impulsadas por láser, aunque su implementación orbital plantea problemas considerables de potencia, óptica, control térmico y apuntado.

---

# 4. Transmisión de energía en el vacío

Se examinó la posibilidad de distribuir energía entre satélites sin utilizar conductores físicos.

El vacío no actúa como un conductor eléctrico convencional. Sin embargo, tampoco constituye una barrera para la propagación de campos electromagnéticos.

Una arquitectura de transmisión puede representarse conceptualmente como:

**generación eléctrica → conversión → emisor → propagación electromagnética → receptor → conversión eléctrica.**

Las tecnologías candidatas incluyen microondas y láseres.

La ventaja potencial consiste en permitir que una red orbital comparta energía sin necesidad de interconectar físicamente todos sus módulos.

La principal dificultad no es la posibilidad física de la transmisión, sino su eficiencia global. Las pérdidas de conversión, divergencia del haz, tamaño de los emisores y receptores, control de apuntado y disipación térmica deben incluirse en cualquier análisis realista.

---

# 5. El problema de la potencia

Una arquitectura basada en láseres de alta potencia requiere una fuente energética considerable.

Para potencias del orden de megavatios, paneles solares convencionales de pequeño tamaño resultan insuficientes. La solución estudiada consiste en construir grandes superficies solares orbitales mediante módulos desplegables.

La arquitectura propuesta es incremental:

**módulo → nodo energético → red → infraestructura de gran potencia.**

Cada lanzamiento debe aportar una capacidad funcional independiente y, posteriormente, integrarse con los módulos anteriores.

Este principio evita depender de un único lanzamiento de gran tamaño.

---

# 6. El problema térmico

La conversión y transmisión de grandes cantidades de energía genera calor residual.

En vacío, la disipación térmica depende principalmente de la radiación:

\[
P=\epsilon\sigma AT^4.
\]

Por tanto:

\[
A=\frac{P}{\epsilon\sigma T^4}.
\]

El área radiadora requerida disminuye al aumentar la temperatura de operación, pero los materiales y componentes imponen límites térmicos.

Una infraestructura orbital de alta potencia necesita, por tanto, radiadores de gran superficie.

Los radiadores constituyen una de las aplicaciones principales del concepto de despliegue compacto: una estructura relativamente pequeña durante el lanzamiento puede transformarse en una superficie térmica considerable una vez en órbita.

---

# 7. El problema del lanzamiento

El estudio de Solaris volvió posteriormente al acceso orbital.

La dificultad fundamental es la dependencia cuadrática del arrastre aerodinámico:

\[
F_D=\frac12\rho A C_Dv^2.
\]

A velocidades elevadas, la atmósfera se convierte en una penalización importante.

Esto llevó a reconsiderar una arquitectura basada exclusivamente en una centrifugadora terrestre capaz de acelerar una carga hasta velocidades suborbitales.

El problema es que la velocidad debe adquirirse mientras el vehículo continúa atravesando la atmósfera. La energía cinética puede ser elevada, pero el arrastre aumenta aproximadamente con \(v^2\).

La conclusión fue que deben estudiarse métodos capaces de separar la adquisición de altura de la adquisición de velocidad.

---

# 8. Elevación mediante globos

El principio de Arquímedes proporciona:

\[
\vec E=-\rho_{\rm aire}V\vec g.
\]

Para una magnitud vertical positiva:

\[
E=\rho_{\rm aire}Vg.
\]

La condición de flotación es:

\[
\rho_{\rm aire}V>m.
\]

Para un sistema formado por envolvente, gas, estructura y carga útil:

\[
m_{\rm total}
=
m_{\rm seco}
+
\rho_{\rm gas}V.
\]

La capacidad de carga útil queda determinada por:

\[
m_{\rm útil}
=
(\rho_{\rm aire}-\rho_{\rm gas})V-m_{\rm seco}.
\]

Por tanto, el objetivo no consiste en maximizar la densidad del gas, sino en minimizarla manteniendo las propiedades necesarias de seguridad, permeabilidad, temperatura y presión.

Los candidatos principales son hidrógeno y helio. El hidrógeno proporciona mayor capacidad de sustentación específica, mientras que el helio presenta ventajas operativas por su carácter no inflamable.

La densidad atmosférica disminuye con la altura. Como aproximación inicial puede utilizarse:

\[
\rho_{\rm aire}(h)
=
\rho_0e^{-h/H}.
\]

El modelo exponencial es útil para estimaciones iniciales, pero debe reemplazarse por un modelo atmosférico estándar en estudios de diseño.

El globo no permite alcanzar directamente el espacio. Su función consiste en elevar la carga hasta una región donde la densidad atmosférica sea mucho menor antes de iniciar la fase de aceleración.

---

# 9. Transición entre globo y propulsión

La transición entre un globo y un vehículo propulsado constituye un problema independiente.

Un ramjet no puede funcionar desde velocidad cero porque necesita flujo de aire suficiente para producir compresión y combustión.

Se consideraron varias secuencias:

- separación y encendido de un cohete;
- turbojet seguido de ramjet;
- aceleración inicial mediante un sistema auxiliar;
- transición posterior a propulsión cohete.

La secuencia general sería:

**separación → distanciamiento → estabilización → aceleración inicial → régimen propulsivo principal.**

La prioridad es evitar que el encendido produzca interacción térmica o mecánica perjudicial con el globo y garantizar que el vehículo alcance una configuración aerodinámica y de control estable antes de entrar en un régimen de alta aceleración.

---

# 10. Propulsión química desde gran altura

Una alternativa conceptualmente más sencilla consiste en utilizar el globo únicamente como plataforma de lanzamiento y encender posteriormente un cohete.

La velocidad orbital circular baja es aproximadamente 7.8–7.9 km/s. La rotación terrestre proporciona una contribución adicional para lanzamientos hacia el este:

\[
v_{\rm rot}=\omega R\cos\phi.
\]

Para una latitud aproximada de 35°:

\[
v_{\rm rot}\approx0.38\ {\rm km/s}.
\]

El incremento de velocidad restante continúa siendo del orden de varios kilómetros por segundo, y las pérdidas gravitatorias y aerodinámicas no desaparecen.

Por tanto, un globo puede reducir considerablemente la densidad atmosférica inicial, pero no elimina la necesidad de una etapa de alta relación de masas.

La ecuación de Tsiolkovski sigue siendo fundamental:

\[
\Delta v=v_e\ln\left(\frac{m_0}{m_f}\right).
\]

Para un \(I_{sp}\) de 320 s y un \(\Delta v\) ideal de 8 km/s:

\[
\frac{m_0}{m_f}\approx12.8.
\]

Esto demuestra que el problema dominante continúa siendo la masa estructural y propulsiva.

El TWR, en cambio, puede diseñarse para ser elevado incluso en vehículos pequeños.

---

# 11. Propulsión hipergólica

Los propelentes hipergólicos ofrecen una ventaja operacional relevante: el encendido puede realizarse mediante contacto entre los componentes, sin un sistema de ignición convencional.

Para una etapa pequeña pueden simplificar el sistema de encendido y almacenamiento.

Sin embargo, su toxicidad, masa de tanques, presurización y rendimiento deben compararse con otras familias de propelentes.

La conclusión preliminar es que una etapa hipergólica puede ser útil como sistema compacto de alta fiabilidad, pero no resuelve por sí misma el problema fundamental de la relación de masas orbital.

---

# 12. Aceleración electromagnética

Se consideró trasladar parte de la aceleración desde el vehículo hacia infraestructura externa.

La energía cinética específica es:

\[
\frac{E_k}{m}=\frac12v^2.
\]

Por ejemplo:

- 1 km/s corresponde a 0.5 MJ/kg;
- 3 km/s corresponde a 4.5 MJ/kg.

El interés de un acelerador electromagnético consiste en que esta energía puede suministrarse desde tierra en lugar de almacenarse completamente a bordo.

Las arquitecturas consideradas incluyen:

- coilguns;
- railguns;
- aceleradores lineales;
- mass drivers.

El problema fundamental pasa entonces del vehículo a la infraestructura: longitud, potencia, disipación, precisión, aceleración admisible, interacción atmosférica y resistencia estructural.

---

# 13. Campo magnético terrestre

Se estudió específicamente la posibilidad de aprovechar directamente el campo magnético terrestre.

La fuerza de Lorentz para un conductor es:

\[
\vec F=I\vec L\times\vec B.
\]

En magnitud:

\[
F=ILB
\]

cuando el conductor es perpendicular al campo.

Tomando un campo terrestre aproximado de \(30\ \mu{\rm T}\), un conductor de 100 m necesitaría corrientes del orden de cientos de kiloamperios para producir fuerzas de cientos de newtons.

Además, en un campo aproximadamente uniforme, las fuerzas sobre un circuito cerrado se compensan.

Por tanto, el campo magnético terrestre por sí solo no constituye una fuente práctica de empuje orbital significativa para un sistema pequeño.

La investigación electromagnética debe centrarse en campos artificiales producidos por infraestructura externa.

---

# 14. Despliegue orbital

La necesidad de construir grandes infraestructuras con pocos lanzamientos condujo a una de las líneas principales de Solaris.

Los tres mecanismos fundamentales identificados son:

1. **Gases**
2. **Robótica**
3. **Origami**

No son tecnologías excluyentes. Pueden utilizarse conjuntamente.

---

## 14.1. Gases

Las estructuras inflables permiten transformar pequeños volúmenes de lanzamiento en grandes volúmenes funcionales.

Aplicaciones:

- soportes;
- antenas;
- estructuras tensadas;
- radiadores;
- elementos de protección;
- estructuras temporales.

La ventaja principal es la elevada relación entre volumen desplegado y volumen almacenado.

---

## 14.2. Robótica

La robótica orbital permite:

- conectar módulos;
- desplegar segmentos;
- tensar cables;
- corregir geometrías;
- reemplazar componentes;
- reparar daños;
- ensamblar estructuras mayores.

Esto transforma el lanzamiento desde una operación de transporte hacia una operación de suministro de componentes.

---

## 14.3. Origami espacial

Las técnicas de plegado permiten almacenar membranas y elementos estructurales grandes dentro de volúmenes reducidos.

Aplicaciones:

- velas;
- paneles solares;
- radiadores;
- antenas;
- reflectores.

El objetivo es maximizar la superficie desplegada por unidad de masa.

---

# 15. Centrifugación espacial

La rotación proporciona una fuerza centrífuga efectiva:

\[
F_c=m\omega^2r.
\]

Puede utilizarse para tensar o desplegar elementos radiales.

Aplicaciones potenciales:

- estructuras radiales;
- cables;
- redes;
- centrifugadoras;
- estructuras habitables;
- sistemas de despliegue.

Una ventaja importante es que la tensión puede proceder de la dinámica del sistema en lugar de requerir una estructura rígida pesada.

---

# 16. Grandes redes solares

Una red solar orbital puede construirse de forma modular.

Cada módulo debe incorporar:

- generación;
- conversión;
- control;
- comunicaciones;
- interfaces mecánicas;
- capacidad de conexión energética.

El sistema debe ser funcional desde sus primeras etapas y crecer mediante nuevos lanzamientos.

Una arquitectura posible es:

**módulo → nodo → subred → red energética orbital.**

La capacidad acumulada puede emplearse para alimentar los siguientes elementos del sistema.

---

# 17. Arquitectura energética orbital

La red energética puede combinar:

- conexiones físicas locales;
- transmisión electromagnética entre nodos;
- almacenamiento;
- generación solar;
- conversión eléctrica a láser;
- receptores fotónicos.

Esto permitiría separar espacialmente generación, transmisión y utilización de energía.

La consecuencia más importante es arquitectónica:

> Un satélite no necesita producir toda la energía que consume si existe una infraestructura orbital capaz de distribuirla.

---

# 18. Velas solares y láseres

Las velas solares constituyen una de las aplicaciones naturales de la infraestructura energética propuesta.

La fuerza depende de la intensidad incidente y de la superficie reflectante.

Para una superficie ideal:

\[
F=\frac{2IA}{c}.
\]

La aceleración específica queda determinada por \(A/m\).

El problema principal no es solamente fabricar la vela, sino controlar:

- orientación;
- tensión;
- deformaciones;
- temperatura;
- reflectividad;
- estabilidad;
- actitud.

La vela debe poder cambiar su orientación con precisión para controlar la dirección del vector de aceleración.

---

# 19. Propulsión durante eclipses

La existencia de eclipses introduce un régimen en el que la vela no recibe radiación solar directa.

Una red orbital de láseres puede proporcionar una fuente externa de fotones durante estos períodos.

La arquitectura sería:

**red solar → energía eléctrica → láser → vela → momento orbital.**

Esto permitiría separar la fuente energética del vehículo y, potencialmente, ampliar el tiempo durante el cual una vela puede recibir empuje controlado.

El sistema requiere resolver la geometría de visibilidad, divergencia del haz, apuntado, eficiencia de conversión y disipación térmica.

---

# 20. Retroreflectores y comunicación

El principio de transmitir energía y señales mediante ondas electromagnéticas no es nuevo. La propagación de luz a través del vacío es un fenómeno básico de la electrodinámica.

El mismo principio puede aprovecharse para:

- comunicaciones;
- navegación;
- medición de distancia;
- transferencia energética;
- propulsión fotónica.

La utilización de retroreflectores y sistemas ópticos altamente reflectantes constituye una referencia tecnológica relevante para el desarrollo de superficies orbitales controlables.

---

# 21. Materiales para grandes superficies

Las estructuras de Solaris deben combinar:

- baja masa superficial;
- elevada reflectividad;
- resistencia térmica;
- resistencia a radiación;
- estabilidad dimensional;
- capacidad de plegado;
- resistencia al despliegue repetido cuando sea necesario.

Para velas y membranas reflectantes, la métrica crítica continúa siendo:

\[
\frac{A}{m}.
\]

Para radiadores, la métrica cambia hacia:

\[
\frac{P_{\rm disipable}}{m}.
\]

Para estructuras solares:

\[
\frac{P_{\rm eléctrica}}{m}.
\]

El desarrollo de materiales debe, por tanto, evaluarse según la función final y no mediante una única métrica universal.

---

# 22. Filosofía de modularidad

Solaris debe evitar depender de una única estructura gigantesca.

El modelo preferente es:

**lanzamiento → nodo → despliegue → integración → expansión.**

Cada nodo debe proporcionar una función concreta y poder integrarse posteriormente en una red.

Las ventajas son:

- reducción del riesgo de misión;
- crecimiento progresivo;
- capacidad de sustitución;
- redundancia;
- mantenimiento;
- experimentación incremental;
- posibilidad de modificar la arquitectura durante su desarrollo.

La infraestructura debe ser capaz de evolucionar.

---

# 23. Arquitectura conceptual integrada

La arquitectura resultante puede representarse de forma simplificada:

**Tierra**

↓

**Elevación atmosférica**

↓

**Globo estratosférico**

↓

**Separación y estabilización**

↓

**Aceleración electromagnética y/o propulsión química**

↓

**Inserción orbital**

↓

**Despliegue mediante gas, origami y robótica**

↓

**Construcción de nodos solares**

↓

**Integración en red energética**

↓

**Transmisión electromagnética**

↓

**Láseres orbitales**

↓

**Velas solares y velas impulsadas por láser**

En paralelo:

**estructuras centrífugas + radiadores + sistemas de comunicación y control**

constituyen infraestructura transversal.

---

# 24. Métricas de diseño

El desarrollo de Solaris debe basarse en métricas cuantitativas.

## Acceso orbital

\[
TWR=\frac{T}{mg}
\]

\[
\Delta v=v_e\ln\left(\frac{m_0}{m_f}\right).
\]

## Globo

\[
m_{\rm útil}
=
(\rho_{\rm aire}-\rho_{\rm gas})V-m_{\rm seco}.
\]

## Vela

\[
a=
\frac{2IA}{mc}.
\]

## Despliegue

\[
\eta_A=\frac{A_{\rm desplegada}}{M_{\rm lanzada}}.
\]

## Radiadores

\[
A_{\rm rad}
=
\frac{P}{\epsilon\sigma T^4}.
\]

## Aceleración electromagnética

\[
F=ILB
\]

para la geometría ideal correspondiente.

Estas métricas deben permitir comparar tecnologías aparentemente diferentes bajo una escala común de masa, energía y capacidad funcional.

---

## Calculadora interactiva de métricas de diseño

<style>
  #sw-widget * { box-sizing: border-box; }
  #sw-widget { font-family: 'IBM Plex Sans', sans-serif; color: var(--text-dark-soft); }
  #sw-widget p.sw-sub { color: var(--text-muted); font-size: 13px; line-height: 1.6; margin: 0 0 1.25rem; }
  #sw-widget .sw-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 1rem; }
  #sw-widget .sw-panel { background: var(--paper-dim); border: 1px solid var(--ink-line); border-radius: var(--radius); padding: 1rem 1.1rem; }
  #sw-widget .sw-panel h3 { font-family: 'Space Grotesk', sans-serif; font-size: 14.5px; font-weight: 600; margin: 0 0 0.6rem; color: var(--text-light); }
  #sw-widget .sw-eq { margin: 0 0 0.9rem; overflow-x: auto; font-size: 14px; }
  #sw-widget .sw-eq mjx-container { color: var(--text-light) !important; }
  #sw-widget .sw-field { margin-bottom: 0.7rem; }
  #sw-widget .sw-field label { font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 0.02em; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 4px; }
  #sw-widget .sw-field label span.sw-v { color: var(--text-light); }
  #sw-widget select { width: 100%; padding: 5px 7px; border-radius: var(--radius); border: 1px solid var(--ink-line); background: var(--ink-soft); color: var(--text-light); font-family: 'IBM Plex Mono', monospace; font-size: 12.5px; }
  #sw-widget input[type=range] { width: 100%; -webkit-appearance: none; appearance: none; height: 3px; border-radius: 2px; background: var(--ink-line); outline: none; margin: 2px 0; }
  #sw-widget input[type=range]::-webkit-slider-thumb { -webkit-appearance: none; appearance: none; width: 13px; height: 13px; border-radius: 50%; background: var(--accent); cursor: pointer; box-shadow: 0 0 0 4px var(--accent-soft); }
  #sw-widget input[type=range]::-moz-range-thumb { width: 13px; height: 13px; border: none; border-radius: 50%; background: var(--accent); cursor: pointer; box-shadow: 0 0 0 4px var(--accent-soft); }
  #sw-widget .sw-out { font-family: 'IBM Plex Mono', monospace; font-size: 13px; color: var(--accent); margin: 0.5rem 0 0.7rem; line-height: 1.5; }
  #sw-widget .sw-out b { color: var(--text-light); font-weight: 500; }
  #sw-widget .sw-chart { position: relative; width: 100%; height: 150px; }
</style>

<div id="sw-widget">
<p class="sw-sub">Las cuatro métricas de la Sección 24, con sliders para explorar cómo responde cada una. Los valores por defecto son órdenes de magnitud típicos, no un diseño específico.</p>

<div class="sw-grid">

  <div class="sw-panel">
    <h3>Globo estratosférico</h3>
    <div class="sw-eq">$$m_{útil} = (\rho_{aire}-\rho_{gas})V - m_{seco}$$</div>
    <div class="sw-field">
      <label>Gas de sustentación</label>
      <select id="sw-gas">
        <option value="0.0899">Hidrógeno (ρ₀ = 0.0899 kg/m³)</option>
        <option value="0.1786">Helio (ρ₀ = 0.1786 kg/m³)</option>
      </select>
    </div>
    <div class="sw-field">
      <label>ρ<sub>aire</sub> (densidad ambiente) <span class="sw-v" id="sw-rho-out">0.50 kg/m³</span></label>
      <input type="range" id="sw-rho" min="0.05" max="1.225" step="0.01" value="0.5">
    </div>
    <div class="sw-field">
      <label>Volumen V <span class="sw-v" id="sw-V-out">500 m³</span></label>
      <input type="range" id="sw-V" min="10" max="2000" step="10" value="500">
    </div>
    <div class="sw-field">
      <label>Masa seca <span class="sw-v" id="sw-mseco-out">30 kg</span></label>
      <input type="range" id="sw-mseco" min="1" max="200" step="1" value="30">
    </div>
    <div class="sw-out" id="sw-globo-out">-</div>
    <div class="sw-chart"><canvas id="sw-chart-globo"></canvas></div>
  </div>

  <div class="sw-panel">
    <h3>Vela solar</h3>
    <div class="sw-eq">$$a = \dfrac{2IA}{mc} \qquad I = \dfrac{I_\odot}{d^2}$$</div>
    <div class="sw-field">
      <label>Distancia al Sol (d) <span class="sw-v" id="sw-d-out">1.00 UA</span></label>
      <input type="range" id="sw-d" min="0.3" max="2" step="0.01" value="1">
    </div>
    <div class="sw-field">
      <label>A/m (área/masa) <span class="sw-v" id="sw-am-out">10.0 m²/kg</span></label>
      <input type="range" id="sw-am" min="1" max="50" step="0.5" value="10">
    </div>
    <div class="sw-out" id="sw-vela-out">-</div>
    <div class="sw-chart"><canvas id="sw-chart-vela"></canvas></div>
  </div>

  <div class="sw-panel">
    <h3>Radiador térmico</h3>
    <div class="sw-eq">$$A_{rad} = \dfrac{P}{\epsilon\sigma T^4}$$</div>
    <div class="sw-field">
      <label>Potencia a disipar (P) <span class="sw-v" id="sw-P-out">100 kW</span></label>
      <input type="range" id="sw-P" min="1" max="5000" step="1" value="100">
    </div>
    <div class="sw-field">
      <label>Temperatura de operación (T) <span class="sw-v" id="sw-T-out">300 K</span></label>
      <input type="range" id="sw-T" min="200" max="600" step="1" value="300">
    </div>
    <div class="sw-field">
      <label>Emisividad (ε) <span class="sw-v" id="sw-eps-out">0.90</span></label>
      <input type="range" id="sw-eps" min="0.1" max="0.98" step="0.01" value="0.9">
    </div>
    <div class="sw-out" id="sw-rad-out">-</div>
    <div class="sw-chart"><canvas id="sw-chart-rad"></canvas></div>
  </div>

  <div class="sw-panel">
    <h3>Cohete (Tsiolkovski)</h3>
    <div class="sw-eq">$$\Delta v = v_e\ln\!\left(\dfrac{m_0}{m_f}\right), \quad v_e = I_{sp}\,g_0$$</div>
    <div class="sw-field">
      <label>Impulso específico (Isp) <span class="sw-v" id="sw-isp-out">320 s</span></label>
      <input type="range" id="sw-isp" min="200" max="450" step="1" value="320">
    </div>
    <div class="sw-field">
      <label>Δv deseado <span class="sw-v" id="sw-dv-out">8.0 km/s</span></label>
      <input type="range" id="sw-dv" min="3" max="12" step="0.1" value="8">
    </div>
    <div class="sw-out" id="sw-cohete-out">-</div>
    <div class="sw-chart"><canvas id="sw-chart-cohete"></canvas></div>
  </div>

  <div class="sw-panel">
    <h3>Propulsión láser</h3>
    <div class="sw-eq">$$F = (1+R)\dfrac{P_{obj}}{c} \qquad P_{el} = \dfrac{P_{obj}}{\eta_{láser}\cdot f_{cap}(d)}$$</div>
    <p class="sw-sub" style="margin-bottom:0.6rem;">Supone un emisor de apertura fija D=10 m a λ=1.064 µm (Nd:YAG) y un objetivo con área reflectante fija de 100 m²; ambos son constantes de referencia, no sliders. f<sub>cap</sub>(d) es la fracción de la mancha del haz (limitada por difracción) que efectivamente cae sobre el objetivo.</p>
    <div class="sw-field">
      <label>Empuje deseado (F) <span class="sw-v" id="sw-laserF-out">0.10 N</span></label>
      <input type="range" id="sw-laserF" min="0.001" max="2" step="0.001" value="0.1">
    </div>
    <div class="sw-field">
      <label>Eficiencia del láser (η) <span class="sw-v" id="sw-laserEta-out">0.40</span></label>
      <input type="range" id="sw-laserEta" min="0.1" max="0.7" step="0.01" value="0.4">
    </div>
    <div class="sw-field">
      <label>Reflectividad del receptor (R) <span class="sw-v" id="sw-laserR-out">0.90</span></label>
      <input type="range" id="sw-laserR" min="0" max="1" step="0.01" value="0.9">
    </div>
    <div class="sw-field">
      <label>Distancia (d) <span class="sw-v" id="sw-laserD-out">50 000 km</span></label>
      <input type="range" id="sw-laserDexp" min="2" max="6" step="0.02" value="4.7">
    </div>
    <div class="sw-out" id="sw-laser-out">-</div>
    <div class="sw-chart"><canvas id="sw-chart-laser"></canvas></div>
  </div>

</div>
</div>

<script>
(function(){
function withChart(run){
  if (window.Chart) { run(); return; }
  var existing = document.getElementById('sw-chartjs-lib');
  if (existing) { existing.addEventListener('load', run); return; }
  var s = document.createElement('script');
  s.id = 'sw-chartjs-lib';
  s.src = 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js';
  s.onload = run;
  document.head.appendChild(s);
}
withChart(function(){

function cssVar(name, fallback) {
  const v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  return v || fallback;
}
const COL_ACCENT = cssVar('--accent', '#6FAFD9');
const COL_MUTED = cssVar('--text-muted', '#7C8D95');
const COL_WARN = '#E3A857';
const COL_GRID = cssVar('--ink-line', 'rgba(214,226,232,0.10)');

Chart.defaults.color = COL_MUTED;
Chart.defaults.borderColor = COL_GRID;
Chart.defaults.font.family = "'IBM Plex Mono', monospace";
Chart.defaults.font.size = 10;

const C_LIGHT = 2.998e8;
const SIGMA = 5.670e-8;
const G0 = 9.80665;
const I_SUN = 1361;

function baseOpts(xTitle, yTitle, logY) {
  return {
    responsive: true, maintainAspectRatio: false,
    animation: false,
    scales: {
      x: { type: 'linear', title: { display: true, text: xTitle, font:{size:10} }, grid:{color:COL_GRID} },
      y: { type: logY ? 'logarithmic' : 'linear', title: { display: true, text: yTitle, font:{size:10} }, grid:{color:COL_GRID} }
    },
    plugins: { legend: { display: false } }
  };
}

function markerDataset(x, yMin, yMax) {
  return { data: [{x:x, y:yMin},{x:x, y:yMax}], borderColor: COL_WARN, borderDash:[4,4], borderWidth:1.5, pointRadius:0 };
}

// ---------- Globo ----------
const gasEl = document.getElementById('sw-gas'), rhoEl = document.getElementById('sw-rho'),
      VEl = document.getElementById('sw-V'), msEl = document.getElementById('sw-mseco');
let chartGlobo;
function updateGlobo() {
  const rho0Gas = parseFloat(gasEl.value);
  const rhoAire = parseFloat(rhoEl.value);
  const V = parseFloat(VEl.value);
  const mSeco = parseFloat(msEl.value);
  const rhoGas = rho0Gas * (rhoAire/1.225);
  const mUtil = (rhoAire - rhoGas) * V - mSeco;

  document.getElementById('sw-rho-out').textContent = rhoAire.toFixed(2) + ' kg/m³';
  document.getElementById('sw-V-out').textContent = V.toFixed(0) + ' m³';
  document.getElementById('sw-mseco-out').textContent = mSeco.toFixed(0) + ' kg';
  document.getElementById('sw-globo-out').innerHTML =
    'ρ<sub>gas</sub> ≈ <b>' + rhoGas.toFixed(4) + ' kg/m³</b> &nbsp;→&nbsp; m<sub>útil</sub> ≈ <b>' + mUtil.toFixed(1) + ' kg</b>' +
    (mUtil < 0 ? ' <span style="color:#E3A857">(no flota)</span>' : '');

  const pts = [];
  for (let v = 10; v <= 2000; v += 20) pts.push({x:v, y: (rhoAire-rhoGas)*v - mSeco});
  if (!chartGlobo) {
    chartGlobo = new Chart(document.getElementById('sw-chart-globo'), {
      type: 'line',
      data: { datasets: [
        { data: pts, borderColor: COL_ACCENT, borderWidth:2, pointRadius:0 },
        markerDataset(V, Math.min(...pts.map(p=>p.y)), Math.max(...pts.map(p=>p.y)))
      ]},
      options: baseOpts('V (m³)', 'm_útil (kg)', false)
    });
  } else {
    chartGlobo.data.datasets[0].data = pts;
    chartGlobo.data.datasets[1] = markerDataset(V, Math.min(...pts.map(p=>p.y)), Math.max(...pts.map(p=>p.y)));
    chartGlobo.update('none');
  }
}
[gasEl, rhoEl, VEl, msEl].forEach(el => el.addEventListener('input', updateGlobo));
updateGlobo();

// ---------- Vela solar ----------
const dEl = document.getElementById('sw-d'), amEl = document.getElementById('sw-am');
let chartVela;
function updateVela() {
  const d = parseFloat(dEl.value);
  const am = parseFloat(amEl.value);
  const I = I_SUN / (d*d);
  const a = (2*I*am) / C_LIGHT;
  const dvDia = a * 86400;

  document.getElementById('sw-d-out').textContent = d.toFixed(2) + ' UA';
  document.getElementById('sw-am-out').textContent = am.toFixed(1) + ' m²/kg';
  document.getElementById('sw-vela-out').innerHTML =
    'I ≈ <b>' + I.toFixed(0) + ' W/m²</b> &nbsp;→&nbsp; a ≈ <b>' + (a*1e6).toFixed(2) + ' µm/s²</b><br>≈ <b>' + dvDia.toFixed(2) + ' m/s</b> de Δv acumulado por día';

  const pts = [];
  for (let x = 1; x <= 50; x += 1) pts.push({x:x, y: (2*I*x)/C_LIGHT * 1e6});
  const yVals = pts.map(p=>p.y);
  if (!chartVela) {
    chartVela = new Chart(document.getElementById('sw-chart-vela'), {
      type: 'line',
      data: { datasets: [
        { data: pts, borderColor: COL_ACCENT, borderWidth:2, pointRadius:0 },
        markerDataset(am, Math.min(...yVals), Math.max(...yVals))
      ]},
      options: baseOpts('A/m (m²/kg)', 'a (µm/s²)', false)
    });
  } else {
    chartVela.data.datasets[0].data = pts;
    chartVela.data.datasets[1] = markerDataset(am, Math.min(...yVals), Math.max(...yVals));
    chartVela.update('none');
  }
}
[dEl, amEl].forEach(el => el.addEventListener('input', updateVela));
updateVela();

// ---------- Radiador ----------
const PEl = document.getElementById('sw-P'), TEl = document.getElementById('sw-T'), epsEl = document.getElementById('sw-eps');
let chartRad;
function updateRad() {
  const P = parseFloat(PEl.value) * 1000;
  const T = parseFloat(TEl.value);
  const eps = parseFloat(epsEl.value);
  const A = P / (eps * SIGMA * Math.pow(T,4));

  document.getElementById('sw-P-out').textContent = (P/1000).toFixed(0) + ' kW';
  document.getElementById('sw-T-out').textContent = T.toFixed(0) + ' K';
  document.getElementById('sw-eps-out').textContent = eps.toFixed(2);
  document.getElementById('sw-rad-out').innerHTML = 'A<sub>rad</sub> ≈ <b>' + A.toFixed(1) + ' m²</b>';

  const pts = [];
  for (let t = 200; t <= 600; t += 10) pts.push({x:t, y: P/(eps*SIGMA*Math.pow(t,4))});
  const yVals = pts.map(p=>p.y);
  if (!chartRad) {
    chartRad = new Chart(document.getElementById('sw-chart-rad'), {
      type: 'line',
      data: { datasets: [
        { data: pts, borderColor: COL_ACCENT, borderWidth:2, pointRadius:0 },
        markerDataset(T, Math.min(...yVals), Math.max(...yVals))
      ]},
      options: baseOpts('T (K)', 'A_rad (m²)', true)
    });
  } else {
    chartRad.data.datasets[0].data = pts;
    chartRad.data.datasets[1] = markerDataset(T, Math.min(...yVals), Math.max(...yVals));
    chartRad.update('none');
  }
}
[PEl, TEl, epsEl].forEach(el => el.addEventListener('input', updateRad));
updateRad();

// ---------- Cohete ----------
const ispEl = document.getElementById('sw-isp'), dvEl = document.getElementById('sw-dv');
let chartCohete;
function updateCohete() {
  const isp = parseFloat(ispEl.value);
  const dv = parseFloat(dvEl.value) * 1000;
  const ve = isp * G0;
  const ratio = Math.exp(dv/ve);

  document.getElementById('sw-isp-out').textContent = isp.toFixed(0) + ' s';
  document.getElementById('sw-dv-out').textContent = (dv/1000).toFixed(1) + ' km/s';
  document.getElementById('sw-cohete-out').innerHTML = 'v<sub>e</sub> ≈ <b>' + ve.toFixed(0) + ' m/s</b> &nbsp;→&nbsp; m₀/m<sub>f</sub> ≈ <b>' + ratio.toFixed(2) + '</b>';

  const pts = [];
  for (let x = 3; x <= 12; x += 0.2) pts.push({x:x, y: Math.exp((x*1000)/ve)});
  const yVals = pts.map(p=>p.y);
  if (!chartCohete) {
    chartCohete = new Chart(document.getElementById('sw-chart-cohete'), {
      type: 'line',
      data: { datasets: [
        { data: pts, borderColor: COL_ACCENT, borderWidth:2, pointRadius:0 },
        markerDataset(dv/1000, Math.min(...yVals), Math.max(...yVals))
      ]},
      options: baseOpts('Δv (km/s)', 'm₀/m_f', true)
    });
  } else {
    chartCohete.data.datasets[0].data = pts;
    chartCohete.data.datasets[1] = markerDataset(dv/1000, Math.min(...yVals), Math.max(...yVals));
    chartCohete.update('none');
  }
}
[ispEl, dvEl].forEach(el => el.addEventListener('input', updateCohete));
updateCohete();

// ---------- Propulsión láser ----------
const LAMBDA = 1.064e-6;   // m, Nd:YAG
const D_EMISOR = 10;       // m, apertura del emisor (constante de referencia)
const A_TARGET = 100;      // m², área reflectante del objetivo (constante de referencia)

function fmtPower(w) {
  if (w >= 1e9) return (w/1e9).toFixed(2) + ' GW';
  if (w >= 1e6) return (w/1e6).toFixed(2) + ' MW';
  if (w >= 1e3) return (w/1e3).toFixed(2) + ' kW';
  return w.toFixed(1) + ' W';
}

const laserFEl = document.getElementById('sw-laserF'), laserEtaEl = document.getElementById('sw-laserEta'),
      laserREl = document.getElementById('sw-laserR'), laserDexpEl = document.getElementById('sw-laserDexp');
let chartLaser;
function laserCap(d_km) {
  const d = d_km * 1000;
  const spotDiam = 2.44 * LAMBDA * d / D_EMISOR;
  const spotArea = Math.PI * Math.pow(spotDiam/2, 2);
  return { spotDiam, fCap: Math.min(1, A_TARGET/spotArea) };
}
function updateLaser() {
  const F = parseFloat(laserFEl.value);
  const eta = parseFloat(laserEtaEl.value);
  const R = parseFloat(laserREl.value);
  const dExp = parseFloat(laserDexpEl.value);
  const d_km = Math.pow(10, dExp);

  document.getElementById('sw-laserF-out').textContent = F.toFixed(3) + ' N';
  document.getElementById('sw-laserEta-out').textContent = eta.toFixed(2);
  document.getElementById('sw-laserR-out').textContent = R.toFixed(2);
  document.getElementById('sw-laserD-out').textContent = d_km >= 1000 ? (d_km/1000).toFixed(0) + ' 000 km' : d_km.toFixed(0) + ' km';

  const { spotDiam, fCap } = laserCap(d_km);
  const P_target = F * C_LIGHT / (1+R);
  const P_elec = P_target / (eta * fCap);

  document.getElementById('sw-laser-out').innerHTML =
    'Mancha del haz ≈ <b>' + spotDiam.toFixed(1) + ' m</b> &nbsp;→&nbsp; captura ≈ <b>' + (fCap*100).toFixed(1) + '%</b><br>' +
    'P<sub>óptica en objetivo</sub> ≈ <b>' + fmtPower(P_target) + '</b> &nbsp;→&nbsp; P<sub>eléctrica</sub> ≈ <b>' + fmtPower(P_elec) + '</b>';

  const pts = [];
  for (let e = 2; e <= 6; e += 0.1) {
    const dk = Math.pow(10, e);
    const cap = laserCap(dk).fCap;
    pts.push({x: dk, y: P_target/(eta*cap)});
  }
  const yVals = pts.map(p=>p.y);
  if (!chartLaser) {
    chartLaser = new Chart(document.getElementById('sw-chart-laser'), {
      type: 'line',
      data: { datasets: [
        { data: pts, borderColor: COL_ACCENT, borderWidth:2, pointRadius:0 },
        markerDataset(d_km, Math.min(...yVals), Math.max(...yVals))
      ]},
      options: Object.assign(baseOpts('d (km)', 'P_eléctrica (W)', true), { scales: { x: { type:'logarithmic', title:{display:true,text:'d (km)', font:{size:10}}, grid:{color:COL_GRID} }, y: { type:'logarithmic', title:{display:true,text:'P_eléctrica (W)', font:{size:10}}, grid:{color:COL_GRID} } } })
    });
  } else {
    chartLaser.data.datasets[0].data = pts;
    chartLaser.data.datasets[1] = markerDataset(d_km, Math.min(...yVals), Math.max(...yVals));
    chartLaser.update('none');
  }
}
[laserFEl, laserEtaEl, laserREl, laserDexpEl].forEach(el => el.addEventListener('input', updateLaser));
updateLaser();

}); // fin withChart
})();
</script>


---

# 25. Problemas abiertos

La investigación requiere resolver, entre otros, los siguientes problemas:

1. Determinar la altura óptima de liberación de un vehículo desde un globo.
2. Determinar el volumen de globo necesario para cargas de distintas masas.
3. Comparar hidrógeno y helio incluyendo masa de envolvente, permeabilidad y operación.
4. Calcular la masa mínima de una etapa propulsiva desde 20–30 km.
5. Determinar el efecto real de la rotación terrestre sobre el lanzamiento.
6. Cuantificar pérdidas gravitatorias y aerodinámicas.
7. Determinar qué fracción del \(\Delta v\) puede trasladarse a un acelerador electromagnético.
8. Dimensionar un acelerador electromagnético para diferentes masas y velocidades de salida.
9. Estudiar las limitaciones térmicas y estructurales de los sistemas de lanzamiento electromagnético.
10. Determinar el límite práctico de \(A/m\) para una vela solar.
11. Identificar materiales adecuados para membranas ultraligeras.
12. Diseñar mecanismos de despliegue fiables para superficies de gran tamaño.
13. Desarrollar sistemas autónomos de ensamblaje orbital.
14. Determinar la arquitectura óptima de una red solar modular.
15. Calcular pérdidas de transmisión electromagnética entre nodos.
16. Dimensionar emisores y receptores para transmisión láser o por microondas.
17. Calcular el calor residual de una estación de potencia.
18. Determinar el área de radiadores necesaria para cada nivel de potencia.
19. Diseñar sistemas de orientación y control para velas solares.
20. Determinar la arquitectura óptima para mantener propulsión durante eclipses.
21. Estudiar la viabilidad de redes orbitales de láseres.
22. Determinar el número mínimo de lanzamientos para una infraestructura determinada.
23. Comparar el coste de masa de las diferentes arquitecturas.
24. Establecer qué tecnologías deben desarrollarse primero y cuáles dependen de otras.

---

# 26. Principio de diseño final

Solaris no plantea que una única tecnología deba resolver el acceso al espacio.

El enfoque consiste en distribuir el problema:

- la flotación proporciona altura;
- la atmósfera puede proporcionar parte de la sustentación o energía propulsiva cuando resulte conveniente;
- la propulsión química proporciona grandes incrementos de velocidad;
- la aceleración electromagnética puede trasladar energía desde tierra hacia la carga;
- el despliegue mecánico transforma cargas compactas en estructuras grandes;
- la energía solar alimenta la infraestructura;
- los láseres permiten transferir energía y momento;
- las velas permiten obtener aceleración sin propelente convencional;
- los radiadores eliminan el calor residual;
- la rotación puede proporcionar tensión y estabilidad estructural.

La arquitectura se basa, por tanto, en la especialización de cada régimen físico.

---

# 27. Norte del Proyecto Solaris

El objetivo final puede resumirse como:

> **Convertir una capacidad limitada de lanzamiento en una capacidad creciente de construcción espacial.**

La métrica de éxito no será únicamente la masa puesta en órbita.

Será la capacidad funcional obtenida por cada unidad de masa, energía y coste introducida en el sistema.

El objetivo de largo plazo es una infraestructura orbital:

- modular;
- ampliable;
- reparable;
- energéticamente interconectada;
- capaz de desplegar grandes superficies;
- capaz de transmitir energía;
- capaz de generar haces dirigidos;
- capaz de utilizar presión de radiación como mecanismo de propulsión.

Solaris deja así de ser un único vehículo y pasa a concebirse como una **arquitectura de infraestructura espacial progresiva**.