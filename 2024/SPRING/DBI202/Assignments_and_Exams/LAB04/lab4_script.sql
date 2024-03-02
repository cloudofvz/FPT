USE FUH_COMPANY;

--1.	Cho biết ai đang quản lý phòng ban có tên: Phòng Nghiên cứu và phát triển. 
--Thông tin yêu cầu: mã số,họ tên nhân viên, mã số phòng ban, tên phòng ban
SELECT e.empName, e.empSSN, d.depNum, d.depName
FROM tblDepartment d
    INNER JOIN tblEmployee e ON d.mgrSSN = e.empSSN
WHERE d.depName = N'Phòng Nghiên cứu và phát triển';

--2.	Cho phòng ban có tên: Phòng Nghiên cứu và phát triển hiện đang quản lý dự án nào. 
--Thông tin yêu cầu: mã số dụ án, tên dự án, tên phòng ban quản lý
SELECT *
FROM tblDepartment d
    INNER JOIN tblProject p ON d.depNum = p.depNum
WHERE d.depName = N'Phòng Nghiên cứu và phát triển';

--3.	Cho biết dự án có tên ProjectB hiện đang được quản lý bởi phòng ban nào. 
--Thông tin yêu cầu: mã số dụ án, tên dự án, tên phòng ban quản lý
SELECT p.proNum, p.proName, d.depName
FROM tblDepartment d
    INNER JOIN tblProject p ON d.depNum = p.depNum
WHERE p.proName = 'ProjectB';

--4.	Cho biết những nhân viên nào đang bị giám sát bởi nhân viên có tên Mai Duy An. 
--Thông tin yêu cầu: mã số nhân viên, họ tên nhân viên
SELECT empSSN, empName
FROM tblEmployee
WHERE supervisorSSN = (SELECT empSSN
FROM tblEmployee
WHERE empName = N'Mai Duy An');

--5.	Cho biết ai hiện đang giám sát những nhân viên có tên Mai Duy An. 
--Thông tin yêu cầu: mã số nhân viên, họ tên nhân viên giám sát.
SELECT empSSN, empName
FROM tblEmployee
WHERE empSSN= (SELECT supervisorSSN
FROM tblEmployee
WHERE empName = N'Mai Duy An');

--6.	Cho biết dự án có tên ProjectA hiện đang làm việc ở đâu. 
--Thông tin yêu cầu: mã số, tên vị trí làm việc.
SELECT l.locNum, l.locName
FROM tblProject p
    INNER JOIN tblLocation l ON p.locNum = l.locNum
WHERE p.proName = 'ProjectA';

--7.	Cho biết vị trí làm việc có tên Tp. HCM hiện đang là chỗ làm việc của những dự án nào. 
--Thông tin yêu cầu: mã số, tên dự án
SELECT p.proNum, p.proName
FROM tblProject p
    INNER JOIN tblLocation l ON p.locNum = l.locNum
WHERE l.locName = N'TP Hồ Chí Minh';

--8.	Cho biết những người phụ thuộc trên 18 tuổi .
--Thông tin yêu cầu: tên, ngày tháng năm sinh của người phụ thuộc, tên nhân viên phụ thuộc vào.
SELECT de.depName, de.depBirthdate, em.empName
FROM tblDependent de INNER JOIN tblEmployee em
    ON de.empSSN = em.empSSN
WHERE YEAR(GETDATE()) - YEAR(de.depBirthdate) >= 18;

--9.	Cho biết những người phụ thuộc  là nam giới. 
--Thông tin yêu cầu: tên, ngày tháng năm sinh của người phụ thuộc, tên nhân viên phụ thuộc vào 
SELECT de.depName, de.depBirthdate, em.empName
FROM tblDependent de INNER JOIN tblEmployee em
    ON de.empSSN = em.empSSN
WHERE de.depSex  = 'M';

--10.	Cho biết những nơi làm việc của phòng ban có tên : Phòng Nghiên cứu và phát triển. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, tên nơi làm việc.
SELECT d.depNum, d.depName, l.locName
FROM tblLocation l
    INNER JOIN tblDepLocation dl ON dl.locNum = l.locNum
    INNER JOIN tblDepartment d ON d.depNum = dl.depNum
WHERE d.depName = N'Phòng Nghiên cứu và phát triển';

