# revision 13822
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-polish
Epoch:		1
Version:	20120224
Release:	10
Summary:	Polish documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-polish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-lshort-polish
Requires:	texlive-tex-virtual-academy-pl
Requires:	texlive-texlive-pl
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-polish package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780249
- Update to latest release.
- Import texlive-collection-documentation-polish
- Import texlive-collection-documentation-polish

