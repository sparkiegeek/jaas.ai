# flake8: noqa

search_data = [{'Id': 'cs:apache2-26', 'Meta': {'charm-metadata': {'Name': 'apache2', 'Summary': 'Apache HTTP Server metapackage', 'Description': "The Apache Software Foundation's goal is to build a secure, efficient\nand extensible HTTP server as standards-compliant open source\nsoftware. The result has long been the number one web server on the\nInternet.  It features support for HTTPS, virtual hosting, CGI, SSI,\nIPv6, easy scripting and database integration, request/response\nfiltering, many flexible authentication schemes, and more.\n", 'Subordinate': False, 'Provides': {'apache-website': {'Name': 'apache-website', 'Role': 'provider', 'Interface': 'apache-website', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'local-monitors': {'Name': 'local-monitors', 'Role': 'provider', 'Interface': 'local-monitors', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'logs': {'Name': 'logs', 'Role': 'provider', 'Interface': 'logs', 'Optional': False, 'Limit': 0, 'Scope': 'global'}, 'nrpe-external-master': {'Name': 'nrpe-external-master', 'Role': 'provider', 'Interface': 'nrpe-external-master', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'balancer': {'Name': 'balancer', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'logging': {'Name': 'logging', 'Role': 'requirer', 'Interface': 'syslog', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'reverseproxy': {'Name': 'reverseproxy', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'vhost-config': {'Name': 'vhost-config', 'Role': 'requirer', 'Interface': 'apache-vhost-config', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'website-cache': {'Name': 'website-cache', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Tags': ['app-servers'], 'SupportedSeries': ['xenial', 'trusty', 'bionic'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'apache2-charmers'}, 'promulgated': {'Promulgated': True}, 'supported-series': {'SupportedSeries': ['xenial', 'trusty', 'bionic']}}}, {'Id': 'cs:~apache2-subordinate-charmers/apache2-subordinate-0', 'Meta': {'charm-metadata': {'Name': 'apache2-subordinate', 'Summary': 'Apache2 subordinate charm', 'Description': 'Apache2 subordinate charm', 'Subordinate': True, 'Provides': {'log-archive': {'Name': 'log-archive', 'Role': 'provider', 'Interface': 'log-archive', 'Optional': False, 'Limit': 0, 'Scope': 'global'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'webservice': {'Name': 'webservice', 'Role': 'requirer', 'Interface': 'webservice', 'Optional': False, 'Limit': 1, 'Scope': 'container'}}, 'Categories': ['app-servers'], 'SupportedSeries': ['xenial', 'bionic', 'trusty'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'apache2-subordinate-charmers'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['xenial', 'bionic', 'trusty']}}}, {'Id': 'cs:precise/apache2-passenger-6', 'Meta': {'charm-metadata': {'Name': 'apache2-passenger', 'Summary': 'Rails and Rack support for Apache2', 'Description': "Phusion Passenger is an application server for Ruby (Rack) apps.\nIt allows you to get your web apps online with the least amount of hassle, by taking\ncare of pretty much all of the heavy lifting for you when it comes to managing\nyour apps' processes and resources.\n", 'Subordinate': False, 'Provides': {'god': {'Name': 'god', 'Role': 'provider', 'Interface': 'god', 'Optional': True, 'Limit': 0, 'Scope': 'container'}, 'rack': {'Name': 'rack', 'Role': 'provider', 'Interface': 'rack', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Categories': ['app-servers'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'charmers'}, 'promulgated': {'Promulgated': True}, 'supported-series': {'SupportedSeries': ['precise']}}}, {'Id': 'cs:~ack/apache2-2', 'Meta': {'charm-metadata': {'Name': 'apache2', 'Summary': 'Apache HTTP Server metapackage', 'Description': "The Apache Software Foundation's goal is to build a secure, efficient\nand extensible HTTP server as standards-compliant open source\nsoftware. The result has long been the number one web server on the\nInternet.  It features support for HTTPS, virtual hosting, CGI, SSI,\nIPv6, easy scripting and database integration, request/response\nfiltering, many flexible authentication schemes, and more.\n", 'Subordinate': False, 'Provides': {'apache-website': {'Name': 'apache-website', 'Role': 'provider', 'Interface': 'apache-website', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'local-monitors': {'Name': 'local-monitors', 'Role': 'provider', 'Interface': 'local-monitors', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'logs': {'Name': 'logs', 'Role': 'provider', 'Interface': 'logs', 'Optional': False, 'Limit': 0, 'Scope': 'global'}, 'nrpe-external-master': {'Name': 'nrpe-external-master', 'Role': 'provider', 'Interface': 'nrpe-external-master', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'balancer': {'Name': 'balancer', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'logging': {'Name': 'logging', 'Role': 'requirer', 'Interface': 'syslog', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'reverseproxy': {'Name': 'reverseproxy', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'vhost-config': {'Name': 'vhost-config', 'Role': 'requirer', 'Interface': 'apache-vhost-config', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'website-cache': {'Name': 'website-cache', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Tags': ['app-servers'], 'SupportedSeries': ['xenial', 'trusty'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'ack'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['xenial', 'trusty']}}}, {'Id': 'cs:~mthaddon/apache2-0', 'Meta': {'charm-metadata': {'Name': 'apache2', 'Summary': 'Apache HTTP Server metapackage', 'Description': "The Apache Software Foundation's goal is to build a secure, efficient\nand extensible HTTP server as standards-compliant open source\nsoftware. The result has long been the number one web server on the\nInternet.  It features support for HTTPS, virtual hosting, CGI, SSI,\nIPv6, easy scripting and database integration, request/response\nfiltering, many flexible authentication schemes, and more.\n", 'Subordinate': False, 'Provides': {'apache-website': {'Name': 'apache-website', 'Role': 'provider', 'Interface': 'apache-website', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'local-monitors': {'Name': 'local-monitors', 'Role': 'provider', 'Interface': 'local-monitors', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'logs': {'Name': 'logs', 'Role': 'provider', 'Interface': 'logs', 'Optional': False, 'Limit': 0, 'Scope': 'global'}, 'nrpe-external-master': {'Name': 'nrpe-external-master', 'Role': 'provider', 'Interface': 'nrpe-external-master', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'balancer': {'Name': 'balancer', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'logging': {'Name': 'logging', 'Role': 'requirer', 'Interface': 'syslog', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'reverseproxy': {'Name': 'reverseproxy', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'vhost-config': {'Name': 'vhost-config', 'Role': 'requirer', 'Interface': 'apache-vhost-config', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'website-cache': {'Name': 'website-cache', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Tags': ['app-servers'], 'SupportedSeries': ['xenial', 'trusty'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'mthaddon'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['xenial', 'trusty']}}}, {'Id': 'cs:~charmers/trusty/apache2-20', 'Meta': {'charm-metadata': {'Name': 'apache2', 'Summary': 'Apache HTTP Server metapackage', 'Description': "The Apache Software Foundation's goal is to build a secure, efficient\nand extensible HTTP server as standards-compliant open source\nsoftware. The result has long been the number one web server on the\nInternet.  It features support for HTTPS, virtual hosting, CGI, SSI,\nIPv6, easy scripting and database integration, request/response\nfiltering, many flexible authentication schemes, and more.\n", 'Subordinate': False, 'Provides': {'apache-website': {'Name': 'apache-website', 'Role': 'provider', 'Interface': 'apache-website', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'local-monitors': {'Name': 'local-monitors', 'Role': 'provider', 'Interface': 'local-monitors', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'logs': {'Name': 'logs', 'Role': 'provider', 'Interface': 'logs', 'Optional': False, 'Limit': 0, 'Scope': 'global'}, 'nrpe-external-master': {'Name': 'nrpe-external-master', 'Role': 'provider', 'Interface': 'nrpe-external-master', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'balancer': {'Name': 'balancer', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'logging': {'Name': 'logging', 'Role': 'requirer', 'Interface': 'syslog', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'reverseproxy': {'Name': 'reverseproxy', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'vhost-config': {'Name': 'vhost-config', 'Role': 'requirer', 'Interface': 'apache-vhost-config', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'website-cache': {'Name': 'website-cache', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Tags': ['app-servers'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'charmers'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['trusty']}}}, {'Id': 'cs:~ack/xenial/apache2-xenial-1', 'Meta': {'charm-metadata': {'Name': 'apache2', 'Summary': 'Apache HTTP Server metapackage', 'Description': "The Apache Software Foundation's goal is to build a secure, efficient\nand extensible HTTP server as standards-compliant open source\nsoftware. The result has long been the number one web server on the\nInternet.  It features support for HTTPS, virtual hosting, CGI, SSI,\nIPv6, easy scripting and database integration, request/response\nfiltering, many flexible authentication schemes, and more.\n", 'Subordinate': False, 'Provides': {'apache-website': {'Name': 'apache-website', 'Role': 'provider', 'Interface': 'apache-website', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'local-monitors': {'Name': 'local-monitors', 'Role': 'provider', 'Interface': 'local-monitors', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'logs': {'Name': 'logs', 'Role': 'provider', 'Interface': 'logs', 'Optional': False, 'Limit': 0, 'Scope': 'global'}, 'nrpe-external-master': {'Name': 'nrpe-external-master', 'Role': 'provider', 'Interface': 'nrpe-external-master', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'balancer': {'Name': 'balancer', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'logging': {'Name': 'logging', 'Role': 'requirer', 'Interface': 'syslog', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'reverseproxy': {'Name': 'reverseproxy', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'vhost-config': {'Name': 'vhost-config', 'Role': 'requirer', 'Interface': 'apache-vhost-config', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'website-cache': {'Name': 'website-cache', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Tags': ['app-servers'], 'SupportedSeries': ['xenial', 'trusty'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'ack'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['xenial']}}}, {'Id': 'cs:~abentley/trusty/apache2-reverseproxy-4', 'Meta': {'charm-metadata': {'Name': 'apache2-reverseproxy', 'Summary': 'Configure an Apache instance to reverse-proxy a site.', 'Description': 'This is a subordinate charm for Apache.  This allows configuration to live\nnear Apache, and still be easy to manage.\n', 'Subordinate': True, 'Requires': {'extension': {'Name': 'extension', 'Role': 'requirer', 'Interface': 'juju-info', 'Optional': False, 'Limit': 1, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Categories': ['misc'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'abentley'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['trusty']}}}, {'Id': 'cs:~evarlast/trusty/apache2-10', 'Meta': {'charm-metadata': {'Name': 'apache2', 'Summary': 'Apache HTTP Server metapackage', 'Description': "The Apache Software Foundation's goal is to build a secure, efficient\nand extensible HTTP server as standards-compliant open source\nsoftware. The result has long been the number one web server on the\nInternet.  It features support for HTTPS, virtual hosting, CGI, SSI,\nIPv6, easy scripting and database integration, request/response\nfiltering, many flexible authentication schemes, and more.\n", 'Subordinate': False, 'Provides': {'apache-website': {'Name': 'apache-website', 'Role': 'provider', 'Interface': 'apache-website', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'local-monitors': {'Name': 'local-monitors', 'Role': 'provider', 'Interface': 'local-monitors', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'logs': {'Name': 'logs', 'Role': 'provider', 'Interface': 'logs', 'Optional': False, 'Limit': 0, 'Scope': 'global'}, 'nrpe-external-master': {'Name': 'nrpe-external-master', 'Role': 'provider', 'Interface': 'nrpe-external-master', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'website': {'Name': 'website', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'balancer': {'Name': 'balancer', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'logging': {'Name': 'logging', 'Role': 'requirer', 'Interface': 'syslog', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'reverseproxy': {'Name': 'reverseproxy', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'vhost-config': {'Name': 'vhost-config', 'Role': 'requirer', 'Interface': 'apache-vhost-config', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'website-cache': {'Name': 'website-cache', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Tags': ['app-servers'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'evarlast'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['trusty']}}}, {'Id': 'cs:~nottrobin/trusty/apache2-wsgi-16', 'Meta': {'charm-metadata': {'Name': 'apache2-wsgi', 'Summary': 'Apache python app server, using mod_wsgi', 'Description': 'Install apache2 with mod_wsgi\nInstall python dependencies, from requirements.txt or from directory\nInstall ruby dependencies, from Gemfile or from directory\nExtract app files\nServe the app on ports 80 and 443\n', 'Subordinate': False, 'Provides': {'nrpe-external-master': {'Name': 'nrpe-external-master', 'Role': 'provider', 'Interface': 'nrpe-external-master', 'Optional': False, 'Limit': 0, 'Scope': 'container'}, 'web-server': {'Name': 'web-server', 'Role': 'provider', 'Interface': 'http', 'Optional': False, 'Limit': 0, 'Scope': 'global'}}, 'Requires': {'http': {'Name': 'http', 'Role': 'requirer', 'Interface': 'http', 'Optional': False, 'Limit': 1, 'Scope': 'global'}, 'mongodb': {'Name': 'mongodb', 'Role': 'requirer', 'Interface': 'mongodb', 'Optional': False, 'Limit': 1, 'Scope': 'global'}}, 'Categories': ['app-servers'], 'min-juju-version': '0.0.0'}, 'owner': {'User': 'nottrobin'}, 'promulgated': {'Promulgated': False}, 'supported-series': {'SupportedSeries': ['trusty']}}}]
