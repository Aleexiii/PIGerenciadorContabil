-- MySQL Script generated by MySQL Workbench
-- Mon Nov  6 15:55:56 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_juriscon
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_juriscon
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_juriscon` DEFAULT CHARACTER SET utf8 ;
SHOW WARNINGS;
-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------
SHOW WARNINGS;
USE `db_juriscon` ;

-- -----------------------------------------------------
-- Table `db_juriscon`.`sisAdmin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_juriscon`.`sisAdmin` (
  `idAdmin` INT(4) NOT NULL,
  `senha` VARCHAR(70) NOT NULL,
  PRIMARY KEY (`idAdmin`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `db_juriscon`.`funcionarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_juriscon`.`funcionarios` (
  `rg` VARCHAR(10) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `data_nasc` DATE NOT NULL,
  `setor` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(70) NOT NULL,
  `num_carteira_de_trabalho` VARCHAR(11) NOT NULL,
  `comprovante_de_residencia` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`rg`),
  UNIQUE INDEX `rg_UNIQUE` (`rg` ASC) VISIBLE,
  UNIQUE INDEX `senha_UNIQUE` (`senha` ASC) VISIBLE,
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `db_juriscon`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_juriscon`.`clientes` (
  `cnpj` INT(14) NOT NULL,
  `funcionário_atendente` VARCHAR(10) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `nome_fantasia` VARCHAR(100) NOT NULL,
  `cpf_responsavel` VARCHAR(11) NOT NULL,
  `endereço` VARCHAR(100) NOT NULL,
  `atividade` VARCHAR(50) NOT NULL,
  `comprovante_de_pagamento` VARCHAR(100) NULL,
  `copia_comprovante_de_residencia` VARCHAR(100) NULL,
  `copia_contrato_locacao_imovel` VARCHAR(100) NULL,
  `copia_iptu_imovel` VARCHAR(100) NULL,
  PRIMARY KEY (`cnpj`),
  UNIQUE INDEX `cnpj_UNIQUE` (`cnpj` ASC) VISIBLE,
  UNIQUE INDEX `cpf_responsavel_UNIQUE` (`cpf_responsavel` ASC) VISIBLE,
  INDEX `fk_func_atend_idx` (`funcionário_atendente` ASC) VISIBLE,
  CONSTRAINT `fk_func_atend`
    FOREIGN KEY (`funcionário_atendente`)
    REFERENCES `db_juriscon`.`funcionarios` (`rg`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;