--11.	Cho biết các dự án làm việc tại Tp. HCM. Thông tin yêu cầu: mã dự án, tên dự án, tên phòng ban chịu trách nhiệm dự án.
SELECT p.proNum, p.proName, d.depName
FROM tblProject p
    INNER JOIN tblLocation l ON p.locNum = l.locNum
    INNER JOIN tblDepartment d ON p.depNum = d.depNum
WHERE l.locName = N'TP Hồ Chí Minh';

--12.	Cho biết những người phụ thuộc là nữ giới, của nhân viên thuộc phòng ban có tên: Phòng Nghiên cứu và phát triển . 
--Thông tin yêu cầu: tên nhân viên, tên người phụ thuộc, mối liên hệ giữa người phụ thuộc với nhân viên
SELECT e.empName, dp.depName, dp.depRelationship
FROM tblDependent dp
    INNER JOIN tblEmployee e ON dp.empSSN = e.empSSN
    INNER JOIN tblDepartment d ON e.depNum = d.depNum
WHERE dp.depSex = 'F' AND d.depName = N'Phòng Nghiên cứu và phát triển';

--13.	Cho biết những người phụ thuộc trên 18 tuổi, của nhân viên thuộc phòng ban có tên: Phòng Nghiên cứu và phát triển. 
--Thông tin yêu cầu: tên nhân viên, tên người phụ thuộc, mối liên hệ giữa người phụ thuộc với nhân viên
SELECT e.empName, dp.depName, dp.depRelationship
FROM tblDependent dp
    INNER JOIN tblEmployee e ON dp.empSSN = e.empSSN
    INNER JOIN tblDepartment d ON e.depNum = d.depNum
WHERE  (YEAR(GETDATE()) - YEAR(dp.depBirthdate) >= 18) AND d.depName = N'Phòng Nghiên cứu và phát triển';

--14.	Cho biết số lượng người phụ thuộc theo giới tính. 
--Thông tin yêu cầu: giới tính, số lượng người phụ thuộc
SELECT dp.depSex, COUNT(dp.empSSN) as dps
FROM tblDependent dp
GROUP BY dp.depSex;

--15.	Cho biết số lượng người phụ thuộc theo mối liên hệ với nhân viên. 
--Thông tin yêu cầu: mối liên hệ, số lượng người phụ thuộc
SELECT dp.depRelationship, COUNT(dp.empSSN) as dps
FROM tblDependent dp
GROUP BY dp.depRelationship;

--16.	Cho biết số lượng người phụ thuộc theo mỗi phòng ban. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng người phụ thuộc
SELECT d.depNum, d.depName, COUNT(*) as dps
FROM tblDependent dp
    INNER JOIN tblEmployee e ON dp.empSSN = e.empSSN
    INNER JOIN tblDepartment d ON e.depNum = d.depNum
GROUP BY d.depNum,
        d.depName;


--17.	Cho biết phòng ban nào có số lượng người phụ thuộc là ít nhất. 
-- Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng người phụ thuộc
WITH
    dp_eachdep
    AS
    (
        SELECT d.depNum, d.depName, COUNT(*) as dps
        FROM tblDependent dp
            INNER JOIN tblEmployee e ON dp.empSSN = e.empSSN
            INNER JOIN tblDepartment d ON e.depNum = d.depNum
        GROUP BY d.depNum,
            d.depName
    )
SELECT *
FROM dp_eachdep
WHERE dps = (SELECT MIN(dps)
FROM dp_eachdep);

--18.	Cho biết phòng ban nào có số lượng người phụ thuộc là nhiều nhất. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng người phụ thuộc
WITH
    dp_eachdep
    AS
    (
        SELECT d.depNum, d.depName, COUNT(*) as dps
        FROM tblDependent dp
            INNER JOIN tblEmployee e ON dp.empSSN = e.empSSN
            INNER JOIN tblDepartment d ON e.depNum = d.depNum
        GROUP BY d.depNum,
            d.depName
    )
SELECT *
FROM dp_eachdep
WHERE dps = (SELECT MAX(dps)
FROM dp_eachdep);

--19.	Cho biết tổng số giờ tham gia dự án của mỗi nhân viên. 
--Thông tin yêu cầu: mã nhân viên, tên nhân viên, tên phòng ban của nhân viên
SELECT
    e.empSSN, e.empName, d.depName, SUM(w.workHours) as total_ews
FROM tblEmployee e
    INNER JOIN tblWorksOn w ON e.empSSN = w.empSSN
    INNER JOIN tblDepartment d ON e.depNum = d.depNum
