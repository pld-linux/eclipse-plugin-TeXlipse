Summary:	TeXlipse - plugin for Eclipse
Summary(pl):	TeXlipse - wtyczka do ¶rodowiska Eclipse
Name:		eclipse-plugin-TeXlipse
Version:	1.0.2
Release:	1
License:	Eclipse Public License
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/texlipse/net.sourceforge.texlipse_%{version}_src.zip
# Source0-md5:	a0d0b5954e65d5bd4287af6a3dde3b81
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

%description -l pl
TeXlipse jest wtyczk± ¶rodowiska LaTeX dla platformy Eclipse.
Dostarcza edytory dla LaTeXa and BibTeXa, wizard tworzenia projektów i
kompletny podrêcznik u¿ytkownika po udogodnieniach wtyczki. Dostêpne
s±:
 - pod¶wietlanie sk³adni
 - zwijanie sekcji
 - dope³nianie poleceñ
 - dope³nianie znaczników ref i cite
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
