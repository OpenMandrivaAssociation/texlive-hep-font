%global tl_name hep-font
%global tl_revision 76220

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Latin modern extended by computer modern
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/hep-font
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-font.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-font.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-font.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The hep-font package loads standard font packages and extends the usual
Latin Modern implementations by replacing missing fonts with Computer
Modern counterparts. The package is loaded with \usepackage{hep-font}.