GROUP BY e.empSSN,
    e.empName,
    d.depName;

--20.	Cho biết tổng số giờ tham gia dự án của mỗi phòng ban.
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, tổng số giờ tham gia dự án
SELECT
    d.depnum,
    d.depName,
    SUM(w.workHours) as total_dws
FROM tblDepartment d
    INNER JOIN tblEmployee e ON d.depNum = e.depNum
    INNER JOIN tblWorksOn w ON e.empSSN = w.empSSN
GROUP BY d.depnum,d.depName;

--21.	Cho biết nhân viên nào có số giờ tham gia dự án là ít nhất. 
--Thông tin yêu cầu: mã nhân viên, tên nhân viên, tổng số giờ tham gia dự án
WITH
    ws
    AS
    (
        SELECT
            e.empSSN, e.empName, d.depName, SUM(w.workHours) as total_ews
        FROM tblEmployee e
            INNER JOIN tblWorksOn w ON e.empSSN = w.empSSN
            INNER JOIN tblDepartment d ON e.depNum = d.depNum
        GROUP BY e.empSSN,
            e.empName,
            d.depName
    )
SELECT *
FROM ws
WHERE total_ews = (SELECT MIN(total_ews)
FROM ws);

--22.	Cho biết nhân viên nào có số giờ tham gia dự án là nhiều nhất. 
--Thông tin yêu cầu: mã nhân viên, tên nhân viên, tổng số giờ tham gia dự án
WITH
    ws
    as
    (
        SELECT e.empSSN, e.empName, SUM(w.workHours) as total_ews
        FROM tblEmployee e
            INNER JOIN tblWorksOn w ON e.empSSN = w.empSSN
            INNER JOIN tblDepartment d ON e.depNum = d.depNum
        GROUP BY e.empSSN, e.empName
    )
SELECT *
FROM ws
WHERE total_ews = (SELECT MAX(total_ews)
from ws);


--23.	Cho biết những nhân viên nào lần đầu tiên tham gia dụ án. 
--Thông tin yêu cầu: mã nhân viên, tên nhân viên, tên phòng ban của nhân viên
WITH
	pc
	AS
(SELECT e.empSSN,e.empName,d.depName,COUNT(p.proNum) as total_pro
FROM tblEmployee e
INNER JOIN tblDepartment d ON e.depNum = d.depNum
INNER JOIN tblProject p ON p.depNum = d.depNum
GROUP BY e.empSSN,e.empName,d.depName)
SELECT empSSN,empName,depName
FROM pc
WHERE total_pro = 1; --Lần đầu tham gia dự án nên đếm số dự án tham gia là 1


-- 24.	Cho biết những nhân viên nào lần thứ hai tham gia dụ án. 
-- Thông tin yêu cầu: mã nhân viên, tên nhân viên, tên phòng ban của nhân viên
WITH
	pc
	AS
(SELECT e.empSSN,e.empName,d.depName,COUNT(p.proNum) as total_pro
FROM tblEmployee e
INNER JOIN tblDepartment d ON e.depNum = d.depNum
INNER JOIN tblProject p ON p.depNum = d.depNum
GROUP BY e.empSSN,e.empName,d.depName)
SELECT empSSN,empName,depName
FROM pc
WHERE total_pro = 2;

--25.	Cho biết những nhân viên nào tham gia tối thiểu hai dụ án. 
--Thông tin yêu cầu: mã nhân viên, tên nhân viên, tên phòng ban của nhân viên
WITH
	pc
	AS
(SELECT e.empSSN,e.empName,d.depName,COUNT(p.proNum) as total_pro
FROM tblEmployee e
INNER JOIN tblDepartment d ON e.depNum = d.depNum
INNER JOIN tblProject p ON p.depNum = d.depNum
GROUP BY e.empSSN,e.empName,d.depName)
SELECT empSSN,empName,depName
FROM pc
WHERE total_pro >= 2;


--26.	Cho biết số lượng thành viên của mỗi dự án. 
--Thông tin yêu cầu: mã dự án, tên dự án, số lượng thành viên
SELECT p.proNum,p.proName,COUNT(e.empSSN) as total_emp
FROM tblProject p
INNER JOIN tblEmployee e ON e.depNum = p.depNum
GROUP BY p.proNum,p.proName;

