@setlocal
@echo off

cd %~d0
docker push nupan/hikepo:latest
if errorlevel 1 (
    exit /b %errorlevel%
)

exit /b 0
