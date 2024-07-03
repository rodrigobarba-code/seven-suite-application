-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: seven_infrastructure
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `interface`
--

DROP TABLE IF EXISTS `interface`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interface` (
  `interface_id` int NOT NULL AUTO_INCREMENT,
  `fk_router_id` varchar(512) NOT NULL,
  `interface_state` tinyint(1) DEFAULT '0',
  `interface_name` varchar(256) DEFAULT NULL,
  `interface_type` varchar(256) NOT NULL,
  `interface_mtu` double DEFAULT NULL,
  PRIMARY KEY (`interface_id`),
  KEY `fk_router_id` (`fk_router_id`),
  CONSTRAINT `interface_ibfk_1` FOREIGN KEY (`fk_router_id`) REFERENCES `router` (`router_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interface`
--

LOCK TABLES `interface` WRITE;
/*!40000 ALTER TABLE `interface` DISABLE KEYS */;
/*!40000 ALTER TABLE `interface` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip_addresses_configuration`
--

DROP TABLE IF EXISTS `ip_addresses_configuration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip_addresses_configuration` (
  `ip_address_id` int NOT NULL AUTO_INCREMENT,
  `fk_ip_address_interface` int NOT NULL,
  `fk_link_type_id` int NOT NULL,
  `ip_address_alias` varchar(512) DEFAULT NULL,
  `ip_address_state` varchar(8) DEFAULT NULL,
  `ip_address` varchar(64) NOT NULL,
  `ip_address_netmask` varchar(64) NOT NULL,
  `ip_address_network` varchar(64) NOT NULL,
  `ip_address_gateway` varchar(64) NOT NULL,
  PRIMARY KEY (`ip_address_id`),
  KEY `fk_ip_address_interface` (`fk_ip_address_interface`),
  KEY `fk_link_type_id` (`fk_link_type_id`),
  CONSTRAINT `ip_addresses_configuration_ibfk_1` FOREIGN KEY (`fk_ip_address_interface`) REFERENCES `interface` (`interface_id`),
  CONSTRAINT `ip_addresses_configuration_ibfk_2` FOREIGN KEY (`fk_link_type_id`) REFERENCES `link_type` (`link_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip_addresses_configuration`
--

LOCK TABLES `ip_addresses_configuration` WRITE;
/*!40000 ALTER TABLE `ip_addresses_configuration` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip_addresses_configuration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `link_type`
--

DROP TABLE IF EXISTS `link_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `link_type` (
  `link_type_id` int NOT NULL AUTO_INCREMENT,
  `link_type_name` varchar(100) NOT NULL,
  `link_type_description` varchar(512) NOT NULL,
  `link_type_segment` int NOT NULL,
  PRIMARY KEY (`link_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `link_type`
--

LOCK TABLES `link_type` WRITE;
/*!40000 ALTER TABLE `link_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `link_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `region` (
  `region_id` int NOT NULL AUTO_INCREMENT,
  `region_name` varchar(100) NOT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `router`
--

DROP TABLE IF EXISTS `router`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `router` (
  `router_id` varchar(512) NOT NULL,
  `router_name` varchar(256) DEFAULT NULL,
  `fk_site_id` int NOT NULL,
  `fk_session_id` int DEFAULT NULL,
  `fk_ip_address_id` int DEFAULT NULL,
  PRIMARY KEY (`router_id`),
  KEY `fk_site_id` (`fk_site_id`),
  KEY `fk_session_id` (`fk_session_id`),
  KEY `fk_ip_address_id` (`fk_ip_address_id`),
  CONSTRAINT `router_ibfk_1` FOREIGN KEY (`fk_site_id`) REFERENCES `site` (`site_id`),
  CONSTRAINT `router_ibfk_2` FOREIGN KEY (`fk_session_id`) REFERENCES `session_information` (`session_id`),
  CONSTRAINT `router_ibfk_3` FOREIGN KEY (`fk_ip_address_id`) REFERENCES `ip_addresses_configuration` (`ip_address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `router`
--

LOCK TABLES `router` WRITE;
/*!40000 ALTER TABLE `router` DISABLE KEYS */;
/*!40000 ALTER TABLE `router` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_information`
--

DROP TABLE IF EXISTS `session_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session_information` (
  `session_id` int NOT NULL AUTO_INCREMENT,
  `session_ip_address` varchar(128) NOT NULL,
  `session_mac_address` varchar(128) DEFAULT NULL,
  `session_username` varchar(256) NOT NULL,
  `session_password` varchar(256) NOT NULL,
  `session_connection_type` varchar(64) NOT NULL,
  `session_brand` varchar(64) DEFAULT NULL,
  `session_model` varchar(64) DEFAULT NULL,
  `allow_remote_access` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_information`
--

LOCK TABLES `session_information` WRITE;
/*!40000 ALTER TABLE `session_information` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_port`
--

DROP TABLE IF EXISTS `session_port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session_port` (
  `session_port_id` int NOT NULL AUTO_INCREMENT,
  `fk_session_id` int NOT NULL,
  `port_number` int NOT NULL,
  `port_status` tinyint(1) DEFAULT '0',
  `port_protocol` varchar(64) NOT NULL,
  PRIMARY KEY (`session_port_id`),
  KEY `fk_session_id` (`fk_session_id`),
  CONSTRAINT `session_port_ibfk_1` FOREIGN KEY (`fk_session_id`) REFERENCES `session_information` (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_port`
--

LOCK TABLES `session_port` WRITE;
/*!40000 ALTER TABLE `session_port` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_port` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `site`
--

DROP TABLE IF EXISTS `site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `site` (
  `site_id` int NOT NULL AUTO_INCREMENT,
  `fk_region_id` int NOT NULL,
  `site_name` varchar(100) NOT NULL,
  `site_segment` int NOT NULL,
  PRIMARY KEY (`site_id`),
  KEY `fk_region_id` (`fk_region_id`),
  CONSTRAINT `site_ibfk_1` FOREIGN KEY (`fk_region_id`) REFERENCES `region` (`region_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `site`
--

LOCK TABLES `site` WRITE;
/*!40000 ALTER TABLE `site` DISABLE KEYS */;
/*!40000 ALTER TABLE `site` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-03 16:43:55
