#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Hash
Summary:	Class::Hash - Perl extension for hashes that look like classes
Summary(pl):	CLass::Hash - rozszerzenie Perla o hasze wygl±daj±ce jak klasy
Name:		perl-Class-Hash
Version:	1.01
Release:	1
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

%description -l pl
Ten pakiet dostarcza oparty na metodach interfejs do haszy. Czasem
bardziej wygodne jest mieæ nazwane metody do dostêpu do hasza zamiast
kluczy. Ten modu³ generalizuje takie zachowanie. Próbuje wyprowadziæ
interfejs powi±zanego hasza.

Ten modu³ próbuje zrobiæ jak najwiêcej lub jak najmniej za
programistê w zale¿no¶ci od potrzeb, dostarczaj±c wiele opcji
konfiguracyjnych. Opcje te pozwalaj± okre¶liæ rodzaj interfejsu, jaki
ma obiekt. Ten interfejs mo¿e byæ tak¿e modyfikowany pó¼niej.

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
