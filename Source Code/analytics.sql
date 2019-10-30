CREATE OR REPLACE STREAM "DEST_STREAM"(
    "device_id"         VARCHAR(16),
    "manufacturer"      VARCHAR(16),
    "model"             VARCHAR(8),
    "pulse"             DOUBLE,
    "systolic"          DOUBLE,
    "diastolic"         DOUBLE,
    "ANOMALY_SCORE"     DOUBLE);

CREATE OR REPLACE PUMP "OUTPUT_PUMP" AS 
    INSERT INTO "DEST_STREAM"
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