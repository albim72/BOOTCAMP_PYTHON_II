CREATE TABLE `sklep`.`klient` (
  `idklienta` INT NOT NULL AUTO_INCREMENT,
  `imie` VARCHAR(50) NOT NULL,
  `nazwisko` VARCHAR(50) NOT NULL,
  `data_ur` DATE NOT NULL,
  `telefon` VARCHAR(20) NULL,
  PRIMARY KEY (`idklienta`),
  UNIQUE INDEX `idklient_UNIQUE` (`idklienta` ASC) VISIBLE);
