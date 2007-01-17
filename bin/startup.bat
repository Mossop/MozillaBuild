@echo off

REM The default build config to start with
SET BUILD_CONFIG_DEFAULT=minefield-noncairo

REM Set this to the vcvars script that comes with Visual C
SET VCVARS="C:\Program Files\Microsoft Visual Studio 8\VC\vcvarsall.bat"

REM Set this to the base dir of cygwin
REM SET UNIX=c:\cygwin
SET UNIX=c:\msys\1.0

REM This is the base dir of the build environment. Only change if the autodetection fails.
SET HOME=%~dp0..

SET GECKO_SDK=c:\gecko-sdk

REM --------------------------------------------------------------------------------------
REM The rest can be left as is.

SET PATH=%UNIX%\bin;%HOME%\tools\moztools\bin;%HOME%\tools\zip;%HOME%\bin;%GECKO_SDK%\bin;%PATH%
call %VCVARS%

%UNIX%\bin\bash --rcfile %HOME%\bin\buildrc
