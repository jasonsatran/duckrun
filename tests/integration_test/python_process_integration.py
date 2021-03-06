import unittest
import os
from duckrun.generic_process import GenericProcess
from duckrun.generic_process_factory import GenericFileProcessFactory
from duckrun.py.py_processor import PyProcessor
from duckrun.container import Container
from duckrun.process_report import ProcessReport

if __name__ == '__main__':
    relative_resource_path = "../resources/py"
    this_file_dir = os.path.dirname(__file__)
    test_file_path = os.path.join(this_file_dir, relative_resource_path)
    abs_path = os.path.abspath(test_file_path)
    processes = GenericFileProcessFactory.load_from_dir(abs_path)
    processor = PyProcessor()
    container = Container(processor, processes)
    container.run()
    process_report = ProcessReport(processes)
    process_report.print()
