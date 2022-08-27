BEGIN 
    DROP TABLE accidentData
END
GO;

CREATE TABLE accidentData (
    [ID] nvarchar(4000),
    [Severity] nvarchar(4000),
    [Start_Time] nvarchar(4000)
)
go;

INSERT INTO accidentData 
SELECT ID, Severity, Start_Time
FROM staging_accidents

go;


