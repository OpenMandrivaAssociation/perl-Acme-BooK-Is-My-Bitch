%define	upstream_name    Acme-BooK-Is-My-Bitch
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Acme::BooK::Is::My::Bitch has a great story behind it
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Acme::MetaSyntactic)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(UNIVERSAL::isa)

BuildArch:	noarch

%description
At YAPC::EU::2006, in Birmingham, England, BooK auctioned the right for
someone to pick a module from CPAN and have that module's name (temporarily)
tattoed in his arm for all the conferences BooK would go to during 2007.

Cog asked if the module had to exist by that time, and BooK said "No."

BIG MISTAKE!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 654830
- rebuild for updated spec-helper

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 503945
- adding missing buildrequires:
- rebuild using %%perl_convert_version
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-5mdv2009.0
+ Revision: 255252
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2008.1
+ Revision: 171022
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2008.0
+ Revision: 85916
- rebuild


* Mon Sep 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-04 14:06:44 (59819)
- 0.02

* Sun Sep 03 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-03 17:37:45 (59697)
- fix buildrequires

* Sun Sep 03 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-03 16:14:31 (59688)
- fix buildrequires, enable test

* Sun Sep 03 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-03 16:06:19 (59678)
- initial contrib

