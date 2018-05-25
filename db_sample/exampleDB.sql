-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: wheretostudy
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `buildings`
--

DROP TABLE IF EXISTS `buildings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `buildings` (
  `building_code` varchar(6) NOT NULL,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`building_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buildings`
--

LOCK TABLES `buildings` WRITE;
/*!40000 ALTER TABLE `buildings` DISABLE KEYS */;
INSERT INTO `buildings` VALUES ('E11','창의학습관'),('E3','정보전자공학동'),('E4','KI빌딩'),('E6','자연과학동'),('E9','학술문화관'),('N1','김병호, 김삼열 IT융합 빌딩'),('N10','교양분관'),('N11','학생식당'),('N13-2','장영신 학생회관'),('N4','인문사회과학부동'),('N7','기계공학동'),('W1','응용공학동'),('W2','서측 학생회관'),('W8','교육지원동');
/*!40000 ALTER TABLE `buildings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location_categories`
--

DROP TABLE IF EXISTS `location_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `location_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_categories`
--

LOCK TABLES `location_categories` WRITE;
/*!40000 ALTER TABLE `location_categories` DISABLE KEYS */;
INSERT INTO `location_categories` VALUES (1,'카페'),(2,'열람실'),(3,'자유석'),(4,'세미나실');
/*!40000 ALTER TABLE `location_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `building_code` varchar(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `available_begin_weekday` time DEFAULT NULL,
  `available_end_weekday` time DEFAULT NULL,
  `available_begin_weekend` time DEFAULT NULL,
  `available_end_weekend` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_LOCATION_CATEGORY_idx` (`category_id`),
  KEY `fk_LOCATION_BUILDING1_idx` (`building_code`),
  CONSTRAINT `fk_LOCATION_BUILDING1` FOREIGN KEY (`building_code`) REFERENCES `buildings` (`building_code`),
  CONSTRAINT `fk_LOCATION_CATEGORY` FOREIGN KEY (`category_id`) REFERENCES `location_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'교양분관 1층','N10',3,'00:00:00','23:59:59','00:00:00','23:59:59'),(2,'교양분관 1층 세미나실','N10',4,'00:00:00','23:59:59','00:00:00','23:59:59'),(3,'교양분관 2층 열람실','N10',2,'00:00:00','23:59:59','00:00:00','23:59:59'),(4,'인문사회과학부동 1층','N4',3,'00:00:00','23:59:59','00:00:00','23:59:59'),(5,'뚜레쥬르','E6',1,'07:00:00','23:00:00','07:00:00','22:00:00'),(6,'투썸플레이스','N1',1,'07:00:00','23:00:00','07:00:00','23:00:00'),(7,'던킨도너츠','E3',1,'07:00:00','23:00:00','07:00:00','23:00:00'),(8,'카페 오가다','E9',1,'08:30:00','21:30:00','08:30:00','21:30:00'),(9,'카페 그랑','N11',1,'08:30:00','20:00:00','10:00:00','19:30:00'),(10,'헨델과 그레텔','N7',1,'08:00:00','23:00:00','08:00:00','22:00:00'),(11,'망고식스','E4',1,'08:30:00','21:30:00','10:30:00','18:00:00'),(12,'커피빈','W2',1,'09:00:00','22:30:00','09:00:00','22:30:00'),(13,'도서관 자유석','E9',3,'09:00:00','23:59:59','13:00:00','23:59:59'),(14,'도서관 한방향 열람실','E9',2,'09:00:00','23:59:59','13:00:00','23:59:59'),(15,'신학관 1,2층','N13-2',3,'00:00:00','23:59:59','00:00:00','23:59:59'),(16,'문화관 자유석','E9',3,'00:00:00','23:59:59','00:00:00','23:59:59'),(17,'문화관 콜라보레이션룸','E9',4,'00:00:00','23:59:59','00:00:00','23:59:59'),(18,'도서관 세미나실','E9',4,'09:00:00','23:59:59','13:00:00','23:59:59'),(20,'KI 빌딩 세미나실','E4',4,'00:00:00','23:59:59','00:00:00','23:59:59');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `reservations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slot_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `begin_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `num_people` int(11) NOT NULL,
  `reservation_purpose` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_RESERVATION_SLOT1_idx` (`slot_id`),
  KEY `begin_date_index` (`begin_date`),
  KEY `end_date_index` (`end_date`),
  KEY `fk_reservation_user1_idx` (`user_id`),
  CONSTRAINT `fk_RESERVATION_SLOT1` FOREIGN KEY (`slot_id`) REFERENCES `slots` (`id`),
  CONSTRAINT `fk_reservation_user1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `like_score` int(11) DEFAULT NULL,
  `crowded_score` int(11) DEFAULT NULL,
  `comment` varchar(300) DEFAULT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_REVIEW_LOCATION1_idx` (`location_id`),
  KEY `fk_review_user1_idx` (`user_id`),
  CONSTRAINT `fk_REVIEW_LOCATION1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`),
  CONSTRAINT `fk_review_user1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,1,1,1,NULL,'사람들이 왔다갔다 해서 시끄러워요','2018-05-13 19:43:00'),(2,1,7,2,0,'도넛이 너무 맛있어요~','2018-05-23 19:18:00'),(3,1,5,2,3,'점심, 저녁, 낮 시간 가리지 않고 사람이 많습니다. 공부보다는 대화하러 가는 편이 좋습니다.','2018-05-24 00:21:51'),(4,1,16,1,2,'Xxxx','2018-05-24 00:22:07'),(5,1,8,2,3,'','2018-05-24 00:23:55'),(6,1,12,3,1,'교육지원동은 구석진 곳에 있어서 그런지 사람들이 잘 안 오네요.','2018-05-24 00:25:46');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slots`
--

DROP TABLE IF EXISTS `slots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `slots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `location_id` int(11) NOT NULL,
  `max_reserve_time` int(11) DEFAULT NULL,
  `minimum_capacity` int(11) DEFAULT NULL,
  `maximum_capacity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_SLOT_LOCATION1_idx` (`location_id`),
  CONSTRAINT `fk_SLOT_LOCATION1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slots`
--

LOCK TABLES `slots` WRITE;
/*!40000 ALTER TABLE `slots` DISABLE KEYS */;
INSERT INTO `slots` VALUES (1,'교양분관 세미나실1',2,4,1,4),(2,'교양분관 세미나실2',2,4,1,4),(3,'교양분관 세미나실3',2,4,1,4),(4,'교양분관 세미나실4',2,4,1,4),(5,'교양분관 세미나실5',2,4,1,4),(6,'교양분관 세미나실6',2,4,1,4),(7,'교양분관 세미나실7',2,4,1,4),(8,'교양분관 세미나실9',2,4,1,4),(9,'교양분관 세미나실A',2,4,1,12),(10,'교양분관 세미나실B',2,4,1,12),(11,'교양분관 세미나실C',2,4,1,12),(12,'교양분관 세미나실D',2,4,1,12),(13,'문화관 콜라보레이션룸 4A',17,2,4,12),(14,'문화관 콜라보레이션룸 4B',17,2,2,6),(15,'문화관 콜라보레이션룸 4C',17,2,3,7),(16,'문화관 콜라보레이션룸 4D',17,2,3,7),(17,'문화관 콜라보레이션룸 4E',17,2,3,7),(18,'문화관 콜라보레이션룸 4F',17,2,2,4),(19,'문화관 콜라보레이션룸 4G',17,2,3,7),(20,'문화관 콜라보레이션룸 4H',17,2,2,5),(21,'문화관 콜라보레이션룸 4I',17,2,3,8),(22,'문화관 콜라보레이션룸 4J',17,2,2,5),(23,'KI 빌딩 Triangle 세미나실1',20,2,1,4),(24,'KI 빌딩 Triangle 세미나실2',20,2,1,4),(25,'KI 빌딩 Triangle 세미나실3',20,2,1,4),(26,'KI 빌딩 Triangle 세미나실4',20,2,1,4),(27,'KI 빌딩 Triangle 세미나실5',20,2,1,4),(28,'KI 빌딩 Triangle 세미나실6',20,2,1,4),(29,'도서관 그룹스터디룸 2A',20,2,2,6),(30,'도서관 그룹스터디룸 2B',20,2,2,6),(31,'도서관 그룹스터디룸 3A',20,2,2,6),(32,'도서관 그룹스터디룸 3B',20,2,2,6),(33,'도서관 그룹스터디룸 3C',20,2,3,8),(34,'도서관 그룹스터디룸 3D',20,2,3,8),(35,'도서관 그룹스터디룸 4A',20,2,2,6),(36,'도서관 그룹스터디룸 4B',20,2,2,6),(37,'도서관 그룹스터디룸 4C',20,2,3,8),(38,'도서관 그룹스터디룸 4D',20,2,3,8);
/*!40000 ALTER TABLE `slots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(15) NOT NULL,
  `person_name` varchar(10) NOT NULL,
  `password_hash` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user','관리자','pbkdf2:sha256:50000$gD8jESrh$ec8e5d1aba337866b1a4df9e47c081f8e768a57682c69806ca1b03efb17ff0dc'),(2,'test1','test1','pbkdf2:sha256:50000$ihPPk3Tu$e9bd09395157b27ceb5929d03306e08e4a0cc4948b5b0ebb2d3a1d473bc4b17f');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'wheretostudy'
--

--
-- Dumping routines for database 'wheretostudy'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-25 17:02:27
