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

En views las rutas más destacadas son add_to_cart, que según la solicitud realizada ubica el precio del platillo o los platillos, y ya con los precios definidos, la cantidad y los toppings agregados (si acaso los hay) se almacenará en la tabla Orderr, los datos se almacenarán de acuerdo a cada usuario, por lo cual, cuando un usuario visite a su carrito, solo podrá ver sus solicitudes, esto lo hace la función cart.

Luego, con la función delete_item() será posible eliminar un articulo del carrito según el usuario.

Posteriormente el usuario podrá confirmar su pedido en confirm_order(), donde los datos de la orden se almacenarán en otra tabla llamada completed_orders, y al confirmar ese pedido se eliminarán esos artículos del carrito de compras.

El usuario podrá visualizar sus pedidos en la página My Orders (únicamentesus pedidos y no el de otra persona), y podrá ver su estado, si se ha iniciado la orden o si se ha completado.

Como toque personal, se ha implementado que para el administrador de la página, en la misma página de my orders, si el usuario es staff pueda marcar como completadas las órdenes de cualquier usuario y que se oculten las órdenes una vez se marquen como completadas.
