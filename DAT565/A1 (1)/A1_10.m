% You are supposed to fill this template. Remember not to change variable names! 
% When you run this file, you should see all these variables in the Workspace with
% the right values! 

%% Vehicle data
% Insert group number for individual parameters: 
group_number = 10;

data = A1_datagen(group_number);        % Generate individual data
m=data(1);                              % Vehicle mass [kg]
a=data(2);                              % "External force resistance gain" [Ns/m]
b=data(3);                              % "Throttle gain" [N/rads/m]
g=9.82;                                 % Gravitational constant [m/s^2]

% Dummy controller parameters (do not modify at this stage)
Kp = 0.0;
Ki = 0.0;

%% Problem 1 - Determine the pole to the system!

p = -0.1552;                 % Ex. p = 45;               


%% Problem 2 - Implement model in Simulink!
% Simulate manual driver mode! What is the steady state speed after 100 seconds?

speed_final = 30;


%% Problem 3 - Determine the closed-loop transfer function!

% Not used - include in written report 

%% Problem 4a - Pole placement design
% a) Poles in -0.2 and -0.8

Kp_4a = 0.1337;
Ki_4a = 0.0253;


%% Problem 4b - Pole placement design
% b) Poles in -0.5+- j*sqrt(2)

Kp_4b = 0.1337;
Ki_4b = 0.3165;


%% Problem 5a - Transient response
% a) Poles in -0.2 and -0.8
% Notice that the parameter names for the controller in the Simulink model
% are denoted Kp and Ki

RiseTime_5a = 2.3905;
SettlingTime_5a = 3.1223;
Overshoot_5a = 1.2751;


%% Problem 5b - Transient response
% b) Poles in -0.5+- j*sqrt(2)
% Notice that the parameter names for the controller in the Simulink model
% are denoted Kp and Ki

RiseTime_5b = 0.7696;
SettlingTime_5b = 5.2040;
Overshoot_5b = 37.2241;


%% Problem 6 - Determine transfer!

Guy_num = -6.322;
Guy_den = [1,0.1552,0]; 
Gwy_num = [1,0.1552];
Gwy_den = [1,0.1552,0];


%% Problem 7 - Pole placement design
% Triple pole in -0.2

Kp_7 = -0.019;
Ki_7 = -0.0013;
Kd_7 = -0.07;


%% Problem 8 - Transient response
% Notice that the parameter names for the controller in the Simulink model
% are denoted Kp, Ki and Kd

p_15m = -0.2139;         % pole placement for min 15 meter
p_0m = -1.332;          % pole placement for collision




