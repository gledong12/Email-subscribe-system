-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: Herren
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'패션/뷰티'),(2,'여행'),(3,'운동/레저'),(4,'IT'),(5,'반려동물');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(4,'Email','category'),(5,'Email','email'),(7,'Email','usercategory'),(6,'Email','useremail'),(2,'sessions','session'),(3,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'user','0001_initial','2021-06-05 05:16:08.646198'),(2,'Email','0001_initial','2021-06-05 05:16:10.553759'),(3,'contenttypes','0001_initial','2021-06-05 05:16:10.766438'),(4,'contenttypes','0002_remove_content_type_name','2021-06-05 05:16:11.178875'),(5,'sessions','0001_initial','2021-06-05 05:16:11.387465');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emails`
--

DROP TABLE IF EXISTS `emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `sender_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emails_sender_id_1fc3d9a2_fk_users_id` (`sender_id`),
  CONSTRAINT `emails_sender_id_1fc3d9a2_fk_users_id` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emails`
--

LOCK TABLES `emails` WRITE;
/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
INSERT INTO `emails` VALUES (1,'이메일제목','이메일내용입니다.','2021-06-05 08:59:34.534386','2021-06-05 08:59:34.534467',NULL,2),(2,'이메일제목','이메일내용입니다.','2021-06-05 09:01:04.771376','2021-06-05 09:01:04.771425',NULL,2),(3,'이메일제목','이메일내용입니다.','2021-06-05 09:02:33.905763','2021-06-05 09:02:33.906121',NULL,2),(4,'이메일제목','이메일내용입니다.','2021-06-05 09:04:27.064251','2021-06-05 09:04:27.064310',NULL,2),(5,'이메일제목','이메일내용입니다.','2021-06-05 09:05:21.824139','2021-06-05 09:05:21.824201',NULL,2),(6,'이메일제목','이메일내용입니다.','2021-06-05 09:06:51.868575','2021-06-05 09:06:51.868628',NULL,2),(7,'이메일제목','이메일내용입니다.','2021-06-05 14:49:18.679896','2021-06-05 14:49:18.679970',NULL,2),(8,'이메일제목','이메일내용입니다.','2021-06-05 14:50:03.352083','2021-06-05 14:50:03.352138',NULL,2),(9,'이메일제목','이메일내용입니다.','2021-06-05 14:51:12.641322','2021-06-05 14:51:12.641405',NULL,2),(10,'이메일제목','이메일내용입니다.','2021-06-05 14:52:41.975988','2021-06-05 14:52:41.976103',NULL,2),(11,'이메일제목','이메일내용입니다.','2021-06-05 14:53:17.896870','2021-06-05 14:53:17.896924',NULL,2),(12,'이메일제목','이메일내용입니다.','2021-06-05 14:53:45.215401','2021-06-05 14:53:45.215613',NULL,2),(13,'이메일제목','이메일내용입니다.','2021-06-05 14:54:07.069938','2021-06-05 14:54:07.070013',NULL,2),(14,'이메일제목','이메일내용입니다.','2021-06-05 14:54:48.668335','2021-06-05 14:54:48.668387',NULL,2),(15,'이메일제목','이메일내용입니다.','2021-06-05 14:55:48.365007','2021-06-05 14:55:48.365054',NULL,2),(16,'안녕하십니','여행 카고리의 구독을 진심으로 감사드립니다.','2021-06-06 07:12:19.598573','2021-06-06 07:12:19.598803',NULL,6),(17,'안녕하십니','반려동물 카테고리의 구독을 진심으로 감사드립니다.','2021-06-06 07:15:21.088426','2021-06-06 07:15:21.088496',NULL,6);
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receive_user`
--

