/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - home_services
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`home_services` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `home_services`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add allocate_service',7,'add_allocate_service'),(20,'Can change allocate_service',7,'change_allocate_service'),(21,'Can delete allocate_service',7,'delete_allocate_service'),(22,'Can add area',8,'add_area'),(23,'Can change area',8,'change_area'),(24,'Can delete area',8,'delete_area'),(25,'Can add areaallocation',9,'add_areaallocation'),(26,'Can change areaallocation',9,'change_areaallocation'),(27,'Can delete areaallocation',9,'delete_areaallocation'),(28,'Can add category',10,'add_category'),(29,'Can change category',10,'change_category'),(30,'Can delete category',10,'delete_category'),(31,'Can add customer',11,'add_customer'),(32,'Can change customer',11,'change_customer'),(33,'Can delete customer',11,'delete_customer'),(34,'Can add feedback',12,'add_feedback'),(35,'Can change feedback',12,'change_feedback'),(36,'Can delete feedback',12,'delete_feedback'),(37,'Can add login',13,'add_login'),(38,'Can change login',13,'change_login'),(39,'Can delete login',13,'delete_login'),(40,'Can add payment',14,'add_payment'),(41,'Can change payment',14,'change_payment'),(42,'Can delete payment',14,'delete_payment'),(43,'Can add requestss',15,'add_requestss'),(44,'Can change requestss',15,'change_requestss'),(45,'Can delete requestss',15,'delete_requestss'),(46,'Can add service',16,'add_service'),(47,'Can change service',16,'change_service'),(48,'Can delete service',16,'delete_service'),(49,'Can add staff',17,'add_staff'),(50,'Can change staff',17,'change_staff'),(51,'Can delete staff',17,'delete_staff');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'domociliary_services','allocate_service'),(8,'domociliary_services','area'),(9,'domociliary_services','areaallocation'),(10,'domociliary_services','category'),(11,'domociliary_services','customer'),(12,'domociliary_services','feedback'),(13,'domociliary_services','login'),(14,'domociliary_services','payment'),(15,'domociliary_services','requestss'),(16,'domociliary_services','service'),(17,'domociliary_services','staff'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-12-21 22:23:14.054535'),(2,'auth','0001_initial','2023-12-21 22:23:26.950002'),(3,'admin','0001_initial','2023-12-21 22:23:29.043271'),(4,'admin','0002_logentry_remove_auto_add','2023-12-21 22:23:29.105745'),(5,'contenttypes','0002_remove_content_type_name','2023-12-21 22:23:30.605402'),(6,'auth','0002_alter_permission_name_max_length','2023-12-21 22:23:31.683274'),(7,'auth','0003_alter_user_email_max_length','2023-12-21 22:23:32.761292'),(8,'auth','0004_alter_user_username_opts','2023-12-21 22:23:32.823671'),(9,'auth','0005_alter_user_last_login_null','2023-12-21 22:23:33.823470'),(10,'auth','0006_require_contenttypes_0002','2023-12-21 22:23:33.870404'),(11,'auth','0007_alter_validators_add_error_messages','2023-12-21 22:23:33.932736'),(12,'auth','0008_alter_user_username_max_length','2023-12-21 22:23:34.776291'),(13,'auth','0009_alter_user_last_name_max_length','2023-12-21 22:23:35.510638'),(14,'domociliary_services','0001_initial','2023-12-21 22:23:55.422787'),(15,'sessions','0001_initial','2023-12-21 22:23:56.781865'),(16,'domociliary_services','0002_auto_20231222_0641','2023-12-22 01:12:10.230982');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

/*Table structure for table `domociliary_services_allocate_service` */

DROP TABLE IF EXISTS `domociliary_services_allocate_service`;

CREATE TABLE `domociliary_services_allocate_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `REQUEST_id` int(11) NOT NULL,
  `STAFF_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_REQUEST_id_5975e5d2_fk_domocilia` (`REQUEST_id`),
  KEY `domociliary_services_STAFF_id_a28ee674_fk_domocilia` (`STAFF_id`),
  CONSTRAINT `domociliary_services_STAFF_id_a28ee674_fk_domocilia` FOREIGN KEY (`STAFF_id`) REFERENCES `domociliary_services_staff` (`id`),
  CONSTRAINT `domociliary_services_REQUEST_id_5975e5d2_fk_domocilia` FOREIGN KEY (`REQUEST_id`) REFERENCES `domociliary_services_requestss` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_allocate_service` */

insert  into `domociliary_services_allocate_service`(`id`,`date`,`status`,`REQUEST_id`,`STAFF_id`) values (1,'','',4,2),(2,'','',4,2),(3,'','',4,1),(4,'2023-12-22','pending',4,1);

/*Table structure for table `domociliary_services_area` */

DROP TABLE IF EXISTS `domociliary_services_area`;

CREATE TABLE `domociliary_services_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cityname` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_area` */

insert  into `domociliary_services_area`(`id`,`cityname`) values (1,'kannur city'),(2,'Edakkad');

/*Table structure for table `domociliary_services_areaallocation` */

DROP TABLE IF EXISTS `domociliary_services_areaallocation`;

CREATE TABLE `domociliary_services_areaallocation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AREA_id` int(11) NOT NULL,
  `STAFF_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_AREA_id_3d6ad75b_fk_domocilia` (`AREA_id`),
  KEY `domociliary_services_STAFF_id_357f082e_fk_domocilia` (`STAFF_id`),
  CONSTRAINT `domociliary_services_STAFF_id_357f082e_fk_domocilia` FOREIGN KEY (`STAFF_id`) REFERENCES `domociliary_services_staff` (`id`),
  CONSTRAINT `domociliary_services_AREA_id_3d6ad75b_fk_domocilia` FOREIGN KEY (`AREA_id`) REFERENCES `domociliary_services_area` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_areaallocation` */

