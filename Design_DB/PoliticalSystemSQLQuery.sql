/*

CREATE TABLE [Person] (
	PersonID integer IDENTITY PRIMARY KEY NOT NULL,
	FirstName varchar(30) NOT NULL,
	LastName varchar(30) NOT NULL,
	VoteFor varchar(30),
	BirthDate date,
  
  )

  
  CREATE TABLE [Country] (
	CountryID integer IDENTITY PRIMARY KEY NOT NULL,
	CountryName varchar(50) NOT NULL,
	City varchar(50) NOT NULL,
	BirthDate date,
	Languag varchar(30)
  
)


CREATE TABLE [GovermentPosition] (
	PositoinID integer IDENTITY PRIMARY KEY NOT NULL,
	TypePosition varchar(50) NOT NULL,
	StartDate date,
	FinishDate date,
	ReportsTo integer REFERENCES [GovermentPosition](PositoinID)

)


CREATE TABLE [PoliticalType] (
	PoliticalTypeID integer IDENTITY PRIMARY KEY NOT NULL,
	PoliticalType varchar(50) 

)


CREATE TABLE [CountryPolitic] (
	CountryID integer REFERENCES [Country](CountryID) NOT NULL,
	PoliticalTypeID integer REFERENCES [PoliticalType](PoliticalTypeID) NOT NULL,
	StartDate date NOT NULL
	PRIMARY KEY (CountryID, PoliticalTypeID)

)


CREATE TABLE [Citizenship] (
	PersonID integer REFERENCES [Person](PersonID) NOT NULL,
	CountryID integer REFERENCES [Country](CountryID) NOT NULL,
	AcceptDate date 
	PRIMARY KEY (CountryID, PersonID)
 
)


CREATE TABLE [Vouting] (
	PersonID integer REFERENCES [Person](PersonID) NOT NULL,
	PositionID integer REFERENCES [GovermentPosition](PositoinID) NOT NULL,
	VotingDate date 
	PRIMARY KEY (PositionID, PersonID)

)

*/
