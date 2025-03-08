### BLOQUE 1 - CONJUNTOS NUMÉRICOS

#### Números Naturales
[Los números naturales son, tal como los conocemos, 1, 2, 3, 4, 5, .... Llamamos N al conjunto de los números naturales, es decir: N = {1, 2, 3, 4, ...}. Estos números se usan a diario para contar. Matemáticamente, contar significa decir cuántos elementos tiene un conjunto. Por ejemplo, el conjunto {a, b, c, d} tiene 4 elementos. ¿Cuántos elementos tiene un conjunto vacío? Como un conjunto vacío no posee ningún elemento, necesitamos un símbolo nuevo que represente la cantidad de elementos de este conjunto. Este símbolo es el 0. Llamamos N0 al conjunto de los números naturales con el cero, o sea: N0 = {0, 1, 2, 3, 4...}.

El conjunto de los números naturales tiene dos operaciones importantes: suma y producto. La suma y el producto de números naturales son operaciones que verifican las siguientes propiedades:

Propiedades de la Suma
Sean a, b, c ∈ N:

Propiedad asociativa: a + (b + c) = (a + b) + c

Propiedad conmutativa: a + b = b + a

Propiedades del Producto
Sean a, b, c ∈ N:

Propiedad asociativa: (a * b) * c = a * (b * c)

Propiedad conmutativa: a * b = b * a

El 1 es el elemento neutro para el producto, es decir: 1 * a = a * 1 = a

Propiedad Distributiva del Producto respecto de la Suma
Las operaciones de suma y producto están relacionadas por: a * (b + c) = a * b + a * c

Notemos que la suma no tiene elemento neutro en N, aunque sí en N0: el 0, ya que a + 0 = 0 + a = a.

Ejemplo 1.1
Veamos cómo se pueden usar estas propiedades para calcular, por ejemplo, el cuadrado de la suma de dos números naturales:

(a + b)^2 = (a + b) * (a + b) (Propiedad distributiva) = (a + b) * a + (a + b) * b (Propiedad distributiva) = a * a + b * a + a * b + b * b = a^2 + ab + ab + b^2 (Propiedad conmutativa del producto) = a^2 + 2ab + b^2

De esto se deduce la identidad: (a + b)^2 = a^2 + 2ab + b^2 La cual resulta de gran utilidad al momento de calcular el cuadrado de un binomio.

Ejercicio 1.2: Encontrar una fórmula para calcular (a + b)^3.]


#### Números Enteros
- Las operaciones y sus propiedades
[Para continuar con el estudio de los números, consideremos N0 el conjunto de los números naturales y el cero. Sabemos que dos números naturales se pueden sumar y se obtiene como resultado otro número natural; también se pueden multiplicar y el resultado es un número natural. Por ejemplo: 13 + 15 = 28 ∈ N 13 * 15 = 195 ∈ N

Además, si quisiéramos restar uno de otro, por ejemplo, hacer 15 - 3, también se puede dentro del conjunto N, es decir: 15 - 3 = 12 ∈ N.

Ejemplo cotidiano: Si Matías tiene 16 figuritas, Pablo le puede pedir prestadas 12 y a Matías aún le quedan 4. Sin embargo, si Matías tuviera solo 10 figuritas, no podría prestarle 12 porque no tiene más de 10. Es decir, ¿qué ocurre si queremos efectuar la operación de resta en el otro sentido, o sea: 10 - 12?

A 10 se le puede "sacar" 12, pero el resultado ya no es un número natural. Esto nos lleva a introducir el concepto de números enteros.

Números enteros (Z): Añadimos a N0 todos los opuestos aditivos de sus elementos (como -1, -2, etc.). Llamaremos al conjunto resultante Z, definido como: Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}

Esto incluye a N y N0. En Z, cualquier número tiene un inverso respecto a la suma, llamado "su opuesto". Por ejemplo: 10 - 12 = 10 + (-12) = -2.

Ejemplo 1.3: Pitágoras nació en el año -582 a.C. y vivió 75 años. ¿En qué año murió? La respuesta se calcula como: -582 + 75 = -507.

Por lo tanto, murió en el año -507.

Ejercicio 1.4: Calcular la diferencia de altura entre la cima del Aconcagua (6959 m sobre el nivel del mar) y el fondo de la Laguna del Carbón (105 m bajo el nivel del mar). Solución: 6959 - (-105) = 6959 + 105 = 7064. Hay una diferencia de 7064 metros.

Propiedades del conjunto Z:
Asociativa de la suma: (a + b) + c = a + (b + c)

Conmutativa de la suma: a + b = b + a

Existe un elemento neutro (0) tal que: a + 0 = 0 + a = a

Cada número tiene un opuesto (-a) tal que: a + (-a) = 0

Asociativa del producto: (a * b) * c = a * (b * c)

Conmutativa del producto: a * b = b * a

Existe un elemento neutro (1) tal que: a * 1 = 1 * a = a

Distributiva del producto respecto a la suma: (a + b) * c = a * c + b * c

Reglas para multiplicar con signos:
El producto de números con el mismo signo es positivo: (+a) * (+b) = +ab (-a) * (-b) = +ab

El producto de números con signos diferentes es negativo: (+a) * (-b) = -ab (-a) * (+b) = -ab]

- Divisibilidad y algoritmo de la división
[Imaginemos que tenemos una tableta de chocolate de seis cuadraditos que dos amigos quieren compartir por igual. Esta operación puede realizarse convenientemente, y a cada uno le tocan tres de las seis partes que tiene la tableta. Ahora, imaginemos que tenemos 7 lapiceras que queremos repartir entre dos amigos. Es claro que, para que a cada uno le toque la misma cantidad, podemos darle tres lapiceras a cada uno, pero sobra una lapicera. Es decir, la lapicera sobrante no puede partirse.

La división es la operación que permite averiguar cuántas veces un número (el divisor) está contenido en otro número (el dividendo). Por ejemplo: 2 está 3 veces en 6 porque 3 * 2 = 6. Por lo tanto: 6 ÷ 2 = 3.

En este sentido, la división es la operación inversa de la multiplicación. Se denomina cociente al resultado entero de la división. Si la división no es exacta, es decir, si el divisor no está contenido un número exacto de veces en el dividendo, la operación tendrá un resto. Por ejemplo, en el caso de las lapiceras: 7 ÷ 2 = 3 (cociente) con un resto de 1. Esto puede expresarse como: 7 = 3 * 2 + 1.

Definición 1.8: Si a, b ∈ Z con a ≠ 0, decimos que a divide a b si existe q ∈ Z tal que: b = q * a, donde q es el cociente de la división de b por a.

Para expresar simbólicamente esto, escribimos: a | b.

También se dice que b es divisible por a, o que a es un divisor de b.

Algoritmo de división: Para efectuar la división de un número natural por otro y obtener la expresión: dividendo = cociente * divisor + resto, el procedimiento es el siguiente:

Por ejemplo: Para el dividendo 4712 y divisor 23: 4712 ÷ 23 se realiza siguiendo los pasos del algoritmo de división.

El algoritmo exige que el resto sea siempre no negativo, es decir, positivo o cero. Esto se sintetiza en el siguiente enunciado:

"Dado un dividendo n y un divisor d con d ≠ 0, el algoritmo de división es el procedimiento que permite escribir de manera única: n = q * d + r donde 0 ≤ r < |d|.

Los números q y r se llaman el cociente y el resto, respectivamente, de la división de n entre d."

Nota: La expresión |d| indica considerar el valor absoluto de d (sin signo).

Ejemplo 1.10: El número 2 divide a 2 porque existe un 1 ∈ Z tal que: 2 = 1 * 2.

Asimismo, el número 2 divide a 4, 6, 8, 20, y a todos los números pares. De hecho, un número es par si es divisible por 2, es decir, si el resto de dividirlo entre 2 es 0. Por lo tanto, si n ∈ Z es par, entonces: n = 2 * k para algún k ∈ Z.

Ejercicio 1.11: ¿Cómo se puede describir a todos los números impares?]

- Teorema fundamental de la aritmética
[Definición 1.12:
Un número entero se dice primo si tiene exactamente cuatro divisores distintos. En otras palabras, un número n ∈ Z es primo si y solo si sus únicos divisores son: 1, -1, n y -n, y todos son distintos entre sí.

Un número entero distinto de 1, -1 y 0 que no es primo se llama compuesto. Esto es porque, si n ≠ 1, -1, 0 no es primo, entonces n puede expresarse como un producto de números primos.

Nota: El número 1 no es primo.

Los primeros números primos positivos son: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67...

Ejemplo 1.13:
Los divisores de 6 son: 1, 2, 3, 6 y sus opuestos: -1, -2, -3, -6.

Por lo tanto, 6 tiene ocho divisores en total y no es primo.

En cambio, los únicos divisores de 7 son: 1, 7 y sus opuestos: -1, -7.

Por lo tanto, 7 es primo.

Teorema 1.14:
Teorema Fundamental de la Aritmética: Todo número n ∈ Z tal que n ≠ 0, 1, -1, puede factorizarse como un producto de números primos. Además, esta factorización es única, salvo por el orden de los factores.

Ejemplo 1.15:
Factorización de un número entero: Calculemos la factorización de 360. El procedimiento consiste en dividir repetidamente el número por primos positivos, en orden, tantas veces como sea posible:

360 ÷ 2 = 180

180 ÷ 2 = 90

90 ÷ 2 = 45

45 ÷ 3 = 15

15 ÷ 3 = 5

5 ÷ 5 = 1

Por lo tanto, la factorización de 360 es: 360 = 2 * 2 * 2 * 3 * 3 * 5

Observación 1.16:
La factorización prima permite calcular todos los divisores de un número. Por ejemplo, los divisores positivos de 360 son: {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360}.

Nota: Aunque aquí solo mostramos los divisores positivos, también asumimos que los opuestos de estos valores dividen a 360.

Observación 1.17:
La factorización prima de un entero negativo se obtiene multiplicando por -1 la factorización prima de su opuesto aditivo.]

- Máximo común divisor
[Además de encontrar todos los divisores de un número, a veces es importante conocer los divisores comunes de dos enteros para responder preguntas como: ¿cuál es el divisor más grande de ambos?

Por ejemplo, los divisores positivos de 54 son: D(54) = {1, 2, 3, 6, 9, 18, 27, 54}.

Por otra parte, los divisores positivos de 60 son: D(60) = {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}.

Los divisores comunes de 54 y 60 son: {1, 2, 3, 6}, de los cuales el máximo es 6. En otras palabras: MCD(54, 60) = 6 o también (54 : 60) = 6.

Definición 1.18:
Dados dos enteros a y b distintos de cero, el Máximo Común Divisor (MCD) de a y b es un número natural d que cumple las siguientes condiciones:

d divide a a y d divide a b. (Esto es, d|a y d|b).

Si existe cualquier otro número c tal que c|a y c|b, entonces c también divide a d.

La primera condición asegura que d es un divisor de a y b, mientras que la segunda garantiza que d es el mayor entre todos los divisores comunes.

Ejemplo 1.19:
Calculemos el MCD de 252 y 360 utilizando sus descomposiciones en factores primos:

252 = 2^2 * 3^2 * 7

360 = 2^3 * 3^2 * 5

Primos comunes:

Para 2, el menor exponente es 2.

Para 3, el menor exponente es 2.

Por lo tanto: MCD(252, 360) = 2^2 * 3^2 = 36.

Observación 1.20:
El MCD de dos números es el producto de los primos comunes elevados a sus menores exponentes.

Ejemplo 1.21:
En una bodega hay tres toneles de vino con capacidades de 250 l, 360 l y 540 l. Queremos envasarlos en garrafas iguales con la mayor capacidad posible. Esto requiere calcular: MCD(250, 360, 540).

Descomposición en factores primos:

250 = 2 * 5^3

360 = 2^3 * 3^2 * 5

540 = 2^2 * 3^3 * 5

Primos comunes:

Para 2, el menor exponente es 1.

Para 5, el menor exponente es 1.

Por lo tanto: MCD(250, 360, 540) = 2 * 5 = 10.

Capacidad máxima de las garrafas: 10 l.

Cantidad de garrafas necesarias:

Para 250 l: 250 ÷ 10 = 25 garrafas.

Para 360 l: 360 ÷ 10 = 36 garrafas.

Para 540 l: 540 ÷ 10 = 54 garrafas.

Total: 25 + 36 + 54 = 115 garrafas de 10 l cada una.]

- Mínimo común múltiplo
[Para lograr un rendimiento óptimo, la fábrica X recomienda a los propietarios de sus autos cambiar el aceite cada 6,000 km y el líquido refrigerante cada 8,000 km. ¿Cuál es la cantidad mínima de km al cabo de la cual hay que renovar los dos líquidos a la vez?

La respuesta a esta pregunta es una cantidad n de km tal que coincida el cambio de aceite con el de líquido refrigerante; es decir que, en miles de km:

n debe ser 6 o 12 o 18, etc., para que toque hacer un cambio de aceite.

Por otra parte, n debe ser 8 o 16 o 24, etc., para que sea necesario efectuar un cambio de refrigerante.

Es decir, que n debe ser a la vez múltiplo de 6 y de 8.

El primer ejemplo que viene a la mente es 48, que es igual a 6 * 8, ya que claramente es un múltiplo de ambos. Sin embargo, no necesariamente es el menor de los múltiplos comunes.

Si pensamos cuidadosamente, nos damos cuenta de que el mínimo natural que satisface estas condiciones es n = 24 (en miles de km).

Respuesta: Cada 24,000 km corresponde renovar ambos líquidos para optimizar el rendimiento.

Denotación: mcm(6, 8) = [6 : 8] = 24.

Definición 1.22:
Dados dos enteros a y b, un número natural m se llama mínimo común múltiplo (mcm) de a y b si verifica:

a|m y b|m.

Si existe otro natural m′ tal que a|m′ y b|m′, entonces m|m′.

La primera condición asegura que m es múltiplo de a y b. La segunda garantiza que m es el mínimo entre todos los múltiplos comunes.

Ejemplo 1.23:
Calculemos el mcm de 252 y 360:

Descomposición en factores primos:

252 = 2^2 * 3^2 * 7

360 = 2^3 * 3^2 * 5

El múltiplo común debe tener:

Todos los factores primos que aparecen en ambas descomposiciones (2, 3, 5, 7).

Elevados a sus mayores exponentes: m = 2^3 * 3^2 * 5 * 7 = 2520.

Respuesta: mcm(252, 360) = 2520.

Nota 1.24:
El mínimo común múltiplo es el producto de los primos comunes y no comunes elevados a su mayor exponente.

Ejemplo 1.25:
Un faro enciende su luz cada 12 segundos, otro cada 18 segundos y un tercero cada 60 segundos. A las 6:30 PM los tres coinciden.

Pregunta: ¿Cuántas veces volverán a coincidir en los próximos 5 minutos?

Solución:

Descomposición en factores primos:

12 = 2^2 * 3

18 = 2 * 3^2

60 = 2^2 * 3 * 5

Calculamos el mcm:

Tomamos los factores comunes y no comunes elevados a sus mayores exponentes: mcm(12, 18, 60) = 2^2 * 3^2 * 5 = 180.

Convertimos el resultado a minutos:

180 segundos = 3 minutos.

Respuesta: Los faros coinciden cada 3 minutos. Por lo tanto, en los siguientes 5 minutos coincidirán una vez más, a las 6:33 PM.

Ejercicio 1.26:
María quiere dividir una cartulina de 40 cm de largo y 30 cm de ancho en cuadrados iguales, tan grandes como sea posible, de forma que no le sobre ningún trozo de cartulina.

Pregunta:

¿Cuánto medirán los lados de los cuadrados obtenidos?

¿Cuántos cuadrados puede hacer con una cartulina?

Solución:

Resultado: Se obtienen 12 cuadrados de 10 cm de lado.

Ejercicio 1.27:
Luis va a ver a su abuela cada 12 días y Ana cada 15 días. Hoy han coincidido los dos.

Pregunta:

¿Cuántos días pasarán hasta que vuelvan a coincidir en casa de su abuela?

Solución:

Resultado: Coincidirán de nuevo en 60 días.

Ejercicio 1.28:
Un autobús pasa por una parada cada 18 minutos, otro cada 25 minutos y un tercer autobús cada 36 minutos. Si a las 9:00 AM han pasado en ese lugar los tres autobuses a la vez:

Pregunta:

¿Cuántas horas mínimo tienen que pasar para que vuelvan a parar los tres simultáneamente?

¿A qué hora vuelven a coincidir?

Solución:

Pasarán 15 horas hasta que vuelvan a encontrarse.

Hora de coincidencia: 12:00 AM del día siguiente.

Ejercicio 1.29:
Eva tiene una cuerda roja de 15 m y una azul de 20 m. Quiere cortarlas en trozos de la misma longitud, de forma que no sobre nada.

Pregunta:

¿Cuál es la longitud máxima de cada trozo de cuerda que puede cortar?

¿Cuántos trozos obtiene luego de los cortes?

Solución:

Longitud de cada trozo: 5 m.

Total de trozos: 7]


#### Números Racionales
[Dos amigos deciden participar en un torneo de beach voley en el cual no tienen un buen desempeño. Como premio consuelo, les dan un solo sándwich de milanesa para compartir.

Pregunta: ¿Cómo hacen para repartir el premio entre los dos?

La respuesta es simple si estamos acostumbrados a trabajar con números: deben tomar medio sándwich cada uno.

Pero, ¿qué quiere decir "la mitad"? ¿Qué representa el número 1/2?

En la primera sección, estudiamos los números naturales y vimos sus aplicaciones. En la segunda, observamos la utilidad de agregar al conjunto de los números naturales un elemento neutro (el cero) y un opuesto aditivo para cada número natural, obteniendo así el conjunto de números enteros.

El conjunto de números naturales tiene dos operaciones importantes; por ello, tratamos de agregar inversos para el producto.

No hay manera de construir un conjunto que contenga los enteros y en el cual cada número tenga inverso multiplicativo, ya que el número debe ser no nulo (pues 0 * b = 0, para cualquier b).

Así, ampliamos el conjunto de números enteros para que todos los números enteros, excepto el cero, tengan inverso multiplicativo.

La manera más intuitiva de hacerlo es considerando fracciones, es decir, cocientes de la forma n/d donde n y d son enteros, y d ≠ 0.

En esta expresión:

n: numerador.

d: denominador.

Interpretación de las fracciones:
La fracción 1/d representa tomar el elemento unidad (1), partirlo en d pedazos iguales, y tomar uno de esos pedazos.

Por ejemplo:

Si n > 0, la fracción n/d representa tomar n veces la fracción 1/d.

Problema con las fracciones:
Consideremos:

1/2: representa "la mitad" de la unidad.

3/6: representa "tres veces la sexta parte de la unidad".

Aunque 1/2 y 3/6 son fracciones distintas, representan la misma cantidad.

Dentro de todas las fracciones que representan el mismo número, hay una que destaca y llamamos irreducible.

Definición 1.30:
Una fracción a/b es irreducible si:

b > 0.

MCD(a, b) = 1.

Nota: MCD(a, b) representa el mayor divisor común de a y b.

Proposición 1.31:
Toda fracción es equivalente a una única fracción irreducible.

Proposición 1.32:
Si a/b es irreducible y a/b es equivalente a c/d, entonces existen m ∈ Z tal que:

c = a * m

d = b * m

Observación 1.33:
Sean a/b y c/d dos fracciones. Para que sean equivalentes, el numerador y denominador de una deben ser múltiplos de los de la otra.

En otras palabras: Si a/b y c/d son equivalentes, entonces:

a * d = c * b.

Ejercicio 1.34:
Indicar cuáles de los siguientes pares de fracciones son equivalentes. Hallar la fracción irreducible equivalente a cada fracción dada:

5/10 y 10/20

32/7 y 64/5

153/2 y 1530/2]

- Las operaciones y sus propiedades
[Cuando extendimos los números naturales para obtener un conjunto en el que (además de los naturales) cada elemento tenga un opuesto aditivo, lo hicimos de manera tal que se mantengan las operaciones inducidas en N (suma y producto) y sus propiedades.

Análogamente, si extendemos el conjunto Z a un nuevo conjunto numérico Q para que cada entero no nulo tenga un inverso multiplicativo, debemos definir nuevamente las operaciones de suma y producto de tal manera que, aplicadas a números enteros, los resultados no varíen y además se mantengan las propiedades previamente válidas.

Definición 1.35: El producto de dos fracciones a/b y c/d se define como: (a/b) * (c/d) = (a * c) / (b * d) Si a, b ∈ Z, entonces: (a/1) * (b/1) = (a * b) / (1 * 1) = a * b

Definición 1.36: La suma de dos fracciones a/b y c/d se define como: (a/b) + (c/d) = (a * d) / (b * d) + (b * c) / (b * d) = (a * d + b * c) / (b * d) Si a, b ∈ Z, entonces: (a/1) + (b/1) = ((a * 1) + (1 * b)) / (1 * 1) = a + b

Propiedades de la Suma y el Producto de Números Racionales: Sean a/b, c/d, e/f ∈ Q:

Asociativa de la suma: ((a/b) + (c/d)) + (e/f) = (a/b) + ((c/d) + (e/f))

Conmutativa de la suma: (a/b) + (c/d) = (c/d) + (a/b)

Existe 0 ∈ Q tal que: (a/b) + 0 = 0 + (a/b) = (a/b)

Para cada a/b ∈ Q, existe un único elemento -a/b ∈ Q tal que: (a/b) + (-a/b) = 0

Asociativa del producto: ((a/b) * (c/d)) * (e/f) = (a/b) * ((c/d) * (e/f))

Conmutativa del producto: (a/b) * (c/d) = (c/d) * (a/b)

Existe 1 ∈ Q tal que: (a/b) * 1 = 1 * (a/b) = (a/b)

Para cada a/b ∈ Q no nulo, existe un único elemento (b/a) ∈ Q tal que: (a/b) * (b/a) = 1

Propiedad distributiva: ((a/b) + (c/d)) * (e/f) = ((a/b) * (e/f)) + ((c/d) * (e/f))

Nota 1.37:

Diferencia: (a/b) - (c/d) = (a/b) + (-c/d)

Cociente: (a/b) : (c/d) = (a/b) * (d/c)

Ejercicio 1.39:

a) 2 * (1/5) + (n/3) - (2/5) - (1/2) * (-3 * (-2/3) - 1 + (1/5)) + 4 * (-5/2) Resultado: -38/5

b) 1 - (8/3) * (-3/4) - (n/2) - ((3/4) - 1 + (2/5) * ((-10 + 15)/4) - 1) Resultado: -11/4

c) (8/15) + (15/8) * (-4/3) + (2/5) * (1/3) - (-2/3) + 1 * (1/2) - (1/3) Resultado: -1
]

