-- =============================================
-- DATABASE: etheriavr_db
-- Description: Esquema base del proyecto EtheriaVR
-- Author: Axel Gasca + ChatGPT
-- =============================================

-- Selecciona la base de datos (creada por docker-compose)
USE etheriavr_db;

-- ===========================
-- TABLE: artist
-- ===========================
CREATE TABLE IF NOT EXISTS artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL
);

-- ===========================
-- TABLE: song
-- ===========================
CREATE TABLE IF NOT EXISTS song (
    song_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    musical_genre VARCHAR(100),
    musical_key VARCHAR(20),
    original_tempo INT,
    duration INT,
    file_path VARCHAR(255),
    CONSTRAINT fk_song_artist
        FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ===========================
-- TABLE: user
-- ===========================
CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

-- ===========================
-- TABLE: user_configuration
-- ===========================
CREATE TABLE IF NOT EXISTS user_configuration (
    user_id INT PRIMARY KEY,
    midi_device_name VARCHAR(255),
    audience_intensity ENUM('Bajo', 'Medio', 'Alto') NOT NULL,
    CONSTRAINT fk_user_config_user
        FOREIGN KEY (user_id) REFERENCES user(user_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ===========================
-- TABLE: practice_session
-- ===========================
CREATE TABLE IF NOT EXISTS practice_session (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    song_id INT NOT NULL,
    practice_datetime DATETIME,
    practice_mode ENUM('piano', 'canto') NOT NULL,
    rhythm_score DECIMAL(5,2) NOT NULL,
    harmony_score DECIMAL(5,2),
    tuning_score DECIMAL(5,2),
    CONSTRAINT fk_practice_user
        FOREIGN KEY (user_id) REFERENCES user(user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_practice_song
        FOREIGN KEY (song_id) REFERENCES song(song_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ===========================
-- INDEXES (for optimization)
-- ===========================
CREATE INDEX IF NOT EXISTS idx_song_artist_id ON song(artist_id);
CREATE INDEX IF NOT EXISTS idx_practice_user_id ON practice_session(user_id);
CREATE INDEX IF NOT EXISTS idx_practice_song_id ON practice_session(song_id);

-- ===========================
-- SAMPLE DATA (optional)
-- ===========================
INSERT INTO artist (artist_name)
VALUES 
    ('Ludwig van Beethoven'),
    ('Freddie Mercury'),
    ('Adele')
ON DUPLICATE KEY UPDATE artist_name = VALUES(artist_name);

INSERT INTO song (artist_id, title, musical_genre, musical_key, original_tempo, duration, file_path)
VALUES
    (1, 'Für Elise', 'Classical', 'A minor', 120, 180, '/music/fur_elise.mp3'),
    (2, 'Bohemian Rhapsody', 'Rock', 'Bb Major', 72, 354, '/music/bohemian.mp3'),
    (3, 'Hello', 'Pop', 'F minor', 88, 300, '/music/hello.mp3')
ON DUPLICATE KEY UPDATE title = VALUES(title);
