%define debug_package   %{nil}

Name:           ssm-meta
Summary:        SSM meta-package
Version:        %{_version}
Release:        %{_release}
License:        Apache-2.0

Requires: MariaDB-server = 10.4.34.1
Requires: MariaDB-client = 10.4.34.1
Requires: prometheus = 2.51.2
Requires: ssm-qan-api = 9.4.12
Requires: ssm-qan-app = 9.4.18
Requires: percona-toolkit = 3.7.0
Requires: ssm-dashboards = 9.4.24
Requires: ssm-server = 9.4.6
Requires: ssm-client = 9.4.20
Requires: ssm-manage = 9.4.6
Requires: ssm-managed = 9.4.15
Requires: rds_exporter = 9.4.4
Requires: snmp_exporter = 9.4.0.25.0.6

%description
SSM meta-package

%files
