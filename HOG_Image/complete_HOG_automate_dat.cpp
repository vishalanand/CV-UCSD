#include <iostream>
#include <fstream>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;

int main(int argc, const char * argv[])
{
	string arg = argv[1];
	Mat img=imread(arg,1);
	HOGDescriptor hog;
	hog.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());

	namedWindow("video capture", CV_WINDOW_AUTOSIZE);
	if(!img.data)
	{
		cout<<"Weird!\n";
		return -1;
	}
	vector<Rect> found, found_filtered;
	vector<double> confidence;
	hog.detectMultiScale(img, found, confidence, 0, Size(8,8), Size(32,32), 1.05, 2);

	size_t i, j;
	for(i=0; i<found.size(); i++)
	{
		Rect r = found[i];
		for(j=0; j<found.size(); j++)
			if(j!=i && (r & found[j])==r)
				break;
		if(j==found.size())
			found_filtered.push_back(r);
	}
	char ch[30];
	for(int abc=0; arg[abc]!='.'; abc++)
		ch[abc]=arg[abc];
	ch[7]='.';
	ch[8]='d';
	ch[9]='a';
	ch[10]='t';
	ch[11]='\0';
	FILE *printing = fopen(ch, "w");
	cout<<ch<<" and "<<arg<<"\n";
	for(i=0; i<found_filtered.size(); i++)
	{
		Rect r = found_filtered[i];
		r.x += cvRound(r.width*0.1);
		r.width += cvRound(r.width*0.1);
		r.y += cvRound(r.width*0.1);
		r.height += cvRound(r.width*0.1);
		rectangle(img, r.tl(), r.br(), cv::Scalar(0,255,0), 2);
		int x=r.x + r.width/3, y=r.y + r.height/3;
		//int x=(r.x + r.height)/2, y=(r.y + r.width)/2;
		ostringstream strs;
		strs << confidence[i];
		string str_value = strs.str();
		putText(img, str_value, Point(x, y), FONT_HERSHEY_SIMPLEX, .5, Scalar(255, 100, 0), 2);
		cout<<confidence[i]<<" is one of the confidences\n";
		fprintf(printing, "%d %d %d %d\n",r.x,r.y,r.width,r.height);
	}
	fclose(printing);
	imshow("video capture", img);
	//waitKey(0);
	return 0;
}
