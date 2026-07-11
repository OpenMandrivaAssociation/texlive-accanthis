%global tl_name accanthis
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Accanthis fonts, with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/accanthis
License:	gpl2+ lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/accanthis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/accanthis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Accanthis No. 3 is designed by Hirwin Harendal and is suitable as an
alternative to fonts such as Garamond, Galliard, Horley old style,
Sabon, and Bembo. The support files are suitable for use with all LaTeX
engines.

