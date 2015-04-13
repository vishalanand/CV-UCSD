rob=[];
IOU=cell(96,1);
prob=cell(96,1);
%dirName = 'C:\Users\shweta\Desktop\outData';              %# folder path
dirName = '/home/va/CV-UCSD/GroundTruth_Dataset/PennPed/refactored/';              %# folder path
files = dir( fullfile(dirName,'ground-*.dat') );   %# list all *.xyz files
files = {files.name}';                      %'# file names

data = cell(numel(files),1);                %# store file contents
for i=1:numel(files)
    fname = fullfile(dirName,files{i});     %# full path to file
    data{i} = load(fname);
    data{i}(:,3)=data{i}(:,3)-data{i}(:,1);
    data{i}(:,4)=data{i}(:,4)-data{i}(:,2);
end

H=hpu1;
for i=1: length(H(:,1))
    h1=H(i,[4:(4+4*H(i,2)-1)]);
    A=data{i,1};
    B=vec2mat(h1,4);
    IOU{i,1}=rectint(A,B);
    C=A(:,3).*A(:,4);
    for j=1:(size(A))(1)
        prob{i,1}(j,:)=IOU{i,1}(j,:)/C(j);
    end
    rob=[rob max(prob{i,:})];
end