insert  into `domociliary_services_areaallocation`(`id`,`AREA_id`,`STAFF_id`) values (1,1,1),(2,2,2);

/*Table structure for table `domociliary_services_category` */

DROP TABLE IF EXISTS `domociliary_services_category`;

CREATE TABLE `domociliary_services_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_category` */

insert  into `domociliary_services_category`(`id`,`category_name`) values (1,'cleaning'),(2,'Mechanic Service');

/*Table structure for table `domociliary_services_customer` */

DROP TABLE IF EXISTS `domociliary_services_customer`;

CREATE TABLE `domociliary_services_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_LOGIN_id_6aa64e9c_fk_domocilia` (`LOGIN_id`),
  CONSTRAINT `domociliary_services_LOGIN_id_6aa64e9c_fk_domocilia` FOREIGN KEY (`LOGIN_id`) REFERENCES `domociliary_services_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_customer` */

insert  into `domociliary_services_customer`(`id`,`name`,`email`,`phone`,`image`,`LOGIN_id`) values (1,'jithu','jin@gmail.com','7896541230','i',4);

/*Table structure for table `domociliary_services_feedback` */

DROP TABLE IF EXISTS `domociliary_services_feedback`;

CREATE TABLE `domociliary_services_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `feedback` varchar(200) NOT NULL,
  `CUSTOMER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_CUSTOMER_id_ba0a83cb_fk_domocilia` (`CUSTOMER_id`),
  CONSTRAINT `domociliary_services_CUSTOMER_id_ba0a83cb_fk_domocilia` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `domociliary_services_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_feedback` */

/*Table structure for table `domociliary_services_login` */

DROP TABLE IF EXISTS `domociliary_services_login`;

CREATE TABLE `domociliary_services_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_login` */

insert  into `domociliary_services_login`(`id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'kd@gmail.com','9256','staff'),(3,'abcd@gmail.com','3408','staff'),(4,'jin@gmail.com','1234','customer');

/*Table structure for table `domociliary_services_payment` */

DROP TABLE IF EXISTS `domociliary_services_payment`;

CREATE TABLE `domociliary_services_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `time` varchar(200) NOT NULL,
  `amount` varchar(200) NOT NULL,
  `REQUEST_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_REQUEST_id_6405f6cf_fk_domocilia` (`REQUEST_id`),
  CONSTRAINT `domociliary_services_REQUEST_id_6405f6cf_fk_domocilia` FOREIGN KEY (`REQUEST_id`) REFERENCES `domociliary_services_requestss` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_payment` */

/*Table structure for table `domociliary_services_requestss` */

DROP TABLE IF EXISTS `domociliary_services_requestss`;

CREATE TABLE `domociliary_services_requestss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(200) NOT NULL,
  `amount` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `CUSTOMER_id` int(11) NOT NULL,
  `SERVICE_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_CUSTOMER_id_d592e188_fk_domocilia` (`CUSTOMER_id`),
  KEY `domociliary_services_SERVICE_id_f7d1b7a2_fk_domocilia` (`SERVICE_id`),
  CONSTRAINT `domociliary_services_SERVICE_id_f7d1b7a2_fk_domocilia` FOREIGN KEY (`SERVICE_id`) REFERENCES `domociliary_services_service` (`id`),
  CONSTRAINT `domociliary_services_CUSTOMER_id_d592e188_fk_domocilia` FOREIGN KEY (`CUSTOMER_id`) REFERENCES `domociliary_services_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_requestss` */

insert  into `domociliary_services_requestss`(`id`,`date`,`amount`,`status`,`CUSTOMER_id`,`SERVICE_id`) values (4,'10.12.23','290','pending',1,3);

/*Table structure for table `domociliary_services_service` */

DROP TABLE IF EXISTS `domociliary_services_service`;

CREATE TABLE `domociliary_services_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(200) NOT NULL,
  `amount` varchar(200) NOT NULL,
  `CATEGORY_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_CATEGORY_id_b972f1d1_fk_domocilia` (`CATEGORY_id`),
  CONSTRAINT `domociliary_services_CATEGORY_id_b972f1d1_fk_domocilia` FOREIGN KEY (`CATEGORY_id`) REFERENCES `domociliary_services_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_service` */

insert  into `domociliary_services_service`(`id`,`service_name`,`amount`,`CATEGORY_id`) values (3,'car wash','300',1),(4,'Plumbing','290',2);

/*Table structure for table `domociliary_services_staff` */

DROP TABLE IF EXISTS `domociliary_services_staff`;

CREATE TABLE `domociliary_services_staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `staffname` varchar(200) NOT NULL,
  `staffpost` varchar(200) NOT NULL,
  `staffplace` varchar(200) NOT NULL,
  `staffpin` varchar(200) NOT NULL,
  `staffcontact_no` varchar(200) NOT NULL,
  `staffemail` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domociliary_services_LOGIN_id_8ddba13a_fk_domocilia` (`LOGIN_id`),
  CONSTRAINT `domociliary_services_LOGIN_id_8ddba13a_fk_domocilia` FOREIGN KEY (`LOGIN_id`) REFERENCES `domociliary_services_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `domociliary_services_staff` */

insert  into `domociliary_services_staff`(`id`,`staffname`,`staffpost`,`staffplace`,`staffpin`,`staffcontact_no`,`staffemail`,`LOGIN_id`) values (1,'ajanya resh','edakkad','edakkad','670669','8547038832','kd@gmail.com',2),(2,'nasib','edakkad','edakkad','670669','07907816284','abcd@gmail.com',3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
