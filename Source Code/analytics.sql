CREATE OR REPLACE STREAM "DEST_STREAM_1"(
    "device_id"         VARCHAR(16),
    "manufacturer"      VARCHAR(16),
    "model"             VARCHAR(8),
    "pulse"             DOUBLE,
    "systolic"          DOUBLE,
    "diastolic"         DOUBLE,
    "ANOMALY_SCORE"     DOUBLE);

CREATE OR REPLACE STREAM "DEST_STREAM_2"(
    "device_id"         VARCHAR(16),
    "manufacturer"      VARCHAR(16),
    "model"             VARCHAR(8),
    "pulse"             DOUBLE,
    "systolic"          DOUBLE,
    "diastolic"         DOUBLE,
    "ANOMALY_SCORE"     DOUBLE);

CREATE OR REPLACE PUMP "OUTPUT_PUMP_1" AS 
    INSERT INTO "DEST_STREAM_1"
        SELECT STREAM
            "device_id",
            "manufacturer",
            "model",
            "pulse",
            "systolic",
            "diastolic",
            ANOMALY_SCORE 
        FROM TABLE(RANDOM_CUT_FOREST(
            CURSOR(SELECT STREAM * FROM "SOURCE_SQL_STREAM_001")));

CREATE OR REPLACE PUMP "OUTPUT_PUMP_2" AS 
    INSERT INTO "DEST_STREAM_2"
    SELECT STREAM * FROM "DEST_STREAM_1";