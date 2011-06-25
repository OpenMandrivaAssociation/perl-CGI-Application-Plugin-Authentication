%define upstream_name    CGI-Application-Plugin-Authentication
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Authentication framework for CGI::Application
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Attribute::Handlers)
BuildRequires: perl(CGI::Application)
BuildRequires: perl(CGI::Cookie)
BuildRequires: perl(Class::ISA)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More) >= 0.940.0
BuildRequires: perl(Test::Regression)
BuildRequires: perl(Test::Taint)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Test::Without::Module)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(CGI::Application::Plugin::Session)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
