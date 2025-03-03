%define debug_package   %{nil}

Name:           ssm-meta
Summary:        SSM meta-package
Version:        %{_version}
Release:        %{_release}
License:        Apache-2.0

Requires: MariaDB-server = 10.4.34.1
Requires: MariaDB-client = 10.4.34.1
Requires: prometheus = 2.51.2
Requires: ssm-qan-api = 9.4.1
Requires: ssm-qan-app = 9.4.1
Requires: percona-toolkit = 3.5.7
Requires: ssm-dashboards = 9.4.5
Requires: ssm-server = 9.4.2
Requires: ssm-client = 9.4.2
Requires: ssm-manage = 9.4.0
Requires: ssm-managed = 9.4.2
Requires: rds_exporter = 9.4.0
Requires: snmp_exporter = 0.25.0.2

%description
SSM meta-package

%files
