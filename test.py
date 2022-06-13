import pytest
import os
from main import D_data


@pytest.fixture()
def instance():
    obj = D_data()
    return obj


# Check if a file extension is .csv
def test_Extension(instance):
    if instance.data_file.lower().endswith('.csv'):
        print('file has .csv ext')

    else:
        assert False


# Check file is empty or not
def test_check(instance):
    file_path = instance.data_file
    if os.stat(file_path).st_size == 0:
        print("File is empty")
    else:
        print("File is not empty")








