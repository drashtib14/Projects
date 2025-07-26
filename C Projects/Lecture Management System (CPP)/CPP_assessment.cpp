#include<iostream>
#include<string>
using namespace std;

class Lecture {
	private:
		// data members
		string lecturer;
		string subject;
		string course;
		int lectures;
		
	public:
		// constructor to initialize values
		Lecture(string lname = "", string sname = "", string cname = "", int lec = 0) {
			lecturer = lname;
			subject = sname;
			course = cname;
			lectures = lec;
		}
		
		// member functions
		// function to get lecture details
		void getLectureDetails(string lname, string sname, string cname, int lec) {
			lecturer = lname;
			subject = sname;
			course = cname;
			lectures = lec;
		}
		
		// function to display lecture details
		void displayLectureDetails(){
			cout << "Lecturer Name: " << lecturer << endl;
	        cout << "Subject Name: " << subject << endl;
	        cout << "Course Name: " << course << endl;
	        cout << "Number of Lectures: " << lectures << endl;
	        cout << "------------------------------" << endl;
		}
};
int main(){
	Lecture lecture1, lecture2, lecture3, lecture4, lecture5;
	
	// getting lecture details
	lecture1.getLectureDetails("Dr. John Smith", "Physics", "B.Sc", 25);
	lecture2.getLectureDetails("Prof. Alice Brown", "Mathematics", "B.Sc", 20);
	lecture3.getLectureDetails("Dr. Carol Lee", "Computer Science", "B.Tech", 30);
	lecture4.getLectureDetails("Prof. David White", "Chemistry", "B.Sc", 22);
	lecture5.getLectureDetails("Dr. Emily Clark", "Biology", "B.Sc", 18);
	
	cout << "Lectures Information: " << endl;
    cout << "------------------------------" << endl;
    
    // displaying lecture details
    lecture1.displayLectureDetails();
	lecture2.displayLectureDetails();
	lecture3.displayLectureDetails();
	lecture4.displayLectureDetails();
	lecture5.displayLectureDetails();
	    	
	return 0;
}
