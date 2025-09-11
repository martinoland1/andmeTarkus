-- TABELI LOOMINE: Loo tabel eelarve jaoks. - CREATE TABLE
CREATE TABLE budgetTable (
	budget_id number
    budget_date DATE,
    sales_rep_name VARCHAR (255),
    budget_sum NUMERIC(12,2)
);
 
-- SISESTA ANDMED KÄSITSI: Sisesta kaks eelarverida. - INSERT INTO
INSERT INTO budgettable (
    budget_date,
    sales_rep_name,
    budget_sum)
VALUES ('2026-01-31',
		'Jane Smith',
         20000), 
        ('2026-01-31',
         'John Doe',
         20000) ;

-- TABELI MUUTMINE
-- LISA TULP: Lisa müügiesindaja ID tulp. - ALTER TABLE ja ADD
ALTER TABLE budgettable
ADD sales_rep_id VARCHAR(255);

-- UUENDA TULBA VÄÄRTUST: Lisa müügiesindajate ID-d. - UPDATE, SET ja WHERE
UPDATE budgettable
SET sales_rep_id = 'SR01'
WHERE sales_rep_name = 'Jane Smith';

select * from budgettable b;

UPDATE budgetTable
SET sales_rep_id = 'SR02' 
WHERE sales_rep_name = 'John Doe';

-- MUUDA TULBA NIME: Lisa täpsustus, et eelarve on eurodes. - ALTER TABLE ja RENAME COLUMN
ALTER TABLE budgetTable
RENAME COLUMN budget_sum TO budget_sum_eur;

-- MUUDA TULBA FORMAATI: Eemalda nime tulbalt pikkuse piirang. - ALTER TABLE ja ALTER COLUMN
ALTER TABLE budgetTable
ALTER COLUMN sales_rep_name TYPE TEXT;

-- KUSTUTA TULP: Eemalda nime tulp. - ALTER TABLE ja DROP COLUMN
ALTER TABLE budgetTable
DROP COLUMN sales_rep_name;

-- KUSTUTA TABEL: Eemalda eelarve tabel. - DROP TABLE
DROP TABLE budgetTable;