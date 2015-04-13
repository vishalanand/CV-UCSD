clc();
a = '/home/va/some_codes/outData_dat/test/';
Files=dir(a);
%disp(Files)
for k=1:length(Files)
   %FileNames=Files(k).name
   disp(Files(k).name)
end
%disp(FileNames)

fileID = fopen('ground-02.dat','r');
formatSpec = '%d';
A = fscanf(fileID,formatSpec)
fclose(fileID);
disp(A);
disp('Hello');
x_g = 68;
y_g = 93;
width_g = 123;
height_g = 287;

x_p = 106;
y_p = 91;
width_p = 198;
height_p = 380;

gt=[x_g,y_g,width_g,height_g];
pr=[x_p,y_p,width_p,height_p];

intersectionArea=rectint(gt,pr);
unionCoords=[min(x_g,x_p),min(y_g,y_p),max(x_g+width_g-1,x_p+width_p-1),max(y_g+height_g-1,y_p+height_p-1)];
unionArea=(unionCoords(3)-unionCoords(1)+1)*(unionCoords(4)-unionCoords(2)+1);
overlapArea=intersectionArea/unionArea; %This should be greater than 0.5 to consider it as a valid detection.

disp(overlapArea);
if(overlapArea>=0.5)
    disp('Yes');
else
    disp('No');
end



%filename = 'myfile01.txt';
%delimiterIn = ' ';
%headerlinesIn = 1;
%A = importdata(filename,delimiterIn,headerlinesIn);