CREATE DATABASE  IF NOT EXISTS `mydbristorante` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydbristorante`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydbristorante
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `Username` varchar(50) NOT NULL,
  `Pwd` varchar(50) DEFAULT NULL,
  `Ruolo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dipendente`
--

DROP TABLE IF EXISTS `dipendente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dipendente` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `CognomeNome` varchar(50) DEFAULT NULL,
  `ruolo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `elementomagazzino`
--

DROP TABLE IF EXISTS `elementomagazzino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elementomagazzino` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idNomeElemento` int DEFAULT NULL,
  `Prezzo` float DEFAULT NULL,
  `Quantita` float DEFAULT NULL,
  `Scadenza` date DEFAULT NULL,
  `Fornitore` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idNomeElemento` (`idNomeElemento`),
  CONSTRAINT `elementomagazzino_ibfk_1` FOREIGN KEY (`idNomeElemento`) REFERENCES `nomeelemento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `elementoordine`
--

DROP TABLE IF EXISTS `elementoordine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elementoordine` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idOrdinazione` int DEFAULT NULL,
  `idProdotto` int DEFAULT NULL,
  `completato` tinyint(1) DEFAULT NULL,
  `sequenza` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idOrdinazione` (`idOrdinazione`),
  KEY `idProdotto` (`idProdotto`),
  CONSTRAINT `elementoordine_ibfk_1` FOREIGN KEY (`idOrdinazione`) REFERENCES `ordinazione` (`id`),
  CONSTRAINT `elementoordine_ibfk_2` FOREIGN KEY (`idProdotto`) REFERENCES `prodottomenu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=365 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fattura`
--

DROP TABLE IF EXISTS `fattura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fattura` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DataEOraFattura` datetime DEFAULT NULL,
  `IDCameriere` int DEFAULT NULL,
  `IDOrdinazione` int DEFAULT NULL,
  `Ricavo` float DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `IDCameriere` (`IDCameriere`),
  KEY `IDOrdinazione` (`IDOrdinazione`),
  CONSTRAINT `fattura_ibfk_1` FOREIGN KEY (`IDCameriere`) REFERENCES `dipendente` (`ID`),
  CONSTRAINT `fattura_ibfk_2` FOREIGN KEY (`IDOrdinazione`) REFERENCES `ordinazione` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ingredienteprodotto`
--

DROP TABLE IF EXISTS `ingredienteprodotto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredienteprodotto` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `IDNomeElemento` int DEFAULT NULL,
  `IDProdotto` int DEFAULT NULL,
  `Quantita` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `nomeelemento`
--

DROP TABLE IF EXISTS `nomeelemento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nomeelemento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  `intolleranze` varchar(45) DEFAULT NULL,
  `vegano` tinyint DEFAULT NULL,
  `piccante` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ordinazione`
--

DROP TABLE IF EXISTS `ordinazione`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordinazione` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idTavolo` int DEFAULT NULL,
  `completato` tinyint DEFAULT NULL,
  `sequenzaCorrente` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idTavolo` (`idTavolo`),
  CONSTRAINT `ordinazione_ibfk_1` FOREIGN KEY (`idTavolo`) REFERENCES `tavolo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prenotazione`
--

DROP TABLE IF EXISTS `prenotazione`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prenotazione` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idTavolo` int DEFAULT NULL,
  `Nome` varchar(50) DEFAULT NULL,
  `NumeroPersone` int DEFAULT NULL,
  `DataEOraPrenotazione` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idTavolo` (`idTavolo`),
  CONSTRAINT `idTavolo` FOREIGN KEY (`idTavolo`) REFERENCES `tavolo` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prodottomenu`
--

DROP TABLE IF EXISTS `prodottomenu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prodottomenu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(50) DEFAULT NULL,
  `descrizione` varchar(500) DEFAULT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `prezzo` float DEFAULT NULL,
  `eliminato` tinyint DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tavolo`
--

DROP TABLE IF EXISTS `tavolo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tavolo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero` int DEFAULT NULL,
  `sala` varchar(50) DEFAULT NULL,
  `stato` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-14 14:50:52
