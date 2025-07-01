CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

CREATE TABLE IF NOT EXISTS api_responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data TEXT NOT NULL,
    activity VARCHAR(256),
    type VARCHAR(100),
    participants INT,
    timestamp DATETIME NOT NULL
);

GRANT ALL PRIVILEGES ON flaskdb.* TO 'flaskuser'@'%';
FLUSH PRIVILEGES;