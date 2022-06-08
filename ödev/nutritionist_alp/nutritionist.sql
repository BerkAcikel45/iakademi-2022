CREATE TABLE users(
	user_name varchar(100),
	user_last_name varchar(100),
	user_weight integer,
	user_height DOUBLE PRECISION,
	user_bmi DOUBLE PRECISION, -- BMI values will be calculated after a successful execution of main.py file
	user_id serial NOT NULL
);

INSERT INTO users values('Alperen', 'Cantez', 75, 174);
INSERT INTO users values('Beatrice', 'Ena', 57, 166);
INSERT INTO users values('Daniel', 'Preesco', 62, 171);
INSERT INTO users values('Mark', 'Tyler', 98, 162);

CREATE TABLE nutritions(
	ntr_name varchar(50) NOT NULL,
	ntr_kcal integer NOT NULL
);

INSERT INTO nutritions values('Potato', 93);
INSERT INTO nutritions values('Fried Egg', 143);
INSERT INTO nutritions values('Bread', 256);
INSERT INTO nutritions values('Almond', 575);
INSERT INTO nutritions values('Meatball', 160);
INSERT INTO nutritions values('Rice', 139);
INSERT INTO nutritions values('Apple', 52);
INSERT INTO nutritions values('Banana', 88);
INSERT INTO nutritions values('Cauliflower', 25);
INSERT INTO nutritions values('Broccoli', 26);

CREATE TABLE menu(
   daily_menu varchar(250),
   days varchar(10),
   menu_ids integer NOT NULL
);

SELECT * FROM users;
