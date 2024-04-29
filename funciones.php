<?php

// Función para conectarse a la base de datos
function conectarDB() {
    $host = 'localhost';
    $usuario = 'root';
    $contraseña = '';
    $nombre_base_de_datos = 'tienda';

    $conexion = new mysqli($host, $usuario, $contraseña, $nombre_base_de_datos);

    if ($conexion->connect_error) {
        die("Error de conexión: " . $conexion->connect_error);
    }

    return $conexion;
}

// Función para obtener los registros de la tabla productos
function obtenerProductos() {
    $conexion = conectarDB();

    $query = "SELECT id, nombre, precio FROM productos";
    $resultado = $conexion->query($query);

    $productos = array();

    if ($resultado->num_rows > 0) {
        while ($fila = $resultado->fetch_assoc()) {
            $productos[] = $fila;
        }
    }

    $conexion->close();

    return $productos;
}

?>
