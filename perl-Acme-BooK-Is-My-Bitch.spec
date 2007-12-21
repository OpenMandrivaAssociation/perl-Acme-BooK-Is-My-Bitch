%define	module	Acme-BooK-Is-My-Bitch
%define	name	perl-%{module}
%define version 0.02
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Acme::BooK::Is::My::Bitch has a great story behind it
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires: perl-Acme-MetaSyntactic >= 0.89
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Find)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
At YAPC::EU::2006, in Birmingham, England, BooK auctioned the right for
someone to pick a module from CPAN and have that module's name (temporarily)
tattoed in his arm for all the conferences BooK would go to during 2007.

Cog asked if the module had to exist by that time, and BooK said "No."

BIG MISTAKE!

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

