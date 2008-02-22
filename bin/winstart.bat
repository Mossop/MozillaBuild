@echo off

REM The default build config to start with
SET BUILD_CONFIG_DEFAULT=minefield

REM Set this to the vcvars script that comes with Visual C
SET VCVARS="C:\Program Files\Microsoft Visual Studio 8\VC\vcvarsall.bat"

REM Set this to the base dir of cygwin
REM SET UNIX=c:\cygwin
SET UNIX=c:\msys\1.0

REM This is the base dir of the build environment. Only change if the autodetection fails.
SET BUILD_BASE=%~dp0..

SET GECKO_SDK=c:\gecko-sdk

REM --------------------------------------------------------------------------------------
REM The rest can be left as is.

SET PATH=%UNIX%\bin;%BUILD_BASE%\tools\moztools\bin;%BUILD_BASE%\tools\zip;%BUILD_BASE%\bin;%GECKO_SDK%\bin;%PATH%
call %VCVARS%

%UNIX%\bin\bash --rcfile %BUILD_BASE%\bin\buildrc
