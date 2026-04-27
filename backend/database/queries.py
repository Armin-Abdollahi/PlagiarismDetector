CREATE_RESULTS_TABLE = """
CREATE TABLE IF NOT EXISTS analysis_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reference_text LONGTEXT NOT NULL,
    suspect_text LONGTEXT NOT NULL,
    lexical_score FLOAT NOT NULL,
    semantic_score FLOAT NOT NULL,
    structure_score FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

INSERT_RESULT = """
INSERT INTO analysis_results (
    reference_text,
    suspect_text,
    lexical_score,
    semantic_score,
    structure_score
) VALUES (%s, %s, %s, %s, %s);
"""

SELECT_RESULT_BY_ID = """
SELECT
    id,
    reference_text,
    suspect_text,
    lexical_score,
    semantic_score,
    structure_score,
    created_at
FROM analysis_results
WHERE id = %s;
"""

SELECT_LATEST_RESULTS = """
SELECT
    id,
    lexical_score,
    semantic_score,
    structure_score,
    created_at
FROM analysis_results
ORDER BY created_at DESC
LIMIT %s;
"""
