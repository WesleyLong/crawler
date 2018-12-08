DROP TABLE IF EXISTS `ResTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ResTable` (
  `id` int(32) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `branch_name` varchar(16) DEFAULT NULL,
  `price` int(5) DEFAULT NULL,
  `star` float(2,1) DEFAULT NULL,
  `taste` float(2,1) DEFAULT NULL,
  `surroundings` float(2,1) DEFAULT NULL,
  `service` float(2,1) DEFAULT NULL,
  `category` varchar(32) DEFAULT NULL,
  `longitude` float(20,14) DEFAULT NULL,
  `latitude` float(20,14) DEFAULT NULL,
  `district` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

