select t.data_sprzed, k.imie, k.nazwisko, tw.nazwa_towaru
from transakcja t join klient k
on t.idklienta = k.idklienta
join towar tw
on t.idtowaru = tw.idtowaru
