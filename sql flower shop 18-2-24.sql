/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 8.0.31 : Database - flower_shop
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`flower_shop` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `flower_shop`;

/*Data for the table `auth_group` */

/*Data for the table `auth_group_permissions` */

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add tbl_ login',7,'add_tbl_login'),
(26,'Can change tbl_ login',7,'change_tbl_login'),
(27,'Can delete tbl_ login',7,'delete_tbl_login'),
(28,'Can view tbl_ login',7,'view_tbl_login'),
(29,'Can add tbl_ staff',8,'add_tbl_staff'),
(30,'Can change tbl_ staff',8,'change_tbl_staff'),
(31,'Can delete tbl_ staff',8,'delete_tbl_staff'),
(32,'Can view tbl_ staff',8,'view_tbl_staff'),
(33,'Can add tbl_ customer',9,'add_tbl_customer'),
(34,'Can change tbl_ customer',9,'change_tbl_customer'),
(35,'Can delete tbl_ customer',9,'delete_tbl_customer'),
(36,'Can view tbl_ customer',9,'view_tbl_customer'),
(37,'Can add tbl_ vendor',10,'add_tbl_vendor'),
(38,'Can change tbl_ vendor',10,'change_tbl_vendor'),
(39,'Can delete tbl_ vendor',10,'delete_tbl_vendor'),
(40,'Can view tbl_ vendor',10,'view_tbl_vendor'),
(41,'Can add tbl_ purmaster',11,'add_tbl_purmaster'),
(42,'Can change tbl_ purmaster',11,'change_tbl_purmaster'),
(43,'Can delete tbl_ purmaster',11,'delete_tbl_purmaster'),
(44,'Can view tbl_ purmaster',11,'view_tbl_purmaster'),
(45,'Can add tbl_ category',12,'add_tbl_category'),
(46,'Can change tbl_ category',12,'change_tbl_category'),
(47,'Can delete tbl_ category',12,'delete_tbl_category'),
(48,'Can view tbl_ category',12,'view_tbl_category'),
(49,'Can add tbl_ flower',13,'add_tbl_flower'),
(50,'Can change tbl_ flower',13,'change_tbl_flower'),
(51,'Can delete tbl_ flower',13,'delete_tbl_flower'),
(52,'Can view tbl_ flower',13,'view_tbl_flower'),
(53,'Can add tbl_ itemmaster',14,'add_tbl_itemmaster'),
(54,'Can change tbl_ itemmaster',14,'change_tbl_itemmaster'),
(55,'Can delete tbl_ itemmaster',14,'delete_tbl_itemmaster'),
(56,'Can view tbl_ itemmaster',14,'view_tbl_itemmaster'),
(57,'Can add tbl_ itemchild',15,'add_tbl_itemchild'),
(58,'Can change tbl_ itemchild',15,'change_tbl_itemchild'),
(59,'Can delete tbl_ itemchild',15,'delete_tbl_itemchild'),
(60,'Can view tbl_ itemchild',15,'view_tbl_itemchild'),
(61,'Can add tbl_ purchild',16,'add_tbl_purchild'),
(62,'Can change tbl_ purchild',16,'change_tbl_purchild'),
(63,'Can delete tbl_ purchild',16,'delete_tbl_purchild'),
(64,'Can view tbl_ purchild',16,'view_tbl_purchild'),
(65,'Can add tbl_ cartmaster',17,'add_tbl_cartmaster'),
(66,'Can change tbl_ cartmaster',17,'change_tbl_cartmaster'),
(67,'Can delete tbl_ cartmaster',17,'delete_tbl_cartmaster'),
(68,'Can view tbl_ cartmaster',17,'view_tbl_cartmaster'),
(69,'Can add tbl_ cartchild',18,'add_tbl_cartchild'),
(70,'Can change tbl_ cartchild',18,'change_tbl_cartchild'),
(71,'Can delete tbl_ cartchild',18,'delete_tbl_cartchild'),
(72,'Can view tbl_ cartchild',18,'view_tbl_cartchild'),
(73,'Can add tbl_ card',19,'add_tbl_card'),
(74,'Can change tbl_ card',19,'change_tbl_card'),
(75,'Can delete tbl_ card',19,'delete_tbl_card'),
(76,'Can view tbl_ card',19,'view_tbl_card'),
(77,'Can add tbl_ order',20,'add_tbl_order'),
(78,'Can change tbl_ order',20,'change_tbl_order'),
(79,'Can delete tbl_ order',20,'delete_tbl_order'),
(80,'Can view tbl_ order',20,'view_tbl_order'),
(81,'Can add tbl_ payment',21,'add_tbl_payment'),
(82,'Can change tbl_ payment',21,'change_tbl_payment'),
(83,'Can delete tbl_ payment',21,'delete_tbl_payment'),
(84,'Can view tbl_ payment',21,'view_tbl_payment'),
(85,'Can add tbl_ review',22,'add_tbl_review'),
(86,'Can change tbl_ review',22,'change_tbl_review'),
(87,'Can delete tbl_ review',22,'delete_tbl_review'),
(88,'Can view tbl_ review',22,'view_tbl_review'),
(89,'Can add tbl_ delivery',23,'add_tbl_delivery'),
(90,'Can change tbl_ delivery',23,'change_tbl_delivery'),
(91,'Can delete tbl_ delivery',23,'delete_tbl_delivery'),
(92,'Can view tbl_ delivery',23,'view_tbl_delivery');

