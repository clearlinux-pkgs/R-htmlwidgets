#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-htmlwidgets
Version  : 1.3
Release  : 15
URL      : https://cran.r-project.org/src/contrib/htmlwidgets_1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/htmlwidgets_1.3.tar.gz
Summary  : HTML Widgets for R
Group    : Development/Tools
License  : MIT
Requires: R-htmltools
Requires: R-jsonlite
Requires: R-shiny
BuildRequires : R-htmltools
BuildRequires : R-jsonlite
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
contexts including the R console, 'R Markdown' documents, and 'Shiny'
    web applications.

%prep
%setup -q -c -n htmlwidgets

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538597183

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1538597183
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmlwidgets
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmlwidgets
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library htmlwidgets
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library htmlwidgets|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/htmlwidgets/DESCRIPTION
/usr/lib64/R/library/htmlwidgets/INDEX
/usr/lib64/R/library/htmlwidgets/LICENSE
/usr/lib64/R/library/htmlwidgets/Meta/Rd.rds
/usr/lib64/R/library/htmlwidgets/Meta/features.rds
/usr/lib64/R/library/htmlwidgets/Meta/hsearch.rds
/usr/lib64/R/library/htmlwidgets/Meta/links.rds
/usr/lib64/R/library/htmlwidgets/Meta/nsInfo.rds
/usr/lib64/R/library/htmlwidgets/Meta/package.rds
/usr/lib64/R/library/htmlwidgets/Meta/vignette.rds
/usr/lib64/R/library/htmlwidgets/NAMESPACE
/usr/lib64/R/library/htmlwidgets/NEWS
/usr/lib64/R/library/htmlwidgets/R/htmlwidgets
/usr/lib64/R/library/htmlwidgets/R/htmlwidgets.rdb
/usr/lib64/R/library/htmlwidgets/R/htmlwidgets.rdx
/usr/lib64/R/library/htmlwidgets/doc/develop_advanced.R
/usr/lib64/R/library/htmlwidgets/doc/develop_advanced.Rmd
/usr/lib64/R/library/htmlwidgets/doc/develop_advanced.html
/usr/lib64/R/library/htmlwidgets/doc/develop_intro.R
/usr/lib64/R/library/htmlwidgets/doc/develop_intro.Rmd
/usr/lib64/R/library/htmlwidgets/doc/develop_intro.html
/usr/lib64/R/library/htmlwidgets/doc/develop_sizing.Rmd
/usr/lib64/R/library/htmlwidgets/doc/develop_sizing.html
/usr/lib64/R/library/htmlwidgets/doc/index.html
/usr/lib64/R/library/htmlwidgets/help/AnIndex
/usr/lib64/R/library/htmlwidgets/help/aliases.rds
/usr/lib64/R/library/htmlwidgets/help/htmlwidgets.rdb
/usr/lib64/R/library/htmlwidgets/help/htmlwidgets.rdx
/usr/lib64/R/library/htmlwidgets/help/paths.rds
/usr/lib64/R/library/htmlwidgets/html/00Index.html
/usr/lib64/R/library/htmlwidgets/html/R.css
/usr/lib64/R/library/htmlwidgets/templates/widget_js.txt
/usr/lib64/R/library/htmlwidgets/templates/widget_r.txt
/usr/lib64/R/library/htmlwidgets/www/htmlwidgets.js
