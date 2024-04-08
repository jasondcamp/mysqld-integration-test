from mysqld_integration_test import Mysqld
import pytest


@pytest.mark.skip
@pytest.mark.integration_test
@pytest.mark.integration_mysql_test
def test_mysqld_run_mysql():
    mysqld = Mysqld(mysqld_binary='tests/data/binaries/mysql-8.0.32-linux-glibc2.17-x86_64-minimal/bin/mysqld')
    instance = mysqld.run()
    assert instance.username == 'root'
