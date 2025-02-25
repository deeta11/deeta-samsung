#include <iostream>
using namespace std;
int main() {
    int arr[10];
    cout << "Enter 10 numbers: ";
    for (int i = 0; i < 10; i++)
        cin >> arr[i];
    int x;
    cout << "Enter pivot (x): ";
    cin >> x;
    int pivot = x;
    int j = 0; 
    for (int i = 0; i < 10; i++) {
        if (arr[i] <= pivot) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            j++;
        }
    }
    cout << "Array after partitioning with pivot " << pivot << ": ";
    for (int i = 0; i < 10; i++)
        cout << arr[i] << " ";
    cout << endl;
    return 0;
}
