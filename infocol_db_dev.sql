/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1(infocol_test)
Source Server Version : 50720
Source Host           : 127.0.0.1:3306
Source Database       : infocol_db_dev

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2021-11-21 13:15:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ipinfo
-- ----------------------------
DROP TABLE IF EXISTS `ipinfo`;
CREATE TABLE `ipinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `ip` varchar(128) DEFAULT NULL COMMENT 'IP',
  `country` varchar(255) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `org` varchar(64) DEFAULT NULL,
  `isp` varchar(64) DEFAULT NULL,
  `loc` varchar(64) DEFAULT NULL,
  `timezone` varchar(64) DEFAULT NULL,
  `source` varchar(64) DEFAULT NULL,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for whoisinfo
-- ----------------------------
DROP TABLE IF EXISTS `whoisinfo`;
CREATE TABLE `whoisinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain_name` varchar(255) DEFAULT NULL COMMENT '域名',
  `registrar` varchar(255) DEFAULT NULL COMMENT '注册商',
  `registrar_email` varchar(128) DEFAULT NULL,
  `registrar_phone` varchar(32) DEFAULT NULL,
  `registrar_creation_date` varchar(32) DEFAULT NULL COMMENT '创建日期',
  `registrar_updated_date` varchar(32) DEFAULT NULL COMMENT '更新日期',
  `registrar_expiry_date` varchar(32) DEFAULT NULL,
  `registrar_whois_server` varchar(255) DEFAULT NULL,
  `name_server` varchar(255) DEFAULT NULL,
  `domain_status` varchar(512) DEFAULT NULL,
  `detail` text,
  `source` varchar(32) DEFAULT NULL,
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
