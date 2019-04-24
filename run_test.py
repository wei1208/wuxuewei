import pytest

from Common import Shell

if __name__ == '__main__':
    # pytest.main(['-s', '-q','./TestCase'])
    shell = Shell.Shell()

    pytest.main(['-s', '-q', '--alluredir', './Report/xml/', './TestCase'])
    cmd = "allure generate ./Report/xml/ -o ./Report/html/ --clean"
    try:
        shell.invoke(cmd)
    except Exception:
        print('XXX')

