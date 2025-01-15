INSERT INTO users (username, password, email) VALUES
('user1', 'password123', 'user1@example.com'),
('user2', 'password456', 'user2@example.com'),
('user3', 'password789', 'user3@example.com');

INSERT INTO genres (title, description) VALUES
('Rock', 'very cool'),
('Jazz', 'very chill'),
('Pop', 'money');

INSERT INTO artists (name, avatar, biography) VALUES
('Artist One', 'avatar1.jpg', 'Blablablablablalbalblablabla'),
('Artist Two', 'avatar2.jpg', 'BlablablablablalbalblablablaBlablablablablalbalblablabla'),
('Artist Three', 'avatar3.jpg', 'BlablablablablalbalblablablaBlablablablablalbalblablablaBlablablablablalbalblablabla');

INSERT INTO albums (title, cover_image, release_date, artist_id) VALUES
('Album One', 'cover1.jpg', '2023-01-01', 1),
('Album Two', 'cover2.jpg', '2023-06-15', 2),
('Album Three', 'cover3.jpg', '2024-02-20', 3);

INSERT INTO songs (title, duration, artist_id, genre_id, album_id) VALUES
('Song One', '03:45', 1, 1, 1),
('Song Two', '04:30', 2, 2, 2),
('Song Three', '05:00', 3, 3, 3);
