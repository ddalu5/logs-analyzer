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
                      '"(.+)"')
}


SERVICES_SWITCHER = {
    'nginx': DEFAULT_NGINX
}
