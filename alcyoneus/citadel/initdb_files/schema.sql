/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

DROP DATABASE IF EXISTS `citadel`;
CREATE DATABASE `citadel`;

USE citadel;

CREATE TABLE `channel` (
  `chid` INT(11) NOT NULL AUTO_INCREMENT,
  `chname` VARCHAR(50) NOT NULL COMMENT 'Name of source of message',
  `description` VARCHAR(50) NOT NULL COMMENT 'Root url of source',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  PRIMARY KEY (`chid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Table storage for channel of source';

CREATE TABLE `source` (
  `sid` INT(11) NOT NULL AUTO_INCREMENT,
  `chid` INT(11) NOT NULL,
  `sname` VARCHAR(50) NOT NULL COMMENT 'Name of source of message',
  `domain` VARCHAR(50) NOT NULL COMMENT 'Root url of source',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  PRIMARY KEY (`sid`),
  FOREIGN KEY (`chid`) REFERENCES channel(`chid`),
  UNIQUE KEY root_url (`domain`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Table storage for sources of message';

CREATE TABLE `decryption` (
    `did` INT(11) NOT NULL AUTO_INCREMENT,
    `sid` INT(11) NOT NULL,
    `start_url` VARCHAR(512) NOT NULL,
    `pagination` VARCHAR(512) NOT NULL,
    `article_url` VARCHAR(512) NOT NULL,
    `category` VARCHAR(512) NOT NULL,
    `title` VARCHAR(512) DEFAULT NULL,
    `author` VARCHAR(512) DEFAULT NULL,
    `tags` VARCHAR(512) DEFAULT NULL,
    `description` VARCHAR(512) DEFAULT NULL,
    `content` VARCHAR(512) DEFAULT NULL,
    `media` VARCHAR(512) DEFAULT NULL,
    `pub_time` VARCHAR(512) DEFAULT NULL,
    `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
    `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
    PRIMARY KEY (`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Table storage for rules for decryption message from universe';

CREATE TABLE `category` (
  `cid` INT(11) NOT NULL AUTO_INCREMENT,
  `cname` VARCHAR(50) DEFAULT '' COMMENT 'Name of source of message',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  `delete_time` TIMESTAMP DEFAULT NULL COMMENT 'Delete time',
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Table storage for categories';

CREATE TABLE `cosmic_message` (
  `mid` INT(11) NOT NULL AUTO_INCREMENT,
  `sid` INT(11) DEFAULT 0 COMMENT 'Source ID',
  `cid` INT(11) DEFAULT 0 COMMENT 'Category ID',
  `url` VARCHAR(256) NOT NULL COMMENT 'Article original link',
  `title` VARCHAR(256) DEFAULT NULL COMMENT 'Aricle title',
  `author` VARCHAR(256) DEFAULT NULL COMMENT 'Article author name',
  `tags` json DEFAULT NULL COMMENT 'Article tags (comma-separated)',
  `description` VARCHAR(512) DEFAULT NULL COMMENT 'The description of the article',
  `abstract` VARCHAR(512) DEFAULT NULL COMMENT 'The content summary of the article',
  `content` MEDIUMTEXT DEFAULT NULL COMMENT 'The whole contents of the article',
  `media` json DEFAULT NULL COMMENT 'The whole image  video of the article',
  `pub_time` DATETIME DEFAULT NULL COMMENT 'The time of article publishing',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  `delete_time` TIMESTAMP DEFAULT NULL COMMENT 'Delete time',
  PRIMARY KEY (`mid`),
  FOREIGN KEY (`sid`) REFERENCES source(`sid`),
  FOREIGN KEY (`cid`) REFERENCES category(`cid`),
  UNIQUE KEY article_url (`url`),
  UNIQUE INDEX USING BTREE (url),
  INDEX USING BTREE (title),
  INDEX USING BTREE (pub_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Table storage for the whole of the crawl result';