/*Data for the table `auth_user` */

/*Data for the table `auth_user_groups` */

/*Data for the table `auth_user_user_permissions` */

/*Data for the table `django_admin_log` */

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'online_flower_shop_app','tbl_login'),
(8,'online_flower_shop_app','tbl_staff'),
(9,'online_flower_shop_app','tbl_customer'),
(10,'online_flower_shop_app','tbl_vendor'),
(11,'online_flower_shop_app','tbl_purmaster'),
(12,'online_flower_shop_app','tbl_category'),
(13,'online_flower_shop_app','tbl_flower'),
(14,'online_flower_shop_app','tbl_itemmaster'),
(15,'online_flower_shop_app','tbl_itemchild'),
(16,'online_flower_shop_app','tbl_purchild'),
(17,'online_flower_shop_app','tbl_cartmaster'),
(18,'online_flower_shop_app','tbl_cartchild'),
(19,'online_flower_shop_app','tbl_card'),
(20,'online_flower_shop_app','tbl_order'),
(21,'online_flower_shop_app','tbl_payment'),
(22,'online_flower_shop_app','tbl_review'),
(23,'online_flower_shop_app','tbl_delivery');

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-02-11 04:27:36.399284'),
(2,'auth','0001_initial','2024-02-11 04:27:36.941101'),
(3,'admin','0001_initial','2024-02-11 04:27:37.145408'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-11 04:27:37.154934'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-02-11 04:27:37.162257'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-11 04:27:37.225412'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-11 04:27:37.261398'),
(8,'auth','0003_alter_user_email_max_length','2024-02-11 04:27:37.295000'),
(9,'auth','0004_alter_user_username_opts','2024-02-11 04:27:37.304661'),
(10,'auth','0005_alter_user_last_login_null','2024-02-11 04:27:37.335461'),
(11,'auth','0006_require_contenttypes_0002','2024-02-11 04:27:37.351803'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-11 04:27:37.357295'),
(13,'auth','0008_alter_user_username_max_length','2024-02-11 04:27:37.402663'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-11 04:27:37.429891'),
(15,'auth','0010_alter_group_name_max_length','2024-02-11 04:27:37.461306'),
(16,'auth','0011_update_proxy_permissions','2024-02-11 04:27:37.461306'),
(17,'auth','0012_alter_user_first_name_max_length','2024-02-11 04:27:37.508912'),
(18,'online_flower_shop_app','0001_initial','2024-02-11 04:27:37.511866'),
(19,'online_flower_shop_app','0002_tbl_staff','2024-02-11 04:27:37.598271'),
(20,'online_flower_shop_app','0003_tbl_customer','2024-02-11 04:27:37.668441'),
(21,'online_flower_shop_app','0004_tbl_vendor','2024-02-11 04:27:37.747864'),
(22,'online_flower_shop_app','0005_alter_tbl_staff_staff_photo','2024-02-11 04:27:37.752540'),
(23,'online_flower_shop_app','0006_tbl_purmaster','2024-02-11 04:27:37.876022'),
(24,'online_flower_shop_app','0007_tbl_category_tbl_flower','2024-02-11 04:27:37.892905'),
(25,'online_flower_shop_app','0008_tbl_itemmaster','2024-02-11 04:27:37.954177'),
(26,'online_flower_shop_app','0009_tbl_itemchild','2024-02-11 04:27:38.068784'),
(27,'online_flower_shop_app','0010_tbl_purchild','2024-02-11 04:27:38.213356'),
(28,'online_flower_shop_app','0011_tbl_cartmaster','2024-02-11 04:27:38.289590'),
(29,'online_flower_shop_app','0012_auto_20240103_1510','2024-02-11 04:27:38.336231'),
(30,'online_flower_shop_app','0013_tbl_cartchild','2024-02-11 04:27:38.449258'),
(31,'online_flower_shop_app','0014_tbl_card','2024-02-11 04:27:38.518304'),
(32,'online_flower_shop_app','0015_auto_20240103_1535','2024-02-11 04:27:38.636646'),
(33,'online_flower_shop_app','0016_tbl_payment','2024-02-11 04:27:38.784423'),
(34,'online_flower_shop_app','0017_tbl_review','2024-02-11 04:27:38.860920'),
(35,'online_flower_shop_app','0018_tbl_delivery','2024-02-11 04:27:38.929934'),
(36,'online_flower_shop_app','0019_auto_20240105_1507','2024-02-11 04:27:39.452216'),
(37,'online_flower_shop_app','0020_auto_20240105_1510','2024-02-11 04:27:39.601823'),
(38,'online_flower_shop_app','0021_auto_20240105_1641','2024-02-11 04:27:39.697965'),
(39,'online_flower_shop_app','0022_tbl_flower_flower_status','2024-02-11 04:27:39.737130'),
(40,'online_flower_shop_app','0023_alter_tbl_staff_staff_photo','2024-02-11 04:27:39.747268'),
(41,'online_flower_shop_app','0024_alter_tbl_flower_img','2024-02-11 04:27:39.747268'),
(42,'online_flower_shop_app','0025_auto_20240124_2252','2024-02-11 04:27:39.792518'),
(43,'sessions','0001_initial','2024-02-11 04:27:39.839955');

/*Data for the table `django_session` */

/*Data for the table `online_flower_shop_app_tbl_card` */

/*Data for the table `online_flower_shop_app_tbl_cartchild` */

/*Data for the table `online_flower_shop_app_tbl_cartmaster` */

insert  into `online_flower_shop_app_tbl_cartmaster`(`id`,`Tot_Amount`,`Cart_Status`,`CUSTOMER_id`) values 
(1,'333','paid',1);

/*Data for the table `online_flower_shop_app_tbl_category` */

insert  into `online_flower_shop_app_tbl_category`(`id`,`Cat_Name`,`Cat_Desc`) values 
(1,'efef','nmd'),
(2,'vc','vcvcx');

/*Data for the table `online_flower_shop_app_tbl_customer` */

insert  into `online_flower_shop_app_tbl_customer`(`id`,`C_Fname`,`C_Lname`,`C_House`,`C_City`,`C_Dist`,`C_Pin`,`C_Place`,`C_Phone`,`C_Gender`,`C_DOB`,`C_Status`,`USERNAME_id`) values 
(1,'sachin','tendulkar','sarvani','mumbai','juinagar','654123','dharavi','9874463215','male','5/8/1975','','ddddd'),
(2,'litib','das','fghj','vbnm','cvbn','989456','vbnm','794561235','Male','2024-02-07','Active','user@gmail.com'),
(3,'u','s','cvbn','vbn','fgb','789456','df','9874563258','Male','2024-02-07','Active','u@gmail.com');

/*Data for the table `online_flower_shop_app_tbl_delivery` */

/*Data for the table `online_flower_shop_app_tbl_flower` */

insert  into `online_flower_shop_app_tbl_flower`(`id`,`Flower_Name`,`Color`,`Img`,`Type`,`Flower_Status`) values 
(1,'nn','hh','static/flower/Acer_Wallpaper_02_3840x2400.jpg','Fresh','Active'),
(2,'jamaica','blue','static/flower/5copy.jpg','Artificial','Active'),
(3,'fdx','fd','static/flower/apj.jpg','Fresh','1');

/*Data for the table `online_flower_shop_app_tbl_itemchild` */

insert  into `online_flower_shop_app_tbl_itemchild`(`id`,`FLOWER_id`,`ITEM_id`) values 
(1,2,1);

/*Data for the table `online_flower_shop_app_tbl_itemmaster` */

insert  into `online_flower_shop_app_tbl_itemmaster`(`id`,`Item_Name`,`Item_Cost`,`Item_Img`,`Stock`,`Item_Status`,`CAT_id`,`Item_Desc`,`Profit_Per`) values 
(1,'hgfds','15','static/item/banner1_tvqAnR6.jpg','1','Active',2,'gfds','4%'),
(2,'dfgn','55','static/item/apj_IxX7qrR.jpg','1','Active',1,'dfgbn','5%');

/*Data for the table `online_flower_shop_app_tbl_login` */

/*Data for the table `online_flower_shop_app_tbl_order` */

insert  into `online_flower_shop_app_tbl_order`(`id`,`Bill_No`,`A_Fname`,`A_Lname`,`A_City`,`A_House`,`A_Dist`,`A_Pin`,`A_Place`,`A_Phone`,`Order_Date`,`Order_Total`,`Add_Amt`,`Order_Status`,`CARTMAST_id`) values 
(1,'cvv','cvbn','vc','vc','vc','v','v','jhg','789','78451','789','456','5',1),
(2,'','','','','','','','','','','','','',0);

/*Data for the table `online_flower_shop_app_tbl_payment` */

/*Data for the table `online_flower_shop_app_tbl_purchild` */

insert  into `online_flower_shop_app_tbl_purchild`(`id`,`Purch_Quantity`,`Cost_Price`,`Selling_Price`,`Cpurch_Status`,`ITEM_id`,`PM_id`) values 
(1,'42','155','555','pais',1,1);

/*Data for the table `online_flower_shop_app_tbl_purmaster` */

insert  into `online_flower_shop_app_tbl_purmaster`(`id`,`Pm_Date`,`Tot_Amt`,`Purch_Status`,`STAFF_id`,`VENDOR_id`) values 
(1,'gggg','555','fff',1,1);

/*Data for the table `online_flower_shop_app_tbl_review` */

insert  into `online_flower_shop_app_tbl_review`(`id`,`Review_Desc`,`CUSTOMER_id`,`ITEM_id`) values 
(1,'4-2-24',1,1);

/*Data for the table `online_flower_shop_app_tbl_staff` */

insert  into `online_flower_shop_app_tbl_staff`(`id`,`Staff_Fname`,`Staff_Lname`,`Staff_City`,`Staff_House`,`Staff_Dist`,`Staff_Pin`,`Staff_Place`,`Staff_Phone`,`Staff_Gender`,`Staff_Photo`,`Staff_DOB`,`Staff_Status`,`USERNAME_id`) values 
(1,'daya','john','kundara','devid','palakkad','789456','kolam','123456789','Female','/2024-02-11-10-20-10.jpg','2024-02-06','Active','daya@gmail.com');

/*Data for the table `online_flower_shop_app_tbl_vendor` */

insert  into `online_flower_shop_app_tbl_vendor`(`id`,`V_name`,`V_Email`,`V_Dist`,`V_Pin`,`V_Place`,`V_Phone`,`V_Status`,`STAFF_id`) values 
(1,'creaft','creaft@gmail.com','calicut','789456','calicut','9874561231','Active',1),
(2,'','','','','','','Active',1),
(3,'luis phogon','luisphogon@gmail.com','ernamkulam','4587661','ekm','987456223','Active',1),
(4,'fghj','d@gmail.com','fghj','679335','edede','7894561230','Active',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
