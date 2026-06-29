FPY1101-videojuego

Videojuego de texto; Adivina personajes animados usando pistas (Pistas, Vidas, Puntos, Ranking).

El Sombrero de las Adivinanzas
Videojuego de texto en Python donde un sombrero magico elige un personaje animado en secreto y el jugador debe adivinar quien es usando pistas progresivas. El juego permite acumular puntos, ganar vidas y competir en un ranking guardado automaticamente.


Funcionalidades

Este proyecto incluye las siguientes funcionalidades:


Jugar: El sombrero elige un personaje al azar y entrega hasta 3 pistas para que el jugador lo adivine.
Sistema de vidas: El jugador empieza con 3 vidas, pierde una si falla y gana una si acierta.
Sistema de puntos: Segun en que pista adivinas, ganas 300, 200 o 100 puntos.
Recompensas: Al superar ciertos puntajes se desbloquean titulos especiales.
Ranking: Guarda y muestra el puntaje de cada jugador usando un archivo CSV.


Requisitos Tecnicos Aplicados


Uso de listas y diccionarios para almacenar personajes y puntajes.
Uso de funciones para cada parte del juego (jugar, mostrar menu, validar, guardar).
Uso de estructuras de control ( if, for, while ).
Validacion de datos ingresados por el usuario.
Validacion de nombre y opciones del menu.
Manejo de excepciones mediante try/except.
Persistencia de datos con archivo CSV para guardar el ranking entre partidas.
Uso de randint para elegir personajes al azar.
Uso de os.system("cls") para limpiar la pantalla
