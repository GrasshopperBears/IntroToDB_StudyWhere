-- MySQL dump 10.13  Distrib 5.7.22, for Win32 (AMD64)
--
-- Host: wheretostudy.cjeg0lv6iq2a.ap-northeast-2.rds.amazonaws.com    Database: wheretostudy
-- ------------------------------------------------------
-- Server version	5.6.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `building_code` varchar(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `available_begin_weekday` time DEFAULT NULL,
  `available_end_weekday` time DEFAULT NULL,
  `available_begin_weekend` time DEFAULT NULL,
  `available_end_weekend` time DEFAULT NULL,
  `avg_like_score` decimal(3,2) DEFAULT '0.00',
  `num_like_score` int(11) DEFAULT '0',
  `avg_crowded_score` decimal(3,2) DEFAULT '0.00',
  `num_crowded_score` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_LOCATION_CATEGORY_idx` (`category_id`),
  KEY `fk_LOCATION_BUILDING1_idx` (`building_code`),
  CONSTRAINT `fk_LOCATION_BUILDING1` FOREIGN KEY (`building_code`) REFERENCES `buildings` (`building_code`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_LOCATION_CATEGORY` FOREIGN KEY (`category_id`) REFERENCES `location_categories` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'교양분관 1층','N10',3,'00:00:00','23:59:59','00:00:00','23:59:59',0.00,0,0.00,0),(2,'교양분관 1층 세미나실','N10',4,'00:00:00','23:59:59','00:00:00','23:59:59',0.00,0,0.00,0),(3,'교양분관 2층 열람실','N10',2,'00:00:00','23:59:59','00:00:00','23:59:59',2.00,0,3.00,0),(4,'인문사회과학부동 1층','N4',3,'00:00:00','23:59:59','00:00:00','23:59:59',1.00,0,0.00,0),(5,'뚜레쥬르','E6',1,'07:00:00','23:00:00','07:00:00','22:00:00',2.00,2,3.00,2),(6,'투썸플레이스','N1',1,'07:00:00','23:00:00','07:00:00','23:00:00',3.00,2,1.00,2),(7,'던킨도너츠','E3',1,'07:00:00','23:00:00','07:00:00','23:00:00',0.00,0,0.00,0),(8,'카페 오가다','E9',1,'08:30:00','21:30:00','08:30:00','21:30:00',0.00,0,0.00,0),(9,'카페 그랑','N11',1,'08:30:00','20:00:00','10:00:00','19:30:00',0.00,0,0.00,0),(10,'헨델과 그레텔','N7',1,'08:00:00','23:00:00','08:00:00','22:00:00',2.00,1,NULL,1),(11,'망고식스','E4',1,'08:30:00','21:30:00','10:30:00','18:00:00',2.00,1,NULL,1),(12,'커피빈','W2',1,'09:00:00','22:30:00','09:00:00','22:30:00',2.00,0,NULL,0),(13,'도서관 자유석','E9',3,'09:00:00','23:59:59','13:00:00','23:59:59',0.00,0,0.00,0),(14,'도서관 한방향 열람실','E9',2,'09:00:00','23:59:59','13:00:00','23:59:59',2.00,1,NULL,1),(15,'신학관 1,2층','N13-2',3,'00:00:00','23:59:59','00:00:00','23:59:59',0.00,0,NULL,1),(16,'문화관 자유석','E9',3,'00:00:00','23:59:59','00:00:00','23:59:59',NULL,0,3.00,0),(17,'문화관 콜라보레이션룸','E9',4,'00:00:00','23:59:59','00:00:00','23:59:59',0.00,0,0.00,0),(18,'도서관 세미나실','E9',4,'09:00:00','23:59:59','13:00:00','23:59:59',0.00,0,0.00,0),(20,'KI 빌딩 세미나실','E4',4,'00:00:00','23:59:59','00:00:00','23:59:59',0.00,0,0.00,0);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  CONSTRAINT `fk_RESERVATION_SLOT1` FOREIGN KEY (`slot_id`) REFERENCES `slots` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_reservation_user1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
