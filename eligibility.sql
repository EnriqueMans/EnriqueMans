USE elements;
DROP TABLE IF EXISTS #EligibilityEvents;

CREATE TABLE #EligibilityEvents (
    MemCodNum INT,
    TransID INT,
    TC_CODE VARCHAR(10),       -- '61' or '51'
    EFFDT DATE
);

INSERT INTO #EligibilityEvents VALUES
-- TC61 Enrollment Events
(1, 101, '61', '2023-01-01'),
(1, 201, '61', '2024-01-01'),
(1, 301, '61', '2025-01-01'),
(2, 102, '61', '2023-03-15'),
(2, 202, '61', '2024-04-01'),
(3, 103, '61', '2023-06-01'),

-- TC51 Termination Events
(1, 150, '51', '2023-12-31'),
(1, 250, '51', '2024-12-31'),
(2, 151, '51', '2023-12-01'),
(2, 251, '51', '2024-12-01'),
(3, 152, '51', '2023-12-31');

SELECT 
    s.MemCodNum,
    s.TransID AS StartTransID,
    s.EFFDT AS StartDate,
    t.TransID AS EndTransID,
    t.EFFDT AS EndDate,
    CASE 
        WHEN t.EFFDT IS NULL THEN 'Open Span'
        ELSE 'Closed Span'
    END AS SpanStatus
FROM #EligibilityEvents s
OUTER APPLY (
    SELECT TOP 1 *
    FROM #EligibilityEvents t
    WHERE t.MemCodNum = s.MemCodNum
      AND t.TC_CODE = '51'
      AND t.EFFDT > s.EFFDT
    ORDER BY t.EFFDT
) t
WHERE s.TC_CODE = '61'
ORDER BY s.MemCodNum, s.EFFDT;

