CREATE TABLE IF NOT EXISTS `sklep`.`towar` (
  `idtowaru` INT NOT NULL AUTO_INCREMENT,
  `nazwa_towaru` VARCHAR(200) NOT NULL,
  `data_prod` DATE NOT NULL,
  `seria` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtowaru`),
  UNIQUE INDEX `idtowaru_UNIQUE` (`idtowaru` ASC) VISIBLE);
