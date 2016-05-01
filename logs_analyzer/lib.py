from logs_analyzer.settings import *
from logs_analyzer.validators import *
from datetime import datetime


def get_service_settings(service_name):
    """
    Get default settings for the said service
    :param service_name: service name (example: nginx, apache2...)
    :return: service settings if found or None
    """
    return SERVICES_SWITCHER.get(service_name)


def get_date_filter(service, minute=datetime.now().minute, hour=datetime.now().hour,
                    day=datetime.now().day, month=datetime.now().month,
                    year=datetime.now().year):
    """
    Get date filter that will be used to filter data from logs
    :param service: string
    :param minute: int
    :param hour: int
    :param day: int
    :param month: int
    :param year: int
    :return: string
    """
    settings = get_service_settings(service)
    if settings is None:
        raise Exception("There is no configuration for the service \""+service+"\"!")

    if not is_valid_year(year) or not is_valid_month(month) or not is_valid_day(day) \
            or not is_valid_hour(hour) or not is_valid_minute(minute):
        raise Exception("Date elements aren't valid")
    if minute != '*' and hour != '*':
        date_format = settings['dateminutes_format']
        date_filter = datetime(year, month, day, hour, minute).strftime(date_format)
    elif minute == '*' and hour != '*':
        date_format = settings['datehours_format']
        date_filter = datetime(year, month, day, hour).strftime(date_format)
    elif minute == '*' and hour == '*':
        date_format = settings['datedays_format']
        date_filter = datetime(year, month, day).strftime(date_format)
    else:
        raise Exception("Date elements aren't valid")
    return date_filter