--27.	Cho biết tổng số giờ làm của mỗi dự án. 
--Thông tin yêu cầu: mã dự án, tên dự án, tổng số giờ làm
SELECT p.proNum,p.proName,SUM(w.workHours) as p_ws
FROM tblProject p 
INNER JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY p.proNum,p.proName;

--28.	Cho biết dự án nào có số lượng thành viên là ít nhất. 
--Thông tin yêu cầu: mã dự án, tên dự án, số lượng thành viên
WITH p_ec AS (
  SELECT p.proNum,
         p.proName,
         COUNT(e.empSSN) AS total_emp
  FROM tblProject p
  INNER JOIN tblEmployee e ON e.depNum = p.depNum
  GROUP BY p.proNum, p.proName
)
SELECT proNum,
       proName,
       total_emp
FROM p_ec
WHERE total_emp = (SELECT MIN(total_emp) FROM p_ec);

--29.	Cho biết dự án nào có số lượng thành viên là nhiều nhất. 
--Thông tin yêu cầu: mã dự án, tên dự án, số lượng thành viên
WITH p_ec AS (
  SELECT p.proNum,
         p.proName,
         COUNT(e.empSSN) AS total_emp
  FROM tblProject p
  INNER JOIN tblEmployee e ON e.depNum = p.depNum
  GROUP BY p.proNum, p.proName
)
SELECT proNum,
       proName,
       total_emp
FROM p_ec
WHERE total_emp = (SELECT MAX(total_emp) FROM p_ec);

--30.	Cho biết dự án nào có tổng số giờ làm là ít nhất. 
--Thông tin yêu cầu: mã dự án, tên dự án, tổng số giờ làm
WITH 
	pws
	AS
(SELECT p.proNum,p.proName,SUM(w.workHours) as total_ws
FROM tblProject p 
INNER JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY p.proNum,p.proName)
SELECT *
FROM pws
WHERE total_ws = (SELECT MIN(total_ws) FROM pws);

--31.	Cho biết dự án nào có tổng số giờ làm là nhiều nhất. 
--Thông tin yêu cầu: mã dự án, tên dự án, tổng số giờ làm
WITH 
	pws
	AS
(SELECT p.proNum,p.proName,SUM(w.workHours) as total_ws
FROM tblProject p 
INNER JOIN tblWorksOn w ON p.proNum = w.proNum
GROUP BY p.proNum,p.proName)
SELECT *
FROM pws
WHERE total_ws = (SELECT MAX(total_ws) FROM pws);

--32.	Cho biết số lượng phòng ban làm việc theo mỗi nơi làm việc. 
--Thông tin yêu cầu: tên nơi làm việc, số lượng phòng ban
SELECT l.locName,COUNT(dl.depNum) AS total_dep
FROM tblLocation l
INNER JOIN tblDepLocation dl ON l.locNum = dl.locNum
GROUP BY l.locName;


--33.	Cho biết số lượng chỗ làm việc theo mỗi phòng ban. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng chỗ làm việc
SELECT d.depNum,d.depName,COUNT(dl.depNum) AS total_dep
FROM tblDepartment d
INNER JOIN tblDepLocation dl ON d.depNum = dl.depNum
GROUP BY d.depNum,d.depName;

--34.	Cho biết phòng ban nào có nhiều chỗ làm việc nhất. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng chỗ làm việc
WITH
	lc_eachdep
	AS
(SELECT d.depNum,d.depName,COUNT(dl.depNum) AS total_dep
FROM tblDepartment d
INNER JOIN tblDepLocation dl ON d.depNum = dl.depNum
GROUP BY d.depNum,d.depName)
SELECT * 
FROM lc_eachdep
WHERE total_dep = (SELECT MAX(total_dep) FROM lc_eachdep);

--35.	Cho biết phòng ban nào có ít chỗ làm việc nhất. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng chỗ làm việc
WITH
	lc_eachdep
	AS
(SELECT d.depNum,d.depName,COUNT(dl.depNum) AS total_dep
FROM tblDepartment d
INNER JOIN tblDepLocation dl ON d.depNum = dl.depNum
GROUP BY d.depNum,d.depName)
SELECT * 
FROM lc_eachdep
WHERE total_dep = (SELECT MIN(total_dep) FROM lc_eachdep);

--36.	Cho biết địa điểm nào có nhiều phòng ban làm việc nhất. 
--Thông tin yêu cầu: tên nơi làm việc, số lượng phòng ban
WITH 
	dep_eachl
	AS
