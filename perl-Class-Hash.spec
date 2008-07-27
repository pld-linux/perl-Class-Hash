#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Hash
Summary:	Class::Hash - Perl extension for hashes that look like classes
Summary(pl.UTF-8):	CLass::Hash - rozszerzenie Perla o hasze wyglądające jak klasy
Name:		perl-Class-Hash
Version:	1.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5366af138b4353755decf464afedccc4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component provides a method-based interface to a hash.
Occasionally, it's more convenient to have named methods to access
a hash than hash keys. This module generalizes this behavior. It tries
to work the tied hash interface inside-out.

This module tries to do as much or as little for you as you want and
provides a number of configuration options. The options allow you to
determine what kind of interface the object has. The interface may
also be altered after-the-fact.

%description -l pl.UTF-8
Ten pakiet dostarcza oparty na metodach interfejs do haszy. Czasem
bardziej wygodne jest mieć nazwane metody do dostępu do hasza zamiast
kluczy. Ten moduł generalizuje takie zachowanie. Próbuje wyprowadzić
interfejs powiązanego hasza.

Ten moduł próbuje zrobić jak najwięcej lub jak najmniej za
programistę w zależności od potrzeb, dostarczając wiele opcji
konfiguracyjnych. Opcje te pozwalają określić rodzaj interfejsu, jaki
ma obiekt. Ten interfejs może być także modyfikowany później.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Hash.pm
%{_mandir}/man3/*
