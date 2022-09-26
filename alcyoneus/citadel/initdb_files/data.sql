-- Insert status datas
INSERT INTO status(STID, MESSAGE)
VALUES
    (-1, 'DELETED'),
    (0, 'CREATED');

-- Insert Category datas
INSERT INTO category(CID, CNAME)
VALUES
    (0, 'Khác'),
    (1, 'Thời sự'),
    (2, 'Thế giới'),
    (3, 'Giáo dục'),
    (4, 'Pháp luật'),
    (5, 'Khoa học'),
    (6, 'Kinh tế - Tài chính'),
    (7, 'Bất động sản'),
    (8, 'Công nghệ'),
    (9, 'Đời sống'),
    (10, 'Thể thao'),
    (11, 'Giải trí'),
    (12, 'Văn hóa');

-- Insert Channel datas
INSERT INTO channel(CHID, CHNAME, DESCRIPTION)
VALUES
    (1, 'news', 'Data is collected from online newspapers.'),
    (2, 'social Network', 'Data is collected from posts on social networks.');

-- Insert source datas
INSERT INTO `source`(sid, chid, sname, domain)
VALUES
    (1, 1, 'cafef', 'cafef.vn');

-- Insert decryption datas
INSERT INTO `decryption`(DID, SID, START_URL, PAGINATION, PAGE_NUMBER, CRAWL_URL, SOURCE_URL, CATEGORY, TITLE, AUTHOR, TAGS, DESCRIPTION, CONTENT, MEDIA, PUB_TIME)
values
    (1, 1, 'https://cafef.vn/doc-nhanh.chn', './/div[@class="page"]/a[last()]/@href', 'https:\/\/cafef\.vn\/doc-nhanh\/trang-(\\d+)\.chn', '//ul[@class="viewport"]/li//div[@class="title-wrap"]/a/@href', '//div[@class="link-source-detail"]/a/@title', '//p[@class="dateandcat"]/a[@class="cat"]/@href', '//h1[@class="title"]/text()', '//div[contains(@class, "contentdetail")]/p[@class="author"]/text()', '//div[@class="tagdetail"]/div/a/text()', './/h2[@class=''sapo'']/text()', '//div[@id="mainContent"]/*[self::p or self::h3]', './/div[@class="media"]/img/@src|.//img[@type="photo"]/@src', './/span[@class="pdate"]/text()');

INSERT INTO
    `category_mapping`(SID, SRC_CATEGORY, TGT_CATEGORY, delete_time)
VALUES
    (1, 'xa-hoi', 1, null),
    (1, 'thi-truong-chung-khoan', 6, null),
    (1, 'bat-dong-san', 7, null),
    (1, 'doanh-nghiep', 6, null),
    (1, 'tai-chinh-ngan-hang',6, null),
    (1, 'tai-chinh-quoc-te', 2, null),
    (1, 'vi-mo-dau-tu', 6, null),
    (1, 'kinh-te-so', 6, null),
    (1, 'thi-truong', 6, null),
    (1, 'song', 9, null),
    (1, 'Lifestyle', 0, null),
    (1, 'doanh-nghiep-gioi-thieu', 6, null);