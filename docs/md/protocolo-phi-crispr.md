El cáncer es una de las principales causas de mortandad a nivel mundial, caracterizado por el crecimiento descontrolado de células que pueden invadir tejidos circundantes y diseminarse a otras partes del cuerpo. La tecnología CRISPR-Cas9, desarrollada como una herramienta de edición genética de alta precisión, ha generado gran expectativa como una posible solución para combatir esta enfermedad.

## Marco Teórico

[![model1](https://img.shields.io/badge/pdf-Arquitectura_Teórica_Preliminar-red)](pdfs/crisprphi.pdf)
[![model2](https://img.shields.io/badge/pdf-Modelo_murino-red)](pdfs/crisprphi2.pdf)
[![model3](https://img.shields.io/badge/pdf-Tomografía_Ultrasónica-red)](pdfs/crisprphi3.pdf)

La herramienta CRISPR-Cas9, inicialmente descubierta como parte del sistema inmunitario adaptativo de bacterias y arqueas, ha sido adaptada para la edición genética en organismos superiores. Su mecanismo principal consiste en el uso de una proteína Cas9, guiada por un ARN dirigido (gRNA), para identificar y cortar secuencias específicas de ADN. Este sistema permite modificar genes con una precisión sin precedentes, lo que lo ha convertido en una revolución para la biología molecular y la medicina.
<br><br>
En el contexto del cáncer, esta tecnología ofrece nuevas perspectivas al abordar directamente las bases genéticas de la enfermedad. El cáncer se origina, en su mayoría, por mutaciones en genes críticos que regulan la proliferación celular, dividiéndose principalmente en dos categorías:

|*Oncogenes*|*Genes supresores de tumores*|
|-|-|
|Genes que, al activarse o sobreexpresarse, promueven el crecimiento descontrolado de células.|Genes que normalmente inhiben el crecimiento celular anormal y cuya inactivación permite la progresión del cáncer.|

CRISPR-Cas9 ofrece la posibilidad de intervenir directamente en estas mutaciones, bien sea corrigiéndolas, desactivándolas o eliminándolas. Además, puede ser utilizada para potenciar tratamientos existentes, como la inmunoterapia, al optimizar el sistema inmunitario para identificar y atacar las células tumorales. Esto abre la puerta a una medicina más personalizada y efectiva, capaz de adaptarse a las características genéticas únicas de cada paciente y tipo de cáncer.
<br><br>
No obstante, el uso de CRISPR-Cas9 también plantea retos significativos, como el riesgo de ediciones fuera del objetivo (off-target), la heterogeneidad de las células tumorales y las dificultades asociadas a la entrega segura y eficiente de esta tecnología al tejido afectado. Por ello, su implementación en el tratamiento del cáncer requiere no solo avances tecnológicos, sino también una comprensión profunda de los mecanismos moleculares que subyacen a esta enfermedad.

---

## Mecanismo de CRISPR-Cas9
CRISPR-Cas9 es una tecnología que permite editar secuencias específicas de ADN mediante **identificación de genes diana** (localiza mutaciones responsables del crecimiento descontrolado de las células cancerosas) y **edición precisa** (modifica, elimina o corrige mutaciones genéticas para frenar la proliferación de las células tumorales)
<br><br>
Entre sus aplicaciones destacadas se encuentran:
<br>
|*Desactivación de oncogenes*|*Reparación de genes supresores de tumores*|*Optimización del sistema inmunitario*|
|-|-|-|
|Genes que promueven el crecimiento tumoral.|Como *TP53* o *BRCA1*, que pierden funcionalidad en ciertos cánceres.|Programación de células CAR-T (células T con receptor de antígeno quimérico) para reconocer<br>y destruir células cancerosas.|

---

## Tratamiento del sistema ΦCRISPR
### Neutralización Oncológica No Letal Inicial
#### Resumen
Se presenta un marco teórico interdisciplinario para la neutralización progresiva del cáncer mediante la integración secuencial de detección algorítmica, inmovilización física y eliminación genética dirigida. El enfoque prioriza la estabilización del sistema tumoral antes de su intervención molecular, reduciendo resistencia adaptativa, daño colateral y dependencia de tratamientos citotóxicos agresivos.
#### 1. Principio rector
El cáncer es modelado como un sistema biológico dinámico inestable, caracterizado por:
- Alta tasa de proliferación.
- Pérdida de mecanismos de control homeostático.
- Capacidad adaptativa acelerada.
Bajo esta definición, el tratamiento no busca la destrucción inmediata del sistema, sino su desacople dinámico, seguido de corrección estructural. El orden de intervención es crítico.
#### 2. Arquitectura General del Sistema
El sistema Phi-CRISPR-Cas9 se compone de tres subsistemas funcionales interdependientes:
1. SDRP<br>
Sistema de Detección y Reconocimiento de Patologías.
2. TTF<br>
Sistema de inmovilización tumoral mediante campos eléctricos alternantes.
3. CRISPR<br>
Intervención genética de precisión a nivel subcelular.
Cada módulo actúa en una fase distinta del proceso patológico, evitando solapamientos funcionales innecesarios.
#### 3. SDRP
#### Sistema de Detección y Reconocimiento de Patologías
#### Objetivo
Identificar, localizar y caracterizar regiones tumorales mediante análisis algorítmico de imágenes médicas.
#### Fundamento teórico
El SDRP se basa en redes neuronales entrenadas para reconocer:
- Asimetrías morfológicas.
- Patrones de crecimiento no compatibles con tejidos sanos.
- Heterogeneidad estructural interna.
#### Salida del sistema
El SDRP no produce un diagnóstico binario, sino un mapa paramétrico tumoral, incluyendo:
- Localización espacial.
- Volumen estimado.
- Índices de irregularidad y actividad relativa.
Este output es utilizado como entrada directa para la modulación del sistema TTF.
### 4. TTF
#### Inmovilización Física del Sistema Tumoral
#### Objetivo
Reducir la capacidad proliferativa y adaptativa del tumor sin inducir necrosis masiva.
#### Principio físico
Se emplean campos eléctricos:
- De baja intensidad.
- Alternantes.
- Intermitentes.
- Con inversión periódica de polaridad.
Estos campos interfieren selectivamente con procesos celulares de alta demanda energética y organización rápida, particularmente la mitosis.
#### Diferencial biológico
- Las células sanas operan lejos del umbral de inestabilidad.
- Las células tumorales dependen de procesos altamente dinámicos y desregulados.
Como consecuencia, el campo actúa como:
- Ruido tolerable para tejido sano.
- Factor desorganizador para células tumorales.
#### Resultado esperado
- Supresión de expansión tumoral.
- Reducción de heterogeneidad genética.
- Estabilización temporal del sistema patológico.
El tumor entra en un estado funcionalmente inerte, pero viable.
### 5. CRISPR
#### Intervención Genética Dirigida
#### Condición de activación
La intervención genética se aplica únicamente tras la estabilización lograda por TTF.
#### Fundamento teórico
Un sistema tumoral inmovilizado:
- Presenta menor tasa mutacional.
- Ofrece blancos genéticos más estables.
- Reduce la probabilidad de escape adaptativo.
#### Objetivo de la intervención
La edición genética se orienta a:
- Oncogenes dominantes.
- Vías críticas de replicación aberrante.
No se busca edición global, sino interrupción selectiva de nodos funcionales clave.
### 6. Integración y Retroalimentación
El sistema opera bajo un esquema de control iterativo:
1. SDRP detecta y caracteriza.
2. TTF actúa según parámetros derivados.
3. SDRP evalúa respuesta.
4. Una vez alcanzado un estado estable, se habilita CRISPR.
5. El sistema inmune del huésped completa la eliminación residual.
No existe una fase única. El proceso es acumulativo y controlado.
### 7. Enfoque Ético y Estratégico
Este marco:
- Evita la destrucción indiscriminada de tejido.
- Reduce dependencia de quimioterapia citotóxica.
- Prioriza tratamientos adaptativos, no reactivos.
El cáncer no es tratado como un enemigo a exterminar, sino como un sistema a desactivar, corregir y absorber.

---

## Inyección localizada de CRISPR-Cas9 en el tratamiento del cáncer
- CRISPR permite identificar mutaciones específicas asociadas a cada tipo de cáncer y dirigir su acción hacia ellas.
- Los oncogenes **no** destruyen los genes BRCA1 ni TP53, sino que las "**desactivan**".
- Para que CRISPR pueda identificar y editar las cadenas de ADN afectadas por el tumor, es necesario diseñar y modificar los parámetros del mismo.
- El desarrollo de nuevas variantes (como Cas12 o Cas13) podría mejorar la especificidad y reducir los efectos fuera del objetivo.
- Es necesario acelerar los ensayos clínicos en humanos para validar la seguridad y eficacia de CRISPR en diferentes tipos de cáncer.
- CRISPR podría integrarse con otras terapias, como la inmunoterapia o la quimioterapia, para atacar diferentes aspectos del tumor simultáneamente.

---

## Limitaciones
Se están evaluando estrategias para mitigar las implicaciones de este protocolo, mencionadas a continuación:

- **Heterogeneidad del cáncer**<br>
El cáncer no es una enfermedad única, sino un conjunto de más de 200 patologías con causas genéticas y ambientales variadas. Además, un mismo tumor puede contener subpoblaciones celulares con mutaciones distintas, dificultando un tratamiento único.

- **Evolución del tumor**<br>
Las células cancerosas tienen una alta tasa de mutación y pueden desarrollar resistencia a los tratamientos, incluso después de una edición genética exitosa.

- **Efectos fuera del objetivo (Off-Target)**<br>
CRISPR-Cas9 podría alterar genes no deseados, generando mutaciones adicionales que podrían causar efectos adversos, incluidos nuevos cánceres.

- **Opciones de entrega**<br>
Asegurar que CRISPR alcance el tejido tumoral de manera efectiva es un desafío técnico. Se están explorando sistemas como nanopartículas, virus modificados (AAV) y Electroporación.

- **Acceso global y costos**<br>
El desarrollo y aplicación de terapias CRISPR requiere recursos significativos. Esto podría limitar su acceso en países con menor infraestructura médica y presupuesto.

---

## Modelo de predictibilidad probabilística

Para evaluar cuán preciso y eficiente es la aplicación del protocolo en un paciente, es necesario refinar el algoritmo analizando y relacionando los resultados de exámenes o investigaciones con CRISPR-Cas9 y modelos de expansión de las células cancerígenas. Se está diseñando y evaluando la mejor aproximación inicial y sus derivadas alternativas para cumplir con este requisito previo, usando modelos de redes neuronales entrenados con datos simulados.

### Probabilidad de éxito del Protocolo ΦCRISPR durante y previa a la etapa 3.
|Tasa de mutación|RBC|
|-|-|
|<img src="https://github.com/user-attachments/assets/be4422cc-ed8b-43b4-8752-6349a9b5a17e" width="100%">|<img src="https://github.com/user-attachments/assets/22b57ccc-6358-451f-b1b2-8e0b8aff1a23" width="100%">|

El **SDRP (Sistema de Detección y Reconocimiento de Patologías)** es un software diseñado para complementar el **Protocolo ΦCRISPR**, permitiendo evaluar la efectividad del tratamiento antes de su aplicación. Su función principal es analizar imágenes médicas, como radiografías y tomografías computarizadas (TAC), mediante algoritmos avanzados de **inteligencia artificial** y **redes neuronales convolucionales** especializadas en el reconocimiento de patrones patológicos.  

Este sistema emplea modelos de aprendizaje profundo entrenados con grandes volúmenes de datos clínicos, lo que le permite identificar, clasificar y cuantificar anomalías con alta precisión. Con base en este análisis, SDRP genera una estimación de la respuesta esperada al tratamiento basado en **ΦCRISPR**, proporcionando a los profesionales médicos información clave para la toma de decisiones.  

Además, el SDRP puede integrarse con bases de datos hospitalarias y plataformas de telemedicina para optimizar la evaluación remota de pacientes, reduciendo el tiempo de diagnóstico y mejorando la personalización de los tratamientos basados en edición genética.

---

## Conclusión
CRISPR-Cas9 representa una de las herramientas más prometedoras en la lucha contra el cáncer, con el potencial de transformar el tratamiento de ciertos tipos de tumores. Sin embargo, debido a la complejidad biológica del cáncer y los desafíos tecnológicos asociados, es poco probable que sea una cura universal en el corto plazo. Con suficiente inversión y desarrollo, podría convertirse en una herramienta clave para convertir ciertos cánceres en enfermedades tratables o incluso curables, marcando un avance significativo en la medicina personalizada.

---

## Modelo interactivo: velocidad de escape de la longevidad

<style>
  #lv-widget * { box-sizing: border-box; }
  #lv-widget { font-family: 'IBM Plex Sans', sans-serif; color: var(--text-dark-soft); }
  #lv-widget .lv-wrap { max-width: 100%; margin: 0 auto; }
  #lv-widget h1.lv-h1 { font-family: 'Space Grotesk', sans-serif; font-size: 19px; font-weight: 600; margin: 0 0 4px; color: var(--text-light); }
  #lv-widget h2.lv-h2 { font-family: 'Space Grotesk', sans-serif; font-size: 16px; font-weight: 600; margin: 2rem 0 0.75rem; color: var(--text-light); }
  #lv-widget p.lv-sub { color: var(--text-muted); font-size: 13px; line-height: 1.6; margin: 0 0 1.25rem; }
  #lv-widget .lv-eq { margin: 0 0 1.25rem; padding: 4px 2px; overflow-x: auto; }
  #lv-widget .lv-eq mjx-container { color: var(--text-light) !important; }
  #lv-widget .lv-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 10px; margin-bottom: 1rem; }
  #lv-widget .lv-card { background: var(--paper-dim); border: 1px solid var(--ink-line); border-radius: var(--radius); padding: 0.8rem 1rem; }
  #lv-widget .lv-card label { font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 0.03em; color: var(--text-muted); display: block; margin-bottom: 6px; }
  #lv-widget .lv-card .lv-val { font-family: 'IBM Plex Mono', monospace; font-size: 13.5px; font-weight: 500; color: var(--text-light); }
  #lv-widget select { width: 100%; padding: 6px 8px; border-radius: var(--radius); border: 1px solid var(--ink-line); background: var(--ink-soft); color: var(--text-light); font-family: 'IBM Plex Mono', monospace; font-size: 13px; }
  #lv-widget input[type=range] { width: 100%; -webkit-appearance: none; appearance: none; height: 3px; border-radius: 2px; background: var(--ink-line); outline: none; margin: 6px 0 2px; }
  #lv-widget input[type=range]::-webkit-slider-thumb { -webkit-appearance: none; appearance: none; width: 14px; height: 14px; border-radius: 50%; background: var(--accent); cursor: pointer; box-shadow: 0 0 0 4px var(--accent-soft); }
  #lv-widget input[type=range]::-moz-range-thumb { width: 14px; height: 14px; border: none; border-radius: 50%; background: var(--accent); cursor: pointer; box-shadow: 0 0 0 4px var(--accent-soft); }
  #lv-widget .lv-chart-box { position: relative; width: 100%; height: 220px; margin-bottom: 1.25rem; background: var(--paper-dim); border: 1px solid var(--ink-line); border-radius: var(--radius); padding: 10px; }
  #lv-widget .lv-badge-ok { color: #3DBD6E; font-weight: 600; }
  #lv-widget .lv-badge-bad { color: #E5484D; font-weight: 600; }
  #lv-widget .lv-note { font-size: 12px; color: var(--text-muted); margin-top: -0.5rem; margin-bottom: 1.5rem; }
</style>

<div id="lv-widget">
<div class="lv-wrap">
  <h1 class="lv-h1">Modelo de longevidad humana L(t)</h1>
  <p class="lv-sub">Ajuste cuadrático por mínimos cuadrados sobre datos reales (Our World in Data, Mundo, ventana de 80 años: 1943&ndash;2023). Valores fijos, sin intervención del lector.</p>

  <p class="lv-sub">Este modelo cuantifica el contexto en el que se inscribe el Protocolo ΦCRISPR: mientras la esperanza de vida global crezca a un ritmo insuficiente para alcanzar una "velocidad de escape" biológica ($dL/dt \ge 1$), tecnologías de intervención dirigida como la edición genética contra el cáncer son una de las palancas que pueden acelerar ese ritmo.</p>

  <div class="lv-eq">$$L(t) = L_0 + v_0 t + \frac{a}{2}t^2 \qquad \dfrac{dL}{dt} = v_0 + a t \qquad \dfrac{d^2L}{dt^2} = a$$</div>

  <div class="lv-row">
    <div class="lv-card"><label>L₀ (ordenada, año inicial de la ventana)</label><div class="lv-val" id="lv-L0-out">-</div></div>
    <div class="lv-card"><label>v₀ (años ganados/año, al inicio de la ventana)</label><div class="lv-val" id="lv-v0-out">-</div></div>
    <div class="lv-card"><label>a = d²L/dt²</label><div class="lv-val" id="lv-a-out">-</div></div>
    <div class="lv-card"><label>R² del ajuste</label><div class="lv-val" id="lv-r2-out">-</div></div>
  </div>

  <div class="lv-row">
    <div class="lv-card">
      <label>d²L/dt² ≥ 0</label>
      <div class="lv-val" id="lv-cond1-out">-</div>
    </div>
    <div class="lv-card">
      <label>dL/dt ≥ 1 (velocidad de escape)</label>
      <div class="lv-val" id="lv-cond2-out">-</div>
    </div>
  </div>

  <div class="lv-chart-box"><canvas id="lv-chartData"></canvas></div>
  <div class="lv-chart-box"><canvas id="lv-chartDeriv"></canvas></div>
  <p class="lv-note" id="lv-fit-note"></p>
</div>
</div>

<script>
(function(){
function withChart(run){
  if (window.Chart) { run(); return; }
  var existing = document.getElementById('lv-chartjs-lib');
  if (existing) { existing.addEventListener('load', run); return; }
  var s = document.createElement('script');
  s.id = 'lv-chartjs-lib';
  s.src = 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js';
  s.onload = run;
  document.head.appendChild(s);
}
withChart(function(){
const DATA = {"World": [[1770,28.5],[1800,28.5],[1820,29.0],[1850,29.3],[1870,29.7],[1900,32.0],[1913,34.1],[1950,46.394],[1951,47.126],[1952,48.218],[1953,48.809],[1954,49.651],[1955,50.206],[1956,50.737],[1957,51.064],[1958,51.615],[1959,49.582],[1960,47.82],[1961,50.346],[1962,53.242],[1963,53.716],[1964,54.26],[1965,53.998],[1966,54.564],[1967,55.068],[1968,55.618],[1969,56.0],[1970,56.266],[1971,56.019],[1972,57.215],[1973,57.692],[1974,58.061],[1975,58.268],[1976,58.575],[1977,59.154],[1978,59.513],[1979,60.157],[1980,60.502],[1981,60.919],[1982,61.343],[1983,61.521],[1984,61.866],[1985,62.209],[1986,62.73],[1987,63.181],[1988,63.367],[1989,63.782],[1990,63.955],[1991,64.064],[1992,64.288],[1993,64.433],[1994,64.299],[1995,64.882],[1996,65.2],[1997,65.541],[1998,65.741],[1999,66.041],[2000,66.433],[2001,66.753],[2002,67.068],[2003,67.401],[2004,67.745],[2005,68.141],[2006,68.614],[2007,69.032],[2008,69.302],[2009,69.681],[2010,70.089],[2011,70.403],[2012,70.824],[2013,71.142],[2014,71.404],[2015,71.606],[2016,71.877],[2017,72.067],[2018,72.388],[2019,72.609],[2020,71.917],[2021,70.865],[2022,72.64],[2023,73.169]],
"Uruguay": [[1900,49.0],[1910,52.0],[1920,52.0],[1930,50.0],[1940,58.0],[1950,65.574],[1951,65.841],[1952,66.056],[1953,66.26],[1954,66.475],[1955,66.691],[1956,66.907],[1957,67.118],[1958,67.329],[1959,67.53],[1960,67.683],[1961,67.81],[1962,67.911],[1963,68.023],[1964,68.112],[1965,68.2],[1966,68.302],[1967,68.407],[1968,68.514],[1969,68.581],[1970,68.734],[1971,68.926],[1972,69.169],[1973,69.348],[1974,69.524],[1975,69.705],[1976,69.887],[1977,70.081],[1978,70.265],[1979,70.255],[1980,70.505],[1981,70.952],[1982,71.528],[1983,71.595],[1984,71.708],[1985,71.861],[1986,72.187],[1987,72.196],[1988,72.408],[1989,72.628],[1990,72.994],[1991,73.198],[1992,73.185],[1993,73.147],[1994,73.162],[1995,73.493],[1996,73.812],[1997,73.92],[1998,74.029],[1999,74.293],[2000,74.693],[2001,74.987],[2002,74.979],[2003,75.086],[2004,75.319],[2005,75.829],[2006,75.888],[2007,76.15],[2008,76.275],[2009,76.67],[2010,76.691],[2011,76.614],[2012,76.691],[2013,76.953],[2014,77.194],[2015,77.285],[2016,77.351],[2017,77.618],[2018,77.527],[2019,77.503],[2020,78.381],[2021,75.434],[2022,76.468],[2023,78.138]]};

function cssVar(name, fallback) {
  const v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  return v || fallback;
}
const COL_ACCENT = cssVar('--accent', '#6FAFD9');
const COL_MUTED = cssVar('--text-muted', '#7C8D95');
const COL_TEXT = cssVar('--text-light', '#D9E2E6');
const COL_WARN = '#E3A857';
const COL_GRID = cssVar('--ink-line', 'rgba(214,226,232,0.10)');

Chart.defaults.color = COL_MUTED;
Chart.defaults.borderColor = COL_GRID;
Chart.defaults.font.family = "'IBM Plex Mono', monospace";
Chart.defaults.font.size = 11;

function solve3(A, b) {
  const M = A.map((row,i)=>[...row, b[i]]);
  for (let i=0;i<3;i++){
    let piv=i;
    for (let k=i+1;k<3;k++) if (Math.abs(M[k][i])>Math.abs(M[piv][i])) piv=k;
    [M[i],M[piv]]=[M[piv],M[i]];
    for (let k=i+1;k<3;k++){
      const f=M[k][i]/M[i][i];
      for (let j=i;j<4;j++) M[k][j]-=f*M[i][j];
    }
  }
  const x=[0,0,0];
  for (let i=2;i>=0;i--){
    let s=M[i][3];
    for (let j=i+1;j<3;j++) s-=M[i][j]*x[j];
    x[i]=s/M[i][i];
  }
  return x;
}

function quadFit(points) {
  const t0 = points[0][0];
  const t = points.map(p=>p[0]-t0);
  const y = points.map(p=>p[1]);
  const n = t.length;
  let S0=n,S1=0,S2=0,S3=0,S4=0,Y0=0,Y1=0,Y2=0;
  for (let i=0;i<n;i++){
    const ti=t[i], yi=y[i];
    S1+=ti; S2+=ti*ti; S3+=ti*ti*ti; S4+=ti*ti*ti*ti;
    Y0+=yi; Y1+=ti*yi; Y2+=ti*ti*yi;
  }
  const A=[[S0,S1,S2],[S1,S2,S3],[S2,S3,S4]];
  const b=[Y0,Y1,Y2];
  const [c0,c1,c2] = solve3(A,b);
  const pred = t.map(ti=>c0+c1*ti+c2*ti*ti);
  const ybar = Y0/n;
  const ssTot = y.reduce((s,yi)=>s+(yi-ybar)**2,0);
  const ssRes = y.reduce((s,yi,i)=>s+(yi-pred[i])**2,0);
  const r2 = 1-ssRes/ssTot;
  return { t0, c0, c1, c2, r2 };
}

const windowEl = { value: 80 };
const CURRENT_YEAR = 2026;

let chartData, chartDeriv;

function fmt(x,d=3){ return Number(x).toFixed(d); }

const STATIC_OPTS = { events: [] };

function updateLongevity() {
  const entity = 'World';
  const all = DATA[entity];
  const winYears = windowEl.value;
  const lastYear = all[all.length-1][0];
  const cutoff = lastYear - winYears;
  const windowed = all.filter(p => p[0] >= cutoff);
  const fit = quadFit(windowed);
  const { t0, c0, c1, c2, r2 } = fit;
  const a = 2*c2, v0 = c1, L0 = c0;

  document.getElementById('lv-L0-out').textContent = fmt(L0,1) + ' años (' + t0 + ')';
  document.getElementById('lv-v0-out').textContent = fmt(v0,3) + ' años/año';
  document.getElementById('lv-a-out').textContent = fmt(a,5) + ' años/año²';
  document.getElementById('lv-r2-out').textContent = fmt(r2,4);

  // Con la ventana fija (Mundo, 80 años) el ajuste da a < 0: los resultados
  // de ambas condiciones son deterministas, por eso van fijos y no por rama.
  const c1out = document.getElementById('lv-cond1-out');
  c1out.textContent = 'no cumple (a < 0)';
  c1out.className = 'lv-val lv-badge-bad';

  const dLdt_now = v0 + a*(CURRENT_YEAR - t0);
  const c2out = document.getElementById('lv-cond2-out');
  c2out.textContent = 'no cumple (a ≤ 0, sin aceleración)';
  c2out.className = 'lv-val lv-badge-bad';
  document.getElementById('lv-fit-note').textContent =
    'dL/dt hoy (' + CURRENT_YEAR + ') ≈ ' + fmt(dLdt_now,3) + ' años/año. Con a ≤ 0 el modelo nunca converge a velocidad de escape.';

  const scatterPts = all.map(p => ({x: p[0]-t0, y: p[1]}));
  const fitStart = windowed[0][0]-t0, fitEnd = lastYear-t0;
  const fitPts = [];
  for (let tt = fitStart; tt <= fitEnd; tt += (fitEnd-fitStart)/40) {
    fitPts.push({x: tt, y: c0 + c1*tt + c2*tt*tt});
  }
  const derivPts = [];
  for (let tt = fitStart; tt <= fitEnd; tt += (fitEnd-fitStart)/40) {
    derivPts.push({x: tt, y: v0 + a*tt});
  }
  const threshPts = [{x: fitStart, y:1},{x: fitEnd, y:1}];

  chartData = new Chart(document.getElementById('lv-chartData'), {
    type: 'scatter',
    data: { datasets: [
      { label: 'Datos reales', data: scatterPts, backgroundColor: COL_MUTED, pointRadius: 2.5, showLine:false },
      { label: 'Ajuste cuadrático', data: fitPts, borderColor: COL_ACCENT, borderWidth: 2, pointRadius: 0, showLine: true, fill:false }
    ]},
    options: Object.assign({ responsive:true, maintainAspectRatio:false,
      scales:{ x:{ title:{display:true,text:'años desde '+t0}, grid:{color:COL_GRID} }, y:{ title:{display:true,text:'L (años)'}, grid:{color:COL_GRID} } },
      plugins:{ legend:{ labels:{ color: COL_MUTED } }, tooltip:{ enabled:false } } }, STATIC_OPTS)
  });

  chartDeriv = new Chart(document.getElementById('lv-chartDeriv'), {
    type: 'line',
    data: { datasets: [
      { label: 'dL/dt', data: derivPts, borderColor: COL_WARN, borderWidth:2, pointRadius:0 },
      { label: 'umbral = 1', data: threshPts, borderColor: COL_MUTED, borderDash:[5,5], borderWidth:1.5, pointRadius:0 }
    ]},
    options: Object.assign({ responsive:true, maintainAspectRatio:false,
      scales:{ x:{ type:'linear', title:{display:true,text:'años desde '+t0}, grid:{color:COL_GRID} }, y:{ title:{display:true,text:'dL/dt'}, grid:{color:COL_GRID} } },
      plugins:{ legend:{ labels:{ color: COL_MUTED } }, tooltip:{ enabled:false } } }, STATIC_OPTS)
  });
}
updateLongevity();
}); // fin withChart
})();
</script>