- Porcentajes y Fracción de un total
[Imaginemos que tenemos una caja con 75 lápices y queremos tomar 2/5 de ellos. Esto significa dividir 75 en cinco partes iguales y de esas partes tomar solo dos. Numéricamente, esta expresión representa: (2 * 75) / 5 = (2/5) * 75 = 30.

Como vemos, tomar una fracción de un total se resuelve multiplicando ambas magnitudes.

Ejemplo 1.40:
Mariana tiene $2025 y gastó 2/5 del dinero en un jean y 1/3 de lo que le quedaba en comprar un libro de aventuras. Pregunta: ¿Cuánto dinero le queda aún?

Solución:

Costo del jean: (2/5) * 2025 = 810 El jean costó $810.

Dinero restante después del jean: 2025 - 810 = 1215.

Costo del libro: (1/3) * 1215 = 405.

Dinero restante después del libro: 1215 - 405 = 810.

Respuesta: A Mariana aún le quedan $810.

Ejercicio 1.41:
Emilia tiene un libro de 144 páginas. En la primera semana, luego de comprarlo, leyó 1/12 del total del libro. La semana siguiente leyó 5/6 de lo que le quedaba.

Pregunta:

¿Cuántas páginas le restan leer aún?

¿Qué fracción del total representan esas páginas?

Solución: Le restan leer 22 páginas.

Ejercicio 1.42:
Mariano tiene que juntar $7200 para irse de vacaciones con sus amigos. Él juntó 1/3 del total, y sus padres le dieron 1/4 del total por haber aprobado todas las materias.

Preguntas:

¿Qué fracción del total juntó? ¿Cuánto representa esta fracción en pesos?

¿Qué fracción le falta?

Si sus abuelos le regalan $1200 más, ¿qué fracción del total tiene ahora?

El término porcentaje es una forma de expresar una fracción o parte de un entero, tomando al entero como 100. Por ejemplo, tomar el 30% de un total significa tomar 30/100 partes de ese total.

Ejemplo 1.43:
Los embalses de agua que abastecen a una ciudad tienen una capacidad total de 400 km³ y se encuentran al 27% de su capacidad.

Pregunta: ¿Cuántos km³ de agua contienen?

Solución:

El 27% de la capacidad total es: (27/100) * 400 = 108.

Respuesta: El embalse contiene 108 km³ de agua.

Ejemplo 1.44:
Una máquina que fabrica tornillos produce un 3% de piezas defectuosas. Si hoy se han apartado 51 tornillos defectuosos:

Pregunta: ¿Cuántas piezas ha fabricado la máquina?

Solución:

El 3% del total de tornillos fabricados es igual a 51: (3/100) * T = 51.

Resolviendo para T: T = 51 / (3/100) = (51 * 100) / 3 = 1700.

Respuesta: La máquina ha fabricado 1700 tornillos.

Ejercicio 1.45:
Berenice ayudó a su papá a vender pizzas a domicilio durante sus vacaciones. Él ofreció pagarle el 15% de todo lo que ella vendiera. Si al finalizar el verano Berenice vendió $735.5, ¿cuánto le pagó su papá?

Ejercicio 1.46:
En una ciudad de 23,500 habitantes, el 68% están contentos con la gestión municipal.

Pregunta: ¿Cuántos ciudadanos están contentos?

Ejercicio 1.47:
María compró mercancía por $4375 en una venta de saldos. Si al vender esa mercancía obtuvo $5425:

Pregunta: ¿Qué porcentaje obtuvo de ganancia?]

- Orden de los Números Racionales
[La forma de comparar números racionales expresados como fracción es buscar fracciones equivalentes con igual denominador y luego comparar sus numeradores.

Ejemplo 1.48:
Ordenar en forma creciente las fracciones: 3/2, 4/3.

Solución:

Busquemos fracciones equivalentes con igual denominador.

El mínimo común múltiplo (mcm) de los denominadores 2 y 3 es: mcm(2, 3) = 6.

Las fracciones equivalentes con denominador 6 son:

(3 * 3) / (2 * 3) = 9/6.

(4 * 2) / (3 * 2) = 8/6.

Comparando:

9/6 > 8/6.

Conclusión: 4/3 < 3/2.

Definición 1.49:
Sean a/b y c/d ∈ Q: a/b < c/d si y solo si (a * d) < (c * b). Por lo tanto: a/b < c/d ⇔ (a * d) < (c * b).

Ejemplo 1.50:
Ordenar en forma creciente las fracciones: 11/10, 9/8, 5/4.

Solución:

Busquemos fracciones equivalentes con igual denominador.

El mcm de 10, 8, y 4 es: mcm(10, 8, 4) = 40.

Las fracciones equivalentes con denominador 40 son:

(11 * 4) / (10 * 4) = 44/40.

(9 * 5) / (8 * 5) = 45/40.

(5 * 10) / (4 * 10) = 50/40.

Comparando:

44/40 < 45/40 < 50/40.

Conclusión: 11/10 < 9/8 < 5/4.]

- Representación decimal de los números racionales
[Otra de las maneras conocidas de representar los números racionales es a partir de su desarrollo decimal. Al estudiar los números enteros, vimos que los podemos representar como una tira finita de números del 0 al 9.

Los números racionales tienen una representación parecida, pero la tira no tiene que ser necesariamente finita, aunque sí debe tener cierto periodo. Es decir, los números racionales pueden representarse por una tira infinita de dígitos que, a partir de cierto lugar, comienzan a repetirse indefinidamente.

Ambas representaciones son equivalentes. Por tanto, dada una fracción, podemos encontrar la expresión decimal que la representa; y al revés, dado el desarrollo decimal de un número racional, podemos hallar una fracción equivalente.

Paso de fracción a expresión decimal:
Para hallar el desarrollo decimal de un número racional dado en forma de fracción, simplemente realizamos la división del numerador por el denominador.

Paso de expresión decimal a fracción:
Para convertir un número en su desarrollo decimal a fracción, identificamos si el número tiene periodo cero o no, y evaluamos los siguientes casos:

Si el número racional tiene en su desarrollo decimal periodo cero: Una fracción equivalente se forma tomando:

Numerador: El número dado (como número entero, sin coma).

Denominador: Un 1 seguido de tantos ceros como cifras haya en la parte decimal.

Ejemplos:

0.953 = 953 / 1000.

12.578 = 12578 / 1000 = 6289 / 500 (simplificada).

Si el número racional tiene periodo no nulo: La fracción se forma así:

Numerador: La parte entera seguida de las partes decimal periódica y no periódica, menos la parte entera y decimal no periódica (todo considerado como un número entero).

Denominador: Un 9 por cada cifra decimal periódica y un 0 por cada cifra decimal no periódica.

Ejemplos:

1.52(3) = (1523 - 152) / 900 = 1371 / 900.

0.7(95) = (795 - 7) / 990 = 788 / 990.

Ejercicio 1.51:
Resuelve los siguientes problemas:

Encuentra fracciones irreducibles que representen a los números 0.(9) y 1.(0).

Encuentra fracciones irreducibles que representen a los números 2.5(9) y 2.6.

¿Qué puedes deducir de los apartados anteriores?

Observación 1.52:
Dos expresiones decimales distintas pueden ser el desarrollo decimal del mismo número real. Las expresiones con las cuales esto ocurre corresponden a los casos mostrados en los ejemplos.]


#### Números Reales
- Números Irracionales
[Podríamos decir que la mayor parte de los científicos de la historia (si no todos), ya sean matemáticos, físicos, químicos, biólogos o de cualquier otra rama, han soñado con realizar un descubrimiento brillante que rompa los esquemas de la ciencia de su tiempo. Pero también es cierto que cuando esto ocurre, la situación no suele ser del todo cómoda para la persona en cuestión.

La historia que vamos a contar se desarrolla en torno al siglo V a.C. en la antigua Grecia, y los protagonistas son los pitagóricos. Sin embargo, el protagonista principal es, por razones que veremos más adelante, Hipaso de Metaponto.

Los pitagóricos tenían la firme creencia de que todo el Universo podía ser explicado con números racionales. Según cuenta la leyenda, Hipaso fue el culpable de demostrar que esto no podía ser real. Hipaso se planteó el problema de medir la diagonal de un cuadrado de lado 1.

Dado que era un pitagórico, Hipaso esperaba que la medida de esta diagonal pudiera expresarse como un número natural o una fracción. Sin embargo, se dio cuenta de que esta medida no podía expresarse ni como un número natural ni como una fracción formada por números naturales.

Hoy sabemos que esta diagonal mide √2, y que es un número conocido como irracional. Cuando Hipaso comunicó este descubrimiento, los pitagóricos, al considerar este hallazgo una "catástrofe", lo arrojaron al mar por revelar este hecho fuera de la secta.

La raíz de la muerte de Hipaso fue exactamente la raíz de dos.

Demostración de que √2 no es un número racional:
Supongamos erróneamente que existe un número racional x, tal que: x = √2.

Si x es una fracción en su expresión irreducible, entonces existirán enteros p y q tales que: x = p / q = √2.

De esta igualdad, deducimos: x^2 = (p / q)^2 = (p^2) / (q^2) = 2.

Despejando: p^2 = 2 * q^2.

Esto implica que p^2 es par, y por lo tanto p también es par. Si p es par, puede escribirse como p = 2k, donde k es un entero. Sustituyendo: p^2 = (2k)^2 = 4k^2 = 2 * q^2.

Dividiendo entre 2: q^2 = 2 * k^2.

Esto implica que q^2 también es par, y por lo tanto q es par.

Llegados a este punto, hemos concluido que tanto p como q son pares, lo que significa que ambos son divisibles por 2. Esto contradice nuestra suposición inicial de que p / q es una fracción irreducible.

Conclusión: El supuesto de que √2 es racional lleva a una contradicción. Por lo tanto, √2 es un número irracional.

Los números racionales (que incluyen a los enteros y por tanto a los naturales) son aquellos cuya expresión decimal tiene infinitas cifras decimales que se repiten con cierto período. Sin embargo, esto no incluye todos los números.

Por ejemplo, considere el número: 0.10110011100011110000...

Esta expresión decimal es no periódica, por lo que no es un número racional, al igual que √2.

Definición:

Al conjunto de números cuya expresión decimal posee infinitas cifras no periódicas, lo llamaremos conjunto de los números irracionales, y lo simbolizaremos con I.

La suma y el producto de números irracionales pueden ser racionales o irracionales.

El conjunto de todos los números (racionales e irracionales) se llama el conjunto de los números Reales y se representa por R., es el conjunto
de todos los números vistos hasta aquí]

- Las operaciones y propiedades
[Las operaciones de suma y producto de Números Reales son cerradas en R. Esto significa que el resultado de estas operaciones pertenece también al conjunto de los números reales.

Además, dichas operaciones verifican las siguientes propiedades. Sean a, b, c ∈ R:

Asociativa de la suma: (a + b) + c = a + (b + c)

Conmutativa de la suma: a + b = b + a

Elemento neutro de la suma: Existe 0 ∈ R tal que para todo a ∈ R: a + 0 = 0 + a = a

Inverso aditivo: Para cada a ∈ R, existe un único elemento -a ∈ R tal que: a + (-a) = 0

Asociativa del producto: (a * b) * c = a * (b * c)

Conmutativa del producto: a * b = b * a

Elemento neutro del producto: Existe 1 ∈ R tal que para todo a ∈ R: a * 1 = 1 * a = a

Inverso multiplicativo: Para cada a ∈ R, no nulo, existe un único elemento a^(-1) ∈ R tal que: a * a^(-1) = 1

Distributiva del producto respecto a la suma: (a + b) * c = (a * c) + (b * c)

Por cumplir las anteriores propiedades, decimos que R tiene estructura de cuerpo.

Además, otras propiedades útiles que verifican los números reales son:

Si a + b = a + c, entonces: b = c

Si a * 0 = 0 * a, entonces: a * 0 = 0

Si a * b = 0, entonces: a = 0 o b = 0

Si a ≠ 0 y a * b = a * c, entonces: b = c]

- El orden en los números reales
[Formalmente, diremos que dados dos números reales a y b, a es menor que b si ocurre que: b - a > 0.

Sin embargo, esta definición no es práctica para establecer el orden entre ellos. Una forma más útil de comparar números reales es a través de su desarrollo decimal.

Ejemplo: Supongamos que: x = 0.1235549 y = 0.1234549

En este caso, los primeros tres dígitos después de la coma (de x y de y) coinciden, pero el cuarto dígito de x es mayor que el de y. Por lo tanto, diremos que: x > y.

Otros ejemplos:
-1.213 < 0.12

1.213 < 1.2132

-1.213 > -1.2132

0.209 < 0.210

Nota 1.53:
Debemos tener cuidado y no usar este método para comparar expresiones distintas que representan el mismo número real (como se vio en ejercicios anteriores).

Por ejemplo, no puede usarse para comparar 1 y 0.(9) porque son expresiones distintas para el mismo número real.

Propiedades del Orden en R:
La relación de orden < verifica, para todos a, b, c ∈ R, las siguientes propiedades:

Tricotomía: Vale una y solo una de las siguientes relaciones:

a < b

a = b

a > b

Transitividad: Si a < b y b < c, entonces: a < c

Multiplicación positiva: Si 0 < a y b < c, entonces: a * b < a * c

Multiplicación negativa: Si a < 0 y b < c, entonces: a * b > a * c

Adición: Si a < b, entonces: a + c < b + c

Notas adicionales:
Nota 1.54: Diremos que a ∈ R es positivo si: a > 0.

Nota 1.55: La relación a ≤ b indica que: a < b o a = b.

Nota 1.56: Entre dos números reales cualesquiera a y b, hay infinitos números reales. En particular, existe m = (a + b) / 2 tal que: a ≤ m ≤ b.

Ejercicio 1.57:
Sabiendo que: 0.4 < a < 0.8 0.4 < b < 1

Responda:

¿Entre qué valores está a + b?

¿Entre qué valores está 1 / a?

¿Entre qué valores está -b?

Solución:

Para a + b:

Mínimo: 0.4 + 0.4 = 0.8.

Máximo: 0.8 + 1 = 1.8. Respuesta: 0.8 < a + b < 1.8.

Para 1 / a:

Mínimo: 1 / 0.8 = 1.25.

Máximo: 1 / 0.4 = 2.5. Respuesta: 1.25 < 1 / a < 2.5.

Para -b:

Mínimo: -1.

Máximo: -0.4. Respuesta: -1 < -b < -0.4.]

- La recta numérica
[Un concepto fundamental que relaciona la noción abstracta de número real con la noción geométrica de punto es la representación de cada número sobre una recta orientada llamada recta numérica.

La recta numérica es una línea recta en la cual:

Se elige un punto que representará el origen (el 0).

Se toma otro punto a la derecha del origen que representará el número 1.

La distancia entre 0 y 1 determina la escala de la recta, y por lo tanto es la distancia que se usará para separar cada número entero de su anterior y su siguiente.

Se indica el sentido creciente de la recta mediante una flecha en el extremo derecho.

Cada punto en la recta representa la distancia del mismo al origen.

Como ya sabemos, los números racionales no llenan la recta numérica, pues existen puntos en la recta que no son alcanzados por ningún número racional.

Por ejemplo, el número π. Sin embargo, a cada número real se le puede asociar un punto en la recta, y viceversa: a cada punto de la recta se le puede asociar un único valor real.

Aunque representar con exactitud cualquier número es imposible, podemos hacerlo de manera aproximada.

Ejemplo 1.58:
Marca en la recta real 7/4.

Solución: Para ubicar 7/4 en la recta numérica:

Dividimos cada unidad en 4 partes iguales.

Marcamos el séptimo punto contando desde el origen.

Ejemplo 1.59:
Marca en la recta real 2/5 y 3/2.

Solución:

Dividimos cada unidad primero en 5 partes iguales y luego en 2 partes iguales.

Para poder marcar ambas fracciones en la misma recta, usamos el mcm(2, 5): mcm(2, 5) = 10.

Entonces dividimos cada unidad en 10 partes iguales para ubicar correctamente ambas fracciones.

Ejemplo 1.60:
Ubica en la recta real el número irracional √2.

Solución: Para calcular la posición de √2, recordemos que: 2 = 1 + 1. Por lo tanto: (√2)^2 = 1 + 1.

Aplicando el Teorema de Pitágoras:

Dibujamos un triángulo rectángulo ABC donde:

Los catetos AB y AC miden 1.

La hipotenusa BC mide √2.

Coincidimos uno de los catetos con el segmento [0, 1] en la recta numérica.

En ángulo recto, trazamos el otro cateto.

Usamos un compás para transportar la longitud de la hipotenusa √2 a la recta numérica.

Ejercicio 1.61:
Marcar en una misma recta numérica los puntos:

√3

5/2

3/9

Pregunta: Ordena los números en orden ascendente.]


#### Potenciación y Radicación
- Potenciación
Definición 1.62:
Siendo a un número real y n un número entero positivo, la potencia enésima de a se define como el número real a^n, resultado del producto de n factores iguales a a.

En símbolos: a^n = a * a * a ... (n factores).

Donde:

a: base de la potencia.

n: exponente.

a^n: potencia enésima de a.

Ejemplos:
(−5)^2: (−5)^2 = (−5) * (−5) = 25.

x^3: x^3 = x * x * x.

(-2/3)^3: (-2/3)^3 = (-2/3) * (-2/3) * (-2/3) = -8/27.

Observación 1.66:
“La potencia de un número solo es negativa cuando la base es negativa y el exponente es impar; en los otros casos, el resultado es positivo.”

Definición 1.67:
Si a es un número real distinto de 0 y n es un número entero positivo, definimos: a^(-n) = 1 / (a^n).

Ejemplos:
3^(-2): 3^(-2) = 1 / (3^2) = 1 / 9.

(3/2)^(-3): (3/2)^(-3) = (2/3)^3 = (2 * 2 * 2) / (3 * 3 * 3) = 8 / 27.

4^(-1): 4^(-1) = 1 / 4 = 1/4.

Propiedades de la potenciación:
Propiedad distributiva respecto al producto: Si a y b son números reales, y n es un número entero positivo, entonces: (a * b)^n = (a^n) * (b^n).

Ejemplo: ((-3) * x)^4 = ((-3)^4) * (x^4) = 81 * x^4.

Propiedad distributiva respecto al cociente: Si a ∈ R, b ∈ R - {0} y n es un número entero positivo, entonces: (a / b)^n = (a^n) / (b^n).

Ejemplo: ((x / y)^2) = (x^2) / (y^2).

Observación 1.73:
La potenciación no es distributiva respecto a la suma ni a la resta.

Ejemplo:

(a + b)^n ≠ a^n + b^n.

(x + 3)^2 ≠ x^2 + 9.

Producto de potencias de igual base: Si a ∈ R y m, n son números enteros positivos: a^m * a^n = a^(m + n).

Ejemplo: (-2)^3 * (-2)^6 * (-2)^(-2) = (-2)^(3 + 6 - 2) = (-2)^7 = -128.

Cociente de potencias de igual base: Si a ∈ R - {0} y m, n son enteros: (a^m) / (a^n) = a^(m - n).

Ejemplo: (3^5) / (3^2) = 3^(5 - 2) = 3^3 = 27.

Observación 1.78:
Cuando m = n: (a^m) / (a^n) = a^(m - n) = a^0.

Pero sabemos que: (a^m) / (a^n) = 1. Por lo tanto: a^0 = 1.

Potencia de potencia: Si a ∈ R y m, n son números enteros positivos: (a^m)^n = a^(m * n).

Ejemplo: (x^5)^2 = x^(5 * 2) = x^10.

Ejercicio 1.81:
Determina cuáles de las siguientes propiedades de potenciación están bien aplicadas. Si son incorrectas, corrígelas:

(a * b)^n = a^n * b^n.

(a^m) / (a^n) = a^(m + n).

(a + b)^n = a^n + b^n.

a^m * a^n = a^(m * n).

(a^m)^n = a^(m * n).

Ejercicio 1.82:
Resuelve los siguientes ejercicios aplicando las propiedades de potenciación:

3 * ((2 * 3)^(-1)) * (1 / 2)^3 * ((3 * 2^2)^(-2)).

((2/3)^2 * ((6/3) * (2^2)) * ((2/3)^(-1)))^(-2).

((3^2)^3 * (2 * 3^5)^(-2) * (18)^2).

(((2/3)^(-2))^4 * ((3/4)^(-1))^2).]

- Radicación
[La potenciación nos permite calcular la potencia de un número cuando se conoce la base y el exponente.

Ejemplo: 3^3 = 27 (potencia cúbica de 3).

Sin embargo, ¿qué operación nos permite encontrar la base cuando conocemos la potencia y el exponente? Por ejemplo, si se tiene x^3 = 27, nos interesa conocer el valor de x que, al elevarlo al cubo, nos da 27.

Definición 1.83:
Dado un número entero n > 1 y un número real a, llamamos raíz enésima de a al número real b que cumple: b^n = a.

Donde:

n: índice de la raíz.

a: radicando.

Ejemplos:
Raíz cúbica de 8: 2^3 = 8. Respuesta: La raíz cúbica de 8 es 2.

Raíz quinta de -32: (-2)^5 = -32. Respuesta: La raíz quinta de -32 es -2.

Raíz cuadrada de 25:

5^2 = 25.

(-5)^2 = 25. Respuesta: Tanto 5 como -5 son raíces cuadradas de 25.

Notación 1.87:
La raíz enésima de a se denota como √n(a). En particular:

√2(a) = √a (raíz cuadrada de a).

√3(a) (raíz cúbica de a).

√4(a) (raíz cuarta de a).

√5(a) (raíz quinta de a).

Ejemplo 1.88:
Si b^2 = -4, no existe un número real b cuyo cuadrado resulte negativo.

Observación 1.89: Si el radicando a < 0, entonces:

√n(a) está definido solo si n es impar.

No existe raíz real de índice par de un número negativo.

Propiedades de la radicación:
Sean a, b números reales y m, n enteros mayores que 1. Las siguientes propiedades son válidas:

Producto bajo raíz: √n(a * b) = √n(a) * √n(b) Solo si:

n es impar.

n es par y a ≥ 0, b ≥ 0.

Ejemplo: √(4 * 25) = √4 * √25 = 2 * 5 = 10.

Cociente bajo raíz: (√n(a / b)) = (√n(a)) / (√n(b)) Solo si:

n es impar y b ≠ 0.

n es par, a ≥ 0 y b > 0.

Ejemplo: √((121 * x^4) / (64 * y^12)) = (√(121 * x^4)) / (√(64 * y^12)) = (11 * x^2) / (8 * y^6).

Potencia de una raíz: (√n(a))^m = √n(a^m) Solo si:

n es impar.

n es par y a ≥ 0.

Ejemplo: (√3(-2))^6 = √3((-2)^6) = √3(64) = 4.

Raíz de raíz: √n(√m(a)) = √(n * m)(a) Solo si:

a ≥ 0.

a < 0 y n, m son impares.

Ejemplo: √3(√(64)) = √6(64) = 2.
]

- Potencia con exponente racional positivo
[Hasta el momento, definimos la potenciación cuando el exponente es un número entero. Ahora introducimos el concepto de potenciación cuando el exponente es un número racional.

Potenciación con exponente racional de la forma 1/n:
Definición 1.95: Siendo n un número entero mayor que 1, y a un número real tal que √n(a) sea real, definimos: a^(1/n) = √n(a).

Ejemplo 1.96: (-27)^(1/3) = √3(-27) = -3.

Potenciación con exponente racional de la forma m/n:
Si la propiedad: a^(n*m) = (a^n)^m es válida para exponentes racionales, y considerando que: m/n = (1/n) * m, la expresión a^(m/n) puede adoptar las siguientes formas equivalentes: a^(m/n) = (a^(1/n))^m.

Definición 1.97: Sean m, n números enteros positivos con n > 1, y a, √n(a) números reales. Definimos: a^(m/n) = (√n(a))^m.

Esto es válido si:

a ≥ 0, o

a < 0 y n es impar.

En estos casos: (√n(a))^m = √n(a^m).

Ejemplo 1.98: 25^(3/2):

Sacamos la raíz cuadrada de 25: √25 = 5.

Elevamos el resultado al cubo: 5^3 = 125.

Esto coincide con: √(25^3) = √15625 = 125.

Observación 1.99:
Sacar la raíz y luego elevar: (√n(a))^m = (a^(1/n))^m = a^(m/n) es igual a elevar primero y luego sacar la raíz: √n(a^m) = (a^m)^(1/n) cuando √n(a) es real.]

