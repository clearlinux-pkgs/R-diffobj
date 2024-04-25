#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-diffobj
Version  : 0.3.5
Release  : 37
URL      : https://cran.r-project.org/src/contrib/diffobj_0.3.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/diffobj_0.3.5.tar.gz
Summary  : Diffs for R Objects
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-diffobj-lib = %{version}-%{release}
Requires: R-crayon
BuildRequires : R-crayon
BuildRequires : buildreq-R

%description
visualization of their differences.

%package lib
Summary: lib components for the R-diffobj package.
Group: Libraries

%description lib
lib components for the R-diffobj package.


%prep
%setup -q -c -n diffobj
cd %{_builddir}/diffobj

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641000807

%install
export SOURCE_DATE_EPOCH=1641000807
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffobj
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffobj
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffobj
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc diffobj || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/diffobj/COPYRIGHTS
/usr/lib64/R/library/diffobj/DESCRIPTION
/usr/lib64/R/library/diffobj/INDEX
/usr/lib64/R/library/diffobj/Meta/Rd.rds
/usr/lib64/R/library/diffobj/Meta/features.rds
/usr/lib64/R/library/diffobj/Meta/hsearch.rds
/usr/lib64/R/library/diffobj/Meta/links.rds
/usr/lib64/R/library/diffobj/Meta/nsInfo.rds
/usr/lib64/R/library/diffobj/Meta/package.rds
/usr/lib64/R/library/diffobj/Meta/vignette.rds
/usr/lib64/R/library/diffobj/NAMESPACE
/usr/lib64/R/library/diffobj/NEWS.md
/usr/lib64/R/library/diffobj/R/diffobj
/usr/lib64/R/library/diffobj/R/diffobj.rdb
/usr/lib64/R/library/diffobj/R/diffobj.rdx
/usr/lib64/R/library/diffobj/css/diffobj.css
/usr/lib64/R/library/diffobj/doc/diffobj.R
/usr/lib64/R/library/diffobj/doc/diffobj.Rmd
/usr/lib64/R/library/diffobj/doc/diffobj.html
/usr/lib64/R/library/diffobj/doc/embed.R
/usr/lib64/R/library/diffobj/doc/embed.Rmd
/usr/lib64/R/library/diffobj/doc/embed.html
/usr/lib64/R/library/diffobj/doc/index.html
/usr/lib64/R/library/diffobj/help/AnIndex
/usr/lib64/R/library/diffobj/help/aliases.rds
/usr/lib64/R/library/diffobj/help/diffobj.rdb
/usr/lib64/R/library/diffobj/help/diffobj.rdx
/usr/lib64/R/library/diffobj/help/paths.rds
/usr/lib64/R/library/diffobj/html/00Index.html
/usr/lib64/R/library/diffobj/html/R.css
/usr/lib64/R/library/diffobj/script/diffobj.js
/usr/lib64/R/library/diffobj/tests/_helper/breakdown.R
/usr/lib64/R/library/diffobj/tests/_helper/check.R
/usr/lib64/R/library/diffobj/tests/_helper/commonobjects.R
/usr/lib64/R/library/diffobj/tests/_helper/init.R
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1250.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1425.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1450.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/1900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2520.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2530.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2540.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/2900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/3000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/3100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/3200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/3300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/3400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/atomic/900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/common/aaaa.RDS
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/100.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/150.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/200.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/context/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/100.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/1000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/1100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/1200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/1300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/1400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/1500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/200.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/225.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/250.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/300.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/400.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/500.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffChr/900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffDeparse/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffDeparse/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffFile/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffFile/s.o.30dbe0.R
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffFile/s.o.3f1f68.R
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffObj/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffObj/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffObj/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffObj/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/100.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/150.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/150.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1650.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/175.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/175.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/1900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/200.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2150.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2250.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2350.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2370.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2380.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2383.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/2900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/3000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/3100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/3200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/3300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/3400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffPrint/900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/100.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/1000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/1100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/550.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/diffStr/900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/guides/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/guides/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/html/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/html/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/html/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/html/350.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/html/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/1000.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/1100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/1200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/1300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/limit/900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/methods/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/methods/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/pager/100.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/pager/200.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/pager/300.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/style/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/style/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/style/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/style/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/style/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/100.txt
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/400.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/450.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/500.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/600.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/700.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/800.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/summary/900.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/trim/100.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/trim/200.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/trim/300.rds
/usr/lib64/R/library/diffobj/tests/_helper/objs/trim/50.rds
/usr/lib64/R/library/diffobj/tests/_helper/string-gen.R
/usr/lib64/R/library/diffobj/tests/_helper/tools.R
/usr/lib64/R/library/diffobj/tests/test-atomic.R
/usr/lib64/R/library/diffobj/tests/test-atomic.Rout.save
/usr/lib64/R/library/diffobj/tests/test-banner.R
/usr/lib64/R/library/diffobj/tests/test-banner.Rout.save
/usr/lib64/R/library/diffobj/tests/test-capture.R
/usr/lib64/R/library/diffobj/tests/test-capture.Rout.save
/usr/lib64/R/library/diffobj/tests/test-check.R
/usr/lib64/R/library/diffobj/tests/test-check.Rout.save
/usr/lib64/R/library/diffobj/tests/test-context.R
/usr/lib64/R/library/diffobj/tests/test-context.Rout.save
/usr/lib64/R/library/diffobj/tests/test-core.R
/usr/lib64/R/library/diffobj/tests/test-core.Rout.save
/usr/lib64/R/library/diffobj/tests/test-diffChr.R
/usr/lib64/R/library/diffobj/tests/test-diffChr.Rout.save
/usr/lib64/R/library/diffobj/tests/test-diffDeparse.R
/usr/lib64/R/library/diffobj/tests/test-diffDeparse.Rout.save
/usr/lib64/R/library/diffobj/tests/test-diffObj.R
/usr/lib64/R/library/diffobj/tests/test-diffObj.Rout.save
/usr/lib64/R/library/diffobj/tests/test-diffPrint.R
/usr/lib64/R/library/diffobj/tests/test-diffPrint.Rout.save
/usr/lib64/R/library/diffobj/tests/test-diffStr.R
/usr/lib64/R/library/diffobj/tests/test-diffStr.Rout.save
/usr/lib64/R/library/diffobj/tests/test-file.R
/usr/lib64/R/library/diffobj/tests/test-file.Rout.save
/usr/lib64/R/library/diffobj/tests/test-guide.R
/usr/lib64/R/library/diffobj/tests/test-guide.Rout.save
/usr/lib64/R/library/diffobj/tests/test-html.R
/usr/lib64/R/library/diffobj/tests/test-html.Rout.save
/usr/lib64/R/library/diffobj/tests/test-limit.R
/usr/lib64/R/library/diffobj/tests/test-limit.Rout.save
/usr/lib64/R/library/diffobj/tests/test-methods.R
/usr/lib64/R/library/diffobj/tests/test-methods.Rout.save
/usr/lib64/R/library/diffobj/tests/test-misc.R
/usr/lib64/R/library/diffobj/tests/test-misc.Rout.save
/usr/lib64/R/library/diffobj/tests/test-pager.R
/usr/lib64/R/library/diffobj/tests/test-pager.Rout.save
/usr/lib64/R/library/diffobj/tests/test-rdiff.R
/usr/lib64/R/library/diffobj/tests/test-rdiff.Rout.save
/usr/lib64/R/library/diffobj/tests/test-s4.R
/usr/lib64/R/library/diffobj/tests/test-s4.Rout.save
/usr/lib64/R/library/diffobj/tests/test-scaling.R
/usr/lib64/R/library/diffobj/tests/test-ses.R
/usr/lib64/R/library/diffobj/tests/test-ses.Rout.save
/usr/lib64/R/library/diffobj/tests/test-style.R
/usr/lib64/R/library/diffobj/tests/test-style.Rout.save
/usr/lib64/R/library/diffobj/tests/test-subset.R
/usr/lib64/R/library/diffobj/tests/test-subset.Rout.save
/usr/lib64/R/library/diffobj/tests/test-summary.R
/usr/lib64/R/library/diffobj/tests/test-summary.Rout.save
/usr/lib64/R/library/diffobj/tests/test-text.R
/usr/lib64/R/library/diffobj/tests/test-text.Rout.save
/usr/lib64/R/library/diffobj/tests/test-trim.R
/usr/lib64/R/library/diffobj/tests/test-trim.Rout.save
/usr/lib64/R/library/diffobj/tests/test-warnings.R
/usr/lib64/R/library/diffobj/tests/test-warnings.Rout.save
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-cur-all.txt
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-cur.txt
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-tar-all.txt
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-tar.txt
/usr/lib64/R/library/diffobj/tests/valgrind/tests-valgrind.R
/usr/lib64/R/library/diffobj/tests/zz-test-check.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/diffobj/libs/diffobj.so
/usr/lib64/R/library/diffobj/libs/diffobj.so.avx2
/usr/lib64/R/library/diffobj/libs/diffobj.so.avx512
