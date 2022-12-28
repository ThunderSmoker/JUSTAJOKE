#include<iostream>
using namespace std;
template<class T,class U> U sum(T x,U y){
    return x+y;
}
template<class T,class U,class V> V sum(T x,U y,V z){
    return x+y+z;
}
int main(){
    cout<<sum(1,2.4)<<"\n";
    cout<<sum(1,2.4,3.5)<<"\n";
}