(SELECT l.locName,COUNT(dl.depNum) AS total_dep
FROM tblLocation l
INNER JOIN tblDepLocation dl ON l.locNum = dl.locNum
GROUP BY l.locName)
SELECT *
FROM dep_eachl
WHERE total_dep = (SELECT MAX(total_dep) FROM dep_eachl) ;

--37.	Cho biết địa điểm nào có ít phòng ban làm việc nhất. 
--Thông tin yêu cầu: tên nơi làm việc, số lượng phòng ban
WITH 
	dep_eachl
	AS
(SELECT l.locName,COUNT(dl.depNum) AS total_dep
FROM tblLocation l
INNER JOIN tblDepLocation dl ON l.locNum = dl.locNum
GROUP BY l.locName)
SELECT *
FROM dep_eachl
WHERE total_dep = (SELECT MIN(total_dep) FROM dep_eachl) ;

--38.	Cho biết nhân viên nào có nhiều người phụ thuộc nhất. 
--Thông tin yêu cầu: mã số, họ tên nhân viên, số lượng người phụ thuộc
WITH 
	dpc_eache 
	AS
(SELECT e.empSSN,e.empName,COUNT(*) as total_dp
FROM tblEmployee e
INNER JOIN tblDependent dp ON e.empSSN=dp.empSSN
GROUP BY e.empSSN,e.empName)
SELECT *
FROM dpc_eache
WHERE total_dp = (SELECT MAX(total_dp) FROM dpc_eache);

--39.	Cho biết nhân viên nào có ít người phụ thuộc nhất. 
--Thông tin yêu cầu: mã số, họ tên nhân viên, số lượng người phụ thuộc
WITH 
	dpc_eache 
	AS
(SELECT e.empSSN,e.empName,COUNT(*) as total_dp
FROM tblEmployee e
INNER JOIN tblDependent dp ON e.empSSN=dp.empSSN
GROUP BY e.empSSN,e.empName)
SELECT *
FROM dpc_eache
WHERE total_dp = (SELECT MIN(total_dp) FROM dpc_eache);


--40.	Cho biết nhân viên nào không có người phụ thuộc.
--Thông tin yêu cầu: mã số nhân viên, họ tên nhân viên, tên phòng ban của nhân viên
SELECT e.empSSN,e.empName,d.depName
FROM tblEmployee e
INNER JOIN tblDepartment d ON e.depNum = d.depNum
WHERE e.empSSN NOT IN (SELECT empSSN FROM tblDependent);

--41.	Cho biết phòng ban nào không có người phụ thuộc. 
--Thông tin yêu cầu: mã số phòng ban, tên phòng ban
SELECT DISTINCT d.depNum,d.depName
FROM tblDepartment d 
INNER JOIN tblEmployee e ON d.depNum = e.depNum
WHERE e.empSSN NOT IN (SELECT empSSN FROM tblDependent);

--42.	Cho biết những nhân viên nào chưa hề tham gia vào bất kỳ dự án nào. 
--Thông tin yêu cầu: mã số, tên nhân viên, tên phòng ban của nhân viên
WITH
	emp_d_p
	AS
(SELECT e.empSSN,e.empName,d.depName,p.proNum
FROM tblEmployee e 
INNER JOIN tblDepartment d ON e.depNum = d.depNum
LEFT JOIN tblProject p ON d.depNum = p.depNum)
SELECT empSSN,empName,depName
FROM emp_d_P
WHERE proNum is NULL;

--43.	Cho biết phòng ban không có nhân viên nào tham gia (bất kỳ) dự án. 
--Thông tin yêu cầu: mã số phòng ban, tên phòng ban
SELECT d.depNum,d.depName
FROM tblDepartment d
LEFT JOIN tblProject p ON d.depNum = p.depNum
WHERE p.proNum IS NULL;

--44.	Cho biết phòng ban không có nhân viên nào tham gia vào dự án có tên là ProjectA. 
--Thông tin yêu cầu: mã số phòng ban, tên phòng ban
SELECT d.depNum,d.depName,p.proName
FROM tblDepartment d
LEFT JOIN tblProject p ON d.depNum = p.depNum
WHERE p.proName = 'ProjectA' OR p.proNum IS NULL;

