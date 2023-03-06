from mysqld_integration_test import Mysqld
import os
import pytest
# import pytest_mock


@pytest.mark.mysqld_test
def test_mysqld_init():
    mysqld = Mysqld()
    assert mysqld.base_dir is not None


@pytest.mark.mysqld_test
def test_mysqld_run_mariadb():
    mysqld = Mysqld(mysqld_binary='mariadb-10.11.2-linux-systemd-x86_64/bin/mysqld',
                    mysql_install_db_binary='mariadb-10.11.2-linux-systemd-x86_64/scripts/mysql_install_db')
    instance = mysqld.run()
    assert instance.username == 'root'


@pytest.mark.xfail
@pytest.mark.mysqld_test
def test_mysqld_run_mysql():
    mysqld = Mysqld(mysqld_binary='mysql-8.0.32-linux-glibc2.17-x86_64-minimal/bin/mysqld')
    instance = mysqld.run()
    assert instance.username == 'root'


@pytest.mark.mysqld_test
def test_mysqld_tmpdir_delete():
    mysqld = Mysqld()
    base_dir = mysqld.base_dir
    mysqld.close()
    assert not os.path.exists(base_dir)
