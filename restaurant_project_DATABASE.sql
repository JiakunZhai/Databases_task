CREATE TABLE FoodTable(
    tableid INT AUTO_INCREMENT PRIMARY KEY,
    tablenumber int(5),
    tablestate varchar(20)
);

CREATE TABLE Menus(
    menuid INT AUTO_INCREMENT PRIMARY KEY,
    menuname varchar(20),
    mprice varchar(20)
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

CREATE TABLE Expens(
    oderid INT PRIMARY KEY,
    tableid INT,
    oderprice DECIMAL,
    odertime DATETIME,
    FOREIGN KEY(tableid) REFERENCES FoodTable(tableid),
    FOREIGN KEY(oderid) REFERENCES Oder(oderid),
    FOREIGN KEY(oderprice) REFERENCES Oder(oderprice),
    FOREIGN KEY(odertime) REFERENCES Oder(odertime)
);

INSERT INTO FoodTable(tablenumber, tablestate) VALUES
(1,'Y'),
(2,'N'),
(2,'Y'),
(4,'N'),
(4,'Y'),
(6,'N');
INSERT INTO Menus VALUES (menuname, mprice)
('大盘鸡','35'),
('土豆丝','12'),
('红焖羊肉','40'),
('糖醋里脊','25'),
('毛血旺','45'),
('梅菜扣肉','20'),
('红烧肉','30'),
('青椒炒肉','18'),
('佛跳墙','60');