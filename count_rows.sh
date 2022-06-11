#!/bin/bash
docker exec -it spark-submit /bin/bash -c "
cd ../../app
spark-submit --master local[*] --deploy-mode client count_rows.py
"
