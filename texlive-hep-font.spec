Name:		texlive-hep-font
Version:	64900
Release:	1
Summary:	Latin modern extended by computer modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep-font
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-font.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-font.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-font.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The hep-font package loads standard font packages and extends
the usual Latin Modern implementations by replacing missing
fonts with Computer Modern counterparts. The package is loaded
with \usepackage{hep-font}.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/hep-font
%{_texmfdistdir}/tex/latex/hep-font
%doc %{_texmfdistdir}/doc/fonts/hep-font

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
