Name:		perl-Params-Util
Version:	1.00
Release:	3%{?dist}
Summary:	Simple standalone param-checking functions
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Params-Util/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Params-Util-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(Scalar::Util) >= 1.14
BuildRequires:	perl(Test::MinimumVersion) >= 0.007

# Required by the tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::CPAN::Meta) >= 0.07

%description
Params::Util provides a basic set of importable functions that 
makes checking parameters a hell of a lot easier.

%prep
%setup -q -n Params-Util-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test AUTOMATED_TESTING=1

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Params

%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.00-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.00-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.38-1
- Upstream update.

* Thu Feb 12 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.37-1
- Upstream update.
- Pass OPTIMIZE to make.
- Remove *.bs after install.
- Misc. minor spec fixes.

* Sat Nov 29 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.35-1
- Upstream update.
- Remove BuildArch: noarch (package now is arch'ed).
- Remove testsuite hack to accept perl(Test::CPAN::Meta) != 0.07.

* Tue Jul 08 2008 Ralf Corsépius <rc040203@freenet.de> - 0.33-2
- Unconditionally BR: perl(Test::CPAN::Meta).

* Mon Jun 02 2008 Ralf Corsépius <rc040203@freenet.de> - 0.33-1
- Upstream update.
- Conditionally BR: perl(Test::CPAN::Meta).
- Hack testsuite to accept Test::CPAN::Meta != 0.07.

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-6
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-5
- Rebuild for perl 5.10 (again), first pass

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-4
- rebuild normally, second pass

* Sat Jan 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-3.1
- disable Test::MinimumVersion, tests for first pass

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.31-3
- rebuild for new perl

* Sun Nov 25 2007 Ralf Corsépius <rc040203@freenet.de> - 0.31-2
- Add BR: perl(Test::MinimumVersion).

* Mon Nov 19 2007 Ralf Corsépius <rc040203@freenet.de> - 0.31-1
- Upstream update.

* Tue Oct 30 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-1
- Upstream update.

* Thu Sep 06 2007 Ralf Corsépius <rc040203@freenet.de> - 0.29-1
- Upstream update.
- Update licence tag.
- Conditionally disable AUTOMATED_TESTING.

* Sat Jul 28 2007 Ralf Corsépius <rc040203@freenet.de> - 0.26-1
- Upstream update.

* Wed May 30 2007 Ralf Corsépius <rc040203@freenet.de> - 0.25-1
- Upstream update.

* Mon May 14 2007 Ralf Corsépius <rc040203@freenet.de> - 0.24-1
- Upstream update.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 0.23-2
- BR: perl(ExtUtils::MakeMaker).

* Fri Mar 02 2007 Ralf Corsépius <rc040203@freenet.de> - 0.23-1
- Upstream update.

* Fri Nov 03 2006 Ralf Corsépius <rc040203@freenet.de> - 0.22-1
- Upstream update.

* Thu Oct 19 2006 Ralf Corsépius <rc040203@freenet.de> - 0.21-1
- Upstream update.

* Wed Oct 04 2006 Ralf Corsépius <rc040203@freenet.de> - 0.20-1
- Upstream update.

* Mon Sep 18 2006 Ralf Corsépius <rc040203@freenet.de> - 0.19-1
- Upstream update.
- Activate AUTOMATED_TESTING (t/99_author.t).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.17-2
- Mass rebuild.

* Sun Aug 13 2006 Ralf Corsépius <rc040203@freenet.de> - 0.17-1
- Upstream update.

* Wed Jul 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.15-1
- Upstream update.

* Sun May 21 2006 Ralf Corsépius <rc040203@freenet.de> - 0.14-1
- Upstream update.

* Mon May 08 2006 Ralf Corsépius <rc040203@freenet.de> - 0.13-1
- Upstream update.

* Thu Apr 20 2006 Ralf Corsépius <rc040203@freenet.de> - 0.11-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 0.10-2
- Rebuild for perl-5.8.8.

* Wed Jan 18 2006 Ralf Corsépius <rc040203@freenet.de> - 0.10-1
- Upstream update.

* Wed Jan 11 2006 Ralf Corsépius <rc040203@freenet.de> - 0.09-1
- Upstream update.

* Wed Dec 21 2005 Ralf Corsépius <rc040203@freenet.de> - 0.08-1
- Upstream update.

* Wed Oct 12 2005 Ralf Corsepius <rc040203@freenet.de> - 0.07-1
- Upstream update.
