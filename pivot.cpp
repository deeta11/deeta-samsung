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
    int j = 0;  // Pointer for placing elements <= pivot

    // Rearrange elements so that <= pivot are on the left, > pivot on the right
    for (int i = 0; i < 10; i++) {
        if (arr[i] <= pivot) {
            // Swap arr[i] with arr[j] to bring smaller element to the front
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            j++;  // Move pointer forward
        }
    }

    // Print the rearranged array
    cout << "Array after partitioning with pivot " << pivot << ": ";
    for (int i = 0; i < 10; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
