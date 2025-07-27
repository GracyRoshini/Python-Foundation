--DATABASE
Create database CrimeManagement

--TABLES
Create table Crime (CrimeID INT CONSTRAINT pk_crime_ID PRIMARY KEY, IncidentType VARCHAR(255), IncidentDate DATE, Location VARCHAR(255), Description TEXT, Status VARCHAR(20));

Create table Victim (VictimID INT CONSTRAINT pk_victim_ID PRIMARY KEY, CrimeID int CONSTRAINT fk_crime_ID FOREIGN KEY(CrimeID) REFERENCES Crime(CrimeID), Name VARCHAR(255), ContactInfo VARCHAR(255), Injuries VARCHAR(255));

Create table Suspect (SuspectID INT CONSTRAINT pk_suspect_ID PRIMARY KEY, CrimeID int CONSTRAINT fk1_crime_ID FOREIGN KEY(CrimeID) REFERENCES Crime(CrimeID), SuspectName VARCHAR(255), Description TEXT, CriminalHistory TEXT);

--INSERTING VALUES
Insert Crime values (1, 'Robbery', '2023-09-15', '123 Main St Cityville', 'Armed robbery at a convenience store', 'Open'), 
(2, 'Homicide', '2023-09-20', '456 Elm St, Townsville', 'Investigation into a murder case', 'Under Investigation'), 
(3, 'Theft', '2023-09-10', '789 Oak St, Villagetown', 'Shoplifting incident at a mall', 'Closed');

Insert into Victim values (1, 1, 'John Doe', 'johndoe@example.com', 'Minor injuries'), 
(2, 2, 'Jane Smith', 'janesmith@example.com', 'Deceased'),
(3, 3, 'Alice Johnson', 'alicejohnson@example.com', 'None');

Insert into Suspect values (1, 1, 'Robber 1', 'Armed and masked robber', 'Previous robbery convictions'),
(2, 2, 'Unknown', 'Investigation ongoing', NULL),
(3, 3, 'Suspect 1', 'Shoplifting suspect', 'Prior shoplifting arrests');

Insert into Crime Values (4, 'Assault', '2023-09-25', '101 Pine St, Metrocity', 'Street fight involving injuries', 'Closed');

Insert into Victim Values (4, 4, 'Charlie Evans', 'charlie@example.com', 'Bruises', 29);

Insert into Suspect Values (4, 4, 'Tom Hardy', 'Suspect in a street fight', 'No record', 31);

Alter table Victim add Age INT;
Alter table Suspect add Age INT;

Update Victim SET Age = 35 Where VictimID = 1; 
Update Victim SET Age = 28 Where VictimID = 2;  
Update Victim SET Age = 22 Where VictimID = 3;  

Update Suspect SET Age = 40 Where SuspectID = 1; 
Update Suspect SET Age = 30 Where SuspectID = 2;  
Update Suspect SET Age = 25 Where SuspectID = 3; 

Select * from Crime
Select * from Victim
Select * from Suspect

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---QUERIES---

-- 1) Select all open incidents
Select * from Crime where Status = 'Open';

--2) Find the total number of incidents
Select count(*) as TotalIncidents from Crime;

--3) List all unique incident types
Select Distinct IncidentType from Crime;

--4) Retrieve incidents that occurred between '2023-09-01' and '2023-09-30'
Select IncidentType from Crime where IncidentDate BETWEEN '2023-09-01' and '2023-09-30'

--5) List persons involved in incidents in descending order of age
Select * from Victim
Select * from Suspect

Select Name, Age, 'Victim' as Role From Victim
UNION
Select SuspectName, Age, 'Suspect' as Role From Suspect
Order by Age desc;

--6) Find the average age of persons involved in incidents
Select avg(Age) as AverageAgeOFVictimsANDSuspects From (Select Age from Victim 
                                                        UNION ALL
                                                        Select Age from Suspect) as AllPeople;

--7) List incident types and their counts, only for open cases
Select IncidentType, count(*) as CountOFIncidentsWithOpenCase
From Crime
Where Status = 'Open' 
Group by IncidentType;

--8) Find persons with names containing 'Doe'
Select Name from Victim Where Name LIKE '%Doe%'
UNION
Select SuspectName from Suspect Where SuspectName like '%Doe%';

--9) Retrieve names of persons involved in open and closed cases
Select * from Victim
Select * from Crime
Select * from Suspect

