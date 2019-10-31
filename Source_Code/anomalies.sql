-- Compute an anomaly score for each record in the source stream using Random Cut Forest
-- Creates a temporary stream and defines a schema
CREATE OR REPLACE STREAM "TEMP_STREAM_1" (
   "device_id"       VARCHAR(16),
   "manufacturer"    VARCHAR(16),
   "model"           VARCHAR(16),
   "temperature"     integer,
   "pulse"           integer,
   "oxygen_percent"  integer,
   "systolic"        integer,
   "diastolic"       integer,
   "anomaly_score"   double
);

-- Compute an anomaly score for each record in the source stream
-- using Random Cut Forest
CREATE OR REPLACE PUMP "STREAM_PUMP" AS 
INSERT INTO "TEMP_STREAM_1"
SELECT STREAM
     "device_id", 
     "manufacturer", 
     "model", 
     "temperature", 
     "pulse", 
     "oxygen_percent", 
     "systolic", 
     "diastolic", 
     "anomaly_score" 
FROM 
TABLE(RANDOM_CUT_FOREST(
   CURSOR(SELECT STREAM 
       "device_id", 
       "manufacturer", 
       "model", 
       "temperature", 
       "pulse", 
       "oxygen_percent", 
       "systolic", 
       "diastolic"
   FROM "SOURCE_STREAM_001")
 )
);

CREATE OR REPLACE STREAM "TEMP_STREAM_2" (
     "device_id"       VARCHAR(16),
     "manufacturer"    VARCHAR(16),
     "model"           VARCHAR(16),
     "temperature"     integer,
     "pulse"           integer,
     "oxygen_percent"  integer,
     "systolic"        integer,
     "diastolic"       integer,
     "anomaly_score"   double
);

CREATE OR REPLACE PUMP "STREAM_PUMP_2" AS 
INSERT INTO "TEMP_STREAM_2"
SELECT STREAM *
FROM "TEMP_STREAM_1";