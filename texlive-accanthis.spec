# revision 32089
# category Package
# catalog-ctan /fonts/accanthis
# catalog-date 2013-11-06 07:22:54 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-accanthis
Version:	20131106
Release:	5
Summary:	Accanthis fonts, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/accanthis
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accanthis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accanthis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Accanthis No. 3 is designed by Hirwin Harendal and is suitable
as an alternative to fonts such as Garamond, Galliard, Horley
old style, Sabon, and Bembo. The support files are suitable for
use with all LaTeX engines.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/accanthis/acnt_m4gnvn.enc
%{_texmfdistdir}/fonts/enc/dvips/accanthis/acnt_qu6a6x.enc
%{_texmfdistdir}/fonts/enc/dvips/accanthis/acnt_sjpjw4.enc
%{_texmfdistdir}/fonts/enc/dvips/accanthis/acnt_z4e4wk.enc
%{_texmfdistdir}/fonts/map/dvips/accanthis/accanthis.map
%{_texmfdistdir}/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-Regular.otf
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-Bold.pfb
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-Italic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-Regular.pfb
%{_texmfdistdir}/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ts1.vf
%{_texmfdistdir}/tex/latex/accanthis/LY1AccanthisADFStdNoThree-LF.fd
%{_texmfdistdir}/tex/latex/accanthis/OT1AccanthisADFStdNoThree-LF.fd
%{_texmfdistdir}/tex/latex/accanthis/T1AccanthisADFStdNoThree-LF.fd
%{_texmfdistdir}/tex/latex/accanthis/TS1AccanthisADFStdNoThree-LF.fd
%{_texmfdistdir}/tex/latex/accanthis/accanthis.sty
%doc %{_texmfdistdir}/doc/fonts/accanthis/Accanthis-Cat.pdf
%doc %{_texmfdistdir}/doc/fonts/accanthis/COPYING
%doc %{_texmfdistdir}/doc/fonts/accanthis/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/accanthis/README
%doc %{_texmfdistdir}/doc/fonts/accanthis/accanthis-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/accanthis/accanthis-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
