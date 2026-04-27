print("Bienvenido a Pizzeria Bella Napoli!!")
opcion = int(input("Desea ordenar 1) Pizza Vegetariana o 2) Pizza No Vegetariana ? \n "))

match opcion:
    case 1:
        tipopizza = "Pizza Vegetariana"
        ingredientes = input ("Que ingredientes le desea agregar? |'Pimiento' | 'Tofu' | 'Ambos' \n ").lower() # .lower() Es una funcion que se suele utilizar para no generar conflicto con las mayusculas o minusculas al comparar!
        match ingredientes:
            case "pimiento":
                ingredientes = "Pimiento"
            case "tofu":
                ingredientes = "Tofu"
            case "ambos":
                ingredientes = "Pimiento y Tofu"
            case _:
                ingredientes = "Sin condimentos"
    case 2:
        tipopizza = "Pizza No Vegetariana"
        ingredientes = input ("Que ingredientes le desea agregar? |'Peperoni' | 'Jamon' | 'Salmon' | 'Peperoni y Jamon' | Peperoni y Salmon \n").lower()
        match ingredientes:
            case "peperoni":
                ingredientes = "Peperoni"
            case "jamon":
                ingredientes = "Jamon"
            case "salmon":
                ingredientes = "Salmon"
            case "peperoni y jamon":
                ingredientes = "Peperoni y Jamon"
            case "peperoni y salmon":
                ingredientes = "Peperoni y Salmon"
            case _:
                ingredientes = "Sin Condimentos"
mensaje = f'Su pedido esta listo , Usted ordeno:\n \
Pizza: {tipopizza} \n \
Su pedido esta listo , Usted ordeno: \n \
Ingredientes: {ingredientes}\n\
En 15 , 20 min estara listo para retirar , gracias!!    '