--45.	Cho biết số lượng dự án được quản lý theo mỗi phòng ban. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng dự án
SELECT d.depNum,d.depName,COUNT(p.proNum) as total_p
FROM tblDepartment d
LEFT JOIN tblProject p ON d.depNum = p.depNum
GROUP BY d.depNum,d.depName;

--46.	Cho biết phòng ban nào quản lý it dự án nhất. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng dự án
WITH 
	totalp_eachd
	AS
(SELECT d.depNum,d.depName,COUNT(p.proNum) as total_p
FROM tblDepartment d
LEFT JOIN tblProject p ON d.depNum = p.depNum
GROUP BY d.depNum,d.depName)
SELECT *
FROM totalp_eachd
WHERE total_p = (SELECT MIN(total_p) FROM totalp_eachd);

--47.	Cho biết phòng ban nào quản lý nhiều dự án nhất. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng dự án
WITH 
	totalp_eachd
	AS
(SELECT d.depNum,d.depName,COUNT(p.proNum) as total_p
FROM tblDepartment d
LEFT JOIN tblProject p ON d.depNum = p.depNum
GROUP BY d.depNum,d.depName)
SELECT *
FROM totalp_eachd
WHERE total_p = (SELECT MAX(total_p) FROM totalp_eachd);

--48.	Cho biết những phòng ban nào có nhiểu hơn 5 nhân viên đang quản lý dự án gì. 
--Thông tin yêu cầu: mã phòng ban, tên phòng ban, số lượng nhân viên của phòng ban, tên dự án quản lý
WITH 
    totale_p_eachd
    AS
(SELECT d.depNum,d.depName,COUNT(e.empSSN) as total_emp,p.proName
FROM tblDepartment d
INNER JOIN tblEmployee e ON d.depNum = e.depNum
INNER JOIN tblProject p ON d.depNum = p.depNum
GROUP BY d.depNum,d.depName,p.proName)
SELECT *
FROM totale_p_eachd
WHERE total_emp > 5;

--49.	Cho biết những nhân viên thuộc phòng có tên là Phòng nghiên cứu, và không có người phụ thuộc. Thông tin yêu cầu: mã nhân viên,họ tên nhân viên
SELECT e.empSSN,e.empName
FROM tblEmployee e
INNER JOIN tblDepartment d ON e.depNum = d.depNum
WHERE d.depName = N'Phòng Nghiên cứu và phát triển' AND e.empSSN NOT IN (SELECT empSSN FROM tblDependent);

--50.	Cho biết tổng số giờ làm của các nhân viên, mà các nhân viên này không có người phụ thuộc. 
--Thông tin yêu cầu: mã nhân viên,họ tên nhân viên, tổng số giờ làm
SELECT e.empSSN,e.empName,SUM(w.workHours) as totalws
FROM tblWorksOn w
INNER JOIN tblEmployee e ON w.empSSN = e.empSSN
WHERE e.empSSN NOT IN (SELECT empSSN FROM tblDependent)
GROUP BY e.empSSN,e.empName;

--51.	Cho biết tổng số giờ làm của các nhân viên, mà các nhân viên này có nhiều hơn 3 người phụ thuộc. 
--Thông tin yêu cầu: mã nhân viên,họ tên nhân viên, số lượng người phụ thuộc, tổng số giờ làm
WITH 
	ws_dps_eache
	AS
(SELECT e.empSSN,e.empName,SUM(w.workHours) as totalws,COUNT(dp.depName) as total_dps
FROM tblWorksOn w
INNER JOIN tblEmployee e ON w.empSSN = e.empSSN
INNER JOIN tblDependent dp ON e.empSSN = dp.empSSN
GROUP BY e.empSSN,e.empName)
SELECT *
FROM ws_dps_eache
WHERE total_dps>3;

--52.	Cho biết tổng số giờ làm việc của các nhân viên hiện đang dưới quyền giám sát (bị quản lý bởi) của nhân viên Mai Duy An. 
--Thông tin yêu cầu: mã nhân viên, họ tên nhân viên, tổng số giờ làm
SELECT e1.empSSN,e1.empName,SUM(w.workHours) as ws
FROM tblEmployee e1
INNER JOIN tblEmployee e2 ON e1.supervisorSSN = e2.empSSN
INNER JOIN tblWorksOn w ON e1.empSSN = w.empSSN
WHERE e2.empName = N'Mai Duy An'
GROUP BY e1.empSSN,e1.empName;
