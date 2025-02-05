INSERT INTO users (username, password, email) VALUES
('user1', 'password123', 'user1@example.com'),
('user2', 'password456', 'user2@example.com'),
('user3', 'password789', 'user3@example.com');

INSERT INTO genres (title, description) VALUES
('Rock', 'very cool'),
('Jazz', 'very chill'),
('Pop', 'money');

INSERT INTO artists (name, avatar, biography) VALUES
('Artist One', 'profile.png', 'Je suis un artiste'),
('Artist Two', 'profile.png', 'Je suis un autre artiste super'),
('Artist Three', 'profile.png', 'Moi aussi je fais de la musique');

INSERT INTO albums (title, cover_image, release_date, artist_id) VALUES
('Planet 1', 'cover.jpg', '2023-01-01', 1),
('Planet 12', 'cover.jpg', '2024-01-01', 1),
('Arbre Bleu', 'cover.jpg', '2023-06-15', 2),
('Triste Nature!', 'cover.jpg', '2024-02-20', 3);

INSERT INTO songs (title, duration, artist_id, genre_id, album_id) VALUES
  ('Planet 1 - Track 1', '03:30', 1, 1, 1),
  ('Planet 1 - Track 2', '04:05', 1, 1, 1),
  ('Planet 1 - Track 3', '03:50', 1, 1, 1),
  ('Planet 1 - Track 4', '04:00', 1, 1, 1),
  ('Planet 1 - Track 5', '03:45', 1, 1, 1);

-- Album 2 : Planet 12 (4 morceaux)
INSERT INTO songs (title, duration, artist_id, genre_id, album_id) VALUES
  ('Planet 12 - Track 1', '03:15', 1, 1, 2),
  ('Planet 12 - Track 2', '04:20', 1, 1, 2),
  ('Planet 12 - Track 3', '03:55', 1, 1, 2),
  ('Planet 12 - Track 4', '04:05', 1, 1, 2);

-- Album 3 : Arbre Bleu (6 morceaux)
INSERT INTO songs (title, duration, artist_id, genre_id, album_id) VALUES
  ('Arbre Bleu - Track 1', '02:45', 2, 1, 3),
  ('Arbre Bleu - Track 2', '03:30', 2, 1, 3),
  ('Arbre Bleu - Track 3', '03:15', 2, 1, 3),
  ('Arbre Bleu - Track 4', '04:00', 2, 1, 3),
  ('Arbre Bleu - Track 5', '03:50', 2, 1, 3),
  ('Arbre Bleu - Track 6', '04:10', 2, 1, 3);

-- Album 4 : Triste Nature! (7 morceaux)
INSERT INTO songs (title, duration, artist_id, genre_id, album_id) VALUES
  ('Triste Nature! - Track 1', '03:40', 3, 1, 4),
  ('Triste Nature! - Track 2', '04:00', 3, 1, 4),
  ('Triste Nature! - Track 3', '03:35', 3, 1, 4),
  ('Triste Nature! - Track 4', '03:50', 3, 1, 4),
  ('Triste Nature! - Track 5', '04:20', 3, 1, 4),
  ('Triste Nature! - Track 6', '03:55', 3, 1, 4),
  ('Triste Nature! - Track 7', '04:10', 3, 1, 4);
