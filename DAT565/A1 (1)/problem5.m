SimOut=sim('A1_cc','StopTime','20');
t=SimOut.speed.time;
t0=1;
y=SimOut.speed.signals.values;
y0=25;
yf=30;
y_norm = (y-y0)/(yf-y0);
t_norm = t-t0;
 S=stepinfo(y_norm,t_norm,'SettlingTimeThreshold',0.05);


