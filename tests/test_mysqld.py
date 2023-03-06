from mysqld_integration_test import Mysqld
from mysqld_integration_test.settings import ConfigFile
import os
import pytest
import pytest_mock
from mock import patch
import mock
#from unittest.mock import patch

@pytest.mark.mysqld_test
def test_mysqld_init():
    mysqld = Mysqld()
    assert mysqld.base_dir is not None

@pytest.mark.mysqld_test
def test_mysqld_run_mariadb():
    mysqld = Mysqld()
    mysqld.config.variant = "mariadb"
    mysqld.config.version_major = 10
    mysqld.config.version_minor = "5.16"

    instance = mysqld.run()
    assert instance.username == 'root'


@pytest.mark.mysqld_test
def test_mysqld_run_mysql():
    mysqld = Mysqld()
    mysqld.config.variant = "mysql"
    mysqld.config.version_major = 8
    mysqld.config.version_minor = "0.30"

    instance = mysqld.run()
    assert instance.username == 'root'


@pytest.mark.mysqld_test
def test_mysqld_tmpdir_delete():
    mysqld = Mysqld()
    base_dir = mysqld.base_dir
    mysqld.close()
    assert not os.path.exists(base_dir)
