CREATE TABLE #TC61_TRCs (
    TRC_Code VARCHAR(3) PRIMARY KEY,
    TRC_Description VARCHAR(255),
    CMS_DispositionType CHAR(1) -- A, I, M, R
);

INSERT INTO #TC61_TRCs (TRC_Code, TRC_Description, CMS_DispositionType)
VALUES
('001', 'Enrollment accepted as submitted', 'A'),
('002', 'Enrollment accepted; plan data differs from CMS data', 'A'),
('006', 'Enrollment accepted; MBI changed', 'M'),
('011', 'Enrollment accepted after correction', 'A'),
('013', 'Enrollment accepted – prospective change', 'M'),
('045', 'Enrollment rejected; beneficiary ESRD', 'R'),
('071', 'Hospice status set', 'I'),
('072', 'Hospice status terminated', 'I'),
('073', 'ESRD status set', 'I'),
('074', 'ESRD status terminated', 'I'),
('077', 'Medicaid status set', 'I'),
('078', 'Medicaid status terminated', 'I'),
('100', 'Enrollment rejected; election period invalid or not provided', 'R'),
('102', 'Enrollment rejected; beneficiary not in valid election period', 'R'),
('104', 'Enrollment rejected; request received after election period ended', 'R'),
('121', 'LIS status set', 'I'),
('122', 'LIS status terminated', 'I'),
('123', 'LIS status changed', 'I'),
('127', 'Part D enrollment rejected; employer subsidy status', 'R'),
('133', 'LEP status set', 'I'),
('245', 'MSP status set', 'I'),
('280', 'MSP status terminated', 'I');

SELECT * FROM #TC61_TRCs ORDER BY CMS_DispositionType, TRC_Code;