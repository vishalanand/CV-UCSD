clc();
%path_test = '/home/va/some_codes/outData_dat/test_check/';
path_test = '/home/va/some_codes/dataset/Data/FudanPed/refractored/';
pattern= fullfile(path_test,'*.dat');
Files=dir(pattern);

%path_ground = '/home/va/some_codes/outData_dat/ground_check/';
path_ground = '/home/va/some_codes/outData_dat/FudanPed/refractored/';
pattern= fullfile(path_ground,'*.dat');
Files_ground=dir(pattern);
total = 0;
correct = 0;
fileID_print = fopen('IOU.dat','w');

for k=1:length(Files)
   %disp(Files(k).name);
   if Files(k).name(1:1)=='.'
       continue
   end
   open_file_test=strcat(path_test,Files(k).name);
   ground_file = strrep(Files(k).name, 'test', 'ground');
   open_file_ground = strcat(path_ground,ground_file);
   %disp(open_file_test);
   %disp(open_file_ground);
   fileID_test = fopen(open_file_test,'r');
   formatSpec = '%d';
   test_values = fscanf(fileID_test,formatSpec);
   fclose(fileID_test);
   
   try
       fileID_ground = fopen(open_file_ground,'r');
       formatSpec = '%d';
       ground_values = fscanf(fileID_ground,formatSpec);
       fclose(fileID_ground);
   catch
       warning(strcat(ground_file,' does not exist'));
       continue;
   end
   total = total+1;
   
   %disp(test_values);
   %disp(ground_values);
   idx = 1;
   while idx>0 & idx <= numel(test_values)
       x_p = test_values(idx);
       y_p = test_values(idx+1);
       width_p = test_values(idx+2);
       height_p = test_values(idx+3);
       idx = idx+4;
   end
   
   idx = 1;
   while idx>0 & idx <= numel(ground_values)
       x_g = ground_values(idx);
       y_g = ground_values(idx+1);
       width_g = ground_values(idx+2);
       height_g = ground_values(idx+3);
       idx = idx+4;
   end
   
   gt=[x_g,y_g,width_g,height_g];
   pr=[x_p,y_p,width_p,height_p];
   
   intersectionArea=rectint(gt,pr);
   unionCoords=[min(x_g,x_p),min(y_g,y_p),max(x_g+width_g-1,x_p+width_p-1),max(y_g+height_g-1,y_p+height_p-1)];
   unionArea=(unionCoords(3)-unionCoords(1)+1)*(unionCoords(4)-unionCoords(2)+1);
   overlapArea=intersectionArea/unionArea; %This should be greater than 0.5 to consider it as a valid detection.
   
   disp(overlapArea);
   if overlapArea>=0.5
       fprintf(fileID_print,'%s Yes %f\n',Files(k).name,overlapArea);
       correct = correct+1
       disp('Yes');
   else
       fprintf(fileID_print,'%s Yes %f\n',Files(k).name,overlapArea);
       disp('No');
   end
end
disp(correct*100/total);
fclose(fileID_print);