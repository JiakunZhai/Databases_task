CREATE TABLE FoodTable(
    tableid INT AUTO_INCREMENT PRIMARY KEY,
    tablenumber int(5),
    tablestate varchar(20)
);

CREATE TABLE Menus(
    menuid INT AUTO_INCREMENT PRIMARY KEY,
    menuname varchar(20),
    mprice DECIMAL
);

CREATE TABLE Worker(
    workerid INT AUTO_INCREMENT PRIMARY KEY,
    wokername varchar(20)
);

CREATE TABLE User(
    userid INT AUTO_INCREMENT PRIMARY KEY,
    username varchar(20) NOT NULL,
    userphone varchar(20) UNIQUE
);

CREATE TABLE Oder(
    oderid INT AUTO_INCREMENT PRIMARY KEY,
    tableid INT,
    userid INT,
    workerid INT,
    odertime DATETIME,
    oderprice DECIMAL,
    FOREIGN KEY(tableid) REFERENCES FoodTable(tableid),
    FOREIGN KEY(userid) REFERENCES User(userid),
    FOREIGN KEY(workerid) REFERENCES Worker(workerid)
);


-- 为 'Oder' 表的 'oderid' 列添加索引
ALTER TABLE Oder ADD INDEX idx_oderid (oderid);
-- 为 'Oder' 表的 'oderprice' 列添加索引
ALTER TABLE Oder ADD INDEX idx_oderprice (oderprice);
-- 为 'Oder' 表的 'odertime' 列添加索引
ALTER TABLE Oder ADD INDEX idx_odertime (odertime);

--消费记录表
CREATE TABLE Menuoder(
    oderid INT,
    menuid INT,
    menunum INT,
	PRIMARY KEY(oderid),
    FOREIGN KEY(menuid) REFERENCES Menus(menuid)
);

INSERT INTO FoodTable(tablenumber, tablestate) VALUES
(1,'Y'),
(2,'N'),
(2,'Y'),
(4,'N'),
(4,'Y'),
(6,'N');
INSERT INTO Menus(menuname, mprice) VALUES
('大盘鸡','35'),
('土豆丝','12'),
('红焖羊肉','40'),
('糖醋里脊','25'),
('毛血旺','45'),
('梅菜扣肉','20'),
('红烧肉','30'),
('青椒炒肉','18'),
('佛跳墙','60');

INSERT INTO Worker(workerid, wokername) VALUES
("10001", "王五"),
("10002", "李红"),
("10003", "张三")；

