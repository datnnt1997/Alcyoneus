USE citadel;

-- Insert Category datas
INSERT INTO `category`(CID, CNAME)
VALUES
    (1, 'Xã hội'),
    (2, 'Kinh tế'),
    (3, 'Công nghệ'),
    (4, 'Đời sống'),
    (5, 'Thể thao'),
    (6, 'Giải trí'),
    (7, 'Văn hóa');

-- Insert Channel datas
INSERT INTO `channel`(chid, chname, description)
VALUES
    (1, 'news', 'Data is collected from online newspapers.'),
    (2, 'social Network', 'Data is collected from posts on social networks.');

-- Insert source datas
INSERT INTO `source`(sid, chid, sname, domain)
VALUES
    (1, 1, 'cafef', 'cafef.vn');

-- Insert decryption datas
INSERT INTO `decryption`(DID, SID, START_URL, PAGINATION, ARTICLE_URL, CATEGORY, TITLE, AUTHOR, TAGS, DESCRIPTION, CONTENT, MEDIA, PUB_TIME)
values
    (1, 1, 'https://cafef.vn/doc-nhanh.chn', './/div[@class="page"]/a[last()]', './/ul[@class="viewport"]//a[@class="news-title"]', './/header//a[@class="cat"]/@href', './/h1/text()', './/p[@class="author"]/text()', './/div[@class="tagdetail"]/div[@class="row2"]/a/text()', './/h2[@class=''sapo'']/text()', './/div[@id="mainContent"]/p/text()', './/img[@data-field="firstphoto"]|.//img[@type="photo"]/@src', './/time[contains(@class, "op-published")]/@datetime');

