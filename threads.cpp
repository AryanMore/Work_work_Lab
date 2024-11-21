#include<iostream>
#include<pthread.h>
#include<stdio.h>

using namespace std;


int matA[2][3] = {{1,2,3},{4,5,6}};
int matB[3][2] = {{7,8},{9,10},{11,12}};
int matC[2][3];
int rowA = 2, colA = 3, rowB = 3, colB = 2;
int MAX = 100;
struct Threads
{
    int row;
};

/*
void* addition(void* args)
{
    Threads* data = (Threads*)args;
    int row = data->row;
    for(int j = 0; j < colA; j++)
    {
        matC[row][j] = matA[row][j] + matB[row][j];
    }
    return nullptr;
}
*/

void * multiply(void * args)
{
    Threads* data = (Threads*)args;
    int row = data->row;

    for(int i = 0; i < colB; i++)
    {
        matC[row][i] = 0;
        for(int j = 0; j < colA; j++)
        {
            matC[row][i] += matA[row][j] * matB[j][i];
        }
    }
    return nullptr;
}

int main()
{
    Threads data [MAX];
    pthread_t threads[MAX];

    for(int i = 0; i < rowA; i++)
    {
        data[i].row = i;
        pthread_create(&threads[i],NULL, multiply, &data[i]);
    }
    for(int i = 0; i < rowA; i++)
    {
        pthread_join(threads[i], NULL);
    }
    cout << "Matrix A" << endl;

    for(int i = 0; i < rowA; i++)
    {
        for(int j = 0; j < colA; j++)
        {
            cout << matA[i][j] << " ";
        }
        cout << "\n";
    }

    cout << "Matrix B" << endl;

    for(int i = 0; i < rowB; i++)
    {
        for(int j = 0; j < colB; j++)
        {
            cout << matB[i][j] << " ";
        }
        cout << "\n";
    }

    cout << "Addition Matrix C" << endl;

    for(int i = 0; i < rowA; i++)
    {
        for(int j = 0; j < colB; j++)
        {
            cout << matC[i][j] << " ";
        }
        cout << "\n";
    }
}