/* heirarchical inheritance - Create 2 classes Ds And Ml with course code and credit
    print no of Ds and No of ML
*/

#include<bits/stdc++.h>
using namespace std;
int noofds=0;
int noofml=0;
class Base{
    public:
    
    int cour_code;
    int credit;
    Base(){
    
    }
};
class Ds:public Base{
    public:
    
    Ds(){
    cour_code=21510098;
    credit=3;
    noofds++;
    
    }

};
class Ml:public Base{
    public:
    Ml(){
    cour_code=21510088;
    credit=4;
    noofml++;
    }

};
int main(){
   
    Ds hello=Ds();
    Ml hello1=Ml();
    Ds hello3=Ds();
    Ds hello2=Ds();
    cout<<noofds<<"\n";
    cout<<noofml<<"\n";
    cout<<hello1.cour_code<<"\n";
    cout<<hello1.credit<<"\n";
    cout<<hello2.credit<<"\n";
    cout<<hello2.cour_code<<"\n";

}
