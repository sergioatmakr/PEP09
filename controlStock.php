<?php
// Parámetros de conexión (ejemplo)
$mysqli = new mysqli("localhost", "usuario", "password", "basedatos");

$id_producto = 123;
$cantidad_vender = 5;

// 1. Consultar stock actual
$query = "SELECT stock_actual FROM productos WHERE id_producto = ?";
$stmt = $mysqli->prepare($query);
$stmt->bind_param("i", $id_producto);
$stmt->execute();
$stmt->bind_result($stock_actual);
$stmt->fetch();
$stmt->close();

// 2. Verificar stock suficiente
if ($stock_actual >= $cantidad_vender) {
    // 3. Actualizar stock y registrar movimiento en transacción
    $mysqli->begin_transaction();

    try {
        // Actualizar stock
        $update = "UPDATE productos SET stock_actual = stock_actual - ? WHERE id_producto = ?";
        $stmt = $mysqli->prepare($update);
        $stmt->bind_param("ii", $cantidad_vender, $id_producto);
        $stmt->execute();
        $stmt->close();

        // Insertar movimiento
        $insert = "INSERT INTO movimientos_stock (id_producto, cantidad, tipo_movimiento, fecha_movimiento) VALUES (?, ?, 'salida', NOW())";
        $stmt = $mysqli->prepare($insert);
        $cantidad_negativa = -$cantidad_vender;
        $stmt->bind_param("ii", $id_producto, $cantidad_negativa);
        $stmt->execute();
        $stmt->close();

        $mysqli->commit();
        echo "Venta realizada correctamente.";
    } catch (Exception $e) {
        $mysqli->rollback();
        echo "Error en la venta: " . $e->getMessage();
    }
} else {
    // 4. No hay stock suficiente
    echo "No hay suficiente stock para realizar la venta.";
}

$mysqli->close();
?>