- Potencia con exponente racional negativo
[Consideremos ahora la expresión a^(-m/n) con m y n enteros positivos, tal que ambos no tienen factores comunes enteros distintos que 1. Las propiedades de potenciación nos permiten escribir:

a^(-m/n) = (a^(1/n))^(-m) = 1 / ((a^(1/n))^m).

Definición 1.100:
Sean m, n números enteros positivos con n > 1 y tanto a como √n(a) números reales, con a ≠ 0. Definimos:

a^(-m/n) = 1 / (a^(m/n)) = 1 / (√n(a))^m.

Ejemplo 1.101: 32^(-2/5):

Sacamos la raíz quinta de 32: √5(32) = 2.

Elevamos el resultado al cuadrado: 2^2 = 4.

Tomamos el inverso: 1 / 4. Resultado: 32^(-2/5) = 1/4.

Observación 1.102:
Todas las propiedades de potenciación mencionadas previamente son válidas para potencias con exponente racional.

Ejemplo 1.103: Sea a > 0: a^(-2/3) * √a * a^(-7/6):

Usando las propiedades de producto de potencias: a^(-2/3) * a^(1/2) * a^(-7/6).

Sumando los exponentes: -2/3 + 1/2 - 7/6 = 0.

Resultado: a^0 = 1.

Ejemplo 1.104: Sean x, y, a números reales, con a ≠ 0 y x > 0. Reducimos las siguientes expresiones:

(3a) * (3a^2) * (3a)^(-3):

Sumamos los exponentes de 3: 3^(1 + 1 - 3) = 3^(-1) = 1/3.

Sumamos los exponentes de a: a^(1 + 2 - 3) = a^0 = 1. Resultado: (1/3).

(a * x^2) / (y^(-1/3) * 2 * x^(-1/2) * y^3):

Simplificando las potencias: a * x^(2 - (-1/2)) * y^(1/3 - 3) / 2.

Resulta en: a * x^(5/2) * y^(-10/3) / 2. Resultado: (a * x^(5/2) * y^(-10/3)) / 2.

Ejercicio 1.105:
Resuelve las siguientes expresiones aplicando propiedades de potenciación y radicación:

(√x * x^(-1) * √(x^3) * x^(-2)).

(√3(x^2 * z^5)) * (√3(x^7 * z^3)).

[((2 * 3) / 9)^(−2) * ((9 / 4)^2) * (2/5)^(-1)]^(-1).

((3 * z^2 * y^(-1))^5) / ((4 * y^5 * z^(-3))^(-2)).

(a^2 / (2^3 * x^(-2))) * ((a^2)^(-6)) - (2 / (x * (a^2 * 2^(-1))^2))^(-2).

(x^(-2) + x^(-3)) * (√3(x / √(x^7))).

(x^(-3) * √3(x^4)) / (x^(-2) * √(x)).

√3(x^2 / √(a * x)).

(3 * (2 * 3)^(-1) * 1/2)^3 * (3 * (2^2))^(-2).

3^(√(2^(-3) + (13/4)) - ((2/5)^(-2) + (3/8)^(-1))).

Soluciones:

x^(9/4).

x^3 * z^2.

5/8.

(3^54 * z^4) / (2 * y^5).

0.

x^(-5/2) + x^(-7/2).

x^(-1/6).

a^(1/6) * x^(5/6).

(1/2^8) * 3^2.

-25/12.]

- Notación Científica
[Escribir 2400 en notación científica.
Corramos la coma hasta obtener una cifra significativa (1 ≤ a < 10).
Movemos la coma 3 lugares hacia la izquierda: 2400 = 2.4 × 10^3.
Verificamos que 2.4 × 10^3 = 2400.

Ejemplo 2: Escribir 0.0081 en notación científica.
Corramos la coma hasta obtener una cifra significativa.
Movemos la coma 3 lugares hacia la derecha: 0.0081 = 8.1 × 10^-3.
Verificamos que 8.1 × 10^-3 = 0.0081.

Regla práctica:
Para números grandes, mueve la coma hacia la izquierda; aumenta n en 10^n.
Para números pequeños, mueve la coma hacia la derecha; disminuye n en 10^-n.

Ejemplo 1.107: Convertir números a notación científica.
743.788 = 7.43788 × 10^2.
0.007680 = 7.680 × 10^-3.

Ejercicio 1.108:
Pregunta: Al multiplicar 1.789 por 10^5, ¿hacia dónde se desplaza la coma?
Solución: Hacia la derecha, 5 lugares.

Ejercicio 1.109:
Pregunta: ¿Cuáles números están en notación científica?
0.641 × 10^3
2 × 10^1
9.999 × 10^4
4.38 × 5 × 10

Solución: Los correctos son:
2 × 10^1.
9.999 × 10^4.

Ejercicio 1.110:
Pregunta: ¿Quién escribió correctamente el peso del auto de 1600 kg en notación científica?
María: 16.0 × 10^2.
Juan: 0.16 × 10^4.
Ana: 1.6 × 10^3.

Solución: Ana escribió correctamente: 1.6 × 10^3.

Ejercicio 1.111:
Pregunta: Escribe 1.7 × 10^-24 en notación decimal.
Solución: 1.7 × 10^-24 = 0.0000000000000000000000017

Ejercicio 1.112:
Pasar los siguientes números a notación científica:
53200000
0.000000789
7420 × 10^2
4300000
0.00008
0.25

Solución:
53200000 = 5.32 × 10^7.
0.000000789 = 7.89 × 10^-7.
7420 × 10^2 = 7.42 × 10^5.
4300000 = 4.3 × 10^6.
0.00008 = 8 × 10^-5.
0.25 = 2.5 × 10^-1.

Ejercicio 1.113:
Transformar números de notación científica a decimal:
4.2 × 10^5
1.16 × 10^-3
5.018 × 10^-6
5.3 × 10^4
2.15 × 10^-3

Solución:
4.2 × 10^5 = 420000.
1.16 × 10^-3 = 0.00116.
5.018 × 10^-6 = 0.000005018.
5.3 × 10^4 = 53000.
2.15 × 10^-3 = 0.00215.]

---

### BLOQUE 2 - ECUACIONES E INECUACIONES

#### Ecuaciones
[Una expresión algebraica es una expresión matemática en las cuales se combinan números, letras y operaciones.

Definición 2.1: Una ecuación es una igualdad entre dos expresiones algebraicas en las que aparece un valor desconocido llamado incógnita. Habitualmente la incógnita será representada por la letra x, aunque puede denotarse con cualquier letra del alfabeto. Resolver una ecuación significa encontrar el valor de la incógnita, es decir, determinar un valor real que hace verdadera la igualdad. A este valor se lo denomina Solución o Raíz. Las ecuaciones pueden no tener solución, o bien tener una, varias o infinitas soluciones. El conjunto de todas las soluciones de la ecuación se denomina Conjunto Solución. Para encontrar el conjunto solución necesitamos determinar ecuaciones equivalentes a la ecuación dada.

Definición 2.2: Dos ecuaciones son equivalentes cuando tienen el mismo conjunto solución.

Métodos para obtener ecuaciones equivalentes:
- Sumar (o restar) una constante o expresión en x, a ambos miembros de la ecuación.
- Multiplicar (o dividir) ambos miembros de la ecuación por un número distinto de cero.

La finalidad de obtener ecuaciones equivalentes es para que la ecuación que nos quede finalmente sea más fácil de resolver que la dada.

Ejemplo 2.3: Resolver la ecuación: 
-5x = 3x + 24.

Restamos 3x en ambos lados de la igualdad: 
-5x - 3x = 3x + 24 - 3x 
-8x = 24.

Dividimos por -8 ambos miembros: 
x = 24/-8 = -3.

Verificación: Sustituimos el valor obtenido x = -3 en la ecuación dada: 
-5(-3) = 3(-3) + 24. 
15 = -9 + 24. 
15 = 15.

Conclusión: -3 es la solución de la ecuación.

Conjunto Solución: 
S = {-3}.

Las ecuaciones que trabajaremos en este protolibro son:
- Ecuaciones de Primer Grado en una Variable: La incógnita está elevada a la potencia 1.
- Ecuaciones de Segundo Grado en una Variable: La incógnita está elevada a la potencia 2.]

- Ecuaciones de Primer Grado
[Definición 2.4. Una ecuación de la forma ax + b = 0, donde a, b ∈ R y a ≠ 0,
recibe el nombre de Ecuación de Primer Grado en una variable o incógnita.

Observación 2.5. La ecuación lineal ax + b = 0 con a, b números reales y a ≠ 0
tiene solución única y el conjunto solución es:
S = { -b / a }

Ejemplo 2.6. Vamos a resolver la siguiente ecuación:
6x + 2 − 3x = 7x + 4

Resolución: Para encontrar el conjunto solución, obtenemos ecuaciones equivalentes
de esta manera:
1. Restamos (−7x) en ambos miembros:
6x + 2 − 3x − 7x = 7x + 4 − 7x 
2. Restamos (−2) en ambos miembros:
6x + 2 − 3x − 7x − 2 = 4 − 2
3. Asociamos los valores con x de un lado de la igualdad y del otro lado los valores
constantes:
−4x = 2
4. Dividimos todo por (−4):
x = 2 / −4 = −1/2

Verificación: Sustituimos el valor obtenido x = -1/2 en la ecuación dada:

6 * (-1/2) + 2 - 3 * (-1/2) = 7 * (-1/2) + 4

Simplificando cada lado:

6 * (-1/2) = -3
3 * (-1/2) = -3/2
7 * (-1/2) = -7/2

Sustituimos estos valores en la ecuación:

-3 + 2 + 3/2 = -7/2 + 4

Agrupamos términos semejantes:

(-3 + 2) + 3/2 = (-7/2 + 4)

-1 + 3/2 = -7/2 + 4

Convertimos a un denominador común y sumamos:

-2/2 + 3/2 = -7/2 + 8/2

1/2 = 1/2

Resultado: Esto confirma que x = -1/2 es solución de la ecuación.
Respuesta: El conjunto solución es:
S = { -1/2 }
Ejemplo 2.7. Vamos a resolver la siguiente ecuación:
1.5 + 4(x - 0.5) = 3x - 0.5

Resolución: Para encontrar el conjunto solución, obtenemos ecuaciones equivalentes de esta manera:
1. Pasamos a fracción todos los números decimales:
   3/2 + 4(x - 1/2) = 3x - 1/2

2. Aplicamos la propiedad distributiva:
   3/2 + 4x - 4/2 = 3x - 1/2

3. Restamos 3x en ambos miembros:
   3/2 + 4x - 4/2 - 3x = 3x - 1/2 - 3x

4. Restamos 3/2 y sumamos 4/2 (equivalente a 2) en ambos miembros:
   3/2 + 4x - 2 - 3x - 3/2 + 2 = -1/2 - 3/2 + 2

5. Asociamos los valores con x de un lado de la igualdad y del otro lado los valores constantes:
   x = 0

Verificación: Es conveniente verificar que el resultado obtenido satisface la ecuación. Para ello, reemplazamos en la ecuación dada este valor y si se obtiene una identidad, la solución es correcta:

   1.5 + 4(0 - 0.5) = 3 * 0 - 0.5

Simplificando:
   -1/2 = -1/2

Por lo tanto, 0 es solución de la ecuación.

Respuesta: El conjunto solución es:
   S = {0}

Ejemplo 2.8. Vamos a resolver ahora la siguiente ecuación:
   2 - (3x - 5) = 4 - 2x + 3 - x

Resolución: Para encontrar el conjunto solución, obtenemos ecuaciones equivalentes de esta manera:

1. Aplicamos propiedad distributiva:
   2 - 3x + 5 = 4 - 2x + 3 - x

2. Sumamos 2x y x en ambos miembros:
   2 - 3x + 5 + 2x + x = 4 - 2x + 3 - x + 2x + x

3. Restamos 2 y 5 en ambos miembros:
   2 - 3x + 5 + 2x + x - 2 - 5 = 4 + 3 - 2 - 5

4. Asociamos los valores con x de un lado de la igualdad y del otro lado los valores constantes:
   0x = 0 

Luego obtenemos con este resultado que la ecuación tiene infinitas soluciones, es decir, admite como solución cualquier número real. 
   (S = R)

Ejemplo 2.9. Vamos a resolver la siguiente ecuación:
   3(x + 4) − 6x = 8 − 3(x + 5)

Resolución: Para encontrar el conjunto solución, obtenemos ecuaciones equivalentes de esta manera:
1. Aplicamos propiedad distributiva:
   3x + 12 − 6x = 8 − 3x − 15

2. Sumamos 3x en ambos miembros:
   3x + 12 − 6x + 3x = 8 − 3x − 15 + 3x

3. Restamos (−12) en ambos miembros:
   3x + 12 − 6x + 3x − 12 = 8 − 15 − 12

4. Asociamos los valores con x de un lado de la igualdad y del otro lado los valores constantes:
   0x = −19

Vemos entonces que la ecuación no tiene solución real alguna, pues 0 es distinto de −19, con lo cual la expresión 0 = −19 representa un absurdo. Así, 
   S = ∅.

Ejercicio 2.10. Resolver las siguientes ecuaciones de primer grado:

1. (17/5)x = -(8/5)x + 150
2. 7(x - 2) + 9 = 10x - 4(-3 - x)
3. (1/2)(x - 5) = (3/2) + (9/6)(x - 2)
4. (2/3)(x - (1 - (x - 2)/3)) + 1 = x
5. 2(x + 1) - 3(x - 2) = -x + 6
6. 2x + 2 - 3(x - 2) = -x + 6
7. 2 - (3x - 5) = 4 - 2x + 3 - x
8. (6/8)(x + 1) - (2x - 3)/16 = (3/4)x - (1/4) - (3/8)(3x - 2)

Solución:
1. S = {30}
2. S = { -17/7 }
3. S = {-1}
4. S = {-1}
5. S = ∅
6. S = ∅
7. S = R
8. S = { 15/9 }

Ejercicio 2.11. Se sabe que la ecuación:
(2a - 1)(x + 1) + x = a

Tiene por solución x = -2. ¿Cuál es el valor de a?
Solución: a = -1/3]

- Ecuaciones de Segundo Grado
[Definición 2.12. Una ecuación que puede escribirse en la forma:
ax^2 + bx + c = 0 donde a, b y c ∈ R y a ≠ 0, 
recibe el nombre de Ecuación de Segundo Grado en la variable x.

Ejemplo 2.13.
6x^2 + 7x − 3 = 0 donde a = 6, b = 7 y c = −3.

Ejemplo 2.14.
x^2 − 7 = 0 donde a = 1 y c = −7.

Ejemplo 2.15.
−4x + 3x^2 = 0 donde a = 3 y b = −4.

Para determinar la solución de la ecuación de segundo grado, existe una fórmula resolvente, denominada fórmula resolvente de Bhaskara, definida por:
x1, x2 = (−b ± √(b^2 − 4·a·c)) / 2a

En donde x1 y x2 son las soluciones de la ecuación. El valor ∆ = b^2 − 4·a·c se llama Discriminante de la ecuación cuadrática, y nos indica la cantidad de soluciones que tiene esta ecuación en el conjunto de los números reales. Según el discriminante:
i. Si ∆ > 0, la ecuación tiene dos soluciones reales distintas.
ii. Si ∆ = 0, la ecuación tiene una única solución real.
iii. Si ∆ < 0, la ecuación no tiene solución real.

Observación 2.16. Sean x1, x2 dos soluciones de la ecuación cuadrática ax^2 + bx + c = 0, podemos expresarla en forma factorizada como:
ax^2 + bx + c = a(x − x1)(x − x2)

Ejemplo 2.17. Vamos a resolver la siguiente ecuación cuadrática:
3x^2 + 3x − 6 = 0

Resolución: 
Primero determinamos el valor del discriminante:
∆ = 3^2 − 4·3·(−6) = 81
Como es un valor positivo, la ecuación cuadrática tiene dos soluciones reales.

Aplicamos la fórmula resolvente:
x1 = (−3 + √81) / (2·3) = (−3 + 9) / 6 = 1
x2 = (−3 − √81) / (2·3) = (−3 − 9) / 6 = −2

Luego, x1 = 1 y x2 = −2 son las soluciones de la ecuación dada. Expresada en forma factorizada queda:
3x^2 + 3x − 6 = 3(x − 1)(x + 2)

Ejemplo 2.18. Vamos a resolver la siguiente ecuación cuadrática:
x^2 + x + 1 = 0

Resolución:
Primero determinamos el valor del discriminante:
∆ = 1^2 − 4·1·1 = −3
Como es un valor negativo, la ecuación cuadrática no tiene solución real.

Ejercicio 2.19. Resolver las siguientes ecuaciones de segundo grado. En el caso de que tenga raíces reales, expresar la ecuación en forma factorizada.

1. 2x^2 + 4x − 6 = 0
2. x^2 + 2x + 1 = 0
3. −2x^2 + x = 0
4. x^2 − 2x + 2 = 0
5. 4x + x^2 − 2x = 0
6. 2 + x^2 − 2x = 0
7. x^2 − 6x = −9

Solución:
1. S = {−3; 1} → 2x^2 + 4x − 6 = 2(x − 1)(x + 3)
2. S = {−1} → x^2 + 2x + 1 = (x + 1)^2
3. S = {0; 1/2} → −2x^2 + x = −2x(x − 1/2)
4. S = ∅
5. S = {−2; 0} → x^2 + 2x = x(x + 2)
6. S = ∅
7. S = {3} → x^2 − 6x + 9 = (x − 3)^2

Método de Completar Cuadrados:
Para entender este concepto, recordemos dos igualdades denominadas cuadrados de un binomio:
(a + b)^2 = a^2 + 2ab + b^2
(a − b)^2 = a^2 − 2ab + b^2

El proceso de completar cuadrados aplicado sobre la ecuación general de segundo grado ax^2 + bx + c = 0, se realiza aplicando los siguientes pasos:

1. Se suma el opuesto del término independiente (c) miembro a miembro.
2. Se dividen todos los términos por el valor de a (coeficiente que acompaña a x^2).
3. Se suma en ambos lados de la igualdad, el cuadrado de la mitad del coeficiente que acompaña al término lineal.
4. Finalmente, en uno de los lados de la igualdad queda el desarrollo del binomio al cuadrado.

Partimos de la ecuación general:
ax^2 + bx + c = 0

1. Sumamos el opuesto del término independiente (c):
ax^2 + bx + c - c = 0 - c
ax^2 + bx = -c

2. Dividimos todos los términos por a:
(ax^2)/a + (bx)/a = -c/a
x^2 + (b/a)x = -c/a

3. Sumamos el cuadrado de la mitad del coeficiente del término lineal en ambos lados:
x^2 + (b/a)x + (b/2a)^2 = -c/a + (b/2a)^2

4. Reescribimos la ecuación como un binomio al cuadrado:
(x + b/2a)^2 = (b^2 - 4ac) / 4a^2

5. Al despejar x obtenemos:
x1,2 = -(b/2a) ± √((b^2 - 4ac) / 4a^2)
x1,2 = -(b/2a) ± √(b^2 - 4ac) / 2a
x1,2 = (-b ± √(b^2 - 4ac)) / 2a

Esta fórmula se corresponde exactamente con la fórmula resolvente de Bhaskara, demostrando su origen a partir del método de completar cuadrados.

Ejemplo 2.20. Hallar el conjunto solución de la ecuación:
2x^2 + 6x − 5 = 0 usando el método de completar cuadrados.

1. Sumamos 5 a ambos miembros:
2x^2 + 6x = 5

2. Dividimos todos los términos por 2:
x^2 + 3x = 5/2

3. Sumamos el cuadrado de la mitad de 3 a ambos lados:
x^2 + 3x + (3/2)^2 = 5/2 + (3/2)^2
x^2 + 3x + 9/4 = 5/2 + 9/4

4. Simplificamos y reescribimos como un binomio al cuadrado:
(x + 3/2)^2 = 19/4

5. Resolviendo para x obtenemos:
x1,2 = -(3/2) ± √(19/4)
x1 = √19 / 2 - 3 / 2
x2 = -√19 / 2 - 3 / 2

Por lo tanto, las soluciones son:
x1 = (√19 / 2) - (3 / 2)
x2 = -(√19 / 2) - (3 / 2)

Ejemplo 2.21. Resolvamos ahora, completando cuadrados, la siguiente ecuación:
x^2 − 7x − 18 = 0

1. Sumamos miembro a miembro el opuesto del término independiente, en nuestro caso 18:
   x^2 − 7x − 18 + 18 = 18
   x^2 − 7x = 18

2. Sumamos en ambos miembros el cuadrado de un medio del coeficiente que acompaña al término lineal:
   x^2 − 7x + (7/2)^2 = 18 + (7/2)^2

3. En el lado izquierdo de la igualdad queda el desarrollo del binomio al cuadrado de (x − 7/2), y del otro lado un valor constante:
   (x − 7/2)^2 = 121/4

4. Las soluciones de la ecuación de segundo grado son:
   x1,2 = ±√(121/4) + 7/2

Es decir:
   x1 = 11/2 + 7/2
   x2 = −11/2 + 7/2

Ejercicio 2.22. Resolver las siguientes ecuaciones de segundo grado por el método de completar cuadrados:
1. x^2 + 2x + 1 = 0
2. x^2 + x − 6 = 0
3. x^2 − 4x + 3 = 0
4. x^2 − 8x = −4
5. 2x^2 − 6x − 16 = 0

Solución:
1. S = {−1}
2. S = {−3; 2}
3. S = {1; 3}
4. S = {√12 + 4; −√12 + 4}
5. S = {(√41 / 4) + 3 / 2; −(√41 / 4) + 3 / 2}

Ejercicio 2.23. Para qué valores de k, la ecuación:
kx^2 − kx + 1 = 0
admite una única solución.

Solución: k = 4]

