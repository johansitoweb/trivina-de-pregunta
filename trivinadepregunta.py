def trivia():  
    preguntas = {  
        "¿Cuál es la capital de Francia?": "paris",  
        "¿Cuál es el océano más grande del mundo?": "pacifico",  
        "¿Qué lengua se habla en Brasil?": "portugues",  
        "¿Quién escribió 'Cien años de soledad'?": "gabriel garcia marquez",  
        "¿Cuál es el planeta más cercano al sol?": "mercurio"  
    }  

    print("¡Bienvenido a la Trivia! Responde las preguntas a continuación.")  
    
    puntuacion = 0  

    for pregunta, respuesta_correcta in preguntas.items():  
        respuesta_usuario = input(pregunta + " ").lower()  
        if respuesta_usuario == respuesta_correcta:  
            print("¡Correcto!")  
            puntuacion += 1  
        else:  
            print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")  

    print(f"Tu puntuación: {puntuacion}/{len(preguntas)}")  

# Ejecuta el juego  
trivia()