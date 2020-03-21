#include <stdio.h>
#include <math.h>
#define jingdu 1e-7
#define pi 3.1415926
unsigned long fac(unsigned long n)  
{
    unsigned long i,m;
    for(i=0,m=1;i<=n;i++)
    {
        if(i!=0)
            m=m*i;
    }
    return m;
}
double fcos(double x)
{
    double temp=0.0,t=5;
    int i=0;
    while(x>=2*pi) x=x-2*pi;       //���ֻ��2�и�����
    while(t>=jingdu)
    {
        t=(pow(x,2*i))/fac(2*i);
        temp+=pow(-1,i)*t;
        i++;
      
    }
    return temp;
}
int main()
{
    double r;
    printf("�����뻡��ֵ��180���Ӧ3.1415926���ȣ��Դ�����...\n");
    printf("����(rad):");
    scanf("%lf",&r);
   
    printf("%.5lf\n",fcos(r));
    printf("%.51f\n",cos(r));//��ϵͳ�������жԱ�
}