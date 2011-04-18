%define	upstream_name    Acme-BooK-Is-My-Bitch
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Acme::BooK::Is::My::Bitch has a great story behind it
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif

BuildRequires: perl(Acme::MetaSyntactic)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Find)
BuildRequires: perl(UNIVERSAL::isa)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
At YAPC::EU::2006, in Birmingham, England, BooK auctioned the right for
someone to pick a module from CPAN and have that module's name (temporarily)
tattoed in his arm for all the conferences BooK would go to during 2007.

Cog asked if the module had to exist by that time, and BooK said "No."

BIG MISTAKE!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