- Ecuaciones como Modelo Matemático
[Muchas veces se requiere del planteo de una ecuación para resolver distintas situaciones problemáticas; es decir, se requiere de ecuaciones como Modelo Matemático. En las diferentes situaciones problemáticas deben identificarse claramente:
a. los datos;
b. las incógnitas;
c. las condiciones que las incógnitas deben cumplir.

Los pasos a seguir para la resolución de situaciones problemáticas son los siguientes:
1. Lea cuidadosamente el problema hasta comprender su enunciado.
2. Identifique los datos e incógnita del problema; y utilice una variable para representar a la incógnita, por ejemplo x.
3. Traduzca al lenguaje simbólico el enunciado del problema, planteando una o varias ecuaciones.
4. Resuelva la o las ecuaciones planteadas.
5. Verifique la solución encontrada.
6. Concluya respondiendo a la o las preguntas del problema.

Ejemplo 2.24.
Se pintan de rojo los tres séptimos de un poste y luego, los cinco sextos del resto. Si aún quedan dos metros sin pintar, ¿Cuál es la altura del poste?
Solución:
Se considera como incógnita, x, la altura del poste, pues es el valor que se desconoce y que pide el problema; luego la ecuación que plantea la situación problemática es:
   (3/7)x + (5/6)(x - (3/7)x) + 2 = x
Resolvemos la ecuación:
   (3/7)x + (5/6)(4/7)x - x = -2
   (-2/21)x = -2
   x = 21
Respuesta:
   La altura del poste es de 21 metros.

Ejemplo 2.25.
Una persona gasta la sexta parte de su sueldo y luego las tres cuartas partes del resto. Si aún le quedan $187500, ¿Cuál es su sueldo?
Solución:
Consideramos como incógnita, x, el sueldo de la persona, pues es lo que nos pregunta el problema, y por lo tanto es el valor desconocido; luego la ecuación que planteamos frente a la situación problemática dada es:
   (1/6)x + (3/4)(x - (1/6)x) + 187500 = x
Resolvemos la ecuación:
   (1/6)x + (5/8)x - x = -187500
   (-10/48)x = -187500
   x = 900000
Respuesta:
   El sueldo de la persona es de $900000.

Ejercicio 2.26. Escribir en forma simbólica los siguientes enunciados:
1. Un número x y su consecutivo suman 23.
2. z es el número natural que sumado a 12 da 26.
3. Juan tiene 16 años. La suma de su edad y la mía es igual a 50.
4. El largo de un campo de fútbol es el doble del ancho más 10 metros.

Ejercicio 2.27. Resolver los siguientes problemas:
1. El perímetro de un jardín rectangular es de 58m. Si el lado mayor mide 11m más que el lado menor, ¿Cuánto miden los lados del jardín?
   Solución:
   Los lados del jardín miden 9m y 20m.
2. Roberto obtuvo las calificaciones siguientes en distintos exámenes de biología: 73, 62, 58 y 64. ¿Qué calificación debe obtener en un próximo examen para que su promedio sea de 70?
   Solución:
   Su calificación debe ser de 93 puntos.
3. Durante una prueba realizada en una fábrica que produce latas, se obtuvo que la máquina A produce x latas, la máquina B el doble de A y la máquina C, 6 latas más que A. La producción total fue de 3810 latas. ¿Cuántas latas produjo cada máquina?
   Solución:
   La máquina A produjo 951 latas, la máquina B produjo 1902 latas y la máquina C produjo 957 latas.

Ejemplo 2.28.
Hallar x considerando el triángulo rectángulo de la figura.
Solución:
La ecuación que representa la situación problemática la obtenemos al aplicar Pitágoras al triángulo rectángulo:
   (2x + 4)^2 = (2x + 2)^2 + (2x)^2
   4x^2 + 16x + 16 = 4x^2 + 8x + 4 + 4x^2
   4x^2 − 8x − 12 = 0
Resolviendo esta ecuación obtenemos como resultados:
   x1 = 3 y x2 = −1
El valor de x = 3 es la solución buscada, pues de ser x = −1, 2x y (2x + 2) no representarían las longitudes de un triángulo.
Respuesta:
   El valor de x es 3.

Ejercicio 2.29. Resolver el siguiente problema:
Calcular un número natural tal que, la suma del mismo y la tercera parte del cuadrado de su consecutivo sea 35.
Solución:
   El número natural es 8.]

#### Inecuaciones
[Definición 2.30. Una inecuación o desigualdad es una relación entre dos expresiones algebraicas que no siempre son iguales y por lo tanto se relacionan con los símbolos >, ≥, < y ≤.

Ejemplo 2.31.
Resolver la desigualdad: 3x − 7 < 6(x − 2)
Resolver una desigualdad es encontrar el conjunto de todos los números reales que hacen que la desigualdad sea verdadera; este conjunto solución, por lo general, es un intervalo completo de números reales o, en otros casos, la unión de tales intervalos.

- Intervalos:
Para indicar subconjuntos de números reales se emplea la siguiente notación. Dados a, b ∈ R, a < b, se define:
1. (a, b) = {x ∈ R : a < x < b} Intervalo abierto.
2. [a, b) = {x ∈ R : a ≤ x < b} Intervalo semiabierto.
3. (a, b] = {x ∈ R : a < x ≤ b} Intervalo semiabierto.
4. [a, b] = {x ∈ R : a ≤ x ≤ b} Intervalo cerrado.
5. (a, +∞) = {x ∈ R : x > a}
6. [a, +∞) = {x ∈ R : x ≥ a}
7. (−∞, b) = {x ∈ R : x < b}
8. (−∞, b] = {x ∈ R : x ≤ b}

Ejemplo 2.32.
Escribamos cada desigualdad usando la notación de intervalos y grafiquemos los mismos en la recta real, donde x ∈ R:
1. −1 ≤ x ≤ 8
   Notación de intervalo: [-1, 8]
2. x ≥ 9
   Notación de intervalo:  [9, ∞

- Resolución de Desigualdades
[El procedimiento para resolver una inecuación o desigualdad lineal consiste en transformar la desigualdad de a un paso a la vez, hasta que el conjunto solución sea obvio. Podemos realizar ciertas operaciones, que se corresponden con las propiedades del orden en los reales, en ambos lados de la desigualdad sin cambiar su conjunto solución. En particular:
1. Podemos sumar el mismo número a ambos lados de una desigualdad.
2. Podemos multiplicar ambos lados de una desigualdad por el mismo número positivo.
3. Podemos multiplicar ambos lados de una desigualdad por el mismo número negativo, pero entonces debemos invertir el sentido del signo de la desigualdad.

Ejemplo 2.33.
Resolver la siguiente inecuación:
3x < 5x − 10

Solución:
1. Restamos 5x en ambos miembros:
   3x − 5x < 5x − 10 − 5x
   −2x < −10

2. Multiplicamos por −1/2 en ambos miembros (y cambiamos el sentido de la desigualdad):
   x > −10/−2 = 5

Respuesta:
La solución buscada es (5; ∞).

Este tipo de desigualdad presentada es una inecuación lineal o desigualdad de primer grado, pues el mayor exponente de la incógnita en la desigualdad es de grado uno.

Ejercicio 2.34. Resolver las siguientes inecuaciones de primer grado:
1. 2x − 3 > x + 5
2. x + 6 < x + 2
3. 2(x + 1) − 3(x − 2) < x + 6
4. 2x − 3 − x < 3x − 4(x − 1)

Solución:
1. S = (8; ∞)
2. S = ∅
3. S = (1; ∞)
4. S = (−∞; 7/3)

La desigualdad de segundo grado o inecuación cuadrática con una incógnita es cualquier desigualdad que, directamente o mediante transformaciones de equivalencia, aplicando las propiedades de orden en R, se puede expresar de la forma siguiente:
* ax^2 + bx + c > 0
* ax^2 + bx + c < 0
* ax^2 + bx + c ≥ 0
* ax^2 + bx + c ≤ 0

con a, b, c ∈ R y a ≠ 0.

Resolver estas inecuaciones consiste en encontrar el o los intervalos de la recta real donde se verifica la desigualdad. Para su estudio, lo que se va a realizar es llevar la desigualdad que está expresada en forma polinómica a su forma factorizada, y de ahí bastará con estudiar el signo de los tres factores de acuerdo al signo de la desigualdad y resolver las inecuaciones lineales que quedan.

1. ax^2 + bx + c = a(x − x1)(x − x2) ≥ 0, luego debemos analizar:
   a) Si a ≤ 0 nos queda (x − x1)(x − x2) ≤ 0, y de acá analizamos:
      i. (x − x1) ≥ 0 y (x − x2) ≤ 0, ó
      ii. (x − x1) ≤ 0 y (x − x2) ≥ 0.
   Luego, la solución de la desigualdad a) es la unión de las soluciones de i. y ii.

   b) Si a ≥ 0 nos queda (x − x1)(x − x2) ≥ 0, y de acá analizamos:
      i. (x − x1) ≥ 0 y (x − x2) ≥ 0, ó
      ii. (x − x1) ≤ 0 y (x − x2) ≤ 0.
   Luego, la solución de la desigualdad b) es la unión de las soluciones de i. y ii.

2. ax^2 + bx + c = a(x − x1)(x − x2) ≤ 0, luego debemos analizar:
   a) Si a ≤ 0 nos queda (x − x1)(x − x2) ≥ 0, y de acá analizamos:
      i. (x − x1) ≥ 0 y (x − x2) ≥ 0, ó
      ii. (x − x1) ≤ 0 y (x − x2) ≤ 0.
   Luego, la solución de la desigualdad a) es la unión de las soluciones de i. y ii.

   b) Si a ≥ 0 nos queda (x − x1)(x − x2) ≤ 0, y de acá analizamos:
      i. (x − x1) ≥ 0 y (x − x2) ≤ 0, ó
      ii. (x − x1) ≤ 0 y (x − x2) ≥ 0.
   Luego, la solución de la desigualdad b) es la unión de las soluciones de i. y ii.

De igual manera, resolvemos para las desigualdades con > y <.

Ejemplo 2.35. Debemos hallar el conjunto solución de la desigualdad:
√2(x − 1)(x + 1) > 0

Como a = √2 > 0, la desigualdad que nos queda por resolver es:
(x − 1)(x + 1) > 0

Debemos analizar entonces:
i. (x − 1) > 0 y (x + 1) > 0 ó
ii. (x − 1) < 0 y (x + 1) < 0

Resolución:
i. (x − 1) > 0 → x > 1 y (x + 1) > 0 → x > −1; luego la solución es la intersección de las soluciones de ambas inecuaciones:
Si. = (1; +∞)

ii. (x − 1) < 0 → x < 1 y (x + 1) < 0 → x < −1; luego la solución es la intersección de las soluciones de ambas inecuaciones:
Sii. = (−∞; −1)

Finalmente la solución de la desigualdad dada es:
Si. ∪ Sii. = (1; +∞) ∪ (−∞; −1) = (−∞; −1) ∪ (1; +∞)

Ejemplo 2.36. Hallemos el conjunto solución de la desigualdad:
x^2 + 4x + 4 ≥ 0

Analizamos aquí para que valores de x, (x + 2)^2 debe de ser mayor o igual que cero;
y esto ocurre para cualquier valor real, entonces la solución de la desigualdad es R.

Ejemplo 2.37. Hallemos ahora, el conjunto solución de la desigualdad:
x^2 − 6x + 9 < 0
Como la desigualdad está expresada en forma polinómica la expresamos en su forma
factorizada:
x^2 − 6x + 9 = (x − 3)^2 < 0
Analizamos aquí para que valores de x, (x − 3)^2 debe de ser menor que cero; y esto
no ocurre para ningún valor real, pues ningún número real elevado al cuadrado puede
dar como resultado un valor negativo. Por lo tanto la desigualdad no tiene solución
real, o bien decimos que tiene solución vacío (S = ∅).

Otro tipo de inecuaciones que vamos a resolver son las desigualdades o inecuaciones racionales, las cuales se resuelven por el método de los signos, como hemos
aplicado en las inecuaciones de segundo grado. Veamos un par de ejemplos de esta
situación:

Ejemplo 2.38. Debemos hallar el conjunto solución de la desigualdad:
(x − 2) / (x + 2) ≥ 0
Por la regla de los signos debemos analizar dos casos, recordando que el denominador
no puede tomar el valor cero:
i. (x − 2) ≥ 0 y (x + 2) > 0 o
ii. (x − 2) ≤ 0 y (x + 2) < 0

Resolución:
i. (x − 2) ≥ 0 → x ≥ 2 y (x + 2) > 0 → x > −2; luego la solución es la
intersección de las soluciones de ambas inecuaciones:
Si. = [2; +∞)

ii. (x − 2) ≤ 0 → x < 2 y (x + 2) < 0 → x < −2; luego la solución es la
intersección de las soluciones de ambas inecuaciones:
Sii. = (−∞; −2)

Ejemplo 2.39. Debemos hallar el conjunto solución de la desigualdad:
(x + 1) / (x + 3) < 2
Primero debemos sumar el opuesto de 2 en ambos lados de la desigualdad para poder obtener una inecuación como la del ejemplo anterior y así aplicar la regla de los
signos para su resolución:
(x + 1) / (x + 3) < 2 →
(x + 1) / (x + 3) − 2 < 0 →
(−x − 5) / (x + 3) < 0
Nos queda entonces por analizar:
i. (−x − 5) < 0 y (x + 3) > 0 o
ii. (−x − 5) > 0 y (x + 3) < 0

Resolución:
i. (−x − 5) < 0 → x > −5 y (x + 3) > 0 → x > −3; luego la solución es la
intersección de las soluciones de ambas inecuaciones:
Si. = (−3; +∞)

ii. (−x − 5) > 0 → x < −5 y (x + 3) < 0 → x < −3; luego la solución es la
intersección de las soluciones de ambas inecuaciones:
Sii. = (−∞; −5)

Finalmente la solución de la desigualdad dada es la unión de las soluciones obtenidas en i. y ii.:
Si. ∪ Sii. = (−∞; −5) ∪ (−3; +∞)

Ejercicio 2.40. Indicar si la siguiente resolución es verdadera o falsa, justificando la
respuesta.
3 / x < 2
3 / x x < 2x
3 < 2x
1 / 2
3 < 1 / 2
2x / 3
2 / < x

Ejercicio 2.41. Resolver las siguientes inecuaciones:
1. x^2 − 6x + 8 > 0
2. −x^2 + 4x − 4 < 0
3. 7x^2 + 21x − 28 < 0
4. x^2 + x + 1 < 0
5. −2 (x − 1) / (x + 4) ≤ 0
6. (x − 2) / (x + 1) > 0
7. (x + 4) / (x − 2) ≥ 3

Solución:
1. S = (−∞; 2) ∪ (4; ∞)
2. S = R − {2}
3. S = (−4; 1)
4. S = ∅
5. S = (−∞; −4) ∪ [1; ∞)
6. S = (−∞; −1) ∪ (2; ∞)
7. S = (2; 5]]

- Inecuaciones en la vida real
[Te encuentras con desigualdades matemáticas casi todos los días, pero tal vez no
las notas porque te son familiares. Piensa en las siguientes situaciones: límites de
velocidad en la autopista, pagos mínimos en las tarjetas de crédito, la cantidad de
gigabyte a consumir en tu celular por mes, el tiempo que te toma llegar a la facultad.
Todas estas situaciones pueden ser representadas como desigualdades matemáticas.
Y, de hecho, usas pensamiento matemático cuando las consideras cada día. Veamos
un ejemplo para entender tal situación.

Ejemplo 2.42. Un utilitario Kangoo pesa 875kg. La diferencia entre el peso
del utilitario vacío y el peso de la carga que lleva no debe ser inferior que 415kg. 
Si hay que cargar 4 cajones iguales, ¿Cuánto puede pesar, como máximo cada uno de los cajones 
para poder llevarlas en el utilitario?

Solución: En primer lugar traducimos el enunciado al lenguaje simbólico, llamamos
x al peso de cada cajón y planteamos la siguiente inecuación:
Peso del utilitario = 875
− Peso de 4 cajones = 4x
No es menor que 415kg:
875 − 4x ≥ 415

Resolvemos:
875 − 4x ≥ 415
−4x ≥ 415 − 875
x ≤ (−460) / (−4)
x ≤ 115

Esto significa que el peso de cada cajón no podrá superar los 115kg. Y además, como
el peso debe ser positivo, necesariamente el peso de los cajones cae en el intervalo
(0; 115].

Ejercicio 2.43. Resolver los siguientes problemas:

1. Una fábrica paga a sus viajantes $10 por artículo vendido más una
cantidad fija de $500. Otra fábrica de la competencia paga $15 por
artículo y $300 fijos. ¿Cuántos artículos debe vender el viajante de la
competencia para ganar más dinero que el primero?

Solución: El viajante debe vender más de 40 artículos.

2. Si el lado de un cuadrado es mayor o igual que 7m, ¿Qué se puede
decir de su perímetro?

Solución: El perímetro es mayor o igual que 28m.

3. Un coche se desplaza por una ruta a una velocidad comprendida
entre 100km/h y 150km/h. ¿Entre qué valores oscila la distancia del
coche al punto de partida al cabo de 3h?

Solución: La distancia oscila entre 300km y 450km. (300km ≤ distancia ≤ 450km.)]


#### Valor absoluto
[El concepto de valor absoluto de un número se puede entender como la distancia
que existe entre el 0 y el número. Si tomamos un punto cualquiera a y este es positivo,
la distancia de a al origen es igual a a; y si fuera negativo, la distancia de a al origen
es igual a (−a). Esto se debe a que una distancia no puede ser negativa, ya que no
tendría sentido. Todas las distancias son positivas y por lo mismo, el valor absoluto
de un número, que es una distancia, debe de ser positivo. De manera formal definimos
el valor absoluto de un número a por:

|a| = 
  a si a ≥ 0
  −a si a < 0

Ejemplo 2.44:
|6| = 6
|−5| = −(−5)
|0| = 0

De manera análoga, se deduce la distancia que existe entre dos números reales
como el valor absoluto de su diferencia; y se lo indica |x − a| (distancia entre x y a).

Ejemplo 2.45:
|x − 4| = 8 nos representa que la distancia de x a 4 es de 8 unidades.
Si nos interesa determinar cuál es ese valor de x debemos considerar la definición
de valor absoluto dada al comienzo y resolver las ecuaciones que nos quedan:

|x − 4| = 
  x − 4 si x − 4 ≥ 0
  −(x − 4) si x − 4 < 0

Entonces:

x − 4 = 8 → x = 8 + 4 = 12
−x + 4 = 8 → −x = 8 − 4 → x = −4

Luego x = 12 y x = −4 son los valores cuya distancia al 4 es de 8 unidades.

Observación 2.46: 
Como x^2 es un número positivo, independientemente del signo de x y √ representa
la raíz cuadrada positiva, tenemos la siguiente expresión algebraica para definir
el valor absoluto:

|x| = √(x^2)

- Propiedades de valor absoluto
Dados a, b números reales se verifican las siguientes propiedades:
1. |a.b| = |a| |b|
2. |a / b| = |a| / |b| con b ≠ 0.
3. |a + b| ≤ |a| + |b|
4. |a − b| ≥ | |a| − |b| |

Ejercicio 2.47. Resolver las siguientes ecuaciones con módulo:
1. |x − 2| = 5
2. |−2x + 4| = 2
3. (1/2)x + (3/2) = 1
4. |x + 3| = 4

Soluciones:
1. S = {−3, 7}
2. S = {1, 3}
3. S = {−5, −1}
4. S = {1, −7}]

- Desigualdades que incluyen valor absoluto
[Como |x| es la distancia entre el número x y el origen, la solución de la desigualdad
|x| < b (con b número real positivo); es el conjunto de los números reales x que están
a una distancia menor que b respecto al origen; en otras palabras x debe de ser menor
que b y mayor que (−b); esto es −b < x < b. Se tiene así la siguiente proposición
cuando b > 0:

i. |x| < b si y solo si −b < x < b.

Ejemplo 2.48:
|x| < 3 si y solo si −3 < x < 3, es decir la solución de esta desigualdad son los x que están entre −3 y 3.

Por otra parte, la solución de la desigualdad |x| > b; (con b número real positivo) es
el conjunto de los números reales x que están a una distancia mayor que b respecto
del origen; y esto puede suceder cuando x > b o x < −b. Se tiene así la siguiente
proposición:

ii. |x| > b si y solo si x > b o x < −b.

Ejemplo 2.49:
|x| > 2 si y solo si x > 2 o x < −2; es decir, la distancia de x al origen debe de ser mayor que 2.

Análogamente se verifica para |x| ≤ b y |x| ≥ b.

i. |x| ≤ b si y solo si −b ≤ x ≤ b.
ii. |x| ≥ b si y solo si x ≥ b o x ≤ −b.

Ejercicio 2.50. Resolver las siguientes desigualdades con módulo:
1. |x| ≤ 3
2. |x| > 5
3. 2 |x| > 4
4. −3 |x| < −6

Solución:
1. S = [−3; 3]
2. S = (−∞; −5) ∪ (5; ∞)
3. S = (−∞; −2) ∪ (2; ∞)
4. S = (−∞, −2) ∪ (2, ∞)

Ejemplo 2.51:
¿Qué pasa cuando tenemos que resolver desigualdades del tipo:
|x − 4| < 2?
Esta desigualdad nos dice que la distancia entre x y 4 no debe de ser mayor que 2;
y para poder determinar los valores de x que hacen verdadera esa desigualdad usamos
la propiedad i., sustituyendo x por (x − 4); entonces nos queda:
|x − 4| < 2 si y solo si − 2 < x − 4 < 2

Resolviendo esta última desigualdad obtenemos:
2 < x < 6

Es decir, los valores de x cuya distancia a 4 es menor que 2; son los números que
están entre 2 y 6, luego la solución expresada en intervalos es:
S = (2; 6)

Ejemplo 2.52:
Se tiene ahora la desigualdad:
|x − 5| ≥ 1
Esta desigualdad nos dice que la distancia de x a 5 debe de ser mayor o igual que
1; entonces para determinar los valores de x que hacen verdadera la desigualdad
aplicamos la propiedad ii., sustituyendo x por (x − 5):
|x − 5| ≥ 1 si y solo si x − 5 ≥ 1 o x − 5 ≤ −1

Resolviendo ambas desigualdades obtenemos como solución:
x ≥ 6 o x ≤ 4

Es decir, los valores de x cuya distancia a 5 es mayor o igual que 1 son aquellos
valores mayores a 6 o bien los x menores o iguales a 4. En notación de intervalos es:
(−∞; 4] ∪ [6; +∞)

Ejemplo 2.53:
Vamos a resolver la siguiente desigualdad:
|x − 1| < |2x + 1|
Primero vamos analizar si la desigualdad se verifica cuando |2x + 1| = 0, es decir
para x = −1/2, pues de ser así −1/2 es solución de la desigualdad y se tendrá que considerar
a este valor a la hora de escribir la solución final. En el caso de que no
sea solución no vamos a tener problema a la hora de dividir a |x − 1| por |2x + 1|
para poder resolver la desigualdad dada.

Como en este caso |x − 1| < 0 no se verifica para x = −1/2, este valor no es solución
y comenzamos a resolver la desigualdad sin problema multiplicando en ambos lados de la misma por
el inverso multiplicativo de |2x + 1|. Nos queda entonces por resolver:
|x − 1| / |2x + 1| = (x − 1) / (2x + 1) < 1

Resolvemos aplicando la propiedad i., en donde en nuestro caso b = 1:
−1 < (x − 1) / (2x + 1) < 1

Luego debemos resolver:
−1 < (x − 1) / (2x + 1)  (1)
y (x − 1) / (2x + 1) < 1  (2)

Resolviendo 1, para ello, sumamos 1 en ambos lados de la desigualdad, para que
nos quede una desigualdad que resolveremos aplicando la regla de los signos:
(x − 1) / (2x + 1) + 1 > 0, resolviendo 3x / (2x + 1) > 0

Luego al aplicar la regla de los signos nos queda por resolver:
i) 3x > 0 y 2x + 1 > 0
ii) 3x < 0 y 2x + 1 < 0

La solución de 1 es la unión de la solución de i) y ii):
S1. = (−∞; −1/2) ∪ (0; ∞)

Resolviendo 2, para ello, sumamos −1 en ambos lados de la desigualdad, para que
nos quede una desigualdad que resolveremos aplicando la regla de los signos:
(x − 1) / (2x + 1) − 1 < 0, resolviendo −x − 2 / (2x + 1) < 0

Luego al aplicar la regla de los signos nos queda por resolver:
i) −x − 2 > 0 y 2x + 1 < 0
ii) −x − 2 < 0 y 2x + 1 > 0

