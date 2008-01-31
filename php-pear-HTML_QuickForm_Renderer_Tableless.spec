%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm_Renderer_Tableless
%define		_status		beta
%define		_pearname	HTML_QuickForm_Renderer_Tableless
Summary:	%{_pearname} - A replacement for the default renderer that uses only XHTML and CSS but no table tags
Summary(pl.UTF-8):	%{_pearname} - zamiennik dla domyślnego renderera korzystający tylko z XHTML i CSS ale bez znaczników tabel
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	2
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b7f56124a49d1e8597fd933b45ddcb08
URL:		http://pear.php.net/package/HTML_QuickForm_Renderer_Tableless/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.6
Requires:	php-pear-PEAR-core >= 1:1.4.9
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
%dir %{php_pear_dir}/data/HTML_QuickForm_Renderer_Tableless
%dir %{php_pear_dir}/data/HTML_QuickForm_Renderer_Tableless/data
%{php_pear_dir}/data/HTML_QuickForm_Renderer_Tableless/data/stylesheet.css
