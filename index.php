<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta de Productos</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&family=Pacifico&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@300..700&display=swap');

        body {
            background-image: url(descarga.jpg);
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
            margin: 0; /* Para eliminar el margen predeterminado */
            padding: 0; /* Para eliminar el relleno predeterminado */
            height: 100vh; /* Altura completa de la ventana */
            display: flex;
            justify-content: center; /* Centrar horizontalmente */
            align-items: flex-start; /* Centrar verticalmente en la parte superior */
        }

        .table-container {
            margin-top: 50px; /* Espacio adicional en la parte superior */
        }

        .table {
            font-family: "Comfortaa";
            font-weight: 400;
            font-style: normal;
            color: aliceblue;
            text-align: center;
        }

        .pacifico-regular {
            font-family: "Dancing Script";
            font-weight: 400;
            font-style: normal;
            color: aliceblue;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="table-container">
    <h1 class="pacifico-regular">Top Vendas de Juegos</h1>
    <table class="table" border="1">
        <tr>
            <th>ID</th>
            <th>Nombre del juego</th>
            <th>Precio</th>
            <th>Ventas</th>
        </tr>
        <?php
        include 'funciones.php';

        $productos = obtenerProductos();

        foreach ($productos as $producto) {
            echo "<tr>";
            echo "<td>" . $producto['id'] . "</td>";
            echo "<td>" . $producto['nombre'] . "</td>";
            echo "<td>" . $producto['precio'] . "</td>";
            echo "<td>" . $producto['cant_des'] . "</td>";
            echo "</tr>";
        }
        ?>
    </table>
</div>

</body>
</html>