Select v.Name, 'Victim' as Role, c.Status
From Victim v
INNER JOIN Crime c
ON v.CrimeID = c.CrimeID
Where c.Status IN ('Open', 'Closed', 'Under Investigation')
UNION
Select s.SuspectName, 'Suspect' as Role, c.Status
from Suspect s
INNER JOIN Crime c
ON s.CrimeID = c.CrimeID
Where c.Status IN ('Open', 'Closed', 'Under Investigation');

--10) List incident types where persons aged 30 or 35 are involved
Select * from Crime
Select * from Victim
Select * from Suspect

Select Distinct c.IncidentType
From Crime c
INNER JOIN Victim v 
ON c.CrimeID = v.CrimeID
Where v.Age IN (30, 35)
UNION
Select Distinct c.IncidentType
From Crime c
INNER JOIN Suspect s
ON c.CrimeID = s.CrimeID
Where s.Age IN (30, 35);

--11) Find persons involved in incidents of the same type as 'Robbery'
Select Name From Victim
Where CrimeID IN (Select CrimeID From Crime Where IncidentType = 'Robbery')
UNION
Select SuspectName From Suspect
Where CrimeId IN (Select CrimeID From Crime Where IncidentType = 'Robbery');

--12) List incident types with more than one open case
Insert into Crime values (5, 'Robbery', '2023-09-28', '22 Lakeview Dr, Lakeside', 'Robbery at electronics store', 'Open');
Select * from Crime

Select IncidentType, count(*) as Count
From Crime
Where Status = 'Open' 
Group by IncidentType
Having count(*)>1;

--13) List all incidents with suspects whose names also appear as victims in other incidents
Insert into Crime values (6, 'Robbery', '2023-09-30', '99 Park Lane, Rivercity', 'Late night ATM robbery', 'Open');
Insert into Suspect values (6, 6, 'John Doe', 'Repeat offender caught on camera', 'Prior robbery', 36);

Select * from Crime
Select * from Suspect
Select * from Victim

Select s.SuspectName, c.IncidentType
From Crime c
INNER JOIN Suspect s
ON c.CrimeID = s.CrimeID
Where s.SuspectName In (Select Name from Victim);

--14) Retrieve all incidents along with victim and suspect details
Select c.*, v.*, s.* From Crime c
LEFT JOIN Victim v
ON c.CrimeID = v.CrimeID
LEFT JOIN Suspect s
ON c.CrimeID = s.CrimeID;

--15) Find incidents where the suspect is older than any victim
Select * from Crime
Select * from Suspect
Select * from Victim

Select c.IncidentType, c.IncidentDate, s.SuspectName
From Crime c
INNER JOIN Suspect s
ON c.CrimeID = s.CrimeID
Where s.Age > 
ALL (Select Age From Victim v Where v.CrimeID = c.CrimeID)

--16) Find suspects involved in multiple incidents
Select SuspectName, count(*) as IncidentCount
From Suspect
Group by SuspectName
Having count(*)>1;

--17) List incidents with no suspects involved
Select * from Crime 
Select * from Suspect

Select c.IncidentDate, c.IncidentType, c.crimeID from Crime c
LEFT JOIN Suspect s
ON c.CrimeID = s.CrimeID
Where s.CrimeID IS NULL

--18) List all cases where at least one incident is 'Homicide' and all others are 'Robbery'
Select * from Crime
Where 'Homicide' IN (Select IncidentType from Crime)
and Not Exists (Select CrimeID From Crime where IncidentType Not In ('Homicide', 'Robbery'));

--19) Retrieve all incidents and the associated suspects, showing 'No Suspect' if none
Select * from Crime
Select * from Suspect

Select c.CrimeID, c.IncidentType, s.SuspectName 
From Crime c
INNER JOIN Suspect s
ON c.CrimeID = s.CrimeID
UNION
Select c.CrimeID, c.IncidentType, 'No Suspect' as SuspectName
From Crime c
Where c.CrimeID NOT IN (Select CrimeID from Suspect);

--20) List all suspects who have been involved in incidents with incident types 'Robbery' or 'Assault'
Select s.SuspectID, s.SuspectName , s.CrimeID from Suspect s
INNER JOIN Crime c
ON s.CrimeID = c.CrimeID
Where c.IncidentType IN ('Robbery', 'Assault')