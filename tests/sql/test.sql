SELECT p.vorname, p.alter
FROM Person AS p, Instrument AS i, spielt AS s
WHERE p.pID = s.pID
    AND i.iID = s.iID
    AND i.wert > 400