INSERT INTO `reservations` VALUES (3,13,4,'2018-06-19 23:00:00','2018-06-20 01:00:00',7,'ㄹㄹㄹㅇㄹ'),(4,1,4,'2018-06-12 23:00:00','2018-06-13 03:00:00',3,''),(5,13,1,'2018-06-14 17:00:00','2018-06-14 19:00:00',8,'시험 쫑파티를 위한 영화관람'),(6,2,1,'2018-06-12 21:00:00','2018-06-13 01:00:00',3,'시험을 위해 밤을 세고자 합니다.');
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  CONSTRAINT `fk_REVIEW_LOCATION1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_review_user1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (3,1,5,2,3,'점심, 저녁, 낮 시간 가리지 않고 사람이 많습니다. 공부보다는 대화하러 가는 편이 좋습니다.','2018-05-24 00:21:51'),(4,2,16,1,2,'Xxxx','2018-05-24 00:22:07'),(5,1,8,2,3,'','2018-05-24 00:23:55'),(6,4,12,3,1,'교육지원동은 구석진 곳에 있어서 그런지 사람들이 잘 안 오네요.','2018-05-24 00:25:46'),(10,1,2,2,0,'그냥저냥','2018-05-28 01:00:00'),(11,1,3,2,0,'괜찮아요','2018-05-28 01:00:00'),(12,7,4,2,0,'별로에요','2018-05-28 01:00:00'),(13,2,4,2,0,'중간고사 공부 완전 잘됨','2018-05-28 01:00:00'),(14,2,5,2,0,'괜찮은데 사람이 너무 많음','2018-05-28 01:00:00'),(15,1,5,3,0,'다시는 안간다','2018-05-28 01:00:00'),(16,2,3,0,3,NULL,'2018-05-28 01:00:00'),(19,1,7,2,3,'테스트','2018-05-28 00:00:00'),(20,2,2,3,1,'테스트','2018-05-28 00:00:00'),(22,2,6,2,2,'별로야','2018-06-01 12:00:00'),(23,8,15,0,2,'갔다가 앉을 자리 없어서 그냥 나옴','2018-06-01 11:00:00'),(24,6,11,3,3,'3년 동안 공부했는데 갈때마다 좋아요','2018-05-05 14:05:06'),(25,6,5,1,1,'옆자리 앉은 사람이 너무 시끄럽다;;','2018-05-30 18:00:15'),(26,5,5,3,2,'난 좋기만 하구만 왜 별로라 하는지 모르겠다','2018-06-02 01:00:00'),(27,1,6,3,1,'주말에는 사람이 많이 없어 한산합니다.\r\nN1 빌딩 자체가 꽤나 조용해서 좋습니다.','2018-06-03 02:00:17'),(28,1,14,1,3,'사석화가 매우 심한 편이라 자리 구하기가 힘듭니다.\r\n새로 지은 건물이라 그런지 사람들의 관심도가 높고, 이용객이 매우 많습니다.','2018-06-03 02:00:54'),(29,1,10,2,2,'커피는 싸고 접근성이 좋으나, 그만큼 사람들이 많이 찾습니다.\r\n외국인 학우들이 많이 이용하는 곳입니다.','2018-06-03 22:52:25');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`starday123`@`%`*/ /*!50003 TRIGGER `wheretostudy`.`reviews_AFTER_INSERT`
AFTER INSERT ON `wheretostudy`.`reviews`
FOR EACH ROW
BEGIN
	if new.like_score > 0 then
		update locations set avg_like_score=(select avg(like_score) from reviews where (id = new.location_id and like_score != 0)) where id = new.location_id;
		update locations set num_like_score=(num_like_score + 1) where id = new.location_id;
	end if;
    if new.crowded_score > 0 then
		update locations set avg_crowded_score=(select avg(crowded_score) from reviews where (id = new.location_id and crowded_score != 0)) where id = new.location_id;
		update locations set num_crowded_score=(num_crowded_score + 1) where id = new.location_id;
	end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`starday123`@`%`*/ /*!50003 TRIGGER `wheretostudy`.`reviews_AFTER_UPDATE`
AFTER UPDATE ON `wheretostudy`.`reviews`
FOR EACH ROW
BEGIN
	if old.like_score = 0 then
		if new.like_score != 0 then
			update locations set avg_like_score=(select avg(like_score) from reviews where (id = new.location_id and like_score != 0)) where id = new.location_id;
            update locations set num_like_score=(num_like_score + 1) where id = new.location_id;
		end if;
	else
		if new.like_score = 0 then
			update locations set avg_like_score=(if ((select avg(like_score) from reviews where (id = new.location_id and like_score != 0)) is null, 0, (select avg(like_score) from reviews where (id = new.location_id and like_score != 0)))) where id = new.location_id;
			update locations set num_like_score=(num_like_score - 1) where id = new.location_id;
        else
			update locations set avg_like_score=(select avg(like_score) from reviews where (id = new.location_id and like_score != 0)) where id = new.location_id;
		end if;
	end if;
            
	if old.crowded_score = 0 then
		if new.crowded_score != 0 then
			update locations set avg_crowded_score=(select avg(crowded_score) from reviews where (id = new.location_id and crowded_score != 0)) where location_id = new.location_id;
            update locations set num_crowded_score=(num_crowded_score + 1) where id = new.location_id;
		end if;
	else
		if new.crowded_score = 0 then
			update locations set avg_crowded_score=(if ((select avg(crowded_score) from reviews where (id = new.location_id and crowded_score != 0)) is null, 0, (select avg(crowded_score) from reviews where (id = new.location_id and crowded_score != 0)))) where id = new.location_id;
			update locations set num_crowded_score=(num_crowded_score - 1) where id = new.location_id;
        else
			update locations set avg_crowded_score=(select avg(crowded_score) from reviews where (id = new.location_id and crowded_score != 0)) where id = new.location_id;
		end if;
	end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`starday123`@`%`*/ /*!50003 TRIGGER `wheretostudy`.`reviews_AFTER_DELETE`
AFTER DELETE ON `wheretostudy`.`reviews`
FOR EACH ROW
BEGIN
	if old.like_score !=0 then
		update locations set avg_like_score=(if ((select avg(like_score) from reviews where (id = old.location_id and like_score != 0)) is null, 0, (select avg(like_score) from reviews where (id = old.location_id and like_score != 0)))) where id = old.location_id;
		update locations set num_like_score=(num_like_score - 1) where id = old.location_id;
	end if;
    
    if old.crowded_score !=0 then
		update locations set avg_crowded_score=(if ((select avg(crowded_score) from reviews where (id = old.location_id and crowded_score != 0)) is null, 0, (select avg(crowded_score) from reviews where (id = old.location_id and crowded_score != 0)))) where id = old.location_id;
		update locations set num_crowded_score=(num_crowded_score - 1) where id = old.location_id;
	end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `slots`
--

DROP TABLE IF EXISTS `slots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `location_id` int(11) NOT NULL,
  `max_reserve_time` int(11) DEFAULT NULL,
  `minimum_capacity` int(11) DEFAULT NULL,
  `maximum_capacity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_SLOT_LOCATION1_idx` (`location_id`),
  CONSTRAINT `fk_SLOT_LOCATION1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(15) NOT NULL,
  `person_name` varchar(10) NOT NULL,
  `password_hash` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user','관리자','pbkdf2:sha256:50000$gD8jESrh$ec8e5d1aba337866b1a4df9e47c081f8e768a57682c69806ca1b03efb17ff0dc'),(2,'test1','test1','pbkdf2:sha256:50000$ihPPk3Tu$e9bd09395157b27ceb5929d03306e08e4a0cc4948b5b0ebb2d3a1d473bc4b17f'),(3,'user1','[1]이지원','pbkdf2:sha256:50000$F7hsvUUo$6adea0faffecba67d9726ae8db94b1374844630e844b2674b76d45eec818e73b'),(4,'user2','[2]김지현','pbkdf2:sha256:50000$baOBeob2$346cf61958960553aef3b48fb51602f669dedbd3bcdc4caf19f06eaf40b636ca'),(5,'user3','[3]이지은','pbkdf2:sha256:50000$3d03H7Ee$d7877afb9a32a429a63df7649d57a0ff3db18a1c05f3629e3a6d924d855870a2'),(6,'user4','[4]김현지','pbkdf2:sha256:50000$nbapsMd6$47d35913b613f3b566520fc9658414f915a7c08a8e515be2c2a57749c4c177e1'),(7,'user5','[5]박은지','pbkdf2:sha256:50000$WhnEf5ZH$65fb5a3a1fe4dacf910f8ef2ec9f031b0b72657ffcc1d159e338f6c2cdda51a6'),(8,'user6','[6]박예진','pbkdf2:sha256:50000$fnRQ7biV$6583847efcc0981442db33ecb29748f92786734acf4b7811bf0fdc1eb132425e'),(9,'user7','[7]김예지','pbkdf2:sha256:50000$5N7Db5pZ$291f57b5186724c38a024d197fe9554e6f98cd35b9f2609ce720bc3203157bf0'),(10,'user8','[8]김동현','pbkdf2:sha256:50000$viibVguw$b80dc2fab6505540efcdd7a3fd4f1614e883c044a78eac44fe470553bef523c3'),(11,'user9','[9]이지훈','pbkdf2:sha256:50000$Jgf1faXk$d28de67cdd082025b830864041e51a0eae70253bc08d9525257917f70fb4239d'),(12,'user10','[10]김성민','pbkdf2:sha256:50000$FtD9RISA$b4569512d9e7005f4c0e594eade2a5f1b558ef4811503815946ecd65eb0f5c63'),(13,'user11','[11]이현우','pbkdf2:sha256:50000$AE5BKOhx$a5bbd00b578beb54af1ee58dfedc2dd532c2f7280650b454ad0a0d6b8df98f65'),(14,'user12','[12]김준호','pbkdf2:sha256:50000$IgZGipvL$464b3a87d38bf61567585c0faacb09a50f95e6eb1307e44682769b6c400c7af7'),(15,'user13','[13]이민석','pbkdf2:sha256:50000$14cAadtP$84e5fecf3dfd7a0a903c6baafacdc863f72e13db2330bbaf83d5b2cd7820e4e0'),(16,'user14','[14]김민수','pbkdf2:sha256:50000$nUZodJe0$85d419b007e46ea1dfe653911f50eb3b4b43a04f3b4f652b59f241f5e2184049'),(17,'user15','[15]이준혁','pbkdf2:sha256:50000$75olDdBV$ca6a95c6b05b34f5c44e3b795ef4e05cf075343742b89212e08d0687e294cb58'),(18,'user16','[16]김준영','pbkdf2:sha256:50000$Si2nsVhU$7a698e608695e4c7618cc9ff564b864b44906aeb536337b70255ce4094776efc'),(19,'user17','[17]이승현','pbkdf2:sha256:50000$F5XzVwg6$df580bc60bdb0f60edd1eeded04731a25dd571cddbd80365b53f94172fe8f05b'),(20,'user18','[18]김유진','pbkdf2:sha256:50000$45wBTiI8$8ef5749829e1f98481442be31fc4b42f97cb3f961e14dca48036b09afa2fd70e'),(21,'user19','[19]이민서','pbkdf2:sha256:50000$5npwsLke$a9c5c21367860bceb48dd83eefc64103bd98e1bb1ddaefd3ae37bcb7e101fd50'),(22,'user20','[20]김수빈','pbkdf2:sha256:50000$9AqBl6EG$419323d17a5ed1e8fa92f6c2f906d8a6a9de648fa2cc5a9ccf5bfc50ec4a8f2a');
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

-- Dump completed on 2018-06-04 17:05:48
