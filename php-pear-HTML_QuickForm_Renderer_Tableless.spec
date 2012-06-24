%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm_Renderer_Tableless
%define		_status		alpha
%define		_pearname	HTML_QuickForm_Renderer_Tableless

Summary:	%{_pearname} - A replacement for the default renderer that uses only XHTML and CSS but no table tags
Summary(pl):	%{_pearname} - zamiennik dla domy�lnego renderera korzystaj�cy tylko z XHTML i CSS ale bez znacznik�w tabel
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3558887b62914fc38de3de5f1ca613d9
URL:		http://pear.php.net/package/HTML_QuickForm_Renderer_Tableless/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.6
Requires:	php-pear-PEAR >= 1:1.4.-0.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A replacement for the default renderer of HTML_QuickForm that uses
only XHTML and CSS but no table tags.

In PEAR status of this package is: %{_status}.

%description -l pl
Zamiennik dla domy�lnego renderera HTML_QuickForm korzystaj�cy z XHTML
i CSS ale bez znacznik�w tabel

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
%{php_pear_dir}/data/HTML_QuickForm_Renderer_Tableless/data/stylesheet.css
