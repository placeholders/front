CREATE TABLE user (
       id INT(6) AUTO_INCREMENT,
       name VARCHAR(100) NOT NULL,
       login VARCHAR(100) NOT NULL,
       password VARCHAR(100) NOT NULL,

       PRIMARY KEY (id)
);

CREATE TABLE issue (
       id INT(6) AUTO_INCREMENT,
       description VARCHAR(1000),
       user_creator_id INT(6) NOT NULL,
       user_solver_id INT(6) NOT NULL,

       PRIMARY KEY (id),
       FOREIGN KEY (user_creator_id) REFERENCES user(id),
       FOREIGN KEY (user_solver_id) REFERENCES user(id)
);

CREATE TABLE solution (
       id INT(6) AUTO_INCREMENT,
       description VARCHAR(1000),
       user_id INT(6),
       issue_id INT(6),

       PRIMARY KEY (id),
       FOREIGN KEY (user_id) REFERENCES user(id),
       FOREIGN KEY (issue_id) REFERENCES issue(id)
);

CREATE TABLE score (
       id INT(6) AUTO_INCREMENT,
       user_id INT(6),
       issue_id INT(6),
       solution_id INT(6),
       up_votes INT(32),
       down_votes INT(32),

       PRIMARY KEY (id),
       FOREIGN KEY (user_id) REFERENCES user(id),
       FOREIGN KEY (issue_id) REFERENCES issue(id),
       FOREIGN KEY (solution_id) REFERENCES solution(id)
);
