-- Create temp table of all TRCs for TC 61 from TRR data
CREATE TABLE #TC61_TRCs (
    TRC_Code VARCHAR(3) PRIMARY KEY,
    TRC_Description VARCHAR(255)
);

INSERT INTO #TC61_TRCs (TRC_Code, TRC_Description)
SELECT DISTINCT
    t.TRC_Code,
    d.TRC_Description
FROM dbo.TRR AS t
LEFT JOIN dbo.TRC_Dictionary AS d
    ON d.TRC_Code = t.TRC_Code
WHERE t.Transaction_Code = '61';

SELECT * FROM #TC61_TRCs
ORDER BY TRC_Code;