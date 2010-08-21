%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	HTML_QuickForm_Renderer_Tableless
Summary:	%{_pearname} - A replacement for the default renderer that uses only XHTML and CSS but no table tags
Summary(pl.UTF-8):	%{_pearname} - zamiennik dla domyślnego renderera korzystający tylko z XHTML i CSS ale bez znaczników tabel
Name:		php-pear-%{_pearname}
Version:	0.6.1
Release:	2
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	533c6f6b338a4686f22f5f6e4f7a10bb
URL:		http://pear.php.net/package/HTML_QuickForm_Renderer_Tableless/
BuildRequires:	php-pear-PEAR >= 1:1.5.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A replacement for the default renderer of HTML_QuickForm that uses
only XHTML and CSS but no table tags.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Zamiennik dla domyślnego renderera HTML_QuickForm korzystający z XHTML
i CSS ale bez znaczników tabel

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/docs/examples/contact.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/Renderer/Tableless.php

%{php_pear_dir}/data/HTML_QuickForm_Renderer_Tableless
