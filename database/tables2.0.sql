CREATE TABLE `fpdatabase`.`user` (
  `userID` VARCHAR(45) NOT NULL,
  `firstName` VARCHAR(45) NOT NULL,
  `middleName` VARCHAR(45) NULL,
  `lastName` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `profilePicture` LONGBLOB NULL,
  `bio` VARCHAR(450) NULL,
  `admin` BIT(1) DEFAULT FALSE,
  PRIMARY KEY (`userID`));

ALTER TABLE `fpdatabase`.`user` 
CHANGE COLUMN `password` `password` VARCHAR(500) NOT NULL ;

CREATE TABLE `fpdatabase`.`post` (
  `postID` int NOT NULL AUTO_INCREMENT,
  `image` LONGBLOB NULL,
  `description` VARCHAR(450) NULL,
  `createdAt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `postUser` VARCHAR(45) NULL,
  PRIMARY KEY (`postID`),
  INDEX `userID_idx` (`postUser` ASC) VISIBLE,
  CONSTRAINT `postUserID`
    FOREIGN KEY (`postUser`)
    REFERENCES `fpdatabase`.`user` (`userID`)
    ON DELETE SET NULL
    ON UPDATE CASCADE);

CREATE TABLE `fpdatabase`.`event` (
  `eventID` int NOT NULL AUTO_INCREMENT,
  `eventName` VARCHAR(45) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `date` DATE NULL,
  `createdAt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
  ON DELETE SET NULL
  ON UPDATE CASCADE;

CREATE TABLE `fpdatabase`.`postcomment` (
  `comment` VARCHAR(500) NOT NULL,
  `commentUserID` VARCHAR(45) NOT NULL,
  `commentPostID` INT NOT NULL,
  INDEX `PID_idx` (`commentPostID` ASC) VISIBLE,
  INDEX `UID_idx` (`commentUserID` ASC) VISIBLE,
  CONSTRAINT `PID`
    FOREIGN KEY (`commentPostID`)
    REFERENCES `fpdatabase`.`post` (`postID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT `UID`
    FOREIGN KEY (`commentUserID`)
    REFERENCES `fpdatabase`.`user` (`userID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);
