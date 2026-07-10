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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Accanthis No. 3 is designed by Hirwin Harendal and is suitable as an
alternative to fonts such as Garamond, Galliard, Horley old style,
Sabon, and Bembo. The support files are suitable for use with all LaTeX
engines.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/accanthis
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/arkandis
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis
%dir %{_datadir}/texmf-dist/fonts/vf/arkandis
%dir %{_datadir}/texmf-dist/tex/latex/accanthis
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/accanthis
%dir %{_datadir}/texmf-dist/fonts/map/dvips/accanthis
%dir %{_datadir}/texmf-dist/fonts/opentype/arkandis/accanthis
%dir %{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis
%dir %{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis
%dir %{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis
%doc %{_datadir}/texmf-dist/doc/fonts/accanthis/Accanthis-Cat.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/accanthis/COPYING
%doc %{_datadir}/texmf-dist/doc/fonts/accanthis/NOTICE.txt
%doc %{_datadir}/texmf-dist/doc/fonts/accanthis/README
%doc %{_datadir}/texmf-dist/doc/fonts/accanthis/accanthis-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/accanthis/accanthis-samples.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/accanthis/acnt_m4gnvn.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/accanthis/acnt_qu6a6x.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/accanthis/acnt_sjpjw4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/accanthis/acnt_z4e4wk.enc
%{_datadir}/texmf-dist/fonts/map/dvips/accanthis/accanthis.map
%{_datadir}/texmf-dist/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-Bold.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-Italic.otf
%{_datadir}/texmf-dist/fonts/opentype/arkandis/accanthis/AccanthisADFStdNo3-Regular.otf
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1--lcdfj.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-BoldItalicLCDFJ.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-BoldLCDFJ.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-ItalicLCDFJ.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-Regular.pfb
%{_datadir}/texmf-dist/fonts/type1/arkandis/accanthis/AccanthisADFStdNo3-RegularLCDFJ.pfb
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Bold-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-BoldItalic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Italic-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/arkandis/accanthis/AccanthisADFStdNo3-Regular-lf-ts1.vf
%{_datadir}/texmf-dist/tex/latex/accanthis/LY1AccanthisADFStdNoThree-LF.fd
%{_datadir}/texmf-dist/tex/latex/accanthis/OT1AccanthisADFStdNoThree-LF.fd
%{_datadir}/texmf-dist/tex/latex/accanthis/T1AccanthisADFStdNoThree-LF.fd
%{_datadir}/texmf-dist/tex/latex/accanthis/TS1AccanthisADFStdNoThree-LF.fd
%{_datadir}/texmf-dist/tex/latex/accanthis/accanthis.sty
