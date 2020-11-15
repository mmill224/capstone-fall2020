CREATE TABLE `fpdatabase`.`user` (
  `userID` VARCHAR(45) NOT NULL,
  `firstName` VARCHAR(45) NOT NULL,
  `middleName` VARCHAR(45) NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `profilePicture` LONGBLOB NULL,
  `bio` VARCHAR(450) NULL,
  `admin` BIT(1) NOT NULL,
  PRIMARY KEY (`userID`));

CREATE TABLE `fpdatabase`.`post` (
  `postID` VARCHAR(45) NOT NULL,
  `image` LONGBLOB NULL,
  `description` VARCHAR(450) NULL,
  `date` DATE NOT NULL,
  `postUser` VARCHAR(45) NULL,
  PRIMARY KEY (`postID`),
  INDEX `userID_idx` (`postUser` ASC) VISIBLE,
  CONSTRAINT `postUserID`
    FOREIGN KEY (`postUser`)
    REFERENCES `fpdatabase`.`user` (`userID`)
    ON DELETE SET NULL
    ON UPDATE CASCADE);

CREATE TABLE `fpdatabase`.`event` (
  `eventID` VARCHAR(45) NOT NULL,
  `eventName` VARCHAR(45) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `date` DATE NULL,
  `location` VARCHAR(45) NULL,
  PRIMARY KEY (`eventID`));

ALTER TABLE `fpdatabase`.`event` 
ADD COLUMN `eventUser` VARCHAR(45) NULL AFTER `location`,
ADD INDEX `userID_idx` (`eventUser` ASC) VISIBLE;
;

ALTER TABLE `fpdatabase`.`event` 
ADD CONSTRAINT `userID`
  FOREIGN KEY (`eventUser`)
  REFERENCES `fpdatabase`.`user` (`userID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
