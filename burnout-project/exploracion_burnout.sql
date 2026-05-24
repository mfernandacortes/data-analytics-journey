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
