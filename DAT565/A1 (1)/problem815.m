p=-0.2;
kd=(0.155+3*p)/6.322;
kp=3*p^2/(-6.322);
ki=p^3/6.322;
minmum=10;
while minmum <15
    p=p-0.00001;
    kd=(0.155+3*p)/6.322;
    kp=3*p^2/(-6.322);
    ki=p^3/6.322;
    Simout=sim('A1_acc.slx','Stoptime','50');
    minmum=min(Simout.rel_distance.signals.values);
end