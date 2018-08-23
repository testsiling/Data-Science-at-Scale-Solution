-- A σdocid=10398_txt_earn(frequency) 
SELECT count(*) FROM (SELECT * FROM Frequency WHERE (docid = '10398_txt_earn'));


-- B
SELECT count(*) FROM (SELECT term FROM Frequency WHERE (docid = '10398_txt_earn' AND count = 1));


-- C
SELECT count(*) FROM (
	SELECT term FROM Frequency WHERE (docid = '10398_txt_earn' AND count = 1)
	UNION
	SELECT term FROM Frequency WHERE (docid = '925_txt_trade' AND count = 1)
);


-- D
SELECT count(*) FROM (
	SELECT docid FROM Frequency WHERE term = 'law'
	UNION
	SELECT docid FROM Frequency WHERE term = 'legal'
);


-- E
SELECT count(*) FROM (
	SELECT docid FROM Frequency 
	GROUP BY docid 
	HAVING count(count) > 300
);


-- F
SELECT count(*) FROM (
	SELECT docid FROM Frequency WHERE term = 'transactions'
	INTERSECT
	SELECT docid FROM Frequency WHERE term = 'world'
);


-- G
SELECT sum(a.value * b.value)
FROM a JOIN b ON b.row_num = a.col_num AND a.row_num = 2 AND b.col_num = 3
GROUP BY a.row_num, b.col_num;


-- H
SELECT SUM(A.count * B.count)
FROM
(
   SELECT docid, term, count
   FROM frequency
   WHERE docid = '10080_txt_crude'
) A,
(
   SELECT docid, term, count
   FROM frequency
   WHERE docid = '17035_txt_earn'
) B
WHERE A.term = B.term;


-- I
SELECT MAX(count)
FROM
(
  SELECT B.docid, SUM(A.count * B.count) count
  FROM
  (
     SELECT 'q' AS docid, 'washington' AS term, 1 AS count

     UNION

     SELECT 'q' AS docid, 'taxes' AS term, 1 AS count

     UNION

     SELECT 'q' AS docid, 'treasury' as term, 1 AS count
  ) A,
  (
     SELECT * FROM frequency
  ) B
  WHERE A.term = B.term
  GROUP BY B.docid
);