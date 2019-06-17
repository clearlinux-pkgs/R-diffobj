#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-diffobj
Version  : 0.2.3
Release  : 1
URL      : https://cran.r-project.org/src/contrib/diffobj_0.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/diffobj_0.2.3.tar.gz
Summary  : Diffs for R Objects
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-diffobj-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
# diffobj - Diffs for R Objects
[![](https://travis-ci.org/brodieG/diffobj.svg?branch=master)](https://travis-ci.org/brodieG/diffobj)
[![](https://codecov.io/github/brodieG/diffobj/coverage.svg?branch=master)](https://codecov.io/github/brodieG/diffobj?branch=master)
[![](http://www.r-pkg.org/badges/version/diffobj)](https://cran.r-project.org/package=diffobj)
[![Dependencies direct/recursive](https://tinyverse.netlify.com/badge/diffobj)](https://tinyverse.netlify.com/)

%package lib
Summary: lib components for the R-diffobj package.
Group: Libraries

%description lib
lib components for the R-diffobj package.


%prep
%setup -q -c -n diffobj

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560783306

%install
export SOURCE_DATE_EPOCH=1560783306
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffobj
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffobj
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library diffobj
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
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
/usr/lib64/R/library/diffobj/doc/metacomp.R
/usr/lib64/R/library/diffobj/doc/metacomp.Rmd
/usr/lib64/R/library/diffobj/doc/metacomp.html
/usr/lib64/R/library/diffobj/help/AnIndex
/usr/lib64/R/library/diffobj/help/aliases.rds
/usr/lib64/R/library/diffobj/help/diffobj.rdb
/usr/lib64/R/library/diffobj/help/diffobj.rdx
/usr/lib64/R/library/diffobj/help/paths.rds
/usr/lib64/R/library/diffobj/html/00Index.html
/usr/lib64/R/library/diffobj/html/R.css
/usr/lib64/R/library/diffobj/script/diffobj.js
/usr/lib64/R/library/diffobj/tests/run.R
/usr/lib64/R/library/diffobj/tests/scaling.R
/usr/lib64/R/library/diffobj/tests/testthat/helper.commonobjects.R
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1250.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1425.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1450.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/1900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2520.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2530.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2540.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/2900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/3000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/3100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/3200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/3300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/3400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/atomic/900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/100.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/150.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/200.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/context/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/100.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/1000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/1100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/1200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/1300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/1400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/1500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/200.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/225.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/250.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/300.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/400.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/500.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffChr/900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffDeparse/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffDeparse/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffFile/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffFile/s.o.30dbe0.R
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffFile/s.o.3f1f68.R
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffObj/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffObj/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffObj/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffObj/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/100.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/150.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/150.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1650.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/175.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/175.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/1900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/200.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2150.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2250.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2350.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2370.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2380.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2383.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/2900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/3000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/3100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/3200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/3300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/3400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffPrint/900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/100.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/1000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/1100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/diffStr/900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/guides/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/guides/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/html/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/html/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/html/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/html/350.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/html/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/1000.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/1100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/1200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/1300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/limit/900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/methods/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/methods/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/pager/100.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/pager/200.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/pager/300.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/style/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/style/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/style/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/style/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/style/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/100.txt
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/400.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/450.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/500.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/600.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/700.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/800.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/summary/900.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/trim/100.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/trim/200.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/trim/300.rds
/usr/lib64/R/library/diffobj/tests/testthat/helper/trim/50.rds
/usr/lib64/R/library/diffobj/tests/testthat/testthat.atomic.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.banner.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.capture.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.check.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.context.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.core.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.diffChr.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.diffDeparse.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.diffObj.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.diffPrint.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.diffStr.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.file.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.guide.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.html.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.limit.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.methods.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.misc.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.pager.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.rrdiff.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.s4.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.ses.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.style.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.subset.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.summary.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.text.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.trim.R
/usr/lib64/R/library/diffobj/tests/testthat/testthat.warnings.R
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-cur-all.txt
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-cur.txt
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-tar-all.txt
/usr/lib64/R/library/diffobj/tests/valgrind/mdl-tar.txt
/usr/lib64/R/library/diffobj/tests/valgrind/tests-valgrind.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/diffobj/libs/diffobj.so
