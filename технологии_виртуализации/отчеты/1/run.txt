@echo off
chcp 65001 >nul
title Запуск виртуальных машин

:menu
echo ============================
echo   ЗАПУСК ВИРТУАЛЬНЫХ МАШИН  
echo ============================
echo   1. Запустить Windows 10
echo   2. Запустить Ubuntu
echo   3. Показать запущенные ВМ
echo   4. Показать все ВМ
echo   0. Выход
echo ============================

set /p choice="Выберите действие: "

if "%choice%"=="1" goto start_windows
if "%choice%"=="2" goto start_ubuntu
if "%choice%"=="3" goto show_running
if "%choice%"=="4" goto show_all
if "%choice%"=="0" goto exit_program

echo.
echo Неправильный ввод! Попробуйте снова.
pause
goto menu

:start_windows
set vm_name=WS_SIP_win
echo Запуск %vm_name%...
vboxmanage startvm "%vm_name%" --type gui
echo ВМ запущена!
pause
goto menu

:start_ubuntu
set vm_name=WS_SIP_ubuntu
echo Запуск %vm_name%...
vboxmanage startvm "%vm_name%" --type gui
echo ВМ запущена!
pause
goto menu

:show_running
echo.
echo =================================
echo   ЗАПУЩЕННЫЕ ВИРТУАЛЬНЫЕ МАШИНЫ  
echo =================================
vboxmanage list runningvms
echo.
if errorlevel 1 (
    echo Не найдено запущенных ВМ
)
pause
goto menu

:show_all
echo.
echo ==========================
echo   ВСЕ ВИРТУАЛЬНЫЕ МАШИНЫ
echo ==========================
vboxmanage list vms
echo.
if errorlevel 1 (
    echo VirtualBox не найден или нет ВМ
)
pause
goto menu

:exit_program
echo.
echo Выход...
timeout /t 2 >nul
exit