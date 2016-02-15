from qautobots.framework.connection import get_application_settings
from qautobots.framework.qanfig import get_config


def get_api_config(api):
    """Get config for api connection

    :param str api: The API to connect to.
    :returns: :obj:`dict` containting the connection information needed to the
        specified API with :mode:`requests`.

    """
    config = get_config()
    api_config = config['apis'][api]
    return api_config


def get_cookie_support():
    """Get cookies configuration from config file

    Cookie support is a cookie that will be sent to browser
    indicating that the browser is supporting cookie from
    application.
    """
    config = get_config()
    cookies = config['cookie_support']
    cookies['domain'] = get_application_settings()['host']
    return cookies


def get_db_config(database):
    """Get config for database connection

    :param str database: The type of database to connect to. Same as
        :func:`remunerator.stored_procedures.get_db_connection`
        :attr:`database` argument

    :returns: :obj:`dict` containing the connection information needed to
        connect to postgres using :mod:`psycopg2`.

    """
    config = get_config()

    user = config['connections'][database]['user']
    database_config = config['guitests']['postgresql']['users']

    if user not in database_config:
        raise KeyError('User "{0}" does not exist in the config'.format(user))

    new_config = {
        'host': database_config[user]['host'],
        'user': user,
        'password': database_config[user]['password'],
        'port': database_config[user]['port'],
    }
    return new_config


def get_current_browser():
    """Get the browser that is currently in use by GUI-Tests"""

    config = get_config()

    return config['selenium']['browser']
