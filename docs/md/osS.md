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
