
# se define los personajes.
define g = Character('Galex', color="#c6ffc7")
define n= Character ('Nova', color="#c4ffc9")
define p= Character ('Pez', color="#c8ffc9")
define m= Character ('Voz Misteriosa', color="#c5ffc3")

# The game starts here.
label start:
    
    play music "goofish.mp3" loop
    
    #se asignan las imagenes de los personajes, las dibujamos nosotros

    image muelle = "muelle.png"
    image muelle1 = "muelle1.png"
    image pezlibre = "pezlibre.png"
    image pez = "pez.png"
    image galek close up = "galek close up.png"
    image blanco2 = "blanco2.jpeg"
    image galekmuerto = "galekmuerto.png"
    image galektriste = "galektriste.png"
    image encuentro1 = "encuentro1.png"
    image damepez = "damepez.png"
    image kameha = "kameha.png"
    image muahaha= "muahaha.png"
    image falcon = "falcon.png"
    image hadouken = "hadouken.png"
    image perdi = "perdi.png"
    image lost = "lost.png"
    
    #comenzamos la historia
    
    scene blanco2
    show muelle1 at center
    #utilizamos esta variable para guiar el camino de la historia
    $ eleccion = 0
    
    #comenzamos la conversacion
    m "En un mundo bidimensional donde los seres vivientes son conocidos como stickmans"
 
    m "Uno de ellos estaba pescando tranquilamente"
    
    hide muelle1
    scene blanco2
    with dissolve
    show galek close up
    g "Woooooow que divertido es pescar"
    
    hide galek close up
    show muelle at center
    
    
    m "Cuando de repente"
    
    hide muelle
    show pez
    g "Un pescado ha picado!"
    p "Dejame ir porfavor!"
    
    
    #Desplegamos menu para que el usuario tome decisiones y dependiendo de ello cambiamos el valor de eleccion
    menu:
        "Galex hace su mejor esfuerzo y logra atrapar el pescado.":
            $eleccion=1
        "Galex se emociona demasiado y deja escapar al pez.":
           $eleccion=2
    #Utilizamos un if para cambiar la historia dependiendo del valor de eleccion
    
    if eleccion==1:
        hide muelle
        show pez at center
       
        g "Oh si tengo un lindo pescadito."
        p" Te odiooo!"
        hide pez
        show encuentro1
        play music "thief.mp3" loop
        "Un extraño bien mamado se acerca hacia Galex"
        
        hide encuentro1
        show damepez
        n "Hey niño dame ese pescado"
        
        menu:
            "Esta bien":
                $eleccion=3
            "No este es mi pescado!":
                $eleccion=4
        if eleccion==3:
            hide damepez
            play music "End.mp3" loop
            show galektriste
            g "Un ladron de pescados mamado y calvo me acaba de robar!"
            g "Tendre que volver a pescar..."
            g "Fin."
          
        if eleccion==4:
            
            n "Pues pelea por el!"
            
            menu:
                "Usa el kamehameha":
                    show kameha
                    g "AGGH!!"
                    hide kameha
                    hide damepez
                    show lost
                    n " He perdido!...."
                    n " Sos muy poderoso!"
                    hide lost
                    play music "goofish.mp3" loop
                    show galek close up
                    m " Y siguio pescando tranquilo."
                    m "Fin."
            
                "Falcon Punch":
                    $eleccion=5
                        
                "Usa Hadouken":
                    $eleccion=6
                    
        if eleccion==5:
            hide damepez
            show falcon
            g "Faaaaaaaaalcon Puuunch!"
            hide falcon
            show muahaha
            n "HAA!"
            n "Tu debil puño me da risa!"
            n "He ganado! Inutil pescador inservible!..."
            hide muahaha
            show perdi
            m "Fin."
        
        if eleccion==6:
            hide damepez
            show hadouken
            g "Hadouuuken!"
            hide hadouken
            show muahaha
            n "HAA!"
            n "Eso no me afecta a mis musculos, ni a mi calvicie!"
            n "He ganado! Inutil pescador inservible!..."
            hide muahaha
            show perdi
            m "Fin."
          
    if eleccion==2:
        hide pez
        show pezlibre at center
        g "Oh no mi pescado. Se ha escapado!"
        p" SII!, SOY LIBRE!"
        hide pezlibre
        play music "End.mp3" loop
        show galektriste
        g "La desgracia de perder este pescado me vuelve muy triste!"
        g "Creo que esto me esta afectando mucho! oh no..."
        show galekmuerto
        m "La vergueza de perder el pescado hizo que Galex tuviera un ataque al corazon... RIP"
        m "FIN"
        
        
        
           
    return
 