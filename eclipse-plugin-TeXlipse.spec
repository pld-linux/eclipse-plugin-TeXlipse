%define		plugin_name	texlipse

Summary:	TeXlipse - plugin for Eclipse
Summary(pl.UTF-8):	TeXlipse - wtyczka do środowiska Eclipse
Name:		eclipse-plugin-TeXlipse
Version:	1.4.1
Release:	1
License:	Eclipse Public License
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/project/texlipse/texlipse%20plugin/%{version}/texlipse_%{version}_src.zip
# Source0-md5:	d79e6f877665a599d7c32894eef22e33
URL:		http://texlipse.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse >= 3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/eclipse/dropins/%{plugin_name}

%description
TeXlipse plugin adds LaTeX editing support to Eclipse. The plugin
provides both LaTeX and BibTeX editors, project creation wizard and a
complete user manual of the plugin features. Available features
include:
 - Syntax highlighting
 - Document outline
 - Section folding
 - Command completion
 - ref and cite completion
 - Templates
 - Builder integration
 - Viewer integration with inverse search

%description -l pl.UTF-8
TeXlipse jest wtyczką środowiska LaTeX dla platformy Eclipse.
Dostarcza edytory dla LaTeXa and BibTeXa, wizard tworzenia projektów i
kompletny podręcznik użytkownika po udogodnieniach wtyczki. Dostępne
są:
 - podświetlanie składni
 - zwijanie sekcji
 - dopełnianie poleceń
 - dopełnianie znaczników ref i cite
 - szablony

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}/eclipse/plugins

cp -r plugins/net.sourceforge.texlipse_%{version} $RPM_BUILD_ROOT%{_plugindir}/eclipse/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_plugindir}
%dir %{_plugindir}/eclipse
%dir %{_plugindir}/eclipse/plugins
%{_plugindir}/eclipse/plugins/*
