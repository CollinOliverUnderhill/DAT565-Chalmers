% Given Constants
a = 270;
b = 11000;
m = 1740;

% State Space Matrix
A = [0 -1; 0 -a/m];       % System Matrix
B_u = [0; b/m];           % Input Matrix for Throttle u
B_w = [1; 0];             % Input Matrix for Distrubance w
C = [1 0];                % Output Matrix(Relative Distance d)
D_u = 0;                  % Transfer Function for Throttle u
D_w = 0;                  % Transfer Function for Disturbance w

% State Space Model to Transfer Function(Thorttle)
[num_u, den_u] = ss2tf(A, B_u, C, D_u);
G_uy = tf(num_u, den_u);

% State Space Model to Transfer Function(Disturbance)
[num_w, den_w] = ss2tf(A, B_w, C, D_w);
G_wy = tf(num_w, den_w);

% Output Results
disp('G_uy(s) from throttle angle to relative distance:');
G_uy

disp('G_wy(s) from disturbance (front car speed) to relative distance:');
G_wy