La solución de 2 es la unión de la solución de i) y ii):
S2. = (−∞; −2) ∪ (−1/2; ∞)

Finalmente la intersección de la solución 1 (S1.) con la solución 2 (S2.) nos da la
solución de la desigualdad dada:
S = S1. ∩ S2. = (−∞; −2) ∪ (0; ∞)

Ejercicio 2.54. Resolver las siguientes desigualdades con módulo:
1. |7 − 2x| ≥ x − 3
2. |x − 5| ≤ x − 1
3. |x − 1| − |x + 1| < 0

Solución:
1. S = (−∞; 10/3] ∪ [4; ∞)
2. S = [3; ∞)
3. S = (0; ∞)]

---

### BLOQUE 3 - FUNCIONES

#### Sistema de coordenadas rectangulares
[En el plano, se grafican dos copias de la recta real, una horizontal y la otra vertical, de modo que se intersectan en los puntos ceros de las dos rectas. A las rectas se las denomina Ejes Coordenados y a su intersección que se la denota con 0, se la denomina Origen. Por convención, la recta horizontal se llama Eje x y a la recta vertical se la llama Eje y. Los ejes coordenados dividen al plano en cuatro regiones llamadas Cuadrantes.
Un punto P en el plano, se designa por medio de una pareja de números, llamados cada uno Coordenadas Cartesianas. Si una línea vertical y otra horizontal que pasan por P, intersectan a los ejes x e y en a y b, respectivamente, entonces P tiene coordenadas (a; b); luego (a; b) es un par ordenado de números, en donde el primer número a, es la coordenada x o Abscisa; y el segundo número, b, es la coordenada y u Ordenada.

Ejercicio 3.1. Escribir los pares ordenados de cada uno de los puntos ubicados en el siguiente sistema de ejes cartesianos.
Ejercicio 3.2. Representar los siguientes puntos en un sistema de ejes coordenados:

(1/2, 3)
(0, -1)
(√2, 4)
(-4/3, -1/2)
(3/5, 4/3)
(3, 6)
(-8, -6)
(-5, 0)
(1, -√3)]

#### Gráfica de Ecuaciones
[El uso de coordenadas para puntos en el plano nos permite describir curvas por medio de una ecuación. La Gráfica de una Ecuación en x e y consiste en aquellos puntos en el plano cuyas coordenadas (x; y) hacen verdadera la igualdad. En el dictado del curso nos va a interesar graficar ecuaciones de primer y segundo grado.
Observación 3.3. El procedimiento que se menciona a continuación sólo es válido cuando el conjunto de valores que pueden tomar x e y son los reales.]

- Procedimientos para graficar una ecuación
[Obtener las coordenadas de alguno de los puntos que satisfacen la ecuación.
Graficar estos puntos en el plano.
Conectar los puntos con una curva suave.
Ejemplo 3.4. Grafiquemos la ecuación:
y = 3x + 2

El primer paso que vamos a realizar es construir una tabla de valores para determinar las coordenadas de alguno de los puntos que satisfacen la ecuación.
x | y = 3x + 2 | P = (x; y)
-3 | y = 3(-3) + 2 = -7 | (-3; -7)
-2 | y = 3(-2) + 2 = -4 | (-2; -4)
-1 | y = 3(-1) + 2 = -1 | (-1; -1)
0 | y = 3(0) + 2 = 2 | (0; 2)
1 | y = 3(1) + 2 = 5 | (1; 5)
2 | y = 3(2) + 2 = 8 | (2; 8)
3 | y = 3(3) + 2 = 11 | (3; 11)

Graficamos los puntos obtenidos de la tabla, en el plano.

Unimos los puntos con una curva suave.

Observación 3.5. Cuantos más puntos se grafiquen, mejor va a poder ser la realización de la gráfica, pues la idea es guiarse uniendo estos puntos para su construcción.

Ejemplo 3.6. Graficar la ecuación:
y = x² - x + 1

El primer paso que vamos a realizar es construir una tabla de valores para determinar las coordenadas de alguno de los puntos que satisfacen la ecuación.
x | y = x² - x + 1 | P = (x, y)
-2 | y = (-2)² - (-2) + 1 = 7 | (-2; 7)
-1 | y = (-1)² - (-1) + 1 = 3 | (-1; 3)
0 | y = (0)² - (0) + 1 = 1 | (0; 1)
1/2 | y = (1/2)² - (1/2) + 1 = 3/4 | (1/2; 3/4)
1 | y = (1)² - (1) + 1 = 1 | (1; 1)
2 | y = (2)² - (2) + 1 = 3 | (2; 3)
3 | y = (3)² - (3) + 1 = 7 | (3; 7)

Graficamos los puntos obtenidos de la tabla, en el plano.

Unimos los puntos con una curva suave.

Observación 3.7. Al observar de los ejemplos, la tabla de valores realizada para graficar la ecuación, como así también la representación gráfica de las mismas; se ve que en ambas se expresa una relación entre dos magnitudes, x e y. La relación entre estas variables es la siguiente: a cada valor de la variable x, le corresponde uno y solo un valor de la variable y. De aquí que a y se la denomina variable dependiente y a x variable independiente. Esta relación define el concepto de función.

Observación 3.8. A la expresión general de la ecuación de una función se la denota y = f(x).]

#### Funciones
[Antes de empezar a hablar del concepto de Función, entendamos qué se entiende por relación. A las relaciones las encontramos por todos lados, por ejemplo, la relación entre horas que pasa un estudiante con el celular y sus notas en el colegio, pues si están muchas horas frente al celular, sus notas bajarán. Otra relación que podemos ver es entre las preguntas contestadas en un examen y la nota obtenida, pues a más respuestas correctas, mayor será la nota. También otra relación que podemos encontrar a diario es cuando vamos a hacer las compras y lo que vamos a pagar por ello, por ejemplo, si compramos tres gaseosas, cuyo valor de cada una de ellas es de $60, vamos a pagar $180; la relación estaría entre la cantidad de gaseosas y el valor a pagar por ellas; y así podemos encontrar infinidad de ejemplos y de aquí la gran importancia de este tema.

Definición 3.9. Dados dos conjuntos A y B, una función de A en B es una regla de correspondencia o relación entre ambos conjuntos, que asocia a cada elemento x del conjunto A uno y solo un elemento del conjunto B. El conjunto A se llama conjunto de partida o dominio de f, el conjunto B se denomina conjunto de llegada o codominio de f.

Para entender mejor el tema, pensemos en una función como una máquina que toma como entradas un valor x y produce una salida f(x). Cada valor de entrada se hace corresponder con un solo valor de salida. No obstante, puede suceder que diferentes valores de entrada den el mismo valor de salida. La definición no pone restricción sobre los conjuntos del dominio y del codominio.

Por ejemplo, el dominio podría consistir en el conjunto de personas en un curso de Análisis, el codominio el conjunto de las calificaciones que se obtendrán y la regla de correspondencia la asignación de calificaciones; o como vimos en uno de los ejemplos anteriores de relaciones, el dominio puede ser las horas que el estudiante pasa frente al celular, el codominio el conjunto de calificaciones y la regla de correspondencia la asignación de calificaciones. De acuerdo a la definición anterior, para cada elemento x del dominio de A, la función f le hace corresponder un único elemento en el codominio de B; a este elemento lo denotamos f(x). Al conjunto de todos los valores f(x) pertenecientes a B, con x perteneciente al dominio A de la función, se lo denomina conjunto imagen, rango o recorrido de f y lo denotaremos If. En símbolos:
If = {y ∈ B / ∃ x ∈ A / f(x) = y}

Notación 3.10. Usaremos la siguiente notación para denotar “f es función de A en B”:
f : A → B
Siendo A el dominio y B el codominio.

Observación 3.11. Una función puede expresarse mediante un texto, una expresión algebraica, una tabla de valores o bien por medio de un gráfico. A lo largo del curso, nos va a interesar graficar funciones lineales y cuadráticas.

Ejercicio 3.12. Considere la función f : Z → Z que a cada entero le asigna su opuesto:

Escribir simbólicamente f(z)
Calcular f(−3), f(−2), f(−1), f(0), f(1) y f(2).
Representar los valores obtenidos en un sistema de ejes cartesianos.
Ejercicio 3.13.

Encontrar la expresión de alguna función f : R → R que cumpla:
f(−2) = −8, f(−1) = −1, f(0) = 0, f(1) = 1 y f(2) = 8
Representar los valores obtenidos en un sistema de ejes cartesianos.]

#### Función Lineal
[Definición 3.14.
Una función lineal es una función que se puede expresar como una ecuación de la forma:
f(x) = mx + b,
donde m y b son constantes reales y x es una variable real. Esta función se llama lineal porque su representación gráfica es una línea recta en el plano cartesiano. Su dominio e imagen son los números reales.

Ejemplo 3.15.
Representemos gráficamente la ecuación lineal y = 3x. Primero realizamos una tabla de valores y luego ubicamos los puntos obtenidos en el plano cartesiano.

x	f(x) = 3x
-2	-6
-1	-3
0	0
1	3
2	6
Observación 3.16.
Al observar el gráfico, se puede concluir que la recta pasa por el origen (0, 0) y que por cada unidad que x aumenta, y aumenta en 3 unidades.

Ejemplo 3.17.
Representemos gráficamente la función lineal y = 2x + 1.

x	y = 2x + 1
-2	-3
-1	-1
0	1
1	3
2	5
Observación 3.18.
Al observar el gráfico, se concluye que la recta corta al eje y en 1, y luego, por cada unidad que x aumenta, y aumenta en 2 unidades.

Ejemplo 3.19.
Representemos gráficamente la función lineal y = -x + 2.

x	f(x) = -x + 2
-2	4
-1	3
0	2
1	1
2	0
3	-1
Observación 3.20.
Observando el gráfico, concluimos que la recta intersecta al eje y en 2, y que por cada unidad que x aumenta, y disminuye en 1 unidad.

Ejemplo 3.21.
Representemos gráficamente la función lineal y = (2/3)x - 1.

x	f(x) = (2/3)x - 1
-3	-3
-2	-7/3
-1	-5/3
0	-1
1	-1/3
2	1/3
3	1
Observación 3.22.
Al observar el gráfico, concluimos que la recta intersecta al eje y en -1, y que por cada 3 unidades que x aumenta, y aumenta en 2 unidades.

Ejemplo 3.23.
Representemos gráficamente la función lineal f(x) = -(1/2)x - 2.

x	f(x) = -(1/2)x - 2
-2	-1
-1	-3/2
0	-2
1	-5/2
2	-3
3	-7/2
Observación 3.24.
Observando el gráfico, concluimos que la recta intersecta al eje y en -2, y que por cada 2 unidades que x aumenta, y disminuye en 1 unidad.

Conclusión General:
Al observar las gráficas de las distintas rectas y las observaciones obtenidas, concluimos que la recta corta al eje y en el término independiente, que se corresponde al valor de b en la expresión general de la función lineal. Este valor se denomina Ordenada al Origen. A partir de este valor, la recta se mueve a la derecha en x tantos lugares como indica el valor del denominador del coeficiente que acompaña a x. Luego, la recta sube o baja dependiendo de si el coeficiente de x es positivo o negativo, indicando la Pendiente de la recta.

Ejemplo 3.25.
Representemos gráficamente la recta f(x) = -(2/3)x + 2.

Ejercicio 3.27.
Representar gráficamente las siguientes rectas:

f(x) = -(1/2)x - 1
f(x) = (3/2)x + (1/2)
f(x) = -(4/3)x
f(x) = (1/2)x - 1
f(x) = (4/3)x - 2
f(x) = -(2/3)x + 1]

- Rectas paralelas y perpendiculares
[Cuando representamos gráficamente dos ecuaciones lineales en el mismo sistema de ejes cartesianos existen tres posibilidades de acuerdo a la disposición de las mismas en el plano:

Las ecuaciones tienen la misma gráfica, y se corresponden a rectas coincidentes.
Las gráficas se intersectan en un punto, y se corresponden a rectas incidentes.
Las gráficas se corresponden a rectas que no se intersectan en ningún punto.
Dos rectas son paralelas cuando sin ser coincidentes, gráficamente no se cortan en ningún punto del plano y para que ello ocurra deben de tener la misma pendiente.

Ejemplo 3.28. La recta y = 2x - 3 es paralela a la recta y = 2x + 1 pues tienen la misma pendiente, 2. La representación gráfica de ambas rectas es:

Ejemplo 3.29. Determinemos la fórmula de la función lineal que es paralela a la función y = -4x + 1 y que pasa por los puntos (0, 5/2). Luego representemos ambas rectas en un mismo sistema de ejes cartesianos. Como la recta a determinar es paralela a la recta y = -4x + 1, su pendiente es -4; luego aplicando la fórmula de la ecuación de la recta que pasa por un punto con pendiente dada nos queda:

y - 5/2 = -4(x - 0)
→ y = -4x + 5/2
Representación gráfica:

Dos rectas son perpendiculares cuando gráficamente forman un ángulo recto (ángulo de 90°). Esta situación se presenta en los siguientes casos:

Si l1 y l2 son rectas oblicuas cuyas respectivas pendientes m1 y m2 cumplen con que m1 * m2 = -1.
Si una recta es horizontal y la otra es vertical.
Ejemplo 3.30. Determinemos si la recta l1 que pasa por los puntos (-1, 5) y (3, 9) es perpendicular a la recta l2 que pasa por los puntos (-2, 6) y (3, 1). Para determinar si ambas rectas son perpendiculares, debemos determinar cuál es la pendiente de cada una de ellas:

Pendiente de la recta l1:

m1 = (9 - 5) / (3 - (-1)) = 4 / 4 = 1
Pendiente de la recta l2:

m2 = (1 - 6) / (3 - (-2)) = -5 / 5 = -1
Luego:

m1 * m2 = 1 * (-1) = -1
Como el producto de ambas pendientes es (-1), concluimos que las rectas son perpendiculares.

Observación 3.31. El producto m1 * m2 = -1 es equivalente a m1 = -1/m2 o m2 = -1/m1; entonces podemos concluir que dos rectas oblicuas son perpendiculares cuando la pendiente de una de ellas es la inversa y opuesta de la otra.

Ejemplo 3.32. Si la pendiente de una de las rectas es m1 = -3/4, la pendiente de una recta perpendicular a ella es m2 = 4/3.

Ejercicio 3.33:

Encontrar la ecuación de la recta que corta al eje x en 3 y es paralela a la recta 3x - 4y = 4.
Determinar la ecuación de la recta que es perpendicular a la recta 3y - 6x = 5 y pasa por el punto (3, -4).
Encontrar la ecuación de la recta que pasa por el punto (3, 0) y es perpendicular a la recta 3x - 4y = 4.
Solución:

y = (3/4)x - 9/4
y = -1/2 x - 5/2
y = -4/3 x + 4]

- Ecuación de la recta que pasa por dos puntos
[Como ya se ha mencionado, la pendiente de una recta se interpreta como la razón del incremento vertical con respecto al incremento horizontal. Entonces, dados dos puntos por los que pasa la recta, podemos determinar su pendiente. Su interpretación gráfica es la siguiente:

De esta manera, dados dos puntos (x1, y1) y (x2, y2) con x1 ≠ x2, la ecuación de la recta que pasa por los mismos es:

y − y1 = (y2 − y1) / (x2 − x1) (x − x1)   (1)
Ejemplo 3.34. Determinemos la recta que pasa por los puntos P = (0, 5/3) y Q = (3, 1). Aplicando la ecuación (1):

y − 5/3 = (1 − 5/3) / (3 − 0) (x − 0)
→ y − 5/3 = −2/3 * 3x
→ y = −2/9 * x + 5/3
La representación gráfica de la misma es:

Ejercicio 3.35:

Hallar la ecuación de la recta que pasa por los puntos (1, 1) y (0, −2).
Hallar la ecuación de la recta que pasa por los puntos (-2, 0) y (1, −4).
Solución:

y = 3x − 2
y = −4/3x − 8/3]

- Ecuación de la recta que pasa por un punto con pendiente dada
[De la ecuación de la recta que pasa por dos puntos, vimos que la pendiente es:

m = (y2 − y1) / (x2 − x1)
Entonces, haciendo este reemplazo en la ecuación:

y − y1 = (y2 − y1) / (x2 − x1) (x − x1)
se obtiene la ecuación de la recta que pasa por un punto con pendiente dada. Esta es:

y − y1 = m(x − x1)   (2)
con m la pendiente dada y (x1, y1) el punto por el que pasa la recta.

Ejemplo 3.36. Determinemos la ecuación de la recta de pendiente m = −1 que pasa por el punto (2, 5). Aplicando la fórmula (2) nos queda:

y − 5 = −1(x − 2)
→ y = −x + 2 + 5
→ y = −x + 7
Representación gráfica:

Ejercicio 3.37:

Hallar la ecuación de la recta de pendiente −2/5 y que pasa por el punto (0, 2).
Hallar la ecuación de la recta de pendiente 3 y que pasa por el punto (1, −2).
Solución:

y = −2/5 * x + 2
y = 3x − 5]

#### Sistema de ecuaciones lineales con dos incógnitas
[Definición 3.38. Un sistema lineal de dos ecuaciones con dos incógnitas x e y, es un conjunto de dos ecuaciones que puede escribirse en la forma siguiente:

{ 
  a1x + b1y = c1
  a2x + b2y = c2
}
donde a1, a2, b1, b2, c1 y c2 son constantes reales con a1 ≠ 0 y b2 ≠ 0 o bien a2 ≠ 0 y b1 ≠ 0. Estas restricciones aseguran que ambas variables figuren en el sistema y que haya por lo menos una variable en cada ecuación.

Los números a1, a2, b1, y b2 se llaman Coeficientes del sistema y los números c1 y c2 son los Términos Independientes. El Conjunto Solución del sistema es el conjunto de pares ordenados (x; y) que verifican ambas ecuaciones. Como las ecuaciones que componen el sistema son lineales, la gráfica de cada una de ellas es una recta. De esta manera, de acuerdo a la posición relativa de las dos rectas, se da la clasificación de cada sistema.

Ejemplo 3.39. Consideremos el sistema:

{ 
  2x + y = 5
  4x − y = 1
}
Representando ambas ecuaciones lineales en el mismo sistema de ejes cartesianos, concluimos que, como se intersectan en un punto, el sistema tiene una única solución; y es:

S = {(1; 3)}
Este método gráfico de resolver un sistema de ecuaciones no siempre es el más conveniente. Es por eso que existen otros métodos que nos permiten resolver cualquier sistema de ecuaciones con dos incógnitas.]

- Métodos de resolución de sistema de ecuaciones
[Este método consiste en despejar una de las variables de cualquiera de las ecuaciones, para luego sustituirla en la otra ecuación, obteniéndose un sistema equivalente donde una de las ecuaciones depende de una sola variable.

Ejemplo 3.40. Consideramos el sistema del ejemplo anterior:

{ 
  2x + y = 5 (i.)
  4x − y = 1 (ii.)
}
Para resolverlo por este método, lo primero que debemos hacer es despejar una de las variables de una de las ecuaciones. Supongamos que despejamos y de la ecuación (i):
2x + y = 5 → y = 5 − 2x (iii.)
Luego sustituimos este valor de y en la ecuación (ii):
4x − (5 − 2x) = 1
Nos queda entonces una ecuación con una variable, x:
4x − (5 − 2x) = 1 → 4x − 5 + 2x = 1 → 6x = 1 + 5 → x = 1
Reemplazando este valor en (iii):

y = 5 − 2(1) → y = 3
Por lo tanto, la solución del sistema de ecuaciones es:

S = {(1; 3)}
.
Para resolver un sistema por este método, primero se despeja de las dos ecuaciones la misma variable, y luego igualamos las expresiones obtenidas, resultando así una ecuación con una incógnita.

Ejemplo 3.41. Consideramos nuevamente el sistema de los ejemplos anteriores:

{ 
  2x + y = 5 (i.)
  4x − y = 1 (ii.)
}
Para resolverlo por este método, lo primero que debemos hacer es despejar y de ambas ecuaciones:

2x + y = 5 → y = 5 − 2x (iii.)
4x − y = 1 → y = −1 + 4x (iv.)
Luego igualamos ambas ecuaciones:

5 − 2x = −1 + 4x
Nos queda entonces una ecuación con una variable, x:

5 − 2x = −1 + 4x → −2x − 4x = −1 − 5 → −6x = −1 − 5 → x = 1
Reemplazando este valor en (iii) o en (iv):

y = −1 + 4(1) → y = 3
Por lo tanto, la solución del sistema de ecuaciones es:


S = {(1; 3)}

Este método consiste en reducir el sistema de ecuaciones a una sola ecuación con una sola variable por medio de los siguientes pasos:

a) Preparamos las dos ecuaciones, multiplicando por los números que convengan, de modo que las incógnitas que pretendamos eliminar tengan coeficientes opuestos.

b) Al sumar dichas ecuaciones se eliminará dicha incógnita, obteniendo una ecuación en una sola variable.

c) Resolvemos dicha ecuación.

d) Una vez obtenido el valor de dicha incógnita, basta con sustituirlo en cualquiera de las ecuaciones iniciales y despejar la otra incógnita.

Ejemplo 3.42. Nuevamente tomando el sistema de ecuaciones de los ejemplos anteriores:

{ 
  2x + y = 5 (i.)
  4x − y = 1 (ii.)
}
Se toma (i) y se multiplica por (−2):

−4x − 2y = −10
Luego sumamos esta ecuación a la ecuación (ii):

−4x − 2y = −10
4x − y = 1
Nos queda:

0x − 3y = −9
Lo que nos da una ecuación con una sola incógnita, y:

−3y = −9 → y = 3
Luego reemplazamos este valor de y en (i):

2x + 3 = 5 → x = 1
Por lo tanto, la solución del sistema de ecuaciones es:

S = {(1; 3)}
Ejemplo 3.43. Resolvemos el siguiente sistema de ecuaciones:

{ 
  2x + 4y = 2 (i.)
  x + 2y = 1 (ii.)
}
Aplicando el método de reducción por sumas y restas, multiplicamos la ecuación (ii) por (−2):

−2x − 4y = −2
Luego sumamos esta ecuación a (i):

2x + 4y = 2
−2x − 4y = −2
Obtenemos:

0x + 0y = 0
Como hemos obtenido el resultado 0 = 0, esto indica que el sistema tiene infinitas soluciones. A la solución se la puede expresar de las siguientes maneras:


S = {(x; y) : x = 1 − 2y ∀y ∈ R}
O bien:


S = {(x; y) : y = −1/2x + 1/2 ∀x ∈ R}
Ejemplo 3.44. Resolvemos el siguiente sistema de ecuaciones:

{ 
  2x + 4y = 2
  4x + 8y = 16
}
Aplicando el método de igualación, despejamos x de ambas ecuaciones:


2x + 4y = 2 → x = 1 − 2y
4x + 8y = 16 → x = 4 − 2y
Igualando las ecuaciones que obtuvimos:

1 − 2y = 4 − 2y → −2y + 2y = 4 − 1 → 0 = 3
Este absurdo nos indica que el sistema no tiene solución.

Situaciones problem´aticas
En muchas situaciones problemáticas se requiere del planteo de un sistema de ecuaciones para su resolución.

Ejemplo 3.45. En una alcancía hay 50 monedas y un total de $400. Si solo hay monedas de $5 y de $10, ¿cuántas monedas de $5 y de $10 hay en la alcancía?

