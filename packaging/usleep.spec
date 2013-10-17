Name:       usleep
Summary:    Sleeps for microseconds
Version:    1
Release:    4.2
Group:      Base/Utilities
License:    GPL-2.0
URL:        http://moblin.org/
Source0:    %{name}-%{version}.tar.gz
Source100:  usleep.yaml
Source1001: %{name}.manifest
BuildRequires:  popt-devel

%description
A version of /bin/sleep that sleeps for microsecond intervals.



%prep
%setup -q -n %{name}-%{version}

%build

cp %{SOURCE1001} .
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%manifest %{name}.manifest
%license LICENSE
/bin/usleep

%docs_package