DROP TABLE IF EXISTS `receive_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receive_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `receive_user_email_id_9b43fe3c_fk_emails_id` (`email_id`),
  KEY `receive_user_user_id_f2fc2770_fk_users_id` (`user_id`),
  CONSTRAINT `receive_user_email_id_9b43fe3c_fk_emails_id` FOREIGN KEY (`email_id`) REFERENCES `emails` (`id`),
  CONSTRAINT `receive_user_user_id_f2fc2770_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receive_user`
--

LOCK TABLES `receive_user` WRITE;
/*!40000 ALTER TABLE `receive_user` DISABLE KEYS */;
INSERT INTO `receive_user` VALUES (1,6,1),(2,6,2),(3,15,2),(4,16,2),(5,16,5),(6,16,6),(7,17,2),(8,17,5),(9,17,6);
/*!40000 ALTER TABLE `receive_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscribe`
--

DROP TABLE IF EXISTS `subscribe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subscribe` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `subscribe_category_id_2982ba76_fk_categories_id` (`category_id`),
  KEY `subscribe_user_id_9d5b2a55_fk_users_id` (`user_id`),
  CONSTRAINT `subscribe_category_id_2982ba76_fk_categories_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `subscribe_user_id_9d5b2a55_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribe`
--

LOCK TABLES `subscribe` WRITE;
/*!40000 ALTER TABLE `subscribe` DISABLE KEYS */;
INSERT INTO `subscribe` VALUES (9,1,2),(10,2,2),(11,3,2),(12,4,2),(13,5,2),(16,1,5),(17,2,5),(18,3,5),(19,4,5),(20,5,5),(21,1,6),(22,2,6),(23,3,6),(24,4,6),(25,5,6);
/*!40000 ALTER TABLE `subscribe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'이동근,','eagle5424@naver.com,','$2b$12$yjbXaPfg67pN91/8LVEjhuRiFCFZbeNDCmdzZqRHzVkRpQHitEtHG'),(2,'이동근1,','eagle54241@naver.com,','$2b$12$FQ.dS2mkdLqhs6MncFe.DuHENv1qaeEdPGv8Nvr76Hp16KuBli.6a'),(3,'이동근2,','eagle54242@navmer.com,','$2b$12$mwi1lGIqDKp36znFe7cf3.pfxzol08fTYkZhwvZ4ysgDWkRat3/bW'),(4,'이동근3','\'eagle54243@naver.com\'','$2b$12$RGQGUc627ENAPjuvF7h/GOIVibrMg.C37SIi7BxDO9A/OmU/IqOTW'),(5,'이동근4','eagle54244@naver.com','$2b$12$ag4.1F2DoHuwYBPhWVMXfuP9PfiCkdpkpJrbvMW7DFZfbkypP2Hru'),(6,'이동근5','eagle54245@naver.com','$2b$12$go0xssg0D85weyipgJ2qHu.I9/7pyfdUQrd2OeFMkyySImdzDhh2S'),(7,'이동근6','eagle54246@naver.com','$2b$12$jwdmxIDBKuhWhTOiPtwF5uuCEhWfrN7FYy.9ifXIFXcCFE2nI/TbW'),(8,'이동근7','eagle54247@naver.com','$2b$12$MbzQXj.Z7WeIiKNvSSF3duirohdKOjjPzuf7Zr2jTTPLb2YXtvCu.'),(9,'이동근8','eagle54248@naver.com','$2b$12$eA4DSP4wKbaJwAsy.IYP/elFhz6HHlUzQzRWSH9InalzfRQXfvQQa'),(10,'이동근9','eagle54249@shshshshshs.com','$2b$12$BCX0jX37/xCuzeY45n9WE.d5.kxJUU6p8xfBioWvfTlzxT6TW8ccG'),(11,'이동근10','eagle542410@shshshshshs.com','$2b$12$fRd3IyppJaO1v/6ZYeKy2e3/OrNCn6P1mgvPV8DuVp.cACcDeM44G'),(12,'이동근11','eagle542411@shshshshshs.com','$2b$12$S1o589/XJ3uByKzimMGDO.ARQnMOcgf6JRg56JexkfjpvhYbeOzGy');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-06 18:00:45
