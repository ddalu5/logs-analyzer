# Logs-analyzer

![Codeship Status for ddalu5/logs-analyzer](https://codeship.com/projects/b12161a0-f65e-0133-0e7a-7e18ff1a37b8/status?branch=master)

Logs-analyzer is a library containing functions that can help you extract usable data from logs.

## How to install
using pip : `pip install logs-analyzer`

## Settings

Contains the default settings for the supported logs.

### NGINX Settings
```
DEFAULT_NGINX = {
    'dir_path': '/var/log/nginx/',
    'accesslog_filename': 'access.log',
    'errorlog_filename': 'error.log',
    'dateminutes_format': '[%d/%b/%Y:%H:%M',
    'datehours_format': '[%d/%b/%Y:%H',
    'datedays_format': '[%d/%b/%Y',
    'request_model': (r''
                      '(\d+.\d+.\d+.\d+)\s-\s-\s'
                      '\[(.+)\]\s'
                      '(?i)"?(GET|POST|PUT|HEAD|DELETE|OPTIONS|CONNECT|PATCH)\s(.+)\s\w+/.+"'
                      '\s(\d+)\s'
                      '\d+\s"(.+)"\s'
                      '"(.+)"'),
    'date_pattern': (r''
                     '(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+)'),
    'date_keys': {'day': 0, 'month': 1, 'year': 2, 'hour': 3, 'minute': 4, 'second': 5}
}
```

### Apache2 Settings
```
DEFAULT_APACHE2 = {
    'dir_path': '/var/log/apache2/',
    'accesslog_filename': 'access.log',
    'errorlog_filename': 'error.log',
    'dateminutes_format': '[%d/%b/%Y:%H:%M',
    'datehours_format': '[%d/%b/%Y:%H',
    'datedays_format': '[%d/%b/%Y',
    'request_model': (r''
                      '(\d+.\d+.\d+.\d+)\s-\s-\s'
                      '\[(.+)\]\s'
                      '(?i)"?(\w+)\s(.+)\s\w+/.+"'
                      '\s(\d+)\s'
                      '\d+\s"(.+)"\s'
                      '"(.+)"'),
    'date_pattern': (r''
                     '(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+)'),
    'date_keys': {'day': 0, 'month': 1, 'year': 2, 'hour': 3, 'minute': 4, 'second': 5}
}
```
### Auth Settings
```
DEFAULT_AUTH = {
    'dir_path': '/var/log/',
    'accesslog_filename': 'auth.log',
    'dateminutes_format': '%b %e %H:%M:',
    'datehours_format': '%b %e %H:',
    'datedays_format': '%b %e ',
    'request_model': (r''
                      '(\w+\s\s\d+\s\d+:\d+:\d+)\s'
                      '\w+\s(\w+)\[\d+\]:\s'
                      '(.+)'),
    'date_pattern': (r''
                     '(\w+)\s(\s\d+|\d+)\s(\d+):(\d+):(\d+)'),
    'date_keys': {'month': 0, 'day': 1, 'hour': 2, 'minute': 3, 'second': 4}
}
```

## Main functions

### Function get_service_settings
#### Description
Get default settings for the said service from the settings file, three type
of logs are supported right now: `nginx`, `apache2` and `auth`.
#### Parameters
**service_name:** service name  (e.g. nginx, apache2...).
#### Return
Returns a dictionary containing the chosen service settings or `None` if the
service doesn't exists.
#### Sample
`nginx_settings = get_service_settings('nginx')`

### Function get_date_filter
#### Description
Get the date pattern that can be used to filter data from
logs based on the parameters.
#### Parameters
**settings:** the target logs settings.
**minute:** default now, minutes or * to ignore.
**hour:** default now, hours or * to ignore.
**day:** default now, day of month.
**month:** default now, month number.
**year:** default now, year.