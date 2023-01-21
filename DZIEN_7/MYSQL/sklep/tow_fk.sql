ALTER TABLE `sklep`.`transakcja` 
ADD INDEX `trans_tow_fk_idx` (`idtowaru` ASC) VISIBLE;
;
ALTER TABLE `sklep`.`transakcja` 
ADD CONSTRAINT `trans_tow_fk`
  FOREIGN KEY (`idtowaru`)
  REFERENCES `sklep`.`towar` (`idtowaru`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
