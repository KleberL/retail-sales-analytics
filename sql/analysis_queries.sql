-- Ventas y unidades por ciudad

SELECT
    ciudad,
    SUM(unidades) AS unidades_totales,
    SUM(venta_total) AS venta_total
FROM sales
GROUP BY ciudad
ORDER BY venta_total DESC;

-- Rendimiento por producto

SELECT
    producto,
    SUM(unidades) AS unidades_totales,
    SUM(venta_total) AS venta_total,
    ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio
FROM sales
GROUP BY producto
ORDER BY venta_total DESC;