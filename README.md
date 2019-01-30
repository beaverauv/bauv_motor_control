# bauv_motor_control
This package code that manages the pid loops along with calculating the motor values
## Helpful Commands:
```
roslaunch bauv_motor_control pidlauncher.launch
```
This will launch the 6 loops for 6 DoF along with a node publishing to the motor values (in progress), however all movments are relative (no 4th dimensional math yet)
