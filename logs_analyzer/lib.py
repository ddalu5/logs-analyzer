import re
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


def get_date_filter(settings, minute=datetime.now().minute, hour=datetime.now().hour,
                    day=datetime.now().day, month=datetime.now().month,
                    year=datetime.now().year):
    """
    Get date filter that will be used to filter data from logs based on the params
    :raises Exception:
    :param settings: dict
    :param minute: int
    :param hour: int
    :param day: int
    :param month: int
    :param year: int
    :return: string
    """
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


def filter_data(log_filter, data=None, filepath=None, is_casesensitive=True, is_regex=False):
    """
    Filter received data/file content and return the results
    :except IOError:
    :except EnvironmentError:
    :raises Exception:
    :param log_filter: string
    :param data: string
    :param filepath: string
    :param is_casesensitive: boolean
    :param is_regex: boolean
    :return: string
    """
    return_data = ""
    if filepath:
        try:
            with open(filepath, 'r') as file_object:
                for line in file_object:
                    if __check_match(line, log_filter, is_regex, is_casesensitive):
                        return_data += line
            return return_data
        except (IOError, EnvironmentError) as e:
            print(e.strerror)
            exit(2)
    elif data:
        for line in data.splitlines():
            if __check_match(line, log_filter, is_regex, is_casesensitive):
                return_data += line+"\n"
        return return_data
    else:
        raise Exception("Data and filepath values are NULL!")


def __check_match(line, filter_pattern, is_regex, is_casesensitive):
    """
    Check if line contains/matches filter patter
    :param line: string
    :param filter_pattern: string
    :param is_regex: boolean
    :param is_casesensitive: boolean
    :return: boolean
    """
    if is_regex:
        return re.match(filter_pattern, line) if is_casesensitive else re.match(filter_pattern, line, re.IGNORECASE)
    else:
        return (filter_pattern in line) if is_casesensitive else (filter_pattern.lower() in line.lower())


def get_web_requests(data, pattern):
    """
    Analyze data (from the logs) and return list of requests formatted as the model (pattern) defined.
    :param data:
    :param pattern:
    :return: list of dicts
    """
    requests_dict = re.findall(pattern, data)
    requests = []
    for request_tuple in requests_dict:
        requests.append({'IP': request_tuple[0], 'datetime': request_tuple[1], 'method': request_tuple[2],
                         'route': request_tuple[3], 'code': request_tuple[4], 'referrer': request_tuple[5],
                         'useragent': request_tuple[6]})
    return requests


def get_auth_requests(data, pattern):
    requests_dict = re.findall(pattern, data)
    requests = []
    for request_tuple in requests_dict:
        requests.append({'datetime': request_tuple[0], 'service': request_tuple[1],
                         'IP': request_tuple[2], 'info': request_tuple[3]})
    return requests
