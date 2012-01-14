#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MP4
%define	pnam	Info
Summary:	MP4::Info - Fetch info from MPEG-4 files (.mp4, .m4a, .m4p, .3gp)
Summary(pl.UTF-8):	MP4::Info - pobieranie informacji z plików MPEG-4 (.mp4, .m4a, .m4p, .3gp)
Name:		perl-MP4-Info
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MP4/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	39fbc8225b01ecbecf13ff9e4ab9b896
URL:		http://search.cpan.org/dist/MP4-Info/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-String
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MP4::Info module can be used to extract tag and meta information
from MPEG-4 audio (AAC) and video files. It is designed as a drop-in
replacement for MP3::Info.

Note that this module does not allow you to update the information in
MPEG-4 files.

%description -l pl.UTF-8
Moduł Perla MP4::Info służy do wydobywania znaczników i metainformacji
z plików dźwiękowych (AAC) i filmów MPEG-4. Jest zaprojektowany jako
zamiennik MP3::Info.

Uwaga: ten moduł nie pozwala na uaktualnianie informacji w plikach
MPEG-4.

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
%doc INSTALL README
%dir %{perl_vendorlib}/MP4
%{perl_vendorlib}/MP4/*.pm
%{_mandir}/man3/*
