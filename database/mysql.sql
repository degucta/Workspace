-- show databases
-- go 
show tables from bookkeeper;

-- use bookkeeper 
-- go 

-- CREATE TABLE bookkeeper.inputdata(id int, item varchar(500), note varchar(500))
-- go 

use bookkeeper;
-- create table staff(id int not null primary key, name varchar(10));
-- drop table staff; 
-- commit; 

-- create table rawinputdata(id int not null primary key, item varchar(500), note varchar(500));
-- show columns from rawinputdata;
-- show index from rawinputdata;

-- insert into rawinputdata values (1, 'testdata', 'note');
-- insert into rawinputdata values (4, 'testdata4', 'note');
-- commit; 

/* 
delimiter // 
CREATE PROCEDURE simpleproc (OUT param1 INT)
    BEGIN
    SELECT COUNT(*) INTO param1 FROM rawinputdata;
    END//
delimiter ; 
*/

use bookkeeper;
drop procedure insertinputdata;
 
delimiter // 
CREATE PROCEDURE insertinputdata (IN param1 varchar(500), IN param2 varchar(250))
    BEGIN
       select max(id) from rawinputdata into @maxid; 
       set @maxid := @maxid + 1;
       INSERT INTO rawinputdata values (@maxid, param1, param2);
    END//
delimiter ; 

-- test
call insertinputdata('ahaha', 'memo');
select * from rawinputdata;

select version();

select user(), current_user();
SELECT
    ROUTINE_SCHEMA, /* ストアドプロシージャがあるデータベース */
    ROUTINE_NAME,   /* ストアドプロシージャの名前 */
    ROUTINE_TYPE    /* プロシージャとファンクションのどちらかを示す */
FROM
    information_schema.ROUTINES
WHERE
ROUTINE_TYPE = 'PROCEDURE'; /* プロシージャのみ抽出 */

-- stored procedure execution
use bookkeeper; 
set @param1 = 0;
call simpleproc(@param1); 
select @param1;


