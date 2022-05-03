#更改屏幕分辨率为1440*1200
cvt 1440 1200   60 && xrandr --newmode "1440x1200_60.00"  144.50  1440 1536 1688 1936  1200 1203 1213 1245 -hsync +vsync && xrandr --addmode HDMI-A-1-0  "1440x1200_60.00" && xrandr --output HDMI-A-1-0  --mode "1440x1200_60.00"
