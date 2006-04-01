@echo off

REM Set this to the vcvars script that comes with Visual C
SET VCVARS="C:\Program Files\Microsoft Visual Studio 8\VC\vcvarsall.bat"

REM Set this to the base dir of cygwin
SET CYGWIN=c:\cygwin

REM This is the base dir of the build environment. Only change if the autodetection fails.
SET HOME=%~dp0..

REM --------------------------------------------------------------------------------------
REM The rest can be left as is.

set BASEPATH=%PATH%
SET PATH=
call %VCVARS%

%CYGWIN%\bin\bash --rcfile %HOME%\bin\buildrc
