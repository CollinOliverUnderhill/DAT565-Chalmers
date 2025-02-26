p=-0.2;
minmum=100;
while minmum >0
    p=p+0.0001;
    kd=(0.155+3*p)/6.322;
    kp=3*p^2/(-6.322);
    ki=p^3/6.322;
    Simout=sim('A1_acc.slx','Stoptime','50');
    minmum=min(Simout.rel_distance.signals.values);
end