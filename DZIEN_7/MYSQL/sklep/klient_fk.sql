ALTER TABLE `sklep`.`transakcja` 
ADD INDEX `trans_klient_fk_idx` (`idklienta` ASC) VISIBLE;
;
ALTER TABLE `sklep`.`transakcja` 
ADD CONSTRAINT `trans_klient_fk`
  FOREIGN KEY (`idklienta`)
  REFERENCES `sklep`.`klient` (`idklienta`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
