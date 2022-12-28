#include<bits/stdc++.h>
using namespace std;
void fun(int a){
    try{
        if(a<0){
            throw(544);
        }
        else if (a==0)
        {
            throw(433);
        }
        else if(a<10 && a>3){
            throw(200);
        }
        
            throw("b");
        
        
    }
    catch(int e){
        cout<<"Integer Caught "<<e<<"\n";
    }
    catch(char b){
        cout<<"Char Caught"<<b;
    }
}
int main(){
    int a;
    cout<<"ENTER A nUMBER:";
    cin>>a;
    fun(a);
}