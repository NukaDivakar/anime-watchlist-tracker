

CREATE DATABASE IF NOT EXISTS anime_tracker;
USE anime_tracker;

CREATE TABLE anime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    genre VARCHAR(50),
    status VARCHAR(20) NOT NULL,
    total_episodes INT,
    episodes_watched INT DEFAULT 0,
    rating INT
);

-- status will be one of: watching, completed, plan to watch, dropped
-- rating is from 1 to 10, only filled in once you complete an anime