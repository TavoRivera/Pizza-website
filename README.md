# Project 3

Web Programming with Python and JavaScript

Project 3 - Pizza - django

Para empezar tenemos la pagina de registro, donde puedes ingresar datos de un usuario para que pueda entrar a la pagina, haciendo uso 
de django.contrib.auth para crear usuario, hacer login, logout y autenticación.

En la pagina de inicio se muestra el menú. Para la elaboracion de este menú se realizaron los siguientes modelos: 

- Size: Puede ingresar el tamaño de la porcion de la orden
- Type: Se clasifican las ordenes en un tipo específico, como pizzas, fritangas, etc.
- Topping: Se registran la lista de toppings que se podrían agregar a las pizzas regulares
- Inventory: Es donde se almacena cada orden de comida a venderse, en él se coloca un nombre, una imagen del platillo en la base de datos, comentarios, etc.
- ItemCost: Establece los precios para todas las ordenes segun su tamaño
- ToppingCount: Para las pizzas con toppings, almacea el precio para las pizzas que tienen uno, dos hasta tres toppings.
- Orderr: Funciona para el carrito, donde todos los items que enviamos desde el menú los almacena por cantidad, el precio de cad item, el precio total y el usuario específico que está haciendo las peticiones.
- Completed_Order_Ids: Una vez se genere la orden desde cart, esta tabla almacenará informacion de la solicitud del usuario, su nombre y el monto total, y un campo que dice Iniciado, Rechazado y Completado para que el admin de la pagina pueda confirmar su pedido.

Para que desde la base de datos mostrara las imagenes que se pueden subir, en settings en la parte de static se han agregado un par de lineas para que estas imagenes pudieran cargar.

En la parte de frontend se ha utilizado bootstrap para hacer las animaciones con el modal y un poco de js para habilitar y deshabilitar los checkbox para que un usuario no pueda seleccionar mas de tres toppings (porque hasta 3 muestra el menú de PinocchiosPizza). Además de establecer un limite en los pedidos que no exceda a mas de 10 de cada producto, mostrando ua notificacion al usuario.

En views quizás lo mas interesante sea add_to_cart, que del modal del menú extrae la informacion de la solicitud que hicimos y de acuerdo al tamaño del platillo seleccionado, ubica el precio de este, si se agrega toppings, cuenta la cantidad de toppings agregados, eso si el producto es personalizable, y de acuerdo a la cantidad de toppings ubica el precio, ya que el precio de la pizza aumenta si se seleccionan uno o mas toppings. Finalmete con la cantidad y el precio del producto se calcula el total y se almacena en la tabla Orderr, agregandose al carrito.
