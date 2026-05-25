-- ============================================
-- EXPLORACIÓN DATASET BURNOUT
-- Fuente: Kaggle - Digital Burnout & Productivity Analytics
-- 10.000 registros / dataset sintético
-- ============================================

-- Consulta 1: Distribución por nivel de burnout
-- Hallazgo: 52% nivel medio, 26% bajo, 21% alto
SELECT burnout_risk, COUNT(*) as total
FROM small_bournout
GROUP BY burnout_risk
ORDER BY total DESC


-- Consulta 2: Burnout por modo de trabajo
-- Hallazgo: sin diferencia entre remoto, híbrido y presencial (21% alto en los tres)
SELECT 
    CASE 
        WHEN burnout_risk <= 33 THEN 'Bajo'
        WHEN burnout_risk <= 66 THEN 'Medio'
        ELSE 'Alto'
    END AS nivel_burnout,
    COUNT(*) as total
FROM small_bournout
GROUP BY 
    CASE 
        WHEN burnout_risk <= 33 THEN 'Bajo'
        WHEN burnout_risk <= 66 THEN 'Medio'
        ELSE 'Alto'
    END
ORDER BY total DESC

-- Consulta 3: Burnout por uso de pantalla
-- Hallazgo: 99% tiene alto uso (>12hs). Promedio burnout alto uso: 48.3 vs moderado: 32
SELECT 
    work_mode,
    CASE 
        WHEN burnout_risk <= 33 THEN 'Bajo'
        WHEN burnout_risk <= 66 THEN 'Medio'
        ELSE 'Alto'
    END AS nivel_burnout,
    COUNT(*) as total
FROM small_bournout
GROUP BY 
    work_mode,
    CASE 
        WHEN burnout_risk <= 33 THEN 'Bajo'
        WHEN burnout_risk <= 66 THEN 'Medio'
        ELSE 'Alto'
    END
ORDER BY work_mode, total DESC

-- Análisis de descanso:el dataset tiene el nro multiplicado por 10 en filas, 
-- teniendo en cuenta esto, se analiza:

SELECT 
    CASE 
        WHEN sleep_hours < 60 THEN 'Poco (menos de 6hs)'
        WHEN sleep_hours <= 80 THEN 'Normal (6 a 8hs)'
        ELSE 'Mucho (más de 8hs)'
    END AS categoria_sueno,
    ROUND(AVG(CAST(burnout_risk AS float)), 1) AS promedio_burnout,
    COUNT(*) AS total
FROM small_bournout
WHERE sleep_hours IS NOT NULL
GROUP BY 
    CASE 
        WHEN sleep_hours < 60 THEN 'Poco (menos de 6hs)'
        WHEN sleep_hours <= 80 THEN 'Normal (6 a 8hs)'
        ELSE 'Mucho (más de 8hs)'
    END
ORDER BY promedio_burnout DESC

-- análisis del riesgo de burnout por nivel de strees
-- Hallazgo: A medida que el nivel de strees aumenta, el riesgo de burnout también tiende a aumentar, 
-- lo que sugiere una correlación positiva entre ambos factores. 
-- Este hallazgo destaca la importancia de gestionar el stress para reducir el riesgo de burnout en los individuos.
SELECT 
    stress_level,
    ROUND(AVG(CAST(burnout_risk AS float)), 1) AS promedio_burnout,
    COUNT(*) AS total
FROM small_bournout
GROUP BY stress_level
ORDER BY stress_level

-- ahora analizamos el riesgo de burnout por fatiga mental:
-- Hallazgo: en este caso no ocurre lo mismo, ya que el promedio oscila entre 47 y 49 en todos
-- los niveles de fatiga mental, lo que sugiere que no hay una correlación clara entre la fatiga
-- mental y el riesgo de burnout en esta muestra de datos.
SELECT 
    mental_fatigue,
    ROUND(AVG(CAST(burnout_risk AS float)), 1) AS promedio_burnout,
    COUNT(*) AS total
FROM small_bournout
GROUP BY mental_fatigue
ORDER BY mental_fatigue

-- el siguiente es el análisis del riesgo de burnout comparado con la ocupación:
-- Hallazgo: los promedios se mantienen en el mismo rango, por lo tanto no hay una relación directa entre
-- las profesiones del dataset y el riesgo de burnout
SELECT 
    occupation,
    ROUND(AVG(CAST(burnout_risk AS float)), 1) AS promedio_burnout,
    COUNT(*) AS total
FROM small_bournout
GROUP BY occupation
ORDER BY promedio_burnout DESC
