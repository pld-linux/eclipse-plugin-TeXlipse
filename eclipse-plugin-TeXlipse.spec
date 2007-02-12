Summary:	TeXlipse - plugin for Eclipse
Summary(pl.UTF-8):   TeXlipse - wtyczka do środowiska Eclipse
Name:		eclipse-plugin-TeXlipse
Version:	1.1.0
Release:	1
License:	Eclipse Public License
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/texlipse/net.sourceforge.texlipse_%{version}_src.zip
# Source0-md5:	afac4f053457569f346f93ed8e0757c9
URL:		http://texlipse.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86/x86/;s/athlon/x86/;s/pentium./x86/')
%define		_eclipsedir  	%{_libdir}/eclipse

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
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

cp -r * $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_eclipsedir}
%dir %{_eclipsedir}/plugins
%{_eclipsedir}/plugins/*