Resolución: Planteamos el sistema de ecuaciones:


{ 
  x + y = 50 (i.)
  5x + 10y = 400 (ii.)
}
Aplicamos el método de sustitución:

Despejamos y de (i):


y = 50 − x
Sustituimos este valor en (ii):

5x + 10(50 − x) = 400
Resolvemos la ecuación:

5x + 500 − 10x = 400 → −5x = 400 − 500 → x = 20
Por lo tanto, el valor de y es:

y = 50 − 20 = 30
Respuesta: Hay 20 monedas de $5 y 30 monedas de $10.

Ejemplo 3.46.
En una granja se crían gallinas y conejos. Si se cuentan las cabezas de estos animales son 50, y si se cuentan las patas, son 134. ¿Cuántos animales hay de cada clase?

Resolución: Como el problema nos pregunta cuántos animales de cada clase hay, las incógnitas van a representar a la cantidad de animales, es decir, por ejemplo podemos suponer que la variable x representa la cantidad de conejos y la variable y representa a la cantidad de gallinas. Luego con los datos del problema armamos las ecuaciones del sistema:

{
x + y = 50 (i.)
4x + 2y = 134 (ii.)
}

Una vez planteado el sistema de ecuaciones debemos resolverlo por alguno de los métodos de resolución. Aplicamos el método de igualación. Despejamos de (i.) y de (ii.) la variable y:

y = 50 − x
y = (134 − 4x) / 2 = 67 − 2x

Igualando ambas ecuaciones:

50 − x = 67 − 2x
−x + 2x = 67 − 50
x = 17

Luego el valor de y es:

y = 50 − 17 = 33

Respuesta: Hay 17 conejos y 33 gallinas.

Ejercicio 3.47. Resolver los siguientes problemas:

En un almacén hay botellas de aceite de 5 litros y 2 litros. En total hay 1000 litros de aceite y 323 botellas. ¿Cuántas botellas de cada tipo hay?
Solución: Hay 118 botellas de 5 litros y 205 botellas de 2 litros.

Carlos le dice a Juan: “el dinero que yo tengo es el doble del que tú tienes”. Y Juan le responde: “Si me das 600 pesos los dos tendremos la misma cantidad”. ¿Cuánto dinero tiene cada uno?
Solución: Carlos tiene 2400 pesos y Juan 1200.

Ana tiene el triple de la edad que su hijo Jaime. Dentro de 15 años, la edad de Ana será el doble que la de su hijo. ¿Cuántos años más que Jaime tiene su madre?
Solución: La madre tiene 30 años más que su hijo Jaime.

La suma de dos números es 10 y la mitad de uno de ellos es el doble del otro. ¿Qué números son?
Solución: Los números son 2 y 8.]


#### Función Cuadrática
[Definición 3.48. Se llama función cuadrática a la función que se puede expresar como una ecuación que tiene la siguiente forma: f(x) = ax² + bx + c. En este caso, a, b y c son los términos de la ecuación y pueden tomar cualquier valor real, pero a siempre debe de ser diferente de 0. El término ax² es el término cuadrático, mientras que bx es el término lineal y c, el término independiente. Cuando están presentes todos los términos, se habla de una ecuación cuadrática completa. En cambio, si falta el término lineal o el término independiente, se trata de una ecuación cuadrática incompleta. El dominio de esta función es el conjunto de los números reales y la gráfica de la misma es una parábola.]

- Parábolas del tipo y = ax², a ≠ 0
[Al observar la gráfica concluimos: Respecto de la curva y = x², y = ax² verifica:

i. Cuando |a| > 1, la curva se acerca al eje y (eje de simetría). Cuando |a| < 1 se aleja del eje y.

ii. Cuando a > 0, las ramas de la parábola van hacia arriba. Cuando a < 0, las ramas de la parábola van hacia abajo.]

- Parábolas del tipo y = ax² + c, a ≠ 0 y c ≠ 0
[Al observar la gráfica concluimos: Respecto de y = 2x², la curva de ecuación y = ax² + c, con a ≠ 0, es una parábola que:

i. Cuando c > 0, la curva está desplazada c unidades hacia arriba.

ii. Cuando c < 0, la curva está desplazada |c| unidades hacia abajo.]

- Parábolas del tipo y = a(x − h)², a ≠ 0 y h ≠ 0
[Al observar la gráfica concluimos: Respecto de la curva y = 2x², la curva de ecuación y = a(x − h)², con a ≠ 0, es una parábola que:

i. Cuando h > 0, la curva está desplazada h unidades hacia la derecha.

ii. Cuando h < 0, la curva está desplazada |h| unidades hacia la izquierda.]

- Parábolas del tipo y = a(x − h)² + c, a ≠ 0, h ≠ 0 y c ≠ 0
[Al observar la gráfica concluimos: Respecto de la curva y = 2x², la curva de ecuación y = a(x − h)², con a ≠ 0, es una parábola que:

i. Cuando h > 0, la curva está desplazada h unidades hacia la derecha.

ii. Cuando h < 0, la curva está desplazada |h| unidades hacia la izquierda.]

- Parábolas del tipo y = ax² + bx + c, con a, b y c valores reales distintos de cero
Para graficar a este tipo de parábolas se requiere determinar previamente:

La o las intersecciones con el eje x, es decir, los ceros o raíces de la función.
La intersección con el eje y, que se corresponde con el valor del término independiente o bien se obtiene de reemplazar en la función a x por 0.
Vértice de la parábola: v = (xv; yv) donde xv = (x1 + x2) / 2, con x1 y x2 las raíces de la función; o bien la coordenada x del vértice se puede obtener aplicando la fórmula xv = −b / 2a. La coordenada y del vértice se obtiene reemplazando por el valor obtenido de xv en la función; o bien aplicando la fórmula, yv = (4ac − b²) / (2a).
Eje de simetría de la parábola, cuya ecuación que lo representa es x = xv. Es importante ubicar este eje, pues es aquel que indica que las ramas de la parábola son simétricas con respecto a él.
Ejemplo 3.50. Sea f(x) = x² − 2x − 3; para representarla gráficamente buscamos:

Sus raíces o intersecciones con el eje x: como ∆ = (−2)² − 4 · 1 · (−3) = 16 > 0, luego la función tiene dos raíces reales. Aplicando la fórmula resolvente o de Bhaskara tenemos:
x₁, x₂ =
(2 ± √∆) / (2 · 1)
= (2 ± 4) / 2
→ x₁ = 3 y x₂ = −1

Intersección con el eje y:
f(0) = 0² − 2 · 0 − 3 = −3
→ f(0) = −3

Vértice de la parábola: V = (xv; yv)
xv = (3 + (−1)) / 2 = 1
Luego reemplazando por este valor en la función se obtiene el valor de yv:
yv = 1² − 2 · 1 − 3 = −4
Por lo tanto el vértice es:
v = (1; −4)

Eje de simetría:
x = 1

Ahora sí, marcando los resultados encontrados en un sistema de ejes y luego uniéndolos a estos puntos con una curva suave, obtenemos la gráfica de la función. De la gráfica concluimos que en el intervalo (−∞; 1) la función es decreciente, pues cuando los valores de x aumentan, los valores de y disminuyen. Por otro lado, observamos que en el intervalo (1; ∞) la función es creciente, pues a medida que aumentan los valores de x también aumentan los valores de y.
De esta manera tenemos que la función alcanza un mínimo en el vértice de la parábola. Por otro lado, al observar la gráfica concluimos que el conjunto imagen de la función es el intervalo [−4, ∞).
Ejemplo 3.51.
Sea f(x) = x² − 4x + 5; para representarla gráficamente buscamos:

Sus raíces o intersecciones con el eje x: como ∆ = 16 − 4 · 1 · 5 < 0, la función no tiene raíces reales, es decir, las ramas de la parábola no cortan nunca al eje x.

Intersección con el eje y:
f(0) = 5

Vértice de la parábola: V = (xv; yv)
Como no tiene raíces reales la función, la coordenada x del vértice no se puede obtener como el promedio de las raíces; es por eso que aplicamos la fórmula dada con anterioridad:
xv = 4 / (2 · 1) = 2
Luego la coordenada y del vértice es:
f(2) = 2² − 4 · 2 + 5 = 1
Por lo tanto, el vértice de la parábola es:
v = (2; 1)

Eje de simetría:
x = 2

Marcando los puntos recién encontrados en un sistema de ejes, y uniéndolos considerando también el eje de simetría, obtenemos la gráfica de la función:

De la gráfica concluimos que en el intervalo (-∞; 2) la función es decreciente, pues a medida que aumentan los valores de x, los valores de y disminuyen. Por otro lado, observamos que en el intervalo (2; ∞) la función es creciente, ya que cuando los valores de x aumentan, los valores de y también lo hacen. De esta manera, podemos concluir que la función alcanza un mínimo en el vértice de la parábola. Además, al observar la gráfica, concluimos que el conjunto imagen de la función es el intervalo [1, ∞).

Mis disculpas por la confusión anterior. Aquí te transcribo todo el texto sin resumen y en formato plano:

Ejemplo 3.52. Sea f(x) = x^2 + 2x + 1; para representarla gráficamente buscamos:

Sus raíces o intersecciones con el eje x: Como Δ = 4 − 4 · 1 · 1 = 0, la función tiene una única raíz real y, por lo tanto, la gráfica de la función rebota sobre el eje x. Busquemos esta raíz aplicando la fórmula resolvente o de Bhaskara: x1 = x2 = −2 / 2 · 1 = −1 → x1 = −1

Intersección con el eje y: f(0) = 1

Vértice de la parábola: V = (xv; yv). Como tiene una única raíz real, la coordenada x del vértice coincide con la raíz, en este caso xv = −1 y, por lo tanto, la coordenada y del vértice es 0, entonces el vértice de la parábola es el punto del plano: v = (−1; 0)

Eje de simetría: x = −1

Marcando los puntos recién encontrados en un sistema de ejes, y uniéndolos considerando también el eje de simetría, obtenemos la gráfica de la función. De la gráfica concluimos que en el intervalo (−∞; −1) la función es decreciente, pues a medida que aumentan los valores de x disminuyen los valores de y. Por otro lado, observamos que en el intervalo (−1; ∞) la función es creciente, pues cuando los valores de x aumentan, los valores de y también lo hacen. De esta manera, tenemos que la función alcanza un mínimo en el vértice de la parábola. Por otro lado, al observar la gráfica concluimos que el conjunto imagen de la función es el intervalo [0, ∞).

Ejemplo 3.53. Sea f(x) = −(x−1)(x−3) la función cuadrática expresada en forma factorizada y, por lo tanto, no es necesario aplicar algún método para determinar sus raíces, ya que las conocemos de antemano, estas son, 1 y 3. De la forma factorizada conocemos también el valor de a el cual es −1 y de aquí que concluimos que la gráfica de esta función corta al eje x en 1 y 3 y sus ramas van hacia abajo. Para poder graficarla debemos conocer además el vértice de la misma V = (xv; yv), en donde: xv = (1 + 3) / 2 = 2 y entonces yv = −(2 − 1)(2 − 3) = 1, así V = (2; 1); concluimos de aquí que el eje de simetría es x = 2. Por último, nos falta encontrar el valor que corta al eje y, esto es cuando x = 0, f(0) = −(0 − 1)(0 − 3). Finalmente, con todos estos datos estamos en condiciones de representar gráficamente a esta función.

De la gráfica concluimos que en el intervalo (−∞; 2) la función es creciente, pues a medida que aumentan los valores de x aumentan los valores de y. Por otro lado, observamos que en el intervalo (2; ∞) la función es decreciente, pues cuando los valores de x aumentan, los valores de y disminuyen. De esta manera, tenemos que la función alcanza un máximo en el vértice de la parábola. Por otro lado, al observar la gráfica concluimos que el conjunto imagen de la función es el intervalo (−∞, 1).

Ejercicio 3.54. Graficar las siguientes funciones, indicando luego intervalos de crecimiento y de decrecimiento, si alcanza un valor máximo o mínimo y el conjunto imagen de la misma.

f(x) = 2x^2 − 4x + 5
f(x) = 4x^2 + 24x + 32
f(x) = −(1 / 2) x^2 + 2x − 2
Observación 3.55. En resumen, a lo expresado con anterioridad, tenemos que una función cuadrática se la puede encontrar expresada en su forma polinómica (f(x) = ax^2 + bx + c), o en su forma factorizada (f(x) = a(x − x1)(x − x2), donde x1 y x2 son las raíces de la parábola) o bien en su forma canónica (f(x) = a(x − xv)^2 + yv, donde (xv, yv) es el vértice de la parábola). Estas tres formas en que puede presentarse una función cuadrática son equivalentes, es decir, verifican: f(x) = ax^2 + bx + c = a(x − x1)(x − x2) = a(x − xv)^2 + yv. Estas igualdades se verifican aplicando la propiedad distributiva y asociando convenientemente.

Ejercicio 3.56. Verificar las siguientes igualdades. f(x) = 2(x − 1)(x − 3) = 2(x − 2)^2 − 2 = 2x^2 − 8x + 6.]

- Problemas de valores máximos y mínimos
[Con frecuencia nos encontramos con la necesidad de determinar el valor más grande o el valor más pequeño en ciertas situaciones problemáticas. Problemas de la vida cotidiana que involucran maximizar o minimizar una función se pueden encontrar, por ejemplo, en el cálculo de áreas, volúmenes, distancia, tiempo, costos o ganancias de algún producto. A estos problemas se los conoce como problemas de máximos y mínimos y se los puede describir por medio de diferentes funciones. Nosotros nos vamos a detener en el estudio de estas situaciones cuando se representan por medio de funciones cuadráticas.

Ejemplo 3.57. Un granjero dispone de 1200 metros de cerca para construir 3 corrales rectangulares, paralelos e idénticos, como muestra la figura. ¿Cuál es el mayor área total que puede cercar? ¿Cuáles son las dimensiones de cada corral?
Para resolverlo se debe plantear primero la función que representa la situación problemática. Consideramos las siguientes incógnitas sobre la figura dada: luego la relación que se da entre las variables de acuerdo a los datos del problema es:
6x + 4y = 1200 → y = 300 − (3/2)x
entonces si el problema nos pide determinar el mayor área total que se puede cercar, la función a maximizar es:
f(x) = (3x) y reemplazando por el valor de y
f(x) = (3x)(300 − (3/2)x)
factorizamos esta función para determinar sus raíces
f(x) = −(9/2)x(x − 200)
Las raíces de la función son x = 0 y x = 200, entonces el vértice se va a encontrar en:
v = (xv; yv) donde xv = (200 + 0) / 2 = 100 → yv = −(9/2)(100)(100 − 200) = 45000
→ v = (100; 45000) de estos resultados obtenemos la respuesta al problema:
Respuesta: El área total máxima es 45000 y las dimensiones de cada corral son x = 100 e y = 300 − (3/2)(100) = 150.

Ejemplo 3.58. Se introducen abejas en una isla. La población máxima fue de 4410 en el día 11, y se extinguió en 32 días.

Sabiendo que el crecimiento poblacional de las abejas se describe mediante una función cuadrática, indique la expresión de la misma.
Analizando la función obtenida en el apartado anterior, responda a las siguientes preguntas:
a) ¿Cuántas abejas fueron introducidas?
b) ¿En qué días la población fue de 4250 abejas?
Resolvamos cada apartado del problema:
Para encontrar la función cuadrática que describe la evolución en la población de abejas a medida que transcurrieron los días, vamos a utilizar los datos del problema indicando los valores que representan de la misma, en este caso de que la población máxima fue de 4410 en el día 11, obtenemos el vértice de la parábola y de que la población se extinguió a los 32 días, obtenemos un punto de la misma, este es el punto (32, 0). Con estos datos podemos encontrar la forma canónica de la función cuadrática:
f(x) = −10 · (x − 11)² + 4410
a) Para responder a la pregunta de cuántas abejas fueron introducidas, debemos encontrar el valor de la función para x = 0, pues en este instante es cuando comienza la población de abejas.
f(0) = −10 · (0 − 11)² + 4410 = 3200
Por lo tanto, la población introducida fue de 3200 abejas.
b) Para responder a la última pregunta debemos encontrar los valores de x cuando f(x) = 4250, esto es:
4250 = −10 · (x − 11)² + 4410
luego resolviendo la ecuación que nos queda obtenemos que para x = 7 y x = 15 el valor de la función es de 4250, entonces en el día 7 y 15 la población de abejas fue de 4250.
Ejemplo 3.59. Si la diferencia entre dos números es 6, ¿Cuáles deben ser los números para obtener el menor producto? ¿Cuál es ese producto?
Para resolverlo, planteamos la función que representa esta situación. Las incógnitas del problema son los números a encontrar, es por eso que a uno lo definimos como x y al otro como (x − 6), pues la diferencia de ambos debe de ser 6. Luego el problema pide determinar estos números cuando el producto entre ellos sea mínimo, entonces nos queda como función:
f(x) = x(x − 6)
que se corresponde a una función cuadrática expresada en forma factorizada. En el vértice de la parábola se obtiene el valor mínimo, en donde la coordenada x del vértice, en este caso, nos da uno de los números buscados (x), y la coordenada y del vértice nos da, en nuestro caso, el valor del producto mínimo. Determinemos entonces el vértice de la función:
Como las raíces son 0 y 6, xv = (0 + 6) / 2 = 3, entonces yv = 3(3 − 6) = −9, es decir el vértice es:
v = (3; −9)
de este resultado damos respuesta al problema:
Respuesta: Los números para obtener el menor producto son 3 y −3; y el producto entre ellos es −9.
Veamos la representación gráfica de esta función para terminar de entender la respuesta dada al problema.

Ejercicio 3.60. Resolver los siguientes problemas:

Hallar dos números cuya suma sea 10 y cuyo producto sea máximo.
Solución: Los números son el 5.
Un proyectil describe la trayectoria de la gráfica dada por la función
h(t) = 200 + 80t − 16t² donde h(t) es la altura en metros y t el tiempo en segundos. Analizando a la función responder:
a) ¿Cuál es la altura que alcanza a los 3 segundos?
b) ¿Cuál es la altura máxima que alcanza?
c) ¿Qué tiempo emplea en llegar al suelo?]


#### Polinomios
[Los polinomios que estudiaremos son expresiones de la forma:

P(x) = anxⁿ + an₋₁xⁿ₋¹ + an₋₂xⁿ₋² + ......a₁x + a₀

donde an, an₋₁, an₋₂, ......, a₁ son números reales constantes, llamados Coeficientes;
x es la Indeterminada, y los exponentes de cada una de las x (n, n − 1, n − 2, ....., 1, 0) son números naturales constantes. A cada término del polinomio se lo llama Monomio. an es el Coeficiente Principal; en el caso de que an = 1 se dice que el polinomio es Mónico. a₀ es el Término Independiente.

P(x) = −5x⁴ + 2x³ + 4x + 6
|{z}
Coeficiente principal
|{z}
Término independiente

P(x) = √2x + 6x² − 3x³ + 1

P(x) = −3x⁻² + 2x − 4
ojo!! este no es un polinomio pues −2 no es un número natural.

P(x) = x⁷ + 2x³ − √2x
ojo!! este tampoco es un polinomio pues una de las potencias a la que está elevada x no es un número natural.

El Grado de un polinomio es el del monomio de mayor grado que figura en él.

Ejemplo 3.61. P(x) = −6x⁵ + 3x⁴ + x − 9 este polinomio es de grado 5 pues es la mayor potencia a la que está elevada x.

Un polinomio está ordenado cuando los monomios que lo componen están escritos en forma creciente o decreciente según su grado.

Ejemplo 3.62.

P(x) = 3x⁶ − 5x⁴ + 3x³ − 2x + 1 es un polinomio ordenado de manera decreciente.
P(x) = 2 + 3x − 4x³ + 19x⁴ − 10x⁵ es un polinomio ordenado de manera creciente.
P(x) = 5x³ − 4x⁷ + 8x⁴ − 3x + √10 es un polinomio no ordenado.
Un polinomio de grado n es Completo cuando en él figuran (n + 1) monomios, desde el término independiente hasta el grado n. Si el polinomio no está completo, lo podemos completar sumando con coeficientes nulos todos los términos faltantes.

Ejemplo 3.63.

P(x) = −3x² + 5x − 4 es un polinomio completo y ordenado de manera decreciente.

P(x) = x⁷ − 2x⁵ + 3x³ es un polinomio no completo, pero ordenado. Lo podemos completar de la siguiente manera:
P(x) = x⁷ + 0x⁶ − 2x⁵ + 0x⁴ + 3x³ + 0x² + 0x + 0

P(x) = 8x⁶ + x² − 10 + 6x⁵ + √2x este polinomio no está completo, ni ordenado, luego lo podemos ordenar y completar de la siguiente manera:
P(x) = 8x⁶ + 6x⁵ + 0x⁴ + 0x³ + x² + √2x − 10

Un valor de x es Raíz de P(x) si el polinomio se anula para ese valor:
x = a es raíz de P(x) si y solo si P(a) = 0

Ejemplo 3.64.
x = 1 es raíz de P(x) = x⁵ − x³ porque P(1) = 1⁵ − 1³ = 0, como así también −1 es raíz de P(x) = x⁵ − x³, pues P(−1) = 0.

¿Ahora bien cómo hacemos para obtener el valor de las raíces de un polinomio de forma exacta, es decir sin tener la necesidad de ir probando aquel valor que anula al polinomio? Para dar respuesta a este problema requerimos del concepto de Factorización de un polinomio. Factorizar o factorizar un polinomio en ℝ significa expresarlo como producto de polinomios de grado 1 y/o de polinomios de mayor grado irreducibles (aquellos polinomios que no tienen raíces reales). Existen diferentes estrategias que se utilizan para factorizar un polinomio, dependiendo de la estructura que estos presentan.]

