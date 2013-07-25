%define upstream_name    CGI-Application-Plugin-Authentication
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.20
Release:	1

Summary:	Authentication framework for CGI::Application
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/CGI-Application-Plugin-Authentication-0.20.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(CGI::Application)
BuildRequires:	perl(CGI::Cookie)
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More) >= 0.940.0
BuildRequires:	perl(Test::Regression)
BuildRequires:	perl(Test::Taint)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Without::Module)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(CGI::Application::Plugin::Session)

BuildArch:	noarch

%description
CGI::Application::Plugin::Authentication adds the ability to authenticate
users in your the CGI::Application manpage modules. It imports one method
called 'authen' into your CGI::Application module. Through the authen
method you can call all the methods of the
CGI::Application::Plugin::Authentication plugin.

There are two main decisions that you need to make when using this module.
How will the usernames and password be verified (ie from a database, LDAP,
etc...), and how can we keep the knowledge that a user has already logged
in persistent, so that they will not have to enter their credentials again
on the next request (ie how do we 'Store' the authentication information
across requests).

Choosing a Driver
    There are three drivers that are included with the distribution. Also,
    there is built in support for all of the Authen::Simple modules (search
    CPAN for Authen::Simple for more information). This should be enough to
    cover everyone's needs. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Jun 25 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.180.0-3mdv2011.0
+ Revision: 687184
- rebuild

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2
+ Revision: 658519
- rebuild for updated spec-helper

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 553471
- typo fix
- update version prereq
- requiring minimum version in buildrequires:
- adding missing buildrequires:
- update to 0.18

* Mon Jan 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.1
+ Revision: 495701
- update to 0.17

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.1
+ Revision: 493482
- update to 0.16

* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 490486
- update to 0.15

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 460830
- update to 0.14

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 405771
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2010.0
+ Revision: 370016
- update to new version 0.13

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.1
+ Revision: 292552
- import perl-CGI-Application-Plugin-Authentication


* Thu Oct 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.1
- initial mdv release, generated with cpan2dist


