@echo off
chcp 65001
set /p name= "Пожалуйста, введите название:" 


git add -A
git commit -m "%name%"
git push origin main