- Estrategias de Factorización
[Factor común.
Cuando en un polinomio P(x) la variable x figura en todos los términos, es conveniente extraerla como factor común, y se la extrae a la menor potencia.
Ejemplo 3.65.
P(x) = 7x^5 + 5x^4 + x^3
factor común x^3
→ P(x) = x^3 (7x^2 + 5x + 1)

Observación 3.66.
En algunos casos se extrae un número que es factor común en todos los coeficientes.
Ejemplo 3.67.
P(x) = −4x^7 − 8x^3 + 4x^2 + 16x
factor común 4x
→ P(x) = 4x(−x^6 − 2x^2 + x + 4)

Diferencia de cuadrados.
Una diferencia de cuadrados puede escribirse:
a^2 − b^2 = (a − b)(a + b)
esto es, la resta de dos términos, en donde cada uno de ellos está elevado al cuadrado, es igual al producto de su diferencia por su suma.
Ejemplo 3.68.

P(x) = x^2 − 25 = (x − 5)(x + 5)
Este polinomio queda así expresado en su forma factorizada.
P(x) = x^4 − 16 = (x^2 − 4)
| {z } Diferencia de cuadrados
(x^2 + 4)
| {z } Polinomio Irreducible
→ P(x) = x^4 − 16 = (x − 2)(x + 2)(x^2 + 4)
Factor común por grupos.
Algunos polinomios presentan una estructura que nos permite formar grupos de igual cantidad de términos y sacar factor común en cada uno de esos grupos. Una vez hecho esto, aparece un nuevo factor común en todos los grupos.
Ejemplo 3.69.
P(x) = 7x^5 − 5x^4 + 14x − 10
Agrupamos
→ P(x) = (7x^5 − 5x^4) + (14x − 10)
Sacamos factor común en cada grupo
→ P(x) = x^4(7x − 5) + 2(7x − 5)
Sacamos factor común (7x − 5)
→ P(x) = (7x − 5)(x^4 + 2)

Ejemplo 3.70.
P(x) = 3x^8 + x^7 − 2x^5 + 3x^3 + x^2 − 2
Agrupamos
→ P(x) = (3x^8 + x^7 − 2x^5) + (3x^3 + x^2 − 2)
Sacamos factor común en el primer grupo
→ P(x) = x^5(3x^3 + x^2 − 2) + (3x^3 + x^2 − 2)
Sacamos factor común (3x^3 + x^2 − 2)
→ P(x) = (3x^3 + x^2 − 2)(x^5 + 1)

Trinomio Cuadrado Perfecto.
Las expresiones de la forma a^2 + 2ab + b^2 o a^2 − 2ab + b^2 se denominan trinomio cuadrado perfecto y se obtienen al desarrollar (a + b)^2 o (a − b)^2 respectivamente, es decir:
(a + b)^2 = a^2 + 2ab + b^2
(a − b)^2 = a^2 − 2ab + b^2

Para que un trinomio sea un cuadrado perfecto:

Dos de los términos deben ser cuadrados a^2 y b^2.
Antes de a^2 y b^2 no debe haber signo negativo, si lo hubiese, sacar (−1) factor común.
El producto (2ab) es el término restante.
Ejemplo 3.71.
P(x) = x^2
|{z} x^2

10x |{z} 2.x.5
25 |{z} 5^2
→ P(x) = (x + 5)^2
Ejemplo 3.72.
P(x) = 4x^2
|{z} (2x)^2
− 24x |{z} 2.x.6

36 |{z} 6^2
→ P(x) = (2x − 6)^2
Regla de Ruffini.
La Regla de Ruffini consiste en una disposición práctica que permite efectuar en una forma sencilla la división entre polinomios, siempre que el divisor sea de la forma (x − a).

Observación 3.73.
Para aplicar esta regla, el polinomio debe de estar completo y ordenado en forma decreciente.

Ejemplo 3.74.
Se desea dividir al polinomio (3x^3 + 7x^2 + 6x − 1) por (x − (−2)) aplicando la regla de Ruffini. Consideramos entonces los siguientes pasos:

En la primera fila se colocan los coeficientes del polinomio, luego se baja el término que se corresponde al coeficiente principal, para ser multiplicado por el (−2); el resultado de este producto, −6, es sumado al coeficiente que sigue, en este caso, el 7.
El valor obtenido de sumar 7 + (−6) = 1, se lo va a multiplicar por (−2) y el resultado se colocará debajo del tercer coeficiente, 6, para realizar su suma:
Observación 3.73.
Para aplicar esta regla, el polinomio debe de estar completo y ordenado en forma decreciente.

Ejemplo 3.74.
Se desea dividir al polinomio (3x^3 + 7x^2 + 6x − 1) por (x − (−2)) aplicando la regla de Ruffini. Consideramos entonces los siguientes pasos:

En la primera fila se colocan los coeficientes del polinomio, luego se baja el término que se corresponde al coeficiente principal, para ser multiplicado por el (−2); el resultado de este producto, −6, es sumado al coeficiente que sigue, en este caso, el 7.
El valor obtenido de sumar 7 + (−6) = 1, se lo va a multiplicar por (−2) y el resultado se colocará debajo del tercer coeficiente, 6, para realizar su suma:
Observación 3.75.
El resto obtenido al hacer la división es −9, un valor distinto de 0, y por lo tanto no se puede decir que (−2) es raíz del polinomio. A nosotros nos va a interesar aplicar esta regla para poder factorizar un polinomio, entonces queremos que el resto nos dé 0.

Ejemplo 3.76.
Sea P(x) = x^4 + 2x^2 − 2 + x lo queremos dividir por (x + 1) aplicando la regla de Ruffini. Como P(x) no está completo y ordenado, primero debemos hacerlo, para aplicar la regla:
→ P(x) = x^4 + 0x^3 + 2x^2 + x − 2
como el resto obtenido es 0, decimos que −1 es raíz del polinomio. Luego al polinomio dado se lo expresa:
P(x) = (x^3 − x^2 + 3x − 2)(x + 1)

Si queremos seguir reduciendo a este polinomio como un producto de polinomios de grado uno o polinomios de mayor grado irreducible, se debe factorizar a (x^3 − x^2 + 3x − 2); como no es un cuatrinomio al cubo perfecto, aplicamos la regla de Ruffini nuevamente:
Como el resto es un valor distinto de cero, se tiene que 2 no es raíz del polinomio.
Probamos con otro valor:
Como nuevamente el resto es distinto de cero, seguimos probando con distintos números hasta obtener un valor en donde se obtenga resto 0. Pero este método de ir probando, no está bueno, pues se pierde mucho tiempo; entonces recurrimos a lo siguiente:
Las candidatas a raíces racionales de un polinomio son aquellos valores que provienen del cociente de los divisores del término independiente, con los divisores del coeficiente principal. En nuestro ejemplo serían:
±2
±1
;
±1
±1

Observación 3.77.
En el caso de que con estos valores no se obtenga resto cero, al hacer la división, significa que la raíz es irracional y en este caso a la misma se la debe de aproximar; lo cual supera al desarrollo de este curso.

Veamos ahora un par de ejemplos en donde se aplican estas diferentes estrategias para factorizar a un polinomio.
Ejemplo 3.78. Factoricemos el polinomio P(x) = x^5 − 9x^3 + 4x^2 + 12x :

Primero aplicamos factor común x : P(x) = x(x^4 − 9x^2 + 4x + 12)
Debemos factorizar (x^4 − 9x^2 + 4x + 12) y para ello aplicamos la regla de Ruffini; siendo necesario completar primero al polinomio. Consideramos como raíz al valor −1. luego x^4 − 9x^2 + 4x + 12 = (x − (−1))(x^3 − x^2 − 8x + 12)
Aplicamos nuevamente la regla de Ruffini sobre (x^3 − x^2 − 8x + 12) considerando como raíz a 2. luego (x^3 − x^2 − 8x + 12) = (x − 2)(x^2 + x − 6)
Ahora debemos factorizar (x^2 + x − 6) y para ello aplicamos Bhaskara, fórmula vista en el segundo capítulo en la sesión de ecuación de segundo grado: −1 ± √(1 − 4·1·(−6)) / 2·1 = −1 ± √25 / 2·1 = −1 ± 5 / 2 = { x1 = −1 + 5 / 2 = 2 x2 = −1 − 5 / 2 = −3 } luego (x^2 + x − 6) = (x − 2)(x − (−3)) Finalmente uniendo todos los resultados obtenidos expresamos al polinomio en forma factorizada: P(x) = x^5 − 9x^3 + 4x^2 + 12x = x(x + 1)(x − 2)(x − 2)(x + 3) → P(x) = x(x + 1)(x − 2)^2(x + 3)
Observación 3.79. Los métodos que aplicamos para factorizar a un polinomio pueden ser diferentes a los usados en el ejemplo anterior; pero la expresión factorizada de un polinomio es única.

Ejercicio 3.80. Factorizar los siguientes polinomios:

P(x) = x^3 − 9x^2 + 27x − 27
P(x) = x^4 − 3x^2 − 4
P(x) = 16x^4 − 1
P(x) = x^3 + 3x^2 − x − 3
Solución:

P(x) = (x − 3)^3
P(x) = (x − 2)(x + 2)(x^2 + 1)
P(x) = 16(x − 1/2)(x + 1/2)(x^2 + 1/4)
P(x) = (x − 1)(x + 1)(x + 3)]


#### Expresiones Racionales
[Definición 3.81. Se llama Expresión Racional en la variable x, a toda expresión del tipo R(x) = P(x) / Q(x) definida para todo x tal que Q(x) ≠ 0, donde P(x) y Q(x) son polinomios.

Dominio de Validez
Definición 3.82. El Dominio de Validez de la expresión es el conjunto de valores reales de x para los cuales Q(x) ≠ 0.

Ejemplo 3.83. Dada la expresión racional
R(x) = −3x² + 2x − 4 / x² − 9
determinemos su dominio de validez, y para ello busquemos las raíces del polinomio del denominador, ya que estos valores son aquellos que quedan fuera del dominio de validez, dado que dan lugar a una división por cero. Para determinar las raíces de x² − 9, vamos a factorizar a este polinomio.
x² − 9 = (x − 3)(x + 3) Aplicamos diferencia de cuadrados.
Por lo tanto el dominio de validez es:
Dominio: R − {−3; 3}

Ejemplo 3.84. Dada la expresión racional
R(x) = 2x / x³ − 3x² + 2x
determinemos su dominio de validez, y para ello busquemos las raíces del polinomio del denominador, ya que estos valores son aquellos que quedan fuera del dominio de validez, dado que dan lugar a una división por cero. Para determinar las raíces de x³ − 3x² + 2x, vamos a factorizar a este polinomio.
x³ − 3x² + 2x = x(x² − 3x + 2) Aplicamos factor común x.
= x(x − 1)(x − 2) Aplicamos Bhaskara.
Por lo tanto el dominio de validez es:
Dominio: R − {0; 1; 2}] 

- Simplificación de Expresiones Racionales
[Las operaciones realizadas para simplificar expresiones racionales se realizan con el fin de lograr expresiones más sencillas que la expresión dada. Estas expresiones más sencillas serán equivalentes a la original siempre que se las considere definidas en el dominio de validez de la expresión original. Al trabajar con expresiones racionales nos resultará conveniente simplificar sus fórmulas, es decir, su expresión racional. Es posible simplificar cuando existen factores comunes en el numerador y en el denominador; de lo contrario, la expresión racional es irreducible.

Ejemplo 3.85. Simplifiquemos la siguiente expresión racional:
R(x) = (x² − 1) / (x³ + 3x² − x − 3)
Primero debemos buscar el dominio de validez, y para ello calculamos las raíces del polinomio del denominador x³ + 3x² − x − 3 aplicando algún método de factorización o la regla de Ruffini o la fórmula resolvente de Bhaskara.
Aplicando factor común por grupos nos queda:
x³ + 3x² − x − 3 = (x³ + 3x²) + (−x − 3)
= x²(x + 3) − (x + 3)
= (x + 3)(x² − 1)
Ahora factorizamos x² − 1, aplicando diferencia de cuadrados:
x² − 1 = (x − 1)(x + 1)
Finalmente la expresión factorizada del polinomio del denominador es:
(x + 3)(x − 1)(x + 1)
Entonces el dominio de validez es:
Dominio: R − {−3, −1, 1}
Ahora se debe factorizar al polinomio del numerador, x² − 1, y para ello aplicamos el caso de factoreo diferencia de cuadrados:
x² − 1 = (x − 1)(x + 1)
La expresión racional nos queda entonces de la siguiente manera:
R(x) = (x − 1)(x + 1) / (x + 3)(x − 1)(x + 1)
Ahora sí estamos en condiciones de simplificar la expresión:
R(x) = (x − 1)(x + 1) / (x + 3)(x − 1)(x + 1)
Entonces la expresión simplificada de R(x) es:
R(x) = 1 / (x + 3)

Ejemplo 3.86. Simplifiquemos la expresión racional:
R(x) = (x³ − 49x) / (x³ − 14x² + 49x)
Primero debemos buscar el dominio de validez, y para ello calculamos las raíces del polinomio del denominador x³ − 14x² + 49x aplicando algún caso de factorización, la regla de Ruffini o la fórmula resolvente de Bhaskara.
En este caso nos conviene aplicar el caso de factoreo, factor común:
x³ − 14x² + 49x = x(x² − 14x + 49)
Luego x² − 14x + 49, como es un trinomio al cuadrado perfecto, nos queda:
x² − 14x + 49 = (x − 7)²
Finalmente:
x³ − 14x² + 49x = x(x − 7)² = (x − 0)(x − 7)²
Entonces el dominio de validez es:
Dominio: R − {0, 7}
Ahora factorizamos al polinomio del numerador x³ − 49x; y para ello aplicamos el caso de factoreo, factor común:
x³ − 49x = x(x² − 49)
Luego x² − 49, representa una diferencia de cuadrados, entonces se lo puede expresar:
x² − 49 = (x − 7)(x + 7)
Finalmente
x³ − 49x = x(x − 7)(x + 7)
Luego la expresión racional, al expresar a los polinomios del numerador y del denominador en forma factorizada, nos queda:
R(x) = x(x − 7)(x + 7) / x(x − 7)²
Ahora sí estamos en condiciones de simplificar:
R(x) = x(x − 7)(x + 7) / x(x − 7)²
Entonces la expresión simplificada de R(x) es:
R(x) = (x + 7) / (x − 7)

Ejercicio 3.87. Simplificar las siguientes expresiones racionales, determinando previamente su dominio de validez.

R(x) = (x² − 9) / (x² − 5x + 6)
R(x) = (2x³ + 5x² − 3x) / (x³ + 5x² + 3x − 9)
R(x) = (x³ − x) / (x² − 3x + 2)
R(x) = (3x⁴ + 3x³ − 3x² − 3x) / (x² + x)
Solución:

R(x) = (x + 3) / (x − 2) ; Dominio de Validez: R − {2, 3}
R(x) = 2x / ((x − 1)(x + 3)) ; Dominio de Validez: R − {−3, 1}
R(x) = x(x + 1) / (x − 2) ; Dominio de Validez: R − {1, 2}
R(x) = 3(x − 1)(x + 1) ; Dominio de Validez: R − {−1, 0}]

---

### BLOQUE 4 - TRIGONOMETRÍA
[Estudiaremos en este capítulo una parte de la matemática conocida con el nombre de Trigonometría. En griego, el término trigonon significa triángulo y metron medida, por lo cual la trigonometría se especializa en el estudio de la medida de los triángulos y surge de la necesidad de resolver problemas relacionados con la medición de ángulos y distancias en triángulos y otros polígonos.]

#### Ángulos
[En trigonometría se considera que un ángulo plano se genera por el giro de una semirrecta alrededor de su origen, considerado éste un punto fijo. En la figura se representa el ángulo ∧AOB generado por el giro de orientación positiva (antihorario) de una semirrecta en su posición inicial OA hasta su posición final OB. El punto O se llama vértice del ángulo, la semirrecta OA lado inicial y la semirrecta OB lado final del ángulo.

Un giro con orientación positiva es aquel que se realiza en sentido antihorario, es decir, en el sentido contrario al que se mueven las manecillas del reloj. La orientación negativa de un ángulo, por su parte, es la de un giro realizado en sentido horario.

Como ya se adelantó en la imagen anterior, dado un sistema de coordenadas rectangulares, los ángulos que tienen su vértice en el origen del sistema de coordenadas y el semieje positivo de las x como lado inicial, se dice que están en posición normal o estándar. En estas circunstancias, dos ángulos en posición estándar o normal, uno de medida α y otro de medida β, son ángulos coterminales si y solo si comparten el mismo lado terminal.]

#### Sistemas de medición de ángulos
[Existen dos sistemas que permiten caracterizar la medida o amplitud de un ángulo, el Sistema Sexagesimal y el Sistema Circular o Radial.]

- Sistema Sexagesimal
[Este sistema utiliza como unidad de medida el grado sexagesimal 1°, cuya amplitud se define como la 90-ava parte de un ángulo recto. De lo anterior se deduce que un ángulo recto mide 90°.

Los submúltiplos del grado sexagesimal son:

El minuto sexagesimal, definido por la relación 1° = 60'.
El segundo sexagesimal, dado por 1' = 60''.
Ejemplo 4.1: Supongamos que conocemos la medida de un ángulo, y que la misma es de 13,45°. ¿Cómo podemos expresar esta cantidad en grados, minutos y segundos?

Solución:
13,45° = 13° + 0,45°
Aplicamos la regla de tres para calcular los minutos:
1° = 60'
0,45° = (0,45 * 60) = 27'
Por lo tanto, 13,45° = 13° 27'.

Ejemplo 4.2: Calcular la medida del ángulo α sabiendo que es la tercera parte del ángulo β = 95°.

Solución:
95° / 3 = 31,66°
Ahora, convertimos los 0,66° en minutos:
1° = 60'
0,66° = (0,66 * 60) = 39,6'
Expresamos 39,6' en segundos:
1' = 60''
0,6' = (0,6 * 60) = 36''
Por lo tanto, α = 31° 39' 36''.

Ejercicio 4.3: Expresar en grados, minutos y segundos la medida de los siguientes ángulos:

α = 13,2°
β = 45,52°
θ = 637,96°
γ = 0,96°]

- Sistema Circular o Radial
[Consideremos una circunferencia de radio r y un ángulo ∧AOB con su vértice O en el centro de la circunferencia. En el sistema circular, se define la medida α del ángulo ∧AOB como el cociente entre la longitud L del arco que subtiende el ángulo y la longitud r del radio de la circunferencia, es decir:

α = L / r.

Definición 4.4: Se denomina radián a la medida del ángulo que subtiende un arco L de igual longitud que el radio de la circunferencia r, es decir, si L = r, entonces α = 1 rad. Para indicar que la medida del ángulo está en radianes, se añade la unidad de medida "rad" a continuación del valor del ángulo.

Gráficamente, esto se expresa de la siguiente forma: Dado que el perímetro de un círculo es P = 2πr, donde r es el radio de la circunferencia, si α representa un ángulo completo (es decir, un giro), entonces:

α = 2πr / r = 2π rad.

Esto nos permite realizar las siguientes identificaciones:

2π rad = 360°
π rad = 180°
1/2 π rad = 90°
A partir de estas identidades, podemos pasar de un sistema de medición de ángulos al otro, utilizando la regla de tres.

Ejemplo 4.5:
Calculemos la medida del ángulo β en el sistema radial sabiendo que en el sistema sexagesimal mide β = 60°.

Solución:

Usamos la regla de tres: (180° / π rad) = (60° / x)

Despejando x: x = 60° * (π / 180°) = (60 / 180) * π rad = 1/3 π rad.

Por lo tanto, β = 1/3 π rad.

Si usamos el valor de π:

x = 60° * (π / 180°) = 60 / 180 * π rad ≈ 1.047 rad.

En este caso, β = 1.047 rad, porque usamos el valor de π en la regla de tres y el resultado se expresa en "rad".

Ejemplo 4.6:
Calculemos la medida del ángulo α en el sistema sexagesimal sabiendo que en el sistema radial mide α = 3/4 π rad.

Solución:

Usamos la regla de tres: (π rad / 180°) = (3/4 π rad / x)

Despejando x: x = (3/4 * 180°) = 135°.

Por lo tanto, α = 135°.

Ejercicio 4.7:
Encontrar la medida de los siguientes ángulos en ambos sistemas de medición:

α = 132°
β = 1,9 rad
γ = 45° 31'
δ = 3π rad
Ejercicio 4.8:
Hallar el radio de una circunferencia sabiendo que una longitud de arco L = 24,6 m tiene como ángulo correspondiente uno de 70°.]


#### Funciones trigonométricas
[Definiremos las funciones trigonométricas considerando un punto sobre el lado terminal de un ángulo ubicado en posición estándar. Consideremos en el plano R² un ángulo de medida α (en radianes) en posición estándar y un punto P = (c, b) en el lado terminal de α, a una distancia r > 0 del origen de coordenadas. Quedan definidos entonces los siguientes cocientes:

Puede probarse que los resultados de estos cocientes no dependen de la distancia r del punto P al origen (0; 0), sino que quedan determinados por la medida del ángulo α elegido. Nosotros nos conformaremos con ver un ejemplo de lo antes mencionado.

Calculemos los valores de r usando el Teorema de Pitágoras:

rP = √(3² + 4²) = √25 = 5
rQ = √(6² + 8²) = √100 = 10
Las relaciones entre los lados serían entonces:

4/5 = 8/10
3/5 = 6/10
Es decir, no dependen del punto considerado. Como vemos en el ejemplo, los cocientes considerados no dependen necesariamente de la distancia r del punto considerado al origen de coordenadas. En su lugar, esas relaciones varían en función de α y por eso decimos que son “Funciones de α”.

En base a esas razones, definimos las conocidas Funciones Trigonométricas seno y coseno como sigue:

sin(α) = b / r
cos(α) = c / r
Donde α es la medida en radianes del ángulo considerado y sin(α) y cos(α) son números reales (pues b/r y c/r lo son).

A partir de las anteriores se definen otras cuatro funciones trigonométricas conocidas:

Tangente de α: tan(α) = sin(α) / cos(α) = b / c, siempre que cos(α) ≠ 0 (o c ≠ 0).
Cotangente de α: cot(α) = cos(α) / sin(α) = c / b, siempre que sin(α) ≠ 0 (o b ≠ 0).
Secante de α: sec(α) = 1 / cos(α) = r / c, siempre que cos(α) ≠ 0 (o c ≠ 0).
Cosecante de α: csc(α) = 1 / sin(α) = r / b, siempre que sin(α) ≠ 0 (o b ≠ 0).
Nota 4.9: Dado que r > 0, tenemos las siguientes características de las funciones trigonométricas:

El seno y el coseno de α quedan definidos para todo α ∈ R.
La tangente y la secante de α no están definidas para ángulos cuyos lados terminales estén contenidos en el eje de las y, es decir, ángulos como π/2 rad, 3π/2 rad, 5π/2 rad, etc.
La cotangente y la cosecante de α no están definidas para ángulos cuyos lados terminales estén contenidos en el eje de las x, es decir, ángulos como 0 rad, π rad, 2π rad, 3π rad, etc.]

- La Circunferencia Trigonométrica
[Definición 4.10. Considerando en el plano un sistema de ejes cartesianos, llamaremos circunferencia trigonométrica a la circunferencia de radio 1 y centro en el origen de coordenadas.

Siendo α la medida del ángulo en radianes, considerado en posición estándar, la intersección de la circunferencia trigonométrica con el lado terminal del ángulo determina un punto P cuyas coordenadas son P = (cos(α); sin(α)). Podemos verlo gráficamente de la siguiente manera:

Luego P = (c, b) = (cos(α); sin(α)). La posición del punto P dependerá del ángulo α considerado, pero siempre se encontrará sobre la circunferencia trigonométrica, por lo tanto, la abscisa c y la ordenada b del punto siempre estarán entre -1 y 1, es decir:

-1 ≤ sin(α) ≤ 1
-1 ≤ cos(α) ≤ 1
Dado que las funciones trigonométricas se definieron independientemente del valor r de la distancia entre el origen y el punto P seleccionado sobre el lado terminal del ángulo, podemos establecer r = 1 para trabajar más cómodamente sobre la circunferencia trigonométrica, cuando estemos trabajando con funciones trigonométricas.]

