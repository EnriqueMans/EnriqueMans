CREATE TABLE #TC61_TRCs (
    TRC_Code VARCHAR(3) PRIMARY KEY,
    TRC_Description VARCHAR(255)
);

INSERT INTO #TC61_TRCs (TRC_Code, TRC_Description)
VALUES
('001', 'Enrollment accepted as submitted'),
('002', 'Enrollment accepted; plan data differs from CMS data'),
('006', 'Enrollment accepted; MBI changed'),
('011', 'Enrollment accepted after correction'),
('013', 'Enrollment accepted – prospective change'),
('045', 'Enrollment rejected; beneficiary ESRD'),
('071', 'Hospice status set'),
('072', 'Hospice status terminated'),
('073', 'ESRD status set'),
('074', 'ESRD status terminated'),
('077', 'Medicaid status set'),
('078', 'Medicaid status terminated'),
('121', 'LIS status set'),
('122', 'LIS status terminated'),
('127', 'Part D enrollment rejected; employer subsidy status'),
('133', 'LEP status set');

SELECT * FROM #TC61_TRCs ORDER BY TRC_Code;