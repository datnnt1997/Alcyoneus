-- Clean Database
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- Function and Trigger for update modified time
CREATE OR REPLACE FUNCTION update_modified_time()

RETURNS TRIGGER AS $$
BEGIN
    NEW.update_time = current_timestamp;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create status table
CREATE TABLE status (
    "stid" SERIAL PRIMARY KEY ,
    "message" VARCHAR DEFAULT 'CREATED',
    "create_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
    "update_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp
);

-- Update modified time trigger for status.update_time collumn
CREATE TRIGGER update_status_modtime BEFORE UPDATE ON status FOR EACH ROW EXECUTE PROCEDURE  update_modified_time();

-- Add comment for status table
COMMENT ON TABLE status IS 'Table storage for status of all alcyoneus';
COMMENT ON COLUMN status.message IS 'meaning of status code';

-- Create channel table
CREATE TABLE channel (
    "chid" SERIAL PRIMARY KEY,
    "chname" VARCHAR NOT NULL,
    "description" VARCHAR NOT NULL,
    "create_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
    "update_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp
);

-- Update modified time trigger for channel.update_time collumn
CREATE TRIGGER update_status_modtime BEFORE UPDATE ON channel FOR EACH ROW EXECUTE PROCEDURE update_modified_time();

-- Add comment for channel table
COMMENT ON TABLE channel IS 'Table storage for channel of source';
COMMENT ON COLUMN channel.chname IS 'Name of source of message';
COMMENT ON COLUMN channel.description IS 'Detailed description of the channel';

-- Create source table
CREATE TABLE source (
    "sid" SERIAL PRIMARY KEY,
    "chid" INTEGER NOT NULL REFERENCES channel("chid"),
    "sname" VARCHAR NOT NULL,
    "domain" VARCHAR NOT NULL UNIQUE,
    "create_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
    "update_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp
);

-- Update modified time trigger for channel.update_time collumn
CREATE TRIGGER update_status_modtime BEFORE UPDATE ON source FOR EACH ROW EXECUTE PROCEDURE update_modified_time();

-- Add comment for channel table
COMMENT ON TABLE source IS 'Table storage for sources of message';
COMMENT ON COLUMN source.sname IS 'Name of source of message';
COMMENT ON COLUMN source.domain IS 'Root url of source';

-- Create category table
CREATE TABLE category (
  "cid" SERIAL PRIMARY KEY,
  "cname" VARCHAR NOT NULL,
  "create_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
  "update_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
  "delete_time" TIMESTAMP DEFAULT NULL
);

-- Update modified time trigger for category.update_time collumn
CREATE TRIGGER update_status_modtime BEFORE UPDATE ON category FOR EACH ROW EXECUTE PROCEDURE update_modified_time();

-- Add comment for category table
COMMENT ON TABLE category IS 'Table storage for categories';
COMMENT ON COLUMN source.sname IS 'Name of category of message';


-- Create decryption table
CREATE TABLE decryption (
    "did" SERIAL PRIMARY KEY,
    "sid" INTEGER NOT NULL REFERENCES source("sid"),
    "start_url" VARCHAR NOT NULL,
    "pagination" VARCHAR NOT NULL,
    "pagination_limit" VARCHAR DEFAULT NULL,
    "page_number" INTEGER DEFAULT NULL,
    "crawl_url" VARCHAR NOT NULL,
    "source_url" VARCHAR NOT NULL,
    "category" VARCHAR NOT NULL,
    "title" VARCHAR NOT NULL,
    "author" VARCHAR DEFAULT NULL,
    "tags" VARCHAR DEFAULT NULL,
    "description" VARCHAR DEFAULT NULL,
    "content" VARCHAR DEFAULT NULL,
    "media" VARCHAR DEFAULT NULL,
    "pub_time" VARCHAR DEFAULT NULL,
    "create_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
    "update_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp
);

-- Update modified time trigger for decryption.update_time collumn
CREATE TRIGGER update_status_modtime BEFORE UPDATE ON decryption FOR EACH ROW EXECUTE PROCEDURE update_modified_time();

-- Add comment for channel table
COMMENT ON TABLE source IS 'Table storage for rules for decryption message from universe';

-- Create cosmic_message table
CREATE TABLE cosmic_message (
  "mid" SERIAL PRIMARY KEY ,
  "sid" INTEGER DEFAULT 0 REFERENCES source("sid"),
  "cid" INTEGER DEFAULT 0 REFERENCES category("cid"),
  "crawl_url" VARCHAR NOT NULL,
  "source_url" VARCHAR NOT NULL,
  "title" VARCHAR DEFAULT NULL,
  "author" VARCHAR DEFAULT NULL,
  "tags" JSONB DEFAULT NULL,
  "description" VARCHAR DEFAULT NULL,
  "abstract" VARCHAR DEFAULT NULL,
  "content" TEXT DEFAULT NULL,
  "media" JSONB DEFAULT NULL,
  "status_code" INTEGER DEFAULT 0 REFERENCES status("stid"),
  "pub_time" TIMESTAMP DEFAULT NULL,
  "create_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
  "update_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
  "delete_time" TIMESTAMP DEFAULT NULL
);

-- Adding unique constraint using a unique index for cosmic_message
CREATE UNIQUE INDEX crawl_url_index on cosmic_message (crawl_url);
CREATE UNIQUE INDEX source_url_index on cosmic_message (source_url);

-- Update modified time trigger for decryption.update_time collumn
CREATE TRIGGER update_status_modtime BEFORE UPDATE ON cosmic_message FOR EACH ROW EXECUTE PROCEDURE update_modified_time();

-- Add comment for channel table
COMMENT ON TABLE cosmic_message IS 'Table storage for the whole of the crawl result';
COMMENT ON COLUMN cosmic_message.crawl_url IS 'Article crawl link';
COMMENT ON COLUMN cosmic_message.source_url IS 'Article original link';
COMMENT ON COLUMN cosmic_message.tags IS 'Article tags (comma-separated)';
COMMENT ON COLUMN cosmic_message.description IS 'The description of the article';
COMMENT ON COLUMN cosmic_message.abstract IS 'The content summary of the article';
COMMENT ON COLUMN cosmic_message.content IS 'The whole contents of the article';
COMMENT ON COLUMN cosmic_message.media IS 'The whole image and video of the article';
COMMENT ON COLUMN cosmic_message.pub_time IS 'The time of article publishing';

-- Create cosmic_message table
CREATE TABLE category_mapping (
  "sid" INTEGER DEFAULT 0 REFERENCES source("sid"),
  "src_cate" VARCHAR NOT NULL,
  "tgt_cate" INTEGER DEFAULT 0 REFERENCES category("cid"),
  "create_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
  "update_time" TIMESTAMPTZ NOT NULL DEFAULT current_timestamp,
  "delete_time" TIMESTAMP DEFAULT NULL,
  PRIMARY KEY ("sid", "src_cate")
);

-- Update modified time trigger for category_mapping.update_time collumn
CREATE TRIGGER update_status_modtime BEFORE UPDATE ON category_mapping FOR EACH ROW EXECUTE PROCEDURE update_modified_time();

-- Add comment for category_mapping table
COMMENT ON TABLE category_mapping IS 'Table storage for category mapping';
COMMENT ON COLUMN category_mapping.src_cate IS 'Name of raw category of message';
COMMENT ON COLUMN category_mapping.tgt_cate IS 'Category ID';