- Signo de las Funciones Trigonométricas
[Como ya se ha mencionado en el capítulo anterior, los ejes coordenados dividen al plano cartesiano en cuatro cuadrantes. Con el objeto de analizar los signos de sin(α) y cos(α) (y por tanto el del resto de las funciones trigonométricas), se pueden observar las coordenadas del punto P para ángulos de medida α con los lados terminales en los cuatro cuadrantes. Veamos gráficamente cómo sería cada caso:

Observando los gráficos se concluye que:

El seno (ordenada del punto P) es un número positivo para los ángulos del primer y del segundo cuadrante y es negativo para ángulos en el tercero y cuarto cuadrante. Asimismo, vemos que sin(α) es nulo cuando α = 0 rad o α = π rad, sin(α) = 1 cuando α = π/2 rad y sin(α) = -1 cuando α = 3π/2 rad.

El coseno (abscisa del punto P) es un número positivo para los ángulos del primer y del cuarto cuadrante y es negativo para ángulos en el segundo y tercer cuadrante. Asimismo, vemos que cos(α) es nulo cuando α = π/2 rad o α = 3π/2 rad, cos(α) = 1 cuando α = 0 rad y cos(α) = -1 cuando α = π rad.

Los signos de las demás razones trigonométricas son consecuencia de los signos de las funciones seno y coseno. Estas conclusiones son válidas también para ángulos de más de un giro (α > 2π rad), solo debemos mirar en qué cuadrante cae el punto P, es decir, en qué cuadrante se intersectan el lado terminal del ángulo con la circunferencia trigonométrica.

Ejercicio 4.11. Calcular el signo de las restantes funciones trigonométricas, a partir de los datos dados en cada caso:

sin(x) > 0 y cos(x) > 0
cos(x) > 0 y tan(x) < 0]


#### Valores de algunos ángulos característicos
[Cálculo de las funciones trigonométricas para algunos ángulos particulares

Ángulo de 0 rad
Al marcar en la circunferencia trigonométrica un ángulo de α = 0 rad, el punto P que resulta de la intersección del lado terminal del ángulo con la circunferencia es el punto P = (1, 0), y por lo tanto:

sin(α) = 0
cos(α) = 1
tan(α) = 0
Ángulo de π/6 rad
Al marcar en la circunferencia trigonométrica un ángulo de α = π/6 rad, podemos marcar un segundo ángulo de igual medida pero orientación contraria. Esto determina un triángulo ΔOPQ tal que OP = OQ = 1, ya que ambos segmentos son radios de la circunferencia. El triángulo es isósceles, y los ángulos en P y Q son iguales. Aplicando el Teorema de Pitágoras, calculamos el valor de sin(π/6):

sin(π/6) = 1/2
Utilizando el Teorema de Pitágoras para calcular cos(π/6):

cos(π/6) = √3/2
Finalmente, calculamos la tangente:

tan(π/6) = (1/2) / (√3/2) = √3/3
Ángulo de π/4 rad
Notemos que en este caso 45° = π/4 rad. Nuevamente, como los ángulos interiores de todo triángulo suman 180°, conociendo los ángulos de 90° y 45° del triángulo rectángulo ΔOPR, podemos calcular el ángulo ∠OPR faltante, que también resulta ser de 45°. Esto nos dice que el triángulo es isósceles y que, por tanto, OR = PR. Como OP = 1 (dado que es el radio de la circunferencia trigonométrica), aplicamos el Teorema de Pitágoras al triángulo en cuestión. Llamemos OR = PR = x, de donde:

1 = x² + x²
1 = 2x²
x² = 1/2
x = √2/2
Por lo tanto:

sin(π/4) = cos(π/4) = √2/2
tan(π/4) = 1
Ángulo de π/3 rad
En este caso, si marcamos un ángulo de π/3 rad = 60°, notamos que el triángulo que queda definido tiene un ángulo de 30° cuyo seno (que se encuentra representado por el cateto opuesto) coincide con el coseno del ángulo de 60°. Análogamente, el coseno del ángulo de 30° está representado por el cateto adyacente, que es el cateto opuesto al ángulo de 60°. Por este motivo:

sin(π/3) = cos(π/6) = √3/2
sin(π/6) = cos(π/3) = 1/2
tan(π/3) = (√3/2) / (1/2) = √3
Ángulo de π/2 rad
Por último, al marcar un ángulo de π/2 rad en nuestra circunferencia trigonométrica, el lado terminal del mismo coincide con el eje de las y, y por lo tanto el punto P será en este caso P = (0, 1). Deducimos lo siguiente:

sin(π/2) = 1
cos(π/2) = 0
tan(π/2) no está definida.
Resumiendo los valores en una tabla:

α	sin(α)	cos(α)	tan(α)
0 rad	0	1	0
π/6 rad	1/2	√3/2	√3/3
π/4 rad	√2/2	√2/2	1
π/3 rad	√3/2	1/2	√3
π/2 rad	1	0	no definida
Nota: Solo calculamos valores para ángulos dados en el primer cuadrante. En el resto de los cuadrantes, los valores se repiten, aunque debemos analizar el signo de las funciones trigonométricas en cada caso.

Ejemplo 4.12. Calculemos el valor de las funciones trigonométricas seno, coseno y tangente para un ángulo de 3π/4 rad.

Solución:
Como vemos, un ángulo de 3π/4 rad = 135° determina un ángulo de 45° en el segundo cuadrante, para el cual conocemos las razones trigonométricas, solo nos falta evaluar el signo de las mismas:

sin(3π/4) = √2/2
cos(3π/4) = -√2/2
tan(3π/4) = -1
Ejercicio 4.13. Calcular el valor de todas las funciones trigonométricas para los siguientes ángulos:

α = 150°
β = 210°
θ = -45°
γ = 315°]


#### Relaciones Fundamentales de la Trigonometría
[En esta sección se incluyen identidades trigonométricas típicas que nos serán de gran utilidad a la hora de resolver problemas.]

- Identidad Pitagórica
[Aplicando el Teorema de Pitágoras al gráfico de la figura tenemos lo siguiente:
1^2 = c^2 + b^2
De donde:
1 = c^2 + b^2
Lo que nos da la identidad trigonométrica:
1 = sin^2(α) + cos^2(α)

Esta identidad, válida para todo ángulo de medida α, es conocida como Identidad Pitagórica.

Observación 4.14:
Notemos que sin^2(α) = (sin(α))^2.

Espero que esta versión en texto plano sea útil. Si necesitas algo más, avísame.]

- Seno y Coseno de la suma o diferencia de ángulos
[Para todos α, β ∈ R, valen las siguientes identidades:

sin(α ± β) = sin(α) cos(β) ± cos(α) sin(β)
cos(α ± β) = cos(α) cos(β) ∓ sin(α) sin(β)

De estas identidades se deducen otras, algunas de las cuales por su frecuente uso enunciamos a continuación.

Relaciones donde intervienen ángulos opuestos
En este caso, tomemos α = 0.
sin(−β) = sin(0 − β)
= sin(0) · cos(β) − cos(0) · sin(β)
= 0 · cos(β) − 1 · sin(β)
= − sin(β)
Luego, sin(−β) = − sin(β).
Análogamente, realicemos los cálculos para probar que
cos(−β) = cos(β)
cos(−β) = cos(0 − β)
= cos(0) · cos(β) + sin(0) · sin(β)
= 1 · cos(β) + 0 · sin(β)
= cos(β)
Luego, cos(−β) = cos(β).

Relaciones para ángulos que difieren en π/2
En este caso, tomemos β = π/2.
sin(α + π/2) = sin(α) · cos(π/2) + sin(π/2) · cos(α)
= sin(α) · 0 + 1 · cos(α)
= cos(α)
Luego, sin(α + π/2) = cos(α).
Análogamente,
cos(α + π/2) = cos(α) · cos(π/2) − sin(π/2) · sin(α)
= cos(α) · 0 − 1 · sin(α)
= − sin(α)
Luego, cos(α + π/2) = − sin(α).

Relaciones donde intervienen ángulos complementarios
sin(π/2 − α) = sin(π/2) · cos(α) − sin(α) · cos(π/2)
= 1 · cos(α) + sin(α) · 0
= cos(α)
Luego, sin(π/2 − α) = cos(α).
De manera análoga,
cos(α − π/2) = cos(α) · cos(π/2) + sin(α) · sin(π/2)
= cos(α) · 0 + sin(α) · 1
= sin(α)
Luego, cos(α − π/2) = sin(α).

Ejemplo 4.15.
Calculemos sin(75°).
sin(75°) = sin(45° + 30°)
= sin(45°) cos(30°) + sin(30°) cos(45°)
= (√2/2) · (√3/2) + (1/2) · (√2/2)
= (√2/2) · (√3/2) + 1/2
= (√2(1 + √3))/4.

Calculemos ahora cos(15°).
cos(15°) = cos(90° − 75°) = sin(75°)
= (√2(1 + √3))/4.

Calculemos finalmente cos(75°).
Por el Teorema de Pitágoras, sin²(75°) + cos²(75°) = 1,
de donde cos²(75°) = 1 − sin²(75°)
= 1 − [(√2(1 + √3))/4]²
= 1 − 2(1 + 2√3 + 3)/16
= 16 − 4√3 − 8/16
= (2 − √3)/4.
Finalmente,
cos(75°) = √(2 − √3)/4 = √(2 − √3)/2.]
 
- Algunas identidades Simpáticas
[Veamos algunos ejemplos interesantes de identidades trigonométricas generales que pueden resultarnos de interés en un futuro cercano.
Identidad: 1 + tan²(x) = sec²(x)
Demostración:
1 + tan²(x) = 1 + sin²(x) / cos²(x) (definición de tangente)
= (cos²(x) + sin²(x)) / cos²(x) (suma de fracciones)
= 1 / cos²(x) (identidad pitagórica)
= sec²(x) (definición de secante)
Resultado: 1 + tan²(x) = sec²(x).

Identidad: 1 − tan²(x) = cos(2x)
Demostración:
cos(2x) / cos²(x)
= cos(x) cos(x) − sin(x) sin(x) / cos²(x) (coseno de la suma de ángulos)
= (cos²(x) − sin²(x)) / cos²(x)
= cos²(x) / cos²(x) − sin²(x) / cos²(x)
= 1 − tan²(x) (definición de tangente)
Resultado: 1 − tan²(x) = cos(2x).

Identidad: sec²(x) − 1 = tan²(x)
Demostración:
sec²(x) − 1 = 1 / cos²(x) − 1
= (1 − cos²(x)) / cos²(x)
= sin²(x) / cos²(x)
= tan²(x)
Resultado: sec²(x) − 1 = tan²(x).]


#### Periodicidad de las Funciones Trigonométricas
[En la naturaleza y en nuestro entorno habitual hay fenómenos que se repiten a intervalos regulares de tiempo, como el caso de las mareas, los péndulos, entre otras. Las funciones que describen este tipo de fenómenos se conocen con el nombre de funciones periódicas. En estos casos se llama periodo al menor lapso de tiempo que debe transcurrir para que el fenómeno comience a repetirse.

Definición 4.16. Dada una función no constante f : R → R se dice que f es periódica cuando existe un número real p ≠ 0 para el cual se verifica: f(x) = f(x + kp) ∀x ∈ R, k ∈ Z El periodo de la función es el menor número positivo p para el que se cumple la igualdad.

Dado un ángulo cualquiera α ∈ R y sus ángulos coterminales α + 2kπ con k ∈ Z, las funciones trigonométricas satisfacen:

sin(α) = sin(α + 2kπ)
cos(α) = cos(α + 2kπ)
sec(α) = sec(α + 2kπ)
csc(α) = csc(α + 2kπ)

Funciones de periodo 2π:

tan(α) = tan(α + kπ)
cot(α) = cot(α + kπ)

Funciones de periodo π.

Este concepto es fundamental a la hora de realizar los gráficos de las funciones trigonométricas, pues nos dice que solo necesitamos conocer con exactitud el gráfico de las mismas en un periodo completo, por ejemplo en [0; 2π] en el caso de la función f(x) = sin(x), y luego la extenderemos por simple repetición fuera de dicho intervalo.]


#### Gráfico de las Funciones Seno y Coseno
[En esta sección analizaremos el gráfico de las funciones seno y coseno, definidas por las fórmulas:

f : R → R, f(x) = sin(x)
g : R → R, g(x) = cos(x)

ambas en un período completo, es decir, con x ∈ [0; 2π], y luego extenderemos el gráfico para cualquier x ∈ R. Daremos inicio a la sección de gráficos con la gráfica de la función seno, sin embargo, antes de comenzar notemos que es necesario usar dos sistemas de ejes coordenados con igual escala. En uno de ellos representaremos la circunferencia trigonométrica y en el segundo iremos marcando los valores del sin(x) para cada medida x del ángulo elegido. En síntesis, la gráfica se construye tomando diferentes valores de ángulos sobre la circunferencia trigonométrica y hallando el seno de ellos que ya vimos que está representado por el valor de la ordenada del punto P ubicado sobre la circunferencia trigonométrica. Asimismo estuvimos trabajando la deducción del seno de muchos ángulos notables y nos podemos servir de ellos para realizar la representación gráfica de la función seno.

De la gráfica se pueden sacar algunas conclusiones tales como que el dominio de la función seno es el conjunto de todos los números reales y la imagen de la función son los números comprendidos entre −1 y 1, es decir, el conjunto [−1; 1].

Conocida ya la gráfica de la Función Seno, nos concentraremos ahora en conocer la gráfica de la Función Coseno. Para ello, debemos recordar una identidad trigonométrica vista con anterioridad:

cos(x) = sin(x + π/2)

y entonces si aplicamos esta identidad resulta:

g(x) = cos(x) = sin(x + π/2)

lo que indica que su gráfica será igual a la gráfica del seno pero desplazada π/2 unidades hacia la izquierda.]


#### Ecuaciones Trigonométricas
[En esta sección de trigonometría aprenderemos a resolver ecuaciones trigonométricas.

Definición 4.17. Una ecuación trigonométrica es aquella en la que las incógnitas aparecen formando parte de los argumentos de funciones trigonométricas.
Al igual que en las ecuaciones algebraicas, mediante ecuaciones equivalentes se llegará a una nueva expresión en la cual el valor que la satisface es evidente.

Veamos algunos ejemplos ilustrativos.

Ejemplo 4.18. Resolvamos las siguientes ecuaciones trigonométricas en el intervalo [0, 2π].

✓ 2 sin(x) − √2 = 0
Solución:
2 sin(x) − √2 = 0
2 sin(x) = √2
sin(x) = √2/2
Luego, mirando la tabla de valores de sin(x), notamos que, para que sin(x) = √2/2, necesitamos que x = π/4 rad o bien x = 3π/4 rad.
Luego, la solución será S = {π/4 rad, 3π/4 rad}

✓ tan²(x) − 1 = 0
Solución:
tan²(x) − 1 = 0
tan²(x) = 1
tan(x) = ±√1
tan(x) = 1 → x = π/4 o x = 5π/4
tan(x) = −1 → x = 3π/4 o x = 7π/4
Mirando la tabla de valores, notamos que, para que tan(x) = 1, necesitamos que x = π/4 rad o bien x = 5π/4 rad; en cambio, para que tan(x) = −1, notamos que x = 3π/4 rad o bien x = 7π/4 rad.
Luego, la solución será S = {π/4 rad, 3π/4 rad, 5π/4 rad, 7π/4 rad}

✓ cos(x) + sin(2x) = 0
cos(x) + sin(2x) = 0
cos(x) + sin(x) cos(x) + cos(x) sin(x) = 0
cos(x) + 2 sin(x) cos(x) = 0
cos(x) [1 + 2 sin(x)] = 0
De lo anterior se deduce que
cos(x) = 0 o bien 1 + 2 sin(x) = 0
Luego,
x = π/2 rad
x = 3π/2 rad
x = 7π/6 rad
x = 11π/6 rad
La solución será entonces: S = {π/6 rad, 3π/2 rad, 5π/6 rad, 11π/6 rad}
Ejercicio 4.19. Resolver las siguientes ecuaciones trigonométricas, con x ∈ [0; 2π]

a) cos(x) = 0
Solución:
S = {π/2, 3π/2}

b) 2 sin(2x) − 1 = 0
Solución:
S = {π/12, 5π/12, 13π/12, 17π/12}

c) − sin²(x) + 2 cos(x) = −2
Solución:
S = {π}]


#### Relaciones entre los lados y ángulos de un triángulo rectángulo
[Un triángulo rectángulo es aquel que posee un ángulo recto, por ejemplo, todo ángulo en posición estándar cuyo lado terminal se encuentra en el primer cuadrante genera un triángulo rectángulo como se ve en el ejemplo de la figura, donde el ángulo recto es aquel que tiene su vértice en el punto M.
Para analizar los ángulos de un triángulo rectángulo, por ejemplo, el ángulo ∧ MOP de medida α coloquemos al mismo en posición estándar, añadiendo un sistema de ejes coordenados en el vértice del ángulo a analizar. Luego, y de acuerdo a lo antes definido tenemos las siguientes razones:

sin(α) = b/r = longitud del cateto opuesto / hipotenusa
cos(α) = c/r = longitud del cateto adyacente / hipotenusa
tan(α) = b/c = longitud del cateto opuesto / longitud del cateto adyacente

A partir de las anteriores definimos:
csc(α) = r/b = hipotenusa / longitud del cateto opuesto
sec(α) = r/c = hipotenusa / longitud del cateto adyacente
cot(α) = c/b = longitud del cateto adyacente / longitud del cateto opuesto]


#### Resolviendo triángulos rectángulos
[Resolver un triángulo rectángulo significa, como ya lo mencionamos con anterioridad, hallar las medidas de todos sus ángulos y lados. Cuando se dan como dato un conjunto suficiente de esas medidas es posible encontrar las restantes. Para ello debemos conocer conceptos previos, algunos de ellos los hemos desarrollado en las secciones anteriores y otros los veremos a continuación. Entre los más usados se encuentran:

✓ Funciones trigonométricas
✓ Teorema de Pitágoras
✓ La conocida propiedad: La suma de los ángulos interiores de un triángulo es 180°
✓ Los Teoremas de Seno y de Coseno.

De los ítems anteriores hemos visto la mayoría, sólo nos resta enunciar los Teoremas de Seno y de Coseno, cosa que haremos en la inmediatez.

Para resolver un triángulo son necesarios al menos tres datos entre los cuales debe hallarse al menos un lado. Si el triángulo a resolver es rectángulo, uno de los datos es el valor del ángulo recto el cual mide 90° que se opone al lado de mayor longitud, llamado hipotenusa. En los triángulos rectángulos basta entonces con conocer dos datos más. Recordemos que en este tipo de figuras geométricas podemos hacer uso de las razones trigonométricas antes vistas.

Por otro lado, para el caso de un triángulo no rectángulo, en el cual las razones trigonométricas no son aplicables, se recurre a los antes mencionados Teorema de Seno y Coseno, que enunciaremos a continuación:

Teorema del Seno:
a/sin(α) = b/sin(β) = c/sin(γ)

Teorema del Coseno:
a² = b² + c² − 2·b·c·cos(α)

Ejemplo 4.20. Obtengamos las longitudes de los catetos de un triángulo rectángulo cuya hipotenusa mide 5 cm si uno de sus ángulos agudos mide 60°. ¿Cuánto mide el otro ángulo agudo?
Solución:
Lo primero que debemos hacer es un dibujo que represente la situación problemática para poder visualizar los datos que tenemos y aquellos que nos faltan.
De acuerdo a los datos dados uno de los ángulos agudos mide 60°, como el triángulo es rectángulo el ángulo agudo faltante es aquel que sumado a los dados suma 180°, luego β = 180° − 90° − 60° = 30°.
Calculemos ahora los lados del triángulo haciendo uso de las razones trigonométricas antes vistas.

cos(60°) = x / 5 cm ⇒ x = cos(60°) · 5 cm = 5 / 2 cm
sin(60°) = y / 5 cm ⇒ y = sin(60°) · 5 cm = √3 / 2 · 5 cm

Luego hemos resuelto el triángulo dado, es decir, conocemos todos sus lados y ángulos.

Ejemplo 4.21. ¿Qué longitud tiene una escalera si al apoyar su extremo superior sobre una pared a perfecta escuadra, la base queda a dos metros de la pared y forma un ángulo de 60° con el suelo?
Solución:
Lo primero que debemos hacer en cada problema que se nos presente, es un dibujo que represente la situación.
Como vemos en la representación, hemos llamado x a la longitud de la escalera y ubicado los datos correspondientes en el dibujo realizado. En nuestro esquema tenemos el lado adyacente al ángulo conocido y queremos calcular la hipotenusa. La razón trigonométrica a aplicar en este triángulo rectángulo es el coseno pues relaciona los tres datos que tenemos.
cos(60°) = 2m / x ⇒ x = 2m / cos(60°) = 2m / 1/2 ⇒ x = 4m

Luego, la longitud de la escalera es de 4 m.

Ejemplo 4.22. Calculemos la ecuación de una recta si se sabe que pasa por el punto (0, 0) y forma un ángulo de 45° con el semieje positivo de las x.
Solución:
Realizamos en primer lugar el gráfico de una recta que cumple con los datos dados en el ejercicio, es decir que la misma pasa por el origen y forma un ángulo de 45° con el semieje positivo de las x.
Tomemos un punto P = (x; y) sobre la recta, entonces queda determinado el triángulo rectángulo △P Ox, con O representando el origen de coordenadas. Así, la relación que puede establecerse entre ambas variables para determinar la ecuación de la recta viene dada por la tangente del ángulo conocido, es decir:
tan(45°) = y / x ⇒ y = tan(45°) · x ⇒ y = x

Luego la ecuación de la recta es y = x.
Notemos que la tangente del ángulo sólo me da la inclinación, es decir, la pendiente de la recta, pues es el desplazamiento horizontal y vertical de la misma, pero como además la recta pasa por el origen entonces la ordenada al origen es 0.

Ejemplo 4.23. Dos casas se hallan separadas por una laguna. ¿A qué distancia se encuentran una de la otra si al observarlas desde un galpón ubicado a 1500 m de una y a 800 m de la otra, las visuales forman un ángulo de 70°?
Solución:
Lo primero que debemos notar es que el triángulo no es necesariamente rectángulo y que por lo tanto no podemos aplicar las razones trigonométricas, sino que debemos hacer uso de los Teoremas de Seno y Coseno.
Para ello, observemos lo siguiente:
Los datos dados se corresponden con dos lados y el ángulo que ellos forman, y el dato que debemos encontrar es el lado restante. Estamos en las condiciones de aplicar el Teorema de Coseno (aunque claramente cualquiera de los dos teoremas nos llevaría, tarde o temprano, a un resultado). Llamemos H a la distancia entre ambas casas de donde tenemos:
H² = 1500² + 800² − 2·1500·800·cos(70°)
H = √2069151,656
H = 1438,454

Ejercicio 4.24. La sombra de un árbol mide 50 m y el ángulo que forman los rayos del sol con el suelo es de 45°. ¿Cuál es la altura del árbol?
Solución: el árbol mide 50 m.

Ejercicio 4.25. Resolver el siguiente triángulo rectángulo sabiendo que uno de sus ángulos mide 30° y que la altura correspondiente a la hipotenusa mide 2 cm. Calcular además su área y perímetro.

Ejercicio 4.26. Una antena que se encuentra a la orilla de un río tiene una altura de 30 m sobre el nivel del agua. Desde un punto opuesto (al mismo nivel pero en la otra orilla) se observa la parte más alta de la antena con un ángulo de elevación de 30°. ¿Cuál es el ancho del río?

Ejercicio 4.27. En un terreno horizontal se divisa una torre desde un punto A bajo un ángulo de 30°. Al aproximarse 20 m se llega a un punto B, desde el que se observa la torre bajo un ángulo de 45°. Calcular la altura de la torre.
Solución: la torre mide aproximadamente 27,3 m.

Ejercicio 4.28. Los brazos de un compás, que miden 12 cm, forman un ángulo de 50°. ¿Cuál es el radio de la circunferencia que puede trazarse con esa abertura?
Solución: el radio de la circunferencia será aproximadamente de 10,14 cm.]

