# 
# Do not Edit! Generated by:
# spectacle version 0.13
# 
# >> macros
# << macros

Name:       usleep
Summary:    Sleeps for microseconds
Version:    1
Release:    4.2
Group:      System/Base
License:    GPLv2
URL:        http://moblin.org/
Source0:    %{name}-%{version}.tar.gz
Source100:  usleep.yaml
Source1001: %{name}.manifest
BuildRequires:  popt-devel

%description
A version of /bin/sleep that sleeps for microsecond intervals.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

cp %{SOURCE1001} .
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post


# << install post






%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%manifest %{name}.manifest
# >> files
%{_mandir}/man*/*
/bin/usleep
# << files
