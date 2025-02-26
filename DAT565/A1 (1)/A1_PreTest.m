function [] = A1_PreTest(A1_10)
%---------------------------------------------------------------
% Test to check if all variables are available before uploading 
% the script file to canvas
%
% Syntax: A1_PreTest(filename)
% Example: A1_PreTest('A1_template') 
%     - replace template with groupnumber, ex. 'A1_1'
%
% Copyright: Jonas Fredriksson: Chalmers University of Technology
%---------------------------------------------------------------
run("A1_10.m");
V=load('initialVars1');

test_checker = 0;
for k=1:numel(V.initialVars)
    if ~exist(V.initialVars{k})
        disp(['Variable ', V.initialVars{k}, ' does not exist!']);
        test_checker = test_checker + 1;
    end
end

if test_checker == 0
    disp('Everything seems to be ok to submit!');
end
