INSERT into users (id) values (1), (2), (3);
INSERT into works (id, path, name, description) values
  (1, 'work_1.png', 'work #1', 'Submitted work #1!'),
  (2, 'work_2.png', 'work #2', 'Submitted work #2!'),
  (3, 'work_3.png', 'work #3', 'Submitted work #3!'),
  (4, 'work_4.png', 'work #4', 'Submitted work #4!'),
  (5, 'work_5.png', 'work #5', 'Submitted work #5!');
INSERT into user_votes (user_id, work_id, vote) values
  (1, 1, 0), (1, 2, 1),
  (2, 2, 0), (2, 5, 1);