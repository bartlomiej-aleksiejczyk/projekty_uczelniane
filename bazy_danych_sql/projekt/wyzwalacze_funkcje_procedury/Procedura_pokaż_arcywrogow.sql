CREATE PROCEDURE `procedura_ilosc_ofiar` ()
BEGIN
SELECT rasy.nazwa, (SUM(zdarzenia.smiertelnosc_ludzi)), rasy.agresywnosc
FROM 
zdarzenia_reptilian_i_arcywrogow zdarzenia INNER JOIN floty_reptilian_i_arcywrogow floty ON zdarzenia.odpowiedzialna_flota = floty.id_floty
INNER JOIN panstwa_reptilian_i_arcywrogow panstwa ON floty.id_panstwa=panstwa.id_panstwa
INNER JOIN rasy_reptilian_i_arcywrogow rasy ON panstwa.id_rasy = rasy.id_rasy
GROUP BY rasy.nazwa;
END
-- procedura, ktora potrafi zestawic ilosc ofiar reptlian z ich agreswynoscia i nazwa