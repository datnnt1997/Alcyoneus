DROP DATABASE IF EXISTS `citadel`;
CREATE DATABASE `citadel` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE citadel;

CREATE TABLE `source` (
  `sid` INT(11) NOT NULL AUTO_INCREMENT,
  `source_name` VARCHAR(50) NOT NULL COMMENT 'Name of source of message',
  `domain` VARCHAR(50) NOT NULL COMMENT 'Root url of source',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  PRIMARY KEY (`sid`),
)

CREATE TABLE `category` (
  `cid` INT(11) NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(50) DEFAULT '' COMMENT 'Name of source of message',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  `delete_time` TIMESTAMP DEFAULT NULL COMMENT 'Delete time',
  PRIMARY KEY (`cid`),
)

CREATE TABLE `cosmic_message` (
  `mid` INT(11) NOT NULL AUTO_INCREMENT,
  `source_id` TINYINT DEFAULT 0 COMMENT 'Source ID',
  `cate_id` TINYINT DEFAULT 0 COMMENT 'Category ID',
  `url` VARCHAR(512) NOT NULL COMMENT 'Article original link',
  `title` VARCHAR(100) DEFAULT NULL COMMENT 'Aricle title',
  `author` VARCHAR(100) DEFAULT NULL COMMENT 'Article author name',
  `tags` VARCHAR(100) DEFAULT NULL COMMENT 'Article tags (comma-separated)',
  `description` VARCHAR(500) DEFAULT NULL COMMENT 'The description of the article',
  `abstract` VARCHAR(500) DEFAULT NULL COMMENT 'The content summary of the article',
  `content` MEDIUMTEXT DEFAULT NULL COMMENT 'The whole contents of the article',
  `media` json DEFAULT NULL, COMMENT 'The whole image  video of the article',
  `pub_time` DATETIME DEFAULT NULL COMMENT 'The time of article publishing',
  `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Creation time',
  `update_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  `delete_time` TIMESTAMP DEFAULT NULL COMMENT 'Delete time',
  PRIMARY KEY (`mid`),
  FOREIGN KEY (`source_id`) REFERENCES source(`sid`),
  FOREIGN KEY (`cate_id`) REFERENCES category(`cid`),
  UNIQUE INDEX USING BTREE (url),
  INDEX USING BTREE (title),
  INDEX USING BTREE (pub_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Table storage for the whole of the crawl result';

