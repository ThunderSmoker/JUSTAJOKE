#include<iostream>
using namespace std;
class shape
{
public:
    int base;
    int height;
    void setside(int n){
        base=n;
    }
    void setheight(int b){
        height=b;
    }
};
class Triangle:public shape{
    public:
    void area(){
        cout<<"Area="<<0.5*base*height<<"\n";
    }
};
class Rectangle:public shape{
    public:
    void area(){
        cout<<"Area="<<base*height<<"\n";
    }
};
int main(){
    Triangle t;
    t.setside(5);
    t.setheight(3);
    t.area();
    Rectangle to;
    to.setside(5);
    to.setheight(3);
    to.area();
}