---10.1 kõik read eelarve tabelist ja nendega seotud müügiesindajate tabelist

SELECT *
 FROM salesrep_table 
RIGHT JOIN budget_table
ON salesrep_table.sales_rep_id = budget_table.sales_rep_id;



--- 10.3 kõik müügiesindajad müügiesindajate tabelist ja nendega seotud eelarveread eelarve tabelist

SELECT *
FROM salesrep_table AS salesRep
LEFT JOIN budget_table AS budget
       ON budget.sales_rep_id = salesRep.sales_rep_id;

---- 10.4 Read, mis on olemas mõlemas tabelis: Näita ainult ridu, millel on müügiesindajal nii eelarve kui ka väärtus müügiesindajate tabelis. - INNER JOIN

SELECT *
 FROM salesrep_table 
INNER JOIN budget_table
ON salesrep_table.sales_rep_id = budget_table.sales_rep_id;

-- 10.5. Read, mis on olemas ühes või teises tabelis: Näita kõiki eelarveridu ja kõiki müügiesindajate ridu. - FULL OUTER JOIN

SELECT *
FROM salesrep_table AS salesRep
FULL OUTER JOIN budget_table AS budget 
       ON budget.sales_rep_id = salesRep.sales_rep_id;


-- 10.6. Read, mis on olemas esimeses tabelis ja teises ei ole: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - LEFT JOIN ja IS NULL

SELECT *
 FROM budget_table  
LEFT JOIN salesrep_table 
ON salesrep_table.sales_rep_id  = budget_table.sales_rep_id
WHERE salesrep_table.sales_rep_id IS null;

---10.7 Read, mida pole esimeses tabelis, aga on teises tabelis: Näita eelarveridu, millele pole müügiesindaja tabelis müügiesindajat kirjeldatud - RIGHT JOIN ja IS NULL

SELECT *
 FROM salesrep_table 
left JOIN budget_table
ON salesrep_table.sales_rep_id  = budget_table.sales_rep_id
WHERE budget_table.sales_rep_id IS null;

---10.8 Read, mis on puudu ühest või teisest tabelis: Näita müügiesindajaid, kellel on puudu eelarve või müügiesindaja tabelist rida. - FULL OUTER JOIN, IS NULL ja OR
SELECT *
 FROM salesrep_table 
 FULL OUTER JOIN budget_table
ON salesrep_table.sales_rep_id = budget_table.sales_rep_id
WHERE salesrep_table.sales_rep_id  IS NULL OR budget_table.sales_rep_id IS null

-- 10.9. Rohkem kui kahe tabeli ühendamine: Näita müüke, millel on olemas müügiesindaja eelarve ja müügiesindaja tabelis. - INNER JOIN iga seotava tabeli vahele

SELECT *
from sales_table as s
inner join budget_table as bsr
	on s.sales_rep_id = bsr.sales_rep_id
inner join salesrep_table as srt
	on bsr.sales_rep_id = srt.sales_rep_id ;
