#!/usr/bin/env bash
set -e

#
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# 
docker exec -it sample-celery-terminal python -m add_delay.run

# Result
# 1767809324.2277575 add start
# 1767809324.3557348 add value: 30
# 1767809324.3558233 add start
# 1767809334.3922367 add (slow) value: 30
