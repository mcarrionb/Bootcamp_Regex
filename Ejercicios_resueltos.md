# Ejercicios de regex

## Ejercicio 1
He seleccionado los números del principio de cada línea y al final de estos he añadido el parentesis.
```
^(\d+)
```


![alt text](img/ex1.png)

## Ejercicio 2
He seleccionado cada grupo de espacios y los he sustituido por un solo espacio.
```
\s+
```

![alt text](img/ex2.png)

#### Ampliación
Otra forma que he encontrado ha sido mediante las tabulaciones horizontales.
```
[\t ]+
```

![alt text](img/ex2-2.png)

## Ejercicio 3
He buscado la cadena de carácteres entre el @ y el .cl / .cl y la he sustituido por gmail.
```
@[\w.-]+(\.cl|\.ch)
```

![alt text](img/ex3.png)

#### Ampliación
He utilizado el lookahead en el regex del apartado anterior y así al hacer la sustitución no necesito referenciar a .cl/.ch.
```
@[\w.-]+(?=\.cl|\.ch)
```

![alt text](img/ex3-2.png)

## Ejercicio 4
He dividido la expresión en tres grupos. El primer grupo captura todo el contenido a la izquierda del correo electrónico, el segundo grupo contiene el propio correo electrónico, y el tercer grupo recoge todos los caracteres a la derecha del correo. Finalmente, he sustituido toda la línea solo por el email.

```
(.*\s)([\w._-]+@[\w-]+.[\w.]+)(.*)
```

![alt text](img/ex4.png)

## Ejercicio 5
Primero he sustituido los espacios en blanco por punto y coma. A continuación, he añadido el punto y coma al final de todas las líneas que no lo tenían.
![alt text](img/ex5-1.png)
![alt text](img/ex5-2.png)