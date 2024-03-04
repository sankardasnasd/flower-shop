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
(25,'Can add tbl_ card',7,'add_tbl_card'),
(26,'Can change tbl_ card',7,'change_tbl_card'),
(27,'Can delete tbl_ card',7,'delete_tbl_card'),
(28,'Can view tbl_ card',7,'view_tbl_card'),
(29,'Can add tbl_ cartmaster',8,'add_tbl_cartmaster'),
(30,'Can change tbl_ cartmaster',8,'change_tbl_cartmaster'),
(31,'Can delete tbl_ cartmaster',8,'delete_tbl_cartmaster'),
(32,'Can view tbl_ cartmaster',8,'view_tbl_cartmaster'),
(33,'Can add tbl_ category',9,'add_tbl_category'),
(34,'Can change tbl_ category',9,'change_tbl_category'),
(35,'Can delete tbl_ category',9,'delete_tbl_category'),
(36,'Can view tbl_ category',9,'view_tbl_category'),
(37,'Can add tbl_ customer',10,'add_tbl_customer'),
(38,'Can change tbl_ customer',10,'change_tbl_customer'),
(39,'Can delete tbl_ customer',10,'delete_tbl_customer'),
(40,'Can view tbl_ customer',10,'view_tbl_customer'),
(41,'Can add tbl_ flower',11,'add_tbl_flower'),
(42,'Can change tbl_ flower',11,'change_tbl_flower'),
(43,'Can delete tbl_ flower',11,'delete_tbl_flower'),
(44,'Can view tbl_ flower',11,'view_tbl_flower'),
(45,'Can add tbl_ itemmaster',12,'add_tbl_itemmaster'),
(46,'Can change tbl_ itemmaster',12,'change_tbl_itemmaster'),
(47,'Can delete tbl_ itemmaster',12,'delete_tbl_itemmaster'),
(48,'Can view tbl_ itemmaster',12,'view_tbl_itemmaster'),
(49,'Can add tbl_ login',13,'add_tbl_login'),
(50,'Can change tbl_ login',13,'change_tbl_login'),
(51,'Can delete tbl_ login',13,'delete_tbl_login'),
(52,'Can view tbl_ login',13,'view_tbl_login'),
(53,'Can add tbl_ order',14,'add_tbl_order'),
(54,'Can change tbl_ order',14,'change_tbl_order'),
(55,'Can delete tbl_ order',14,'delete_tbl_order'),
(56,'Can view tbl_ order',14,'view_tbl_order'),
(57,'Can add tbl_ staff',15,'add_tbl_staff'),
(58,'Can change tbl_ staff',15,'change_tbl_staff'),
(59,'Can delete tbl_ staff',15,'delete_tbl_staff'),
(60,'Can view tbl_ staff',15,'view_tbl_staff'),
(61,'Can add tbl_ vendor',16,'add_tbl_vendor'),
(62,'Can change tbl_ vendor',16,'change_tbl_vendor'),
(63,'Can delete tbl_ vendor',16,'delete_tbl_vendor'),
(64,'Can view tbl_ vendor',16,'view_tbl_vendor'),
(65,'Can add tbl_ review',17,'add_tbl_review'),
(66,'Can change tbl_ review',17,'change_tbl_review'),
(67,'Can delete tbl_ review',17,'delete_tbl_review'),
(68,'Can view tbl_ review',17,'view_tbl_review'),
(69,'Can add tbl_ purmaster',18,'add_tbl_purmaster'),
(70,'Can change tbl_ purmaster',18,'change_tbl_purmaster'),
(71,'Can delete tbl_ purmaster',18,'delete_tbl_purmaster'),
(72,'Can view tbl_ purmaster',18,'view_tbl_purmaster'),
(73,'Can add tbl_ purchild',19,'add_tbl_purchild'),
(74,'Can change tbl_ purchild',19,'change_tbl_purchild'),
(75,'Can delete tbl_ purchild',19,'delete_tbl_purchild'),
(76,'Can view tbl_ purchild',19,'view_tbl_purchild'),
(77,'Can add tbl_ payment',20,'add_tbl_payment'),
(78,'Can change tbl_ payment',20,'change_tbl_payment'),
(79,'Can delete tbl_ payment',20,'delete_tbl_payment'),
(80,'Can view tbl_ payment',20,'view_tbl_payment'),
(81,'Can add tbl_ itemchild',21,'add_tbl_itemchild'),
(82,'Can change tbl_ itemchild',21,'change_tbl_itemchild'),
(83,'Can delete tbl_ itemchild',21,'delete_tbl_itemchild'),
(84,'Can view tbl_ itemchild',21,'view_tbl_itemchild'),
(85,'Can add tbl_ delivery',22,'add_tbl_delivery'),
(86,'Can change tbl_ delivery',22,'change_tbl_delivery'),
(87,'Can delete tbl_ delivery',22,'delete_tbl_delivery'),
(88,'Can view tbl_ delivery',22,'view_tbl_delivery'),
(89,'Can add tbl_ cartchild',23,'add_tbl_cartchild'),
(90,'Can change tbl_ cartchild',23,'change_tbl_cartchild'),
(91,'Can delete tbl_ cartchild',23,'delete_tbl_cartchild'),
(92,'Can view tbl_ cartchild',23,'view_tbl_cartchild'),
(93,'Can add cart_child_customization',24,'add_cart_child_customization'),
(94,'Can change cart_child_customization',24,'change_cart_child_customization'),
(95,'Can delete cart_child_customization',24,'delete_cart_child_customization'),
(96,'Can view cart_child_customization',24,'view_cart_child_customization');

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
(7,'online_flower_shop_app','tbl_card'),
(8,'online_flower_shop_app','tbl_cartmaster'),
(9,'online_flower_shop_app','tbl_category'),
(10,'online_flower_shop_app','tbl_customer'),
(11,'online_flower_shop_app','tbl_flower'),
(12,'online_flower_shop_app','tbl_itemmaster'),
(13,'online_flower_shop_app','tbl_login'),
(14,'online_flower_shop_app','tbl_order'),
(15,'online_flower_shop_app','tbl_staff'),
(16,'online_flower_shop_app','tbl_vendor'),
(17,'online_flower_shop_app','tbl_review'),
(18,'online_flower_shop_app','tbl_purmaster'),
(19,'online_flower_shop_app','tbl_purchild'),
(20,'online_flower_shop_app','tbl_payment'),
(21,'online_flower_shop_app','tbl_itemchild'),
(22,'online_flower_shop_app','tbl_delivery'),
(23,'online_flower_shop_app','tbl_cartchild'),
(24,'online_flower_shop_app','cart_child_customization');

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-02-18 04:00:17.770382'),
(2,'auth','0001_initial','2024-02-18 04:00:18.215696'),
(3,'admin','0001_initial','2024-02-18 04:00:18.395027'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-18 04:00:18.404223'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-02-18 04:00:18.404223'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-18 04:00:18.467093'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-18 04:00:18.499512'),
(8,'auth','0003_alter_user_email_max_length','2024-02-18 04:00:18.521822'),
(9,'auth','0004_alter_user_username_opts','2024-02-18 04:00:18.531336'),
(10,'auth','0005_alter_user_last_login_null','2024-02-18 04:00:18.562814'),
(11,'auth','0006_require_contenttypes_0002','2024-02-18 04:00:18.562814'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-18 04:00:18.580495'),
(13,'auth','0008_alter_user_username_max_length','2024-02-18 04:00:18.594791'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-18 04:00:18.634764'),
(15,'auth','0010_alter_group_name_max_length','2024-02-18 04:00:18.658676'),
(16,'auth','0011_update_proxy_permissions','2024-02-18 04:00:18.674188'),
(17,'auth','0012_alter_user_first_name_max_length','2024-02-18 04:00:18.698710'),
(18,'online_flower_shop_app','0001_initial','2024-02-18 04:00:19.777321'),
(19,'sessions','0001_initial','2024-02-18 04:00:19.806768'),
(20,'online_flower_shop_app','0002_cart_child_customization','2024-02-19 05:43:08.351632'),
(21,'online_flower_shop_app','0003_remove_cart_child_customization_assign_date_and_more','2024-02-19 05:51:48.699928'),
(22,'online_flower_shop_app','0004_remove_tbl_order_add_amt_and_more','2024-02-19 06:59:08.713729'),
(23,'online_flower_shop_app','0005_alter_tbl_cartchild_cart_quantity_and_more','2024-02-19 08:04:07.081483'),
(24,'online_flower_shop_app','0006_tbl_delivery_delivery_boy','2024-02-19 09:04:53.952485'),
(25,'online_flower_shop_app','0007_tbl_staff_type','2024-02-19 09:18:47.766344'),
(26,'online_flower_shop_app','0008_tbl_delivery_staff','2024-02-19 09:24:16.973653'),
(27,'online_flower_shop_app','0009_remove_tbl_delivery_delivery_boy','2024-02-19 11:38:27.783428'),
(28,'online_flower_shop_app','0010_remove_tbl_vendor_staff_tbl_vendor_login','2024-02-19 15:02:06.470892'),
(29,'online_flower_shop_app','0011_remove_tbl_purmaster_staff_tbl_purmaster_login','2024-02-19 15:05:27.586701'),
(30,'online_flower_shop_app','0012_alter_tbl_purmaster_tot_amt','2024-02-19 15:26:57.065641'),
(31,'online_flower_shop_app','0013_alter_tbl_cartmaster_tot_amount','2024-02-20 09:20:27.290614'),
(32,'online_flower_shop_app','0014_remove_tbl_review_item_tbl_review_order','2024-02-20 10:25:27.233033');

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('356sd82n3u9kpkqz7y5b50zb6g3vchv5','eyJsaWQiOjR9:1rbb3Y:m6-3SQSoDPGFgsQkjuSZUw9honWuABukDk7luLPzfOM','2024-03-03 06:53:44.978507'),
('x4r507wj96cxmuh4mucp076ytbdynpeu','eyJsaWQiOjF9:1rcIeE:diVuy4didiiiRRfUNasHeTid_41TwMXNh85MG4-Z9TY','2024-03-05 05:26:30.842705'),
('o5rccfxahxbo5k24asi0n9b7o1l68xwq','eyJsaWQiOjR9:1rbzGp:-5Gs9tugBTvkLt6ejrN1GBsGN08J_T94EeEcz_V0bcs','2024-03-04 08:45:03.490965'),
('kc3ncc7h31c0jmwysvrtgpsfzhitv9a4','eyJsaWQiOjR9:1rc48v:UKydfARRr6C6J-Jy1t-cSW4x46MgB9z_1etjVz7BrmI','2024-03-04 13:57:13.895231'),
('2sfctbqnl7w4o298729a41rn0f1pfmrg','eyJsaWQiOjR9:1rcH10:kCzn8FBg3TUizIY_cbWsXv746XhVMCatSKy9XIE_icw','2024-03-05 03:41:54.253480'),
('ol5iqn8weupvko3krwr0d7om65jlornw','eyJsaWQiOjR9:1rcNeE:Ppy5JIEsV1p1ubEDmJzj-YobMEC55cx56ph67vy74d0','2024-03-05 10:46:50.874129'),
('s1vwsblwr20cmkfobns5xvn2dr0yujdf','eyJsaWQiOjR9:1rcmGU:8Z9jos4g5fS82zxywf-q8SCLjiBoP3DVjDMftnxapw4','2024-03-06 13:03:58.999909');

/*Data for the table `online_flower_shop_app_cart_child_customization` */

/*Data for the table `online_flower_shop_app_tbl_card` */

insert  into `online_flower_shop_app_tbl_card`(`id`,`Card_No`,`Card_Holdername`,`Expiry_Date`,`CUSTOMER_id`) values 
(1,'123456789123','sankar','22/2024',4);

/*Data for the table `online_flower_shop_app_tbl_cartchild` */

insert  into `online_flower_shop_app_tbl_cartchild`(`id`,`Image`,`Cart_Quantity`,`CARTMAST_id`,`ITEM_id`) values 
(74,'',2,35,19),
(75,'',1,35,21);

/*Data for the table `online_flower_shop_app_tbl_cartmaster` */

insert  into `online_flower_shop_app_tbl_cartmaster`(`id`,`Tot_Amount`,`Cart_Status`,`CUSTOMER_id`) values 
(35,171,'pending',4);

/*Data for the table `online_flower_shop_app_tbl_category` */

insert  into `online_flower_shop_app_tbl_category`(`id`,`Cat_Name`,`Cat_Desc`) values 
(1,'Bouquets','marriage bouque'),
(2,'wreaths','vcvcx'),
(3,'garlands','ok'),
(4,'Corsage',''),
(5,'Boutonniere',''),
(6,'Centerpiece',''),
(7,'Terrarium',''),
(8,'g','asas');

/*Data for the table `online_flower_shop_app_tbl_customer` */

insert  into `online_flower_shop_app_tbl_customer`(`id`,`C_Fname`,`C_Lname`,`C_House`,`C_City`,`C_Dist`,`C_Pin`,`C_Place`,`C_Phone`,`C_Gender`,`C_DOB`,`C_Status`,`USERNAME_id`) values 
(1,'sachin','tendulkarssssssssssss','sarvani','mumbai adolokam','    juinagar','654128','dharavi','9874463215','male','5/8/1975','',3),
(2,'litib','das','fghj','vbnm','cvbn','989456','vbnm','794561235','Male','2024-02-07','Active',0),
(3,'u','s','cvbn','vbn','fgb','789456','df','9874563258','Male','2024-02-07','Active',0),
(4,'sankar','das','dfghj','cvbn','dfghm','789456','vbnm','987456325','Male','2024-02-07','Active',4);

/*Data for the table `online_flower_shop_app_tbl_delivery` */

insert  into `online_flower_shop_app_tbl_delivery`(`id`,`Assign_Date`,`Del_Date`,`Delivery_Status`,`ORDER_id`,`STAFF_id`) values 
(1,'2024-02-19','','delivered',4,2),
(2,'2024-02-19','2024-02-26','delivered',5,2),
(3,'2024-02-19','2024-02-26','delivered',1,2),
(4,'2024-02-19','2024-02-26','delivered',5,2),
(5,'2024-02-19','2024-02-26','Delivered',6,2);

/*Data for the table `online_flower_shop_app_tbl_flower` */

insert  into `online_flower_shop_app_tbl_flower`(`id`,`Flower_Name`,`Color`,`Img`,`Type`,`Flower_Status`) values 
(1,'Rose','rose','static/flower/pexels-pixabay-56866.jpg','Fresh','Active'),
(2,'jamaica','blue','static/flower/pexels-pixabay-68507.jpg','Fresh','Active'),
(3,'sunflower','yellow','static/flower/pexels-pixabay-46216.jpg','Fresh','1'),
(4,'lotus','pinkish','static/flower/lotus-978659_1280.jpg','Fresh','Active'),
(5,'margureite','white','static/flower/marguerite-729510_1920.jpg','Fresh','Active'),
(6,' daliya','violet','static/flower/flower-4202825_1280.jpg','Artificial','Active');

/*Data for the table `online_flower_shop_app_tbl_itemchild` */

insert  into `online_flower_shop_app_tbl_itemchild`(`id`,`FLOWER_id`,`ITEM_id`) values 
(10,1,19),
(9,1,18),
(8,3,17),
(7,6,16),
(6,4,15),
(11,6,20),
(12,1,21),
(13,5,22);

/*Data for the table `online_flower_shop_app_tbl_itemmaster` */

insert  into `online_flower_shop_app_tbl_itemmaster`(`id`,`Item_Name`,`Item_Desc`,`Item_Cost`,`Item_Img`,`Stock`,`Profit_Per`,`Item_Status`,`CAT_id`) values 
(22,'bell flower','wonder ',854,'static/item/bellflower-6532224_1280.jpg','1','10%','Active',7),
(21,'Rose with pinkish','light pinkish',57,'static/item/tulips-2068692_1280.jpg','1','8%','Active',5),
(20,'white lily','white color',58,'static/item/nature-3184889_1280.jpg','1','8%','Active',1),
(19,'anemone','red',57,'static/item/anemone-6288318_1280.jpg','1','5%','Active',4),
(18,'Rose','pink rose',45,'static/item/pexels-pixabay-56866.jpg','1','1%','Active',3),
(17,'sunflower','sun',200,'static/item/pexels-pixabay-46216.jpg','1','5%','Active',6),
(16,'daliya','daliya',50,'static/item/flower-4202825_1280.jpg','1','4%','Active',4),
(15,'lotus','marriage',200,'static/item/lotus-978659_1280.jpg','1','2%','Active',1);

/*Data for the table `online_flower_shop_app_tbl_login` */

insert  into `online_flower_shop_app_tbl_login`(`id`,`Username`,`Password`,`User_Type`,`Status`) values 
(1,'admin','1','admin','Active'),
(2,'staff@gmail.com','1','Staff','Active'),
(3,'user@gmail.com','1','Customer','Active'),
(4,'sankar@gmail.com','1','Customer','Active'),
(5,'staff1@gmail.com','1','Staff','Active'),
(6,'john@gmail.com','a','Staff','Active');

/*Data for the table `online_flower_shop_app_tbl_order` */

insert  into `online_flower_shop_app_tbl_order`(`id`,`Bill_No`,`A_Fname`,`A_Lname`,`A_City`,`A_House`,`A_Dist`,`A_Pin`,`A_Place`,`A_Phone`,`Order_Date`,`Order_Total`,`Order_Status`,`CARTMAST_id`) values 
(1,'cvv','cvbn','vc','vc','vc','v','v','jhg','789','78451','789','Delivered',1),
(2,'','','','','','','','','','','','',0),
(4,'1001','edvin','thomas','karunagapalli','puthan','kottayam','654123','kottaram','9876543215','2024-02-18','110','Ordered',31),
(5,'1001','x','zxcv','vbn','fgvhb','dfghn','789456','sd','7894561238','2024-02-18','110','Delivered',31),
(6,'1001','x','zxcv','vbn','fgvhb','dfghn','789456','sd','7894561238','2024-02-18','110','Delivered',31),
(7,'1001','sury','cart','chennai','ambadi','chennai','987456','trichi','9874563254','2024-02-19','685.0','ordered',33),
(8,'1001','mobashir','das','malappuram dt','kulkunar','cvbn','679338','kulan','9876543215','2024-02-20','685.0','ordered',33),
(9,'1001','fg','muhammed','malappuram dt','srambikkal','malappuram','679338','payyoli','987456325','2024-02-20','58.0','ordered',35),
(10,'1001','fg','muhammed','malappuram dt','srambikkal','cvbn','679338','asdfgh','9874563211','2024-02-20','58.0','ordered',35),
(11,'1001','dj','dfghj','fghj','wd','wgw','987456','wqs','1234567898','2024-02-20','115.0','ordered',35),
(12,'1001','fg','asdfg','malappuram dt','srambikkal','cvbn','679338','cvb','9961207239','2024-02-20','115.0','ordered',35);

/*Data for the table `online_flower_shop_app_tbl_payment` */

insert  into `online_flower_shop_app_tbl_payment`(`id`,`Payment_Date`,`Payment_Status`,`CARD_id`,`ORDER_id`) values 
(5,'2024-02-19','Paid',1,7),
(4,'2024-02-18','Paid',1,6),
(6,'2024-02-20','Paid',1,8),
(7,'2024-02-20','Paid',1,9),
(8,'2024-02-20','Paid',1,11);

/*Data for the table `online_flower_shop_app_tbl_purchild` */

insert  into `online_flower_shop_app_tbl_purchild`(`id`,`Purch_Quantity`,`Cost_Price`,`Selling_Price`,`Cpurch_Status`,`ITEM_id`,`PM_id`) values 
(13,'8','20','25','',15,2),
(6,'55','15','111','',3,3),
(7,'55','15','111','',4,5),
(8,'55','15','111','',8,3),
(9,'54','78','55','',3,4),
(10,'54','78','55','',4,6),
(11,'55','15','111','',13,3),
(12,'2','28','61','',4,2);

/*Data for the table `online_flower_shop_app_tbl_purmaster` */

insert  into `online_flower_shop_app_tbl_purmaster`(`id`,`Pm_Date`,`Tot_Amt`,`Purch_Status`,`VENDOR_id`,`LOGIN_id`) values 
(2,'pending',116,'pending',1,1),
(3,'pending',363,'pending',2,1),
(4,'pending',110,'pending',1,5),
(5,'pending',222,'pending',3,1),
(6,'pending',110,'pending',3,5);

/*Data for the table `online_flower_shop_app_tbl_review` */

insert  into `online_flower_shop_app_tbl_review`(`id`,`Review_Desc`,`CUSTOMER_id`,`ORDER_id`) values 
(1,'4-2-24',1,1),
(2,'12',4,1),
(3,'awesome products\r\n',4,1),
(4,'cvbnm',4,1),
(5,'super',4,1),
(6,'vbnm,.',4,9),
(7,'sdfg',4,9),
(8,'pkkk\r\n',4,12);

/*Data for the table `online_flower_shop_app_tbl_staff` */

insert  into `online_flower_shop_app_tbl_staff`(`id`,`Staff_Fname`,`Staff_Lname`,`Staff_City`,`Staff_House`,`Staff_Dist`,`Staff_Pin`,`Staff_Place`,`Staff_Phone`,`Staff_Gender`,`Staff_Photo`,`Staff_DOB`,`Staff_Status`,`USERNAME_id`,`Type`) values 
(1,'daya','john','kundara','devid','palakkad','7894565','kolam','9874563258','Female','/2024-02-11-10-20-10.jpg','2024-02-06','Active',2,'1'),
(2,'staffy','mon','vbn','dfgh','kwwjw','789456','fgh','987456325','Male','static/staff/pexels-valeria-boltneva-1961792.jpg','2024-02-14','Active',5,'delivery'),
(3,'john','samual','neyyatinkara','mattam','trivandrum','789456','muttam','7874562587','Male','static/staff/pexels-valeriia-miller-3910071.jpg','2024-02-22','Active',6,'Staff');

/*Data for the table `online_flower_shop_app_tbl_vendor` */

insert  into `online_flower_shop_app_tbl_vendor`(`id`,`V_name`,`V_Email`,`V_Dist`,`V_Pin`,`V_Place`,`V_Phone`,`V_Status`,`LOGIN_id`) values 
(1,'creaft','creaft@gmail.com','calicut','789456','calicut','9874561231','Active',1),
(2,'kiswa','kiswa@gmail.com','kannur','789456','thalassery','7874562587','Active',1),
(3,'luis phogon','luisphogon@gmail.com','ernamkulam','4587661','ekm','987456223','Active',1),
(4,'Surya Agency','surya@gmail.com','calicut','679335','east kallayi','9874562874','Active',1),
(5,'luis phogon','sankardasnasd@gmail.com','ernamkulam','789456','vbnm','9874561230','Active',1),
(6,'nn','sankardasnasd@gmail.com','ernamkulamm','789450','wsgwhgws','9874561230','Active',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
