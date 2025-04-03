import getopt
import sys
import os
from benchmarking.workload.workload import runWorkload
from benchmarking.data_types.data_types import IndexTypes, WorkloadTypes
from benchmarking.results import writeDataInCSV
import config
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/benchmarking/files/vector_search.log'),
        logging.StreamHandler()
    ]
)

def main():

    workload_names = os.environ.get("workload", [])
    index_type = os.environ.get("index_type", "all")
    workload_type = os.environ.get("workload_type", WorkloadTypes.INDEX_AND_SEARCH)
    run_id = os.environ.get("run_id", None)

    if len(workload_names) != 0:
        workload_names = workload_names.split(",")

    if run_id is not None:
        config.run_id = run_id

    if workload_type != WorkloadTypes.INDEX_AND_SEARCH:
        workload_type = WorkloadTypes.from_str(workload_type)

    runWorkload(workload_names, index_type, workload_type)
    # writeDataInCSV(workload_names, index_type, workload_type)


if __name__ == "__main__